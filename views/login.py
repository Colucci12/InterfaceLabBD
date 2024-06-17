import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela_Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        #Email
        email_label = tk.Label(self, text="Email", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        email_label.pack(pady=5)
        email_entry = ttk.Entry(self, font=('Helvetica', 12))
        email_entry.pack(pady=10, ipadx=20, ipady=6)

        #Senha
        senha_label = tk.Label(self, text="Senha", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        senha_label.pack(pady=5)
        senha_entry = ttk.Entry(self, font=('Helvetica', 12), show="*")
        senha_entry.pack(pady=10, ipadx=20, ipady=6)

        #Botão
        bt_entrar = tk.Button(self,
                            text="Entrar",
                            command=self.botao_login,
                            background='#7289DA',
                            foreground='white',
                            font=('Helvetica', 12, 'bold')
                            )
        bt_entrar.pack(pady=10, ipadx=20, ipady=6)

    def botao_login(self):
        #TODO: Validar inputs, consultar banco e trocar de tela/mostrar erro
        messagebox.showwarning(title="Exemplo", message="Exemplo de mensagem de erro") #Caso de errado
        self.controller.show_frame("Tela_Overview") #Caso de certo