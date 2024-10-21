import pandas as pd
from util.constants import Constants

class ConcatenarPlanilhas():
    def __init__(self):
        self.df_empresas = pd.read_excel(Constants().DATA_PATH, sheet_name="Dados Empresas")
        self.df_contatos = pd.read_excel(Constants().DATA_PATH, sheet_name="Dados Contatos")
        self.df = self.cria_df()
        pass


    def transformar_telefone(self):
        # tamanho_df_empresa = len(self.df_empresas)
        # filtro_telefone = [f"{self.df_empresas["DDD"][n]}{self.df_empresas["TELEFONE"][n]}" for n in range(tamanho_df_empresa)]
        # self.df["TELEFONE"] = filtro_telefone

        # tamanho_df_contatos = len(self.df_contatos)
        # filtro_contato1 = [f"{self.df_contatos["DDD CEL1"][n]}{self.df_contatos["CEL1"][n]}" for n in range(tamanho_df_contatos)]
        # self.df["CELULAR 1"] = filtro_contato1

        # filtro_contato2 = [f"{self.df_contatos["DDD CEL2"][n]}{self.df_contatos["CEL2"][n]}" for n in range(tamanho_df_contatos)]
        # self.df["CELULAR 2"] = filtro_contato2
        ...

    def cria_df(self):
        lista_cnpj = []
        lista_nome_empresa = []
        lista_segmento = []
        lista_cidade = []
        lista_estado = []
        lista_telefone = []
        lista_cargo = []
        lista_nome = []
        lista_participacao = []
        lista_celular1 = []
        lista_celular2 = []
        lista_email = []


        tamanho_df_contatos = len(self.df_contatos)
        for n in range(tamanho_df_contatos):
            cnpj = self.df_contatos.iloc[n]["CNPJ"]
            # print(cnpj)
            empresa = self.df_empresas.loc[self.df_empresas["CNPJ"] == cnpj]
            nome_empresa = empresa["NOME EMPRESA"].iloc[0]
            # print(nome_empresa)
            segmento = empresa["SEGMENTO"].iloc[0]
            # print(segmento)
            cidade = empresa["CIDADE"].iloc[0]
            # print(cidade)
            estado = empresa["ESTADO"].iloc[0]
            # print(estado)
            telefone = f"{empresa["DDD"].iloc[0]}{empresa["TELEFONE"].iloc[0]}"
            # print(telefone)
            cargo = self.df_contatos.iloc[n]["CARGO"]
            nome = self.df_contatos.iloc[n]["NOME"]
            participacao = self.df_contatos.iloc[n]["PARTICIPAÇÃO"]
            ddd_celular1 = self.df_contatos.iloc[n]["DDD CEL1"]
            ddd_celular2 = self.df_contatos.iloc[n]["DDD CEL2"]
            celular1 = ddd_celular1 + self.df_contatos.iloc[n]["CEL1"]
            celular2 = ddd_celular2 + self.df_contatos.iloc[n]["CEL2"]
            email = self.df_contatos.iloc[n]["E-MAIL"]

            lista_cnpj.append(cnpj)
            lista_nome_empresa.append(nome_empresa)
            lista_segmento.append(segmento)
            lista_cidade.append(cidade)
            lista_estado.append(estado)
            try:
                lista_telefone.append(int(telefone))
            except:
                lista_telefone.append(telefone)

            lista_cargo.append(cargo)
            lista_nome.append(nome)
            lista_participacao.append(participacao)
            lista_celular1.append(celular1)
            lista_celular2.append(celular2)
            lista_email.append(email)


            data = {"CNPJ":lista_cnpj,
                    "NOME EMPRESA":lista_nome_empresa,
                    "SEGMENTO":lista_segmento,
                    "CIDADE":lista_cidade,
                    "ESTADO":lista_estado,
                    "TELEFONE":lista_telefone,
                    "CARGO":lista_cargo,
                    "NOME":lista_nome,
                    "PARTICIPAÇÃO":lista_participacao,
                    "CELULAR 1":lista_celular1,
                    "CELULAR 2":lista_celular2,
                    "E-MAIL":lista_email,}

        df = pd.DataFrame(data=data)
        return df
    
    def salvar(self):
        with pd.ExcelWriter(Constants().DATA_SAIDA) as writer:
            self.df.to_excel(writer, "Dados CRM",index=False)
            self.df_empresas.to_excel(writer, "Dados Empresas", index=False)
            self.df_contatos.to_excel(writer, "Dados Contatos", index=False)
