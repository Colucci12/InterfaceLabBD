import tkinter as tk

class Tela_Overview(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        # Configure the grid to center the elements
        self.grid_columnconfigure(0, weight=1)

        txt_label = tk.Label(self, text="Tela Overview", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.grid(row=0, column=0, pady=5, sticky="n")

        self.nome_label = tk.Label(self, text="Nome: ", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.nome_label.grid(row=1, column=0, pady=5, sticky="n")

        self.id_label = tk.Label(self, text="ID: ", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.id_label.grid(row=2, column=0, pady=5, sticky="n")

        self.bt_func_cargo = tk.Button(self,
                                       text="Funcionalidade Cargo",
                                       command=self.botao_func_cargo,
                                       bg='#7289DA',
                                       fg='white',
                                       font=('Helvetica', 12, 'bold')
                                       )
        self.bt_func_cargo.grid(row=3, column=0, pady=10, ipadx=20, ipady=6, sticky="n")

        self.bt_func_lider = tk.Button(self,
                                       text="Funcionalidade Líder Facção",
                                       command=self.botao_func_lider,
                                       bg='#7289DA',
                                       fg='white',
                                       font=('Helvetica', 12, 'bold')
                                       )
        self.bt_func_lider.grid(row=4, column=0, pady=10, ipadx=20, ipady=6, sticky="n")
        self.bt_func_lider.grid_remove()  # Initially hide the button

        self.bt_relatorio = tk.Button(self,
                                      text="Ir para tela de relatório",
                                      command=self.botao_relatorio,
                                      bg='#7289DA',
                                      fg='white',
                                      font=('Helvetica', 12, 'bold')
                                      )
        self.bt_relatorio.grid(row=5, column=0, pady=10, ipadx=20, ipady=6, sticky="n")

    def botao_func_cargo(self):
        role = self.controller.role
        if role == "Cientista":
            self.controller.show_frame("Tela_Cientista")
        elif role == "Comandante":
            self.controller.show_frame("Tela_Comandante")
        elif role == "Oficial":
            self.controller.show_frame("Tela_Oficial")

    def botao_func_lider(self):
        self.controller.show_frame("Tela_LiderFaccao")

    def botao_relatorio(self):
        self.controller.show_frame("Tela_Relatorio")

    def update_overview(self, nome, id):
        if not nome:
            nome = "Sem nome"
        self.nome_label.config(text=f"Nome: {nome}")
        self.id_label.config(text=f"ID: {id}")

        # Show or hide the leader faction button based on liderFaccao
        if self.controller.liderFaccao:
            self.bt_func_lider.grid()
        else:
            self.bt_func_lider.grid_remove()
