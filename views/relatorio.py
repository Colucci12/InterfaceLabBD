import tkinter as tk
from tkinter import ttk

class Tela_Relatorio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12, 'bold'), background='#7289DA', foreground='white')
        style.configure("TLabel", font=('Helvetica', 12, 'bold'), background='#2C2F33', foreground='white')

        txt_label = ttk.Label(self, text="Tela Relatorio")
        txt_label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        bt_overview = ttk.Button(self,
                                 text="Ir para tela de overview",
                                 command=self.botao_overview,
                                 style="TButton"
                                 )
        bt_overview.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.role_label = ttk.Label(self, text="")
        self.role_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        # Initialize empty space for buttons
        self.button_frame = tk.Frame(self, bg="#2C2F33")
        self.button_frame.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        self.update_buttons()  # Call update_buttons during initialization

    def botao_overview(self):
        self.controller.show_frame("Tela_Overview")

    def update_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()  # Clear previous buttons

        role = self.controller.role
        liderFaccao = self.controller.liderFaccao

        if role:
            self.role_label.config(text=f"Role: {role}")

        if role == "Oficial":
            oficial_button = ttk.Button(self.button_frame,
                                        text="Relatório do Oficial",
                                        command=self.oficial_action,
                                        style="TButton"
                                        )
            oficial_button.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        if role == "Comandante":
            comandante_button1 = ttk.Button(self.button_frame,
                                            text="Relatório de Planetas Dominados",
                                            command=self.comandante_planetas_dominados_action,
                                            style="TButton"
                                            )
            comandante_button1.grid(row=2, column=0, pady=10, padx=10, sticky="w")

            comandante_button2 = ttk.Button(self.button_frame,
                                            text="Relatório de Planetas em Potencial Dominação",
                                            command=self.comandante_planetas_potencial_dominacao_action,
                                            style="TButton"
                                            )
            comandante_button2.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        if role == "Cientista":
            cientista_button1 = ttk.Button(self.button_frame,
                                           text="Relatório de Estrelas",
                                           command=self.cientista_estrelas_action,
                                           style="TButton"
                                           )
            cientista_button1.grid(row=4, column=0, pady=10, padx=10, sticky="w")

            cientista_button2 = ttk.Button(self.button_frame,
                                           text="Relatório de Planetas",
                                           command=self.cientista_planetas_action,
                                           style="TButton"
                                           )
            cientista_button2.grid(row=5, column=0, pady=10, padx=10, sticky="w")

            cientista_button3 = ttk.Button(self.button_frame,
                                           text="Relatório de Sistemas",
                                           command=self.cientista_sistemas_action,
                                           style="TButton"
                                           )
            cientista_button3.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        if liderFaccao:
            lider_faccao_button = ttk.Button(self.button_frame,
                                             text="Relatório da Facção do Líder",
                                             command=self.lider_faccao_action,
                                             style="TButton"
                                             )
            lider_faccao_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")

    def lider_faccao_action(self):
        # Placeholder action for Lider da Facção report
        print("Lider da Facção report action executed")

    def oficial_action(self):
        # Placeholder action for Oficial report
        print("Oficial report action executed")

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
