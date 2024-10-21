
class Constants():
    def __init__(self):
        self.DATA_PATH: str = self.get_data_path()
        self.DATA_SAIDA:str = self.get_data_saida()
        pass

    def get_data_path(self):
        data_path_txt = "util/data_path.txt"
        try:
            with open(data_path_txt, mode="x") as f:
                ...
        except FileExistsError:
            pass
        with open("util/data_path.txt", mode="r", encoding="utf-8") as f:
            data_path = f.read()
            return data_path

    def get_data_saida(self):
        data_path_txt = "util/data_saida.txt"
        try:
            with open(data_path_txt, mode="x") as f:
                ...
        except FileExistsError:
            pass
        with open("util/data_saida.txt", mode="r", encoding="utf-8") as f:
            data_saida = f.read()
            return data_saida
