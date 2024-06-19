import tkinter as tk
from tkinter import ttk

class Tela_Relatorio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        txt_label = tk.Label(self, text="Tela Relatorio", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        bt_overview = tk.Button(self,
                                text="Ir para tela de overview",
                                command=self.botao_overview,
                                bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                )
        bt_overview.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.role_label = tk.Label(self, text="", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        self.role_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        # Initialize empty space for buttons
        self.button_frame = tk.Frame(self, bg="#2C2F33")
        self.button_frame.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        self.update_buttons()  # Call update_buttons during initialization

        # Variable to store the selected option
        self.selected_option = tk.StringVar(value="")

        # Table to display results
        self.table_frame = tk.Frame(self, bg="#2C2F33")
        self.table_frame.grid(row=0, column=1, rowspan=5, pady=10, padx=10, sticky="nsew")

    def botao_overview(self):
        self.controller.show_frame("Tela_Overview")

    def update_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()  # Clear previous buttons

        role = self.controller.role
        liderFaccao = self.controller.liderFaccao

        if role:
            self.role_label.config(text=f"Role: {role}")

        row_counter = 0

        if liderFaccao:
            lider_faccao_button = tk.Button(self.button_frame,
                                            text="Relatório da Facção do Líder",
                                            command=self.lider_faccao_action,
                                            bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                            )
            lider_faccao_button.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

            # Add Checkbuttons for selection options
            self.options_lider = [("Nação", "nacao"), ("Espécie", "especie"), ("Planeta", "planeta"), ("Sistema", "sistema")]
            self.checkbuttons_lider = {}
            for option_text, option_value in self.options_lider:
                var = tk.StringVar(value="")
                cb = tk.Checkbutton(self.button_frame,
                                    text=option_text,
                                    variable=var,
                                    onvalue=option_value,
                                    offvalue="",
                                    bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'),
                                    selectcolor='#2C2F33', activebackground='#7289DA', activeforeground='white',
                                    command=lambda v=option_value: self.toggle_checkbutton(v, self.checkbuttons_lider)
                                    )
                cb.grid(row=row_counter, column=0, pady=5, padx=10, sticky="w")
                self.checkbuttons_lider[option_value] = var
                row_counter += 1

        if role == "Oficial":
            oficial_button = tk.Button(self.button_frame,
                                       text="Relatório do Oficial",
                                       command=self.oficial_action,
                                       bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                       )
            oficial_button.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

            # Add Checkbuttons for selection options
            self.options_oficial = [("Facção", "faccao"), ("Espécie", "especie"), ("Planeta", "planeta"), ("Sistema", "sistema")]
            self.checkbuttons_oficial = {}
            for option_text, option_value in self.options_oficial:
                var = tk.StringVar(value="")
                cb = tk.Checkbutton(self.button_frame,
                                    text=option_text,
                                    variable=var,
                                    onvalue=option_value,
                                    offvalue="",
                                    bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'),
                                    selectcolor='#2C2F33', activebackground='#7289DA', activeforeground='white',
                                    command=lambda v=option_value: self.toggle_checkbutton(v, self.checkbuttons_oficial)
                                    )
                cb.grid(row=row_counter, column=0, pady=5, padx=10, sticky="w")
                self.checkbuttons_oficial[option_value] = var
                row_counter += 1

        if role == "Comandante":
            comandante_button1 = tk.Button(self.button_frame,
                                           text="Relatório de Planetas Dominados",
                                           command=self.comandante_planetas_dominados_action,
                                           bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                           )
            comandante_button1.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

            comandante_button2 = tk.Button(self.button_frame,
                                           text="Relatório de Planetas em Potencial Dominação",
                                           command=self.comandante_planetas_potencial_dominacao_action,
                                           bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                           )
            comandante_button2.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

        if role == "Cientista":
            cientista_button1 = tk.Button(self.button_frame,
                                          text="Relatório de Estrelas",
                                          command=self.cientista_estrelas_action,
                                          bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                          )
            cientista_button1.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

            cientista_button2 = tk.Button(self.button_frame,
                                          text="Relatório de Planetas",
                                          command=self.cientista_planetas_action,
                                          bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                          )
            cientista_button2.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

            cientista_button3 = tk.Button(self.button_frame,
                                          text="Relatório de Sistemas",
                                          command=self.cientista_sistemas_action,
                                          bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                          )
            cientista_button3.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1



    def toggle_checkbutton(self, value, checkbuttons):
        # Deselect other checkbuttons if one is selected
        if checkbuttons[value].get() == value:
            self.selected_option.set(value)
            for opt, var in checkbuttons.items():
                if opt != value:
                    var.set("")
        else:
            self.selected_option.set("")

    def lider_faccao_action(self):
        self.clear_table()
        selected_option = self.selected_option.get()
        print(f"Lider da Facção report action executed with selection: {selected_option}")
        columns = ("faccao_lider", "faccao_nome", "comunidade_nome", "qtd_habitantes", "nacao", "especie", "planeta", "planeta_classificacao", "sistema")
        self.create_table(columns)

    def oficial_action(self):
        self.clear_table()
        selected_option = self.selected_option.get()
        print(f"Oficial report action executed with selection: {selected_option}")
        columns = ("planeta", "especie", "comunidade_nome", "qtd_habitantes", "data_ini", "data_fim", "nacao_nome", "faccao", "sistema")
        self.create_table(columns)

    def comandante_planetas_dominados_action(self):
        self.clear_table()
        columns = ("planeta", "NacaoDominante", "DataInicioDominancia", "DataFimDominancia", "QuantidadeComunidades", "QuantidadeEspecies", "QuantidadeHabitantes", "QuantidadeFaccoes", "FaccaoMajoritaria")
        self.create_table(columns)

    def comandante_planetas_potencial_dominacao_action(self):
        self.clear_table()
        columns = ("planeta", "sistema")
        self.create_table(columns)

    def cientista_estrelas_action(self):
        self.clear_table()
        columns = ("id_estrela", "nome", "classificacao", "massa", "x", "y", "z")
        self.create_table(columns)

    def cientista_planetas_action(self):
        self.clear_table()
        columns = ("id_astro", "massa", "raio", "classificacao")
        self.create_table(columns)

    def cientista_sistemas_action(self):
        self.clear_table()
        columns = ("estrela", "nome")
        self.create_table(columns)

    def liderFaccao_action(self):
        self.clear_table()
        selected_option = self.selected_option.get()
        print(f"Leader Faction report action executed with selection: {selected_option}")
        # Simulate table creation based on selected option
        columns = (selected_option,)
        self.create_table(columns)

    def create_table(self, columns):
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor='center')
        self.tree.pack(fill=tk.BOTH, expand=True)

    def clear_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
