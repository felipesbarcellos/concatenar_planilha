from logging import config
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import filedialog
from app.concatenar_planilhas import ConcatenarPlanilhas
from util.constants import Constants

class JanelaPrincipal():
    def __init__(self):
        self.root: Tk = Tk()
        self.app = SelecaoArquivo(self.root)
        self.app.mainloop()
        pass
    ...

    def construir_janela(self):
        frame = ttk.Frame()
        return frame

class SelecaoArquivo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Tórulo para exibir a explicação
        self.label_explicativa = tk.Label(self, text="Clique no botão para selecionar um arquivo.")
        self.label_explicativa.pack()

        # Rótulo para exibir o caminho do arquivo
        self.caminho_label = tk.Label(self, text="Caminho do arquivo:")
        self.caminho_label.pack(side="left")

        # Entrada para exibir o caminho completo
        self.caminho_entry = tk.Entry(self, width=50)
        self.caminho_entry.pack(side="left")

        self.caminho_entry.insert(0, Constants().DATA_PATH)

        # Botão para selecionar o arquivo
        self.botao_selecionar = tk.Button(self, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.botao_selecionar.pack(side="left")

        botao_frame = tk.Frame(self)
        botao_frame.pack(side="bottom")

        # Botão para executar a concatenação
        self.botao_executar = tk.Button(botao_frame, text="Executar Concatenação", command=self.executar_concatenacao, bg="blue", fg="white", border=1)
        self.botao_executar.pack(side="bottom")


    def selecionar_arquivo(self):
        """Abre um diálogo para o usuário selecionar um arquivo e atualiza o rótulo."""
        arquivo = filedialog.askopenfilename()
        self.caminho_entry.delete(0, tk.END)
        self.caminho_entry.insert(0, arquivo)
        with open("util/data_path.txt", mode="w", encoding="utf-8") as f:
            f.write(arquivo)

    def executar_concatenacao(self):
        """Instancia a classe ConcatenarPlanilhas e executa a concatenação"""
        concatenador = ConcatenarPlanilhas()
        # Assumindo que o método de concatenação se chama concatenar_planilhas
        concatenador.concatenar_planilhas()  # Substitua por o nome do método correto
        print("Você clicou em executar")
        

# Criando a janela principal e o frame



def abrir(JanelaPrincipal, SelecaoArquivo):
    root = JanelaPrincipal().root
    app = SelecaoArquivo(master=root)
    app.mainloop()

if __name__ == "__main__":
    abrir(JanelaPrincipal, SelecaoArquivo)