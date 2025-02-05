import tkinter as tk
from tkinter import messagebox


def is_palindrome(s: str):
    l = len(s)
    i = 0
    while i < l//2:
        if s[i] != s[l-i-1]:
            return False
        i += 1
    return True


class PalindromeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config_window()
        self.basic_config()
        self.create_widgets()
        self.config_widgets()

    def config_window(self):
        self.title("Check palindrome")
        self.geometry("500x200")
        self.resizable(False, False)

    def basic_config(self):
        self.font = ("monospace", 16)

    def create_widgets(self):
        self.label_input = tk.Label()
        self.entry_s = tk.Entry()

        self.button_check = tk.Button()
        self.lable_res = tk.Label()

    def config_widgets(self):
        self.label_input.config(text="Input string:",
                                font=self.font)
        self.entry_s.config(font=self.font)

        self.button_check.config(text="Check",
                                 font=self.font,
                                 command=self.check)
        self.lable_res.config(font=self.font)

        self.label_input.grid(column=0, row=1, pady=10, padx=10)
        self.entry_s.grid(column=1, row=1, pady=10, padx=10)

        self.button_check.grid(column=1, row=2, pady=10)
        self.lable_res.grid(column=1, row=3, pady=10)

    def check(self):
        s = self.entry_s.get()

        if not s:
            messagebox.showinfo("Info", "String is empty")
            return 

        if is_palindrome(s):
            self.lable_res.config(text="Is palindrome")
        else:
            self.lable_res.config(text="In NOT palindrome")


def main():
    app = PalindromeApp()
    app.mainloop()


if __name__ == "__main__":
    # print(is_palindrome("hello"))
    # print(is_palindrome("ollo"))
    # print(is_palindrome("olo"))

    main()
