import tkinter as tk

class Tela_Overview(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        txt_label = tk.Label(self, text="Tela Overview", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.pack(pady=5)

        bt_relatorio = tk.Button(self,
                            text="Ir para tela de relatorio",
                            command=self.botao_relatorio,
                            background='#7289DA',
                            foreground='white',
                            font=('Helvetica', 12, 'bold')
                            )
        bt_relatorio.pack(pady=10, ipadx=20, ipady=6)

    def botao_relatorio(self):
        self.controller.show_frame("Tela_Relatorio")