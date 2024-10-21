import pandas as pd
from util.constants import Constants

class ConcatenarPlanilhas():
    def __init__(self):
        self.df = pd.read_excel(Constants().DATA_PATH)
        pass

    def concatenar_planilhas(self):
        ...