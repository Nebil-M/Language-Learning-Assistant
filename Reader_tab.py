import customtkinter as ct
from tkinter import ttk
import tkinter as tk


# Combining both sides
class ReaderTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        # Creating and griding
        self.text_read = TextRead(self)
        self.text_read.grid(row=0, column=0, sticky='news', padx=10, pady=10)

        self.word = Word(self)
        self.word.grid(row=0, column=1, sticky='news', padx=10, pady=10)
        # self.configure(fg_color='thistle1')



# The left side
class TextRead(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.text = ct.CTkTextbox(self, wrap='word')
        self.text.grid(row=0, column=0, sticky='news')

        # self.configure(fg_color='thistle1')


# The right side
class Word(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Layout
        #self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.word = tk.StringVar(value='word')
        self.word_label = ct.CTkLabel(self, textvariable=self.word, font=('arial', 25), text_color='dark orchid')
        self.definition = ct.CTkTextbox(self, wrap='word', cursor='', state="disabled")
        self.import_button = ct.CTkButton(self, text="Import", fg_color='medium orchid', border_color='purple1',
                                          hover_color='dark orchid', text_color='white', font=('Arial', 24))

        self.import_button.grid(row=2, column=0, padx=40, pady=40, sticky='NEWS')


        self.word_label.grid(row=0, column=0, padx=10, pady=10)
        self.definition.grid(row=1, column=0, sticky='news', padx=10, pady=10)
        # self.configure(fg_color='thistle1')



if __name__ == "__main__":
    window = ct.CTk()

    # window.geometry("1300x550")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    E = ReaderTab(window)
    E.grid(row=0, column=0, sticky='NSEW')

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
