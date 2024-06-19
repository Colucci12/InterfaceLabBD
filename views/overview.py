import tkinter as tk

class Tela_Overview(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        # Configure the grid to center the elements
        self.grid_columnconfigure(0, weight=1)

        txt_label = tk.Label(self, text="Tela Overview", bg="#2C2F33", fg="white", font=('Helvetica', 14, 'bold'))
        txt_label.grid(row=0, column=0, pady=5, sticky="n")

        self.nome_titulo_label = tk.Label(self, text="Nome:", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.nome_titulo_label.grid(row=1, column=0, pady=5, sticky="n")
        self.nome_label = tk.Label(self, text="", bg="#2C2F33", fg="white", font=('Helvetica', 12))
        self.nome_label.grid(row=2, column=0, pady=5, sticky="n")

        self.id_titulo_label = tk.Label(self, text="ID:", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.id_titulo_label.grid(row=3, column=0, pady=5, sticky="n")
        self.id_label = tk.Label(self, text="", bg="#2C2F33", fg="white", font=('Helvetica', 12))
        self.id_label.grid(row=4, column=0, pady=5, sticky="n")

        self.cpi_lider_titulo_label = tk.Label(self, text="CPI do Líder:", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.cpi_lider_titulo_label.grid(row=5, column=0, pady=5, sticky="n")
        self.cpi_lider_label = tk.Label(self, text="", bg="#2C2F33", fg="white", font=('Helvetica', 12))
        self.cpi_lider_label.grid(row=6, column=0, pady=5, sticky="n")

        self.cargo_lider_titulo_label = tk.Label(self, text="Cargo do Líder:", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.cargo_lider_titulo_label.grid(row=7, column=0, pady=5, sticky="n")
        self.cargo_lider_label = tk.Label(self, text="", bg="#2C2F33", fg="white", font=('Helvetica', 12))
        self.cargo_lider_label.grid(row=8, column=0, pady=5, sticky="n")

        self.eh_lider_faccao_titulo_label = tk.Label(self, text="É Líder da Facção:", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.eh_lider_faccao_titulo_label.grid(row=9, column=0, pady=5, sticky="n")
        self.eh_lider_faccao_label = tk.Label(self, text="", bg="#2C2F33", fg="white", font=('Helvetica', 12))
        self.eh_lider_faccao_label.grid(row=10, column=0, pady=5, sticky="n")

        self.bt_func_cargo = tk.Button(self,
                                       text="Funcionalidade Cargo",
                                       command=self.botao_func_cargo,
                                       bg='#7289DA',
                                       fg='white',
                                       font=('Helvetica', 12, 'bold')
                                       )
        self.bt_func_cargo.grid(row=11, column=0, pady=10, ipadx=20, ipady=6, sticky="n")

        self.bt_func_lider = tk.Button(self,
                                       text="Funcionalidade Líder Facção",
                                       command=self.botao_func_lider,
                                       bg='#7289DA',
                                       fg='white',
                                       font=('Helvetica', 12, 'bold')
                                       )
        self.bt_func_lider.grid(row=12, column=0, pady=10, ipadx=20, ipady=6, sticky="n")
        self.bt_func_lider.grid_remove()  # Initially hide the button

        self.bt_relatorio = tk.Button(self,
                                      text="Ir para tela de relatório",
                                      command=self.botao_relatorio,
                                      bg='#7289DA',
                                      fg='white',
                                      font=('Helvetica', 12, 'bold')
                                      )
        self.bt_relatorio.grid(row=13, column=0, pady=10, ipadx=20, ipady=6, sticky="n")

    def botao_func_cargo(self):
        role = self.controller.banco.cargo
        if role == "CIENTISTA":
            self.controller.show_frame("Tela_Cientista")
        elif role == "COMANDANTE":
            self.controller.show_frame("Tela_Comandante")
        elif role == "OFICIAL":
            self.controller.show_frame("Tela_Oficial")

    def botao_func_lider(self):
        self.controller.show_frame("Tela_LiderFaccao")

    def botao_relatorio(self):
        self.controller.show_frame("Tela_Relatorio")

    def update_overview(self):
        self.nome_label.config(text=self.controller.banco.nome)
        self.id_label.config(text=self.controller.banco.id)
        self.cpi_lider_label.config(text=self.controller.banco.cpi)
        self.cargo_lider_label.config(text=self.controller.banco.cargo)
        self.eh_lider_faccao_label.config(text="Sim" if self.controller.banco.lider_faccao else "Não")

        # Show or hide the leader faction button based on eh_lider_faccao
        if self.controller.banco.lider_faccao:
            self.bt_func_lider.grid()
        else:
            self.bt_func_lider.grid_remove()

    def print(self):
        print(self.controller.banco.nome)
