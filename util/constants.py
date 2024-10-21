
class Constants():
    def __init__(self):
        self.DATA_PATH: str = self.get_data_path()
        pass

    def get_data_path(self):
        with open("util/data_path.txt", mode="r", encoding="utf-8") as f:
            data_path = f.read()
            return data_path
