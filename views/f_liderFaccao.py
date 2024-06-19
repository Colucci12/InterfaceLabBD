import tkinter as tk
from tkinter import messagebox

class Tela_LiderFaccao(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        txt_label = tk.Label(self, text="Tela Líder", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.pack(pady=5)

        # Single Column
        single_frame = tk.Frame(self, bg="#2C2F33")
        single_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Container 1: Nome da Facção
        faccao_frame = tk.Frame(single_frame, bg="#2C2F33", relief="raised", bd=2)
        faccao_frame.pack(pady=1, fill=tk.BOTH, expand=True)

        tk.Label(faccao_frame, text="Nome da Facção", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.faccao_nome_entry = tk.Entry(faccao_frame, font=('Helvetica', 12))
        self.faccao_nome_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(faccao_frame,
                  text="Confirmar",
                  command=self.confirmar_faccao,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        # Container 2: CPI
        cpi_frame = tk.Frame(single_frame, bg="#2C2F33", relief="raised", bd=2)
        cpi_frame.pack(pady=1, fill=tk.BOTH, expand=True)

        tk.Label(cpi_frame, text="CPI", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.cpi_text = tk.Text(cpi_frame, height=4, font=('Helvetica', 12))
        self.cpi_text.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(cpi_frame,
                  text="Indicar Novo Líder",
                  command=self.indicar_lider,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        # Container 3: Remover Nação
        remocao_nacao_frame = tk.Frame(single_frame, bg="#2C2F33", relief="raised", bd=2)
        remocao_nacao_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(remocao_nacao_frame, text="Remover Nação", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.remocao_nacao_entry = tk.Entry(remocao_nacao_frame, font=('Helvetica', 12))
        self.remocao_nacao_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(remocao_nacao_frame,
                  text="Remover",
                  command=self.remover_nacao,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        # Container 4: Credenciar Comunidade
        comunidade_frame = tk.Frame(single_frame, bg="#2C2F33", relief="raised", bd=2)
        comunidade_frame.pack(pady=1, fill=tk.BOTH, expand=True)

        tk.Label(comunidade_frame, text="Espécie", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.especie_entry = tk.Entry(comunidade_frame, font=('Helvetica', 12))
        self.especie_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Label(comunidade_frame, text="Comunidade", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.comunidade_entry = tk.Entry(comunidade_frame, font=('Helvetica', 12))
        self.comunidade_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Label(comunidade_frame, text="Quantidade de Habitantes", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.habitantes_entry = tk.Entry(comunidade_frame, font=('Helvetica', 12))
        self.habitantes_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Label(comunidade_frame, text="Planeta", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.planeta_entry = tk.Entry(comunidade_frame, font=('Helvetica', 12))
        self.planeta_entry.pack(pady=5, ipadx=20, ipady=5)

        tk.Button(comunidade_frame,
                  text="Credenciar Comunidade",
                  command=self.credenciar_comunidade,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        # Botão Voltar
        bt_voltar = tk.Button(self,
                              text="Voltar",
                              command=lambda: controller.show_frame("Tela_Overview"),
                              bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                              )
        bt_voltar.pack(pady=10, ipadx=20, ipady=6)

    def confirmar_faccao(self):
        nome = self.faccao_nome_entry.get()
        resposta = self.controller.banco.lider_alterarnome_faccao(nome)
        messagebox.showinfo(title='AVISO', message=resposta)
        self.controller.show_frame("Tela_Overview")

    def indicar_lider(self):
        cpi = self.cpi_text.get()
        resposta = self.controller.banco.lider_indicar_novo(cpi)
        messagebox.showinfo(title='AVISO', message=resposta)
        self.controller.show_frame("Tela_Overview")

    def remover_nacao(self):
        # Lógica para remover nação
        pass

    def credenciar_comunidade(self):
        # Lógica para credenciar comunidade
        pass