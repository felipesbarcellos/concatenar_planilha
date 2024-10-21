from logging import config
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import filedialog
from app.concatenar_planilhas import ConcatenarPlanilhas
from util.constants import Constants

class JanelaPrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.frame_label = ttk.Frame(self.root)
        self.frame_label.pack()

        self.label_explicativa = tk.Label(self.frame_label, text="Clique no botão para selecionar o arquivo de entrada.")
        self.label_explicativa.pack()

        self.caminho_frame = ttk.Frame()
        self.caminho_frame.pack()

        # Rótulo para exibir o caminho do arquivo
        self.caminho_label = tk.Label(self.caminho_frame, text="Caminho do arquivo:")
        self.caminho_label.pack(side="left")

        # Entrada para exibir o caminho completo
        self.caminho_entry = tk.Entry(self.caminho_frame, width=50)
        self.caminho_entry.pack(side="left")

        self.caminho_entry.insert(0, Constants().DATA_PATH)

        self.botao_selecionar = tk.Button(self.caminho_frame, text="Selecionar Arquivo", command=self.selecionar_arquivo_entrada)
        self.botao_selecionar.pack(side="left")

        self.caminho_frame2 = ttk.Frame()
        self.caminho_frame2.pack()

        # Rótulo para exibir o caminho do arquivo
        self.caminho_label2 = tk.Label(self.caminho_frame2, text="Saida do arquivo:")
        self.caminho_label2.pack(side="left")

        # Entrada para exibir o caminho completo
        self.caminho_entry2 = tk.Entry(self.caminho_frame2, width=50)
        self.caminho_entry2.pack(side="left")

        self.caminho_entry2.insert(0, Constants().DATA_SAIDA)

        self.botao_selecionar2 = tk.Button(self.caminho_frame2, text="Escolher local de saida", command=self.selecionar_arquivo_saida)
        self.botao_selecionar2.pack()

        self.frame_label2 = ttk.Frame(self.root)
        self.frame_label2.pack()

        self.label_explicativa2 = tk.Label(self.frame_label2, text="Clique no botão para selecionar o arquivo de saida.")
        self.label_explicativa2.pack()


        self.botao_frame = tk.Frame(self.root)
        self.botao_frame.pack()

        # Botão para selecionar o arquivo


        # Botão para executar a concatenação
        self.botao_executar = tk.Button(self.botao_frame, text="Executar Concatenação", command=self.executar_concatenacao, bg="blue", fg="white", border=1)
        self.botao_executar.pack()

        self.frame_sair = tk.Frame(self.root)
        self.frame_sair.pack()

        self.botao_sair = tk.Button(self.frame_sair, text="SAIR", fg="white", bg="red", command=self.sair)
        self.botao_sair.pack()
        self.root.mainloop()

    def construir_janela(self):
        frame = ttk.Frame()
        return frame

    def sair(self):
        self.root.destroy()

    def selecionar_arquivo_entrada(self):
        """Abre um diálogo para o usuário selecionar um arquivo e atualiza o rótulo."""
        arquivo = filedialog.askopenfilename()
        self.caminho_entry.delete(0, tk.END)
        self.caminho_entry.insert(0, arquivo)
        with open("util/data_path.txt", mode="w", encoding="utf-8") as f:
            f.write(arquivo)

    def selecionar_arquivo_saida(self):
        """Abre um diálogo para o usuário selecionar um arquivo e atualiza o rótulo."""
        arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                          filetypes=[("Todos os arquivos", "*.*"),
                                                    ("Arquivos do excel", "*.xlsx")])
        self.caminho_entry2.delete(0, tk.END)
        self.caminho_entry2.insert(0, arquivo)
        with open("util/data_saida.txt", mode="w", encoding="utf-8") as f:
            f.write(arquivo)

    def executar_concatenacao(self):
        """Instancia a classe ConcatenarPlanilhas e executa a concatenação"""
        concatenador = ConcatenarPlanilhas()
        # Assumindo que o método de concatenação se chama concatenar_planilhas
        concatenador.salvar()  # Substitua por o nome do método correto
        frame = ttk.Frame()
        frame.pack()
        label = ttk.Label(frame, text="Planilha criada com sucesso")
        label.pack()
        print("Você clicou em executar")
class SelecaoArquivo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Tórulo para exibir a explicação
        


        

# Criando a janela principal e o frame


def abrir():
    app = JanelaPrincipal()
    app.mainloop()

if __name__ == "__main__":
    abrir(JanelaPrincipal)