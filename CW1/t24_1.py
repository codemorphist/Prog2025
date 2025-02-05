import tkinter as tk
from tkinter import messagebox


def taylor(x: float, eps: float = 1e-5):
    if abs(x) >= 1:
        raise ValueError(f"Invalid x: {x},  must be |x| < 1")

    res = 0
    el = 1
    i = 1
    while abs(el) > eps:
        res += el
        el *= -(i+1)/i * x 
        i += 1

    return res


class TaylorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config_window()
        self.basic_config()
        self.create_widgets()
        self.config_widgets()

    def config_window(self):
        self.title("Remove content in ()")
        self.geometry("500x400")
        self.resizable(False, False)

    def basic_config(self):
        self.font = ("monospace", 16)

    def create_widgets(self):
        self.label_input_x = tk.Label()
        self.entry_x = tk.Entry()

        self.label_input_e = tk.Label() 
        self.entry_e = tk.Entry()

        self.button_calc = tk.Button()
        self.lable_res = tk.Label()

    def config_widgets(self):
        self.label_input_x.config(text="Input x:",
                                  font=self.font)
        self.entry_x.config(font=self.font)

        self.label_input_e.config(text="Input e:",
                                  font=self.font)
        self.entry_e.config(font=self.font)
        self.entry_e.insert(0, "1e-5")

        self.button_calc.config(text="Calculate",
                                font=self.font,
                                command=self.calculate)
        self.lable_res.config(font=self.font)

        self.label_input_x.grid(column=0, row=1, pady=10, padx=5)
        self.entry_x.grid(column=1, row=1, pady=10)

        self.label_input_e.grid(column=0, row=3, pady=10, padx=5)
        self.entry_e.grid(column=1, row=3, pady=10)

        self.button_calc.grid(column=1, row=5, pady=10, padx=10)
        self.lable_res.grid(column=1, row=7, pady=10, padx=10)

        self.grid_columnconfigure(1, weight=50)

    def get(self, entry: tk.Entry) -> float:
        try:
            data = entry.get()
            val = float(data)
            return val
        except:
            raise ValueError("Value must be float")

    def calculate(self):
        try:
            x = self.get(self.entry_x)
            eps = self.get(self.entry_e)
            res = taylor(x, eps)
            self.lable_res.config(text=f"Result: {res:.10f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    app = TaylorApp() 
    app.mainloop()


if __name__ == "__main__":
    main()

