import tkinter as tk
from tkinter import messagebox

class Tela_Cientista(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        txt_label = tk.Label(self, text="Tela Cientista", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.pack(pady=5)

        # Left Column
        left_frame = tk.Frame(self, bg="#2C2F33")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Container 1: Criar Estrela
        create_frame = tk.Frame(left_frame, bg="#2C2F33")
        create_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(create_frame, text="ID Estrela", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_id_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_id_entry.pack(pady=5)

        tk.Label(create_frame, text="Nome", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_nome_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_nome_entry.pack(pady=5)

        tk.Label(create_frame, text="Classificação", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_classificacao_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_classificacao_entry.pack(pady=5)

        tk.Label(create_frame, text="Massa", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_massa_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_massa_entry.pack(pady=5)

        tk.Label(create_frame, text="Posição X", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_x_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_x_entry.pack(pady=5)

        tk.Label(create_frame, text="Posição Y", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_y_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_y_entry.pack(pady=5)

        tk.Label(create_frame, text="Posição Z", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.create_z_entry = tk.Entry(create_frame, font=('Helvetica', 12))
        self.create_z_entry.pack(pady=5)

        tk.Button(create_frame,
                  text="Criar Estrela",
                  command=self.criar_estrela,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        # Container 2: Remover Estrela
        remove_frame = tk.Frame(left_frame, bg="#2C2F33")
        remove_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(remove_frame, text="ID Estrela", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.remove_id_entry = tk.Entry(remove_frame, font=('Helvetica', 12))
        self.remove_id_entry.pack(pady=5)

        tk.Button(remove_frame,
                  text="Remover Estrela",
                  command=self.remover_estrela,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        # Right Column
        right_frame = tk.Frame(self, bg="#2C2F33")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(right_frame, text="ID Estrela Antiga", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_id_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_id_entry.pack(pady=5)

        tk.Label(right_frame, text="ID Estrela Nova", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_new_id_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_new_id_entry.pack(pady=5)

        tk.Label(right_frame, text="Nome", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_nome_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_nome_entry.pack(pady=5)

        tk.Label(right_frame, text="Classificação", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_classificacao_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_classificacao_entry.pack(pady=5)

        tk.Label(right_frame, text="Massa", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_massa_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_massa_entry.pack(pady=5)

        tk.Label(right_frame, text="Posição X", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_x_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_x_entry.pack(pady=5)

        tk.Label(right_frame, text="Posição Y", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_y_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_y_entry.pack(pady=5)

        tk.Label(right_frame, text="Posição Z", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold')).pack(pady=5)
        self.update_z_entry = tk.Entry(right_frame, font=('Helvetica', 12))
        self.update_z_entry.pack(pady=5)

        tk.Button(right_frame,
                  text="Atualizar Estrela",
                  command=self.atualizar_estrela,
                  bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                  ).pack(pady=10, ipadx=20, ipady=6)

        bt_voltar = tk.Button(self,
                              text="Voltar",
                              command=lambda: controller.show_frame("Tela_Overview"),
                              bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                              )
        bt_voltar.pack(pady=10, ipadx=20, ipady=6)

    def criar_estrela(self):
        estrela = self.create_id_entry.get()
        nome = self.create_nome_entry.get()
        classificacao = self.create_classificacao_entry.get()
        massa = self.create_massa_entry.get()
        x = self.create_x_entry.get()
        y = self.create_y_entry.get()
        z = self.create_z_entry.get()

        resposta = self.controller.banco.insere_estrela(estrela, nome, classificacao, massa, x, y, z)
        messagebox.showinfo(title='AVISO', message=resposta)
        self.controller.show_frame("Tela_Overview")

    def remover_estrela(self):
        id_antigo = self.update_id_entry.get()
        id_novo = self.update_new_id_entry.get()
        nome = self.update_nome_entry.get()
        classificacao = self.update_classificacao_entry.get()
        massa = self.update_massa_entry.get()
        x = self.update_x_entry.get()
        y = self.update_x_entry.get()
        z = self.update_z_entry.get()

        resposta = self.controller.banco.altera_estrela(id_antigo, id_novo, nome, classificacao, massa, x, y, z)
        messagebox.showinfo(title='AVISO', message=resposta)
        self.controller.show_frame("Tela_Overview")

    def atualizar_estrela(self):
        estrela = self.remove_id_entry.get()

        resposta = self.controller.banco.remove_estrela(estrela)
        messagebox.showinfo(title='AVISO', message=resposta)
        self.controller.show_frame("Tela_Overview")