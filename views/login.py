import tkinter as tk
from tkinter import messagebox
from InterfaceLabBD.Models.bancoTudo import BancoTudo
from InterfaceLabBD.Models import login

class Tela_Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        # Email
        email_label = tk.Label(self, text="ID", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        email_label.pack(pady=5)
        self.email_entry = tk.Entry(self, font=('Helvetica', 12))
        self.email_entry.pack(pady=10, ipadx=20, ipady=6)

        # Senha
        senha_label = tk.Label(self, text="Senha", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        senha_label.pack(pady=5)
        self.senha_entry = tk.Entry(self, font=('Helvetica', 12), show="*")
        self.senha_entry.pack(pady=10, ipadx=20, ipady=6)

        # Botão
        bt_entrar = tk.Button(self,
                              text="Entrar",
                              command=self.botao_login,
                              bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                              )
        bt_entrar.pack(pady=10, ipadx=20, ipady=6)

    def botao_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        #EXCEMPLO
        acessos = login(email, senha)
        if type(acessos) == dict:
            #TODO: aqui dentro acontece o login
            self.controller.banco = BancoTudo()
            self.controller.banco.preencher(acessos)
            self.controller.frames['Tela_Relatorio'].update_buttons()
            self.controller.frames['Tela_Overview'].update_overview()
            self.controller.show_frame("Tela_Overview")

        else:
            messagebox.showwarning(title="Erro", message=acessos)