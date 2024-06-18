import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela_Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12, 'bold'), background='#7289DA', foreground='white')
        style.configure("TLabel", font=('Helvetica', 12, 'bold'), background='#2C2F33', foreground='white')

        # Email
        email_label = ttk.Label(self, text="Email")
        email_label.pack(pady=5)
        self.email_entry = ttk.Entry(self, font=('Helvetica', 12))
        self.email_entry.pack(pady=10, ipadx=20, ipady=6)

        # Senha
        senha_label = ttk.Label(self, text="Senha")
        senha_label.pack(pady=5)
        self.senha_entry = ttk.Entry(self, font=('Helvetica', 12), show="*")
        self.senha_entry.pack(pady=10, ipadx=20, ipady=6)

        # Botão
        bt_entrar = ttk.Button(self,
                               text="Entrar",
                               command=self.botao_login,
                               style="TButton"
                               )
        bt_entrar.pack(pady=10, ipadx=20, ipady=6)

    def botao_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        # TODO: Replace this with actual login validation logic
        if email == "admin" and senha == "1234":
            self.controller.role = "Engineer"  # Example role
            self.controller.liderFaccao = True  # Example liderFaccao status
            self.controller.frames["Tela_Relatorio"].update_buttons()  # Update buttons on the report screen
            self.controller.show_frame("Tela_Overview")
        else:
            messagebox.showwarning(title="Erro", message="Credenciais inválidas")
