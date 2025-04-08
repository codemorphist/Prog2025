import re

def get_converter(name: str) -> callable:
    match name:
        case "int":
            return int, r"\d+"
        case "str":
            return str, r"[a-zA-Z]+"
        case _:
            raise NameError(f"Invalid converter name: {name}")


class Path:
    def __init__(self, pattern: str, view: callable):
        self.pattern = Path.normilize(pattern)
        self.view = view

        self.match_params()

    def replace_match(self):
        def _replace(match):
            converter, rex = get_converter(match.group("converter"))
            param = match.group("param")

            self.params[param] = converter

            return f"(?P<{param}>{rex})"

        return _replace

    def match_params(self):
        self.params = {}
        
        param_pattern = r"<(?P<converter>\w+):(?P<param>\w+)>"
        self.regex_pattern = re.sub(param_pattern, self.replace_match(), self.pattern)

    @staticmethod
    def normilize(path: str) -> str:
        return path.strip("/")

    def parse(self, path: str) -> tuple[bool, dict]:
        if self.params == {}:
            matched = Path.normilize(path) == Path.normilize(self.pattern)
            return matched, {}

        params = re.search(self.regex_pattern, path)

        if self.params and params is None:
            return False, {}

        params_values = {}
        for param, converter in self.params.items():
            params_values[param] = converter(params.group(param))

        return True, params_values
    

def path(pattern, view) -> Path:
    return Path(pattern, view)


if __name__ == "__main__":
    p = Path("delete-toy/<int:toy_id>/", lambda _: _)
    print(p.parse("delete-toy/1/"))
    print(p.parse("delete-toy/12"))
