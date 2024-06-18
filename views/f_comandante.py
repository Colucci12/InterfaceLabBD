import tkinter as tk

class Tela_Comandante(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#2C2F33")

        txt_label = tk.Label(self, text="Tela Comandante", bg="#2C2F33", fg="white", font=('Helvetica', 12, 'bold'))
        txt_label.pack(pady=5)

        bt_voltar = tk.Button(self,
                              text="Voltar",
                              command=lambda: controller.show_frame("Tela_Overview"),
                              bg='#7289DA', fg='white', font=('Helvetica', 12, 'bold')
                              )
        bt_voltar.pack(pady=10, ipadx=20, ipady=6)
