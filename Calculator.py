import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Black Calculator")
        self.root.geometry("320x450")
        self.root.configure(bg="black")
        
        self.input_text = ""

        # Display
        self.display = tk.Entry(root, font=("Arial", 32), bg="black", fg="black",
                                bd=0, justify="right", insertbackground="white")
        self.display.pack(fill="both", padx=10, pady=20, ipady=10)
        self.display.config(state="readonly")

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="white")
        btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ["AC", "DEL", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        for r, row in enumerate(buttons):
            btn_frame.grid_rowconfigure(r, weight=1)
            for c, text in enumerate(row):
                btn_frame.grid_columnconfigure(c, weight=1)
                if text == "":
                    tk.Label(btn_frame, bg="black").grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
                    continue

                bg_color = "#333333"
                fg_color = "black"
                if text in "/*-+%= ":
                    if text in "/*-+":
                        bg_color = "#white"  # Orange
                    elif text == "%":
                        bg_color = "#FF9F0A"
                    else:
                        bg_color = "#A5A5A5"
                        fg_color = "black"
                        if text == "=":
                            bg_color = "#FF9F0A"
                            fg_color = "black"
                elif text in ["AC", "DEL"]:
                    bg_color = "#A5A5A5"
                    fg_color = "black"

                btn = tk.Button(btn_frame, text=text, font=("Arial", 20, "bold"),
                                bg=bg_color, fg=fg_color, bd=0, relief="flat",
                                activebackground="#DFE209",
                                command=lambda t=text: self.on_click(t))
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    def update_display(self):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.input_text)
        self.display.config(state="readonly")

    def on_click(self, char):
        if char == "AC":
            self.input_text = ""
        elif char == "DEL":
            self.input_text = self.input_text[:-1]
        elif char == "=":
            try:
                # Safe eval: palitan % para gumana
                expression = self.input_text.replace("%", "/100")
                result = eval(expression)
                # Alisin .0 kung whole number
                if result == int(result):
                    self.input_text = str(int(result))
                else:
                    self.input_text = str(result)
            except:
                self.input_text = ""
                self.display.config(state="normal")
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.display.config(state="readonly")
                return
        else:
            self.input_text += char
        
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
