#!/home/x/Documents/Lectures/Prog2025/CW4/venv/bin/python
import os
import cgi
from string import Template

CGI_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = CGI_DIR

def is_palindrome(s: str) -> bool:
    s = s.lower()
    slen = len(s)
    for i in range(slen//2):
        if s[i] != s[slen-i-1]:
            return False
    return True


def main():
    form = cgi.FieldStorage()
    string = form.getfirst("palindrome", "")

    if is_palindrome(string):
        ispal = "This is palindrome!"
    else:
        ispal = "This is NOT palindrome!"

    answer = f"{string} - {ispal}"

    res_template = os.path.join(TEMPLATE_DIR, "result.html")
    with open(res_template, "r", encoding="utf-8") as html:
        page = Template(html.read()).substitute(answer=answer)

    print("Content-Type: text/html")    # HTML is following
    print()                             # blank line, end of headers
    print(page)


if __name__ == "__main__":
    # print(is_palindrome("hello"))   # False
    # print(is_palindrome("ollo"))    # True
    # print(is_palindrome("testset")) # True
    main()
