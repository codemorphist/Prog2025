import re


def get_converter(name: str) -> callable:
    match name:
        case "int":
            return int, r"\d+"
        case "str":
            return str, r"[a-zA-Z0-9-]+"
        case _:
            raise NameError(f"Invalid converter name: {name}")


class Path:
    PARAM_PATTERN = r"<(?P<converter>\w+):(?P<param>\w+)>"

    def __init__(self, pattern: str, view: callable):
        self.pattern = Path.normilize(pattern)
        self.view = view

        self.match_params()
        self.construct_pattern()

    def replace_match(self):
        def _replace(match):
            converter, rex = get_converter(match.group("converter"))
            param = match.group("param")

            self.params[param] = converter, rex

            return f"(?P<{param}>{rex})"

        return _replace

    def match_params(self):
        self.params = {}
        
        self.regex_pattern = re.sub(Path.PARAM_PATTERN, self.replace_match(), self.pattern)

        if self.pattern.endswith("/"):
            self.regex_pattern += "?"
        else:
            self.regex_pattern += "/?"

        # Fixed bug when for path("test/", ...)
        # test/ and testtest/ both return True
        self.regex_pattern = f"^{self.regex_pattern}"

    def construct_pattern(self):
        self.url_pattern = "/" + re.sub(Path.PARAM_PATTERN, 
                                  r"{\g<param>}", 
                                  self.pattern)

    @staticmethod
    def normilize(path: str) -> str:
        path = path.lstrip("/").rstrip("/")
        return path

    def parse(self, path: str) -> tuple[bool, dict]:
        path = Path.normilize(path)

        if self.params == {}:
            return path == self.pattern, {}

        params = re.search(self.regex_pattern, path)

        if self.params and params is None:
            return False, {}

        params_values = {}
        for param, (converter, _) in self.params.items():
            params_values[param] = converter(params.group(param))

        return True, params_values

    def url(self, **kwargs) -> str:
        for param in self.params.keys():
            if param not in kwargs:
                raise NameError(f"Value for parameter {param} not given")

        for param, value in kwargs.items():
            if param not in self.params:
                raise NameError(f"Invalid parameter {param} ({value})")

            value = str(value)
            converter, rex = self.params[param]
            match = re.match(rex, value)
            if not match:
                raise ValueError(f"Invalid converter {converter} ({rex}) for value '{value}'") 

        return self.url_pattern.format(**kwargs)

    def __repr__(self) -> str:
        return f"<Path ({self.pattern})>"


PATH_REGISTRY = {} 
    

def path(pattern, view, name: str | None = None) -> Path:
    path = Path(pattern, view)

    if name is not None:
        if name in PATH_REGISTRY:
            raise KeyError(f"Path with name {name} already registred")
        PATH_REGISTRY[name] = path

    return path


def url(name: str, **kwargs) -> str:
    if name not in PATH_REGISTRY:
        raise NameError(f"Path with name {name} not registred")
    return PATH_REGISTRY[name].url(**kwargs)
