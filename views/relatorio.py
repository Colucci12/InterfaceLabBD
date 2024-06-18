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

    def botao_overview(self):
        self.controller.show_frame("Tela_Overview")

    def update_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()  # Clear previous buttons

        role = self.controller.role
        liderFaccao = self.controller.liderFaccao

        if role:
            self.role_label.config(text=f"Role: {role}")

        if role == "Engineer":
            engineer_button = ttk.Button(self.button_frame,
                                         text="Engineer Action",
                                         command=self.engineer_action,
                                         style="TButton"
                                         )
            engineer_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        if liderFaccao:
            faction_button = ttk.Button(self.button_frame,
                                        text="Leader Faction Action",
                                        command=self.liderFaccao_action,
                                        style="TButton"
                                        )
            faction_button.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def engineer_action(self):
        # Define action for engineer
        print("Engineer action executed")

    def liderFaccao_action(self):
        # Define action for leader faction
        print("Leader faction action executed")
