import tkinter as tk

class Tela_Comandante(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        txt_label = tk.Label(self, text="Tela Comandante", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.pack(pady=5)

        main_frame = tk.Frame(self, bg="#2C2F33")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Container 1: Incluir Nação na Federação
        incluir_nacao_frame = tk.Frame(main_frame, bg="#2C2F33", highlightbackground="white", highlightthickness=1)
        incluir_nacao_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        tk.Label(incluir_nacao_frame, text="Federação - Incluir Nação", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.incluir_nacao_entry = tk.Entry(incluir_nacao_frame, font=('Helvetica', 12))
        self.incluir_nacao_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(incluir_nacao_frame,
                  text="Incluir Nação",
                  command=self.incluir_nacao,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=5, ipadx=20, ipady=6)

        # Container 2: Excluir Nação da Federação
        excluir_nacao_frame = tk.Frame(main_frame, bg="#2C2F33", highlightbackground="white", highlightthickness=1)
        excluir_nacao_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        tk.Label(excluir_nacao_frame, text="Clique para excluir sua Nação da Federação", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        tk.Button(excluir_nacao_frame,
                  text="Excluir Nação",
                  command=self.excluir_nacao,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=5, ipadx=20, ipady=6)

        # Container 3: Criar Federação
        criar_federacao_frame = tk.Frame(main_frame, bg="#2C2F33", highlightbackground="white", highlightthickness=1)
        criar_federacao_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        tk.Label(criar_federacao_frame, text="Criar Federação", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.criar_federacao_entry = tk.Entry(criar_federacao_frame, font=('Helvetica', 12))
        self.criar_federacao_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(criar_federacao_frame,
                  text="Criar Federação",
                  command=self.criar_federacao,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=5, ipadx=20, ipady=6)

        # Container 4: Adicionar Dominação ao Planeta
        dominacao_planeta_frame = tk.Frame(main_frame, bg="#2C2F33", highlightbackground="white", highlightthickness=1)
        dominacao_planeta_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        tk.Label(dominacao_planeta_frame, text="Nome do Planeta", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.dominacao_planeta_entry = tk.Entry(dominacao_planeta_frame, font=('Helvetica', 12))
        self.dominacao_planeta_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(dominacao_planeta_frame,
                  text="Adicionar Dominação",
                  command=self.adicionar_dominacao,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=5, ipadx=20, ipady=6)

        bt_voltar = tk.Button(self,
                              text="Voltar",
                              command=lambda: controller.show_frame("Tela_Overview"),
                              bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                              )
        bt_voltar.pack(pady=10, ipadx=20, ipady=6)

    def incluir_nacao(self):
        # Lógica para incluir nação na federação
        pass

    def excluir_nacao(self):
        # Lógica para excluir nação da federação
        pass

    def criar_federacao(self):
        # Lógica para criar federação
        pass

    def adicionar_dominacao(self):
        # Lógica para adicionar dominação ao planeta
        pass
