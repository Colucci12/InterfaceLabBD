import tkinter as tk

from views.login import Tela_Login
from views.overview import Tela_Overview
from views.relatorio import Tela_Relatorio

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Navegação entre Páginas")
        self.geometry("800x600")
        self.configure(bg="#2C2F33")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Tela_Login, Tela_Overview, Tela_Relatorio):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Tela_Login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
