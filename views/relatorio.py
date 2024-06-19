import tkinter as tk

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

        # Variables to store the selected options
        self.selected_lider_option = tk.StringVar(value="")
        self.selected_oficial_option = tk.StringVar(value="")

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
                                    command=lambda v=option_value: self.toggle_checkbutton(v, self.checkbuttons_oficial, self.selected_oficial_option)
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

        if liderFaccao:
            lider_faccao_button = tk.Button(self.button_frame,
                                            text="Relatório da Facção do Líder",
                                            command=self.lider_faccao_action,
                                            bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                                            )
            lider_faccao_button.grid(row=row_counter, column=0, pady=10, padx=10, sticky="w")
            row_counter += 1

            # Add Checkbuttons for selection options
            self.options_lider = [("Nação", "nacao"), ("Espécie", "especie"), ("Planeta", "planeta"),
                                  ("Sistema", "sistema")]
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
                                    command=lambda v=option_value: self.toggle_checkbutton(v, self.checkbuttons_lider,
                                                                                           self.selected_lider_option)
                                    )
                cb.grid(row=row_counter, column=0, pady=5, padx=10, sticky="w")
                self.checkbuttons_lider[option_value] = var
                row_counter += 1

    def toggle_checkbutton(self, value, checkbuttons, selected_var):
        # Deselect other checkbuttons if one is selected
        if checkbuttons[value].get() == value:
            selected_var.set(value)
            for opt, var in checkbuttons.items():
                if opt != value:
                    var.set("")
        else:
            selected_var.set("")

    def lider_faccao_action(self):
        # Placeholder action for Lider da Facção report
        selected_option = self.selected_lider_option.get()
        print(f"Lider da Facção report action executed with selection: {selected_option}")

    def oficial_action(self):
        # Placeholder action for Oficial report
        selected_option = self.selected_oficial_option.get()
        print(f"Oficial report action executed with selection: {selected_option}")

    def comandante_planetas_dominados_action(self):
        # Placeholder action for Comandante - Planetas Dominados report
        print("Comandante - Planetas Dominados report action executed")

    def comandante_planetas_potencial_dominacao_action(self):
        # Placeholder action for Comandante - Planetas em Potencial Dominação report
        print("Comandante - Planetas em Potencial Dominação report action executed")

    def cientista_estrelas_action(self):
        # Placeholder action for Cientista - Estrelas report
        print("Cientista - Estrelas report action executed")

    def cientista_planetas_action(self):
        # Placeholder action for Cientista - Planetas report
        print("Cientista - Planetas report action executed")

    def cientista_sistemas_action(self):
        # Placeholder action for Cientista - Sistemas report
        print("Cientista - Sistemas report action executed")

