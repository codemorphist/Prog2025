import re
import tkinter as tk


def remove_content(s: str) -> str:
    """
    Remove all group of characters in brackets ()

    Example:
        IN: Hello (this text in brackets) World! 
        OUT: Hello  World! 
    """
    return re.sub(r"\([^)]*\)", "", s)


class RemoveContentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.basic_config()
        self.add_widgets()

    def basic_config(self):
        self.font = ("monospace", 16)

    def config_window(self):
        self.title("Remove content in ()")
        self.geometry("700x700")
        self.resizable(False, False)

    def add_widgets(self):
        self.entry_content = tk.Text(self,
                                     height=10,
                                     width=50,
                                     font=self.font)
        self.entry_content.pack(pady=20)

        self.remove_button = tk.Button(self,
                                       text="Remove content in ()",
                                       font=self.font)
        self.remove_button.pack(pady=10)
        self.remove_button.config(command=self.remove_button_click)
        self.remove_button.config(width=40)

        self.out_content = tk.Text(self,
                                 height=10,
                                 width=50,
                                 font=self.font)
        self.out_content.config(state=tk.DISABLED)
        self.out_content.pack(pady=20)

    def remove_button_click(self):
        content = self.entry_content.get("1.0", tk.END)
        removed = remove_content(content)
        self.insert_content(removed)

    def insert_content(self, content):
        self.out_content.config(state=tk.NORMAL)
        self.out_content.delete("1.0", tk.END)
        self.out_content.insert("1.0", content)
        self.out_content.config(state=tk.DISABLED)


def main():
    app = RemoveContentApp()
    app.mainloop()


if __name__ == "__main__":
    main()
