import pandas as pd


data = pd.read_csv('Data\Raw\WA_Fn-UseC_-Telco-Customer-Churn.csv')

def initial_inspection(dataset):
    numero_filas_columnas = f'Numero de filas y columnas: {dataset.shape}'
    titulo_info = 'Informacion completa:'
     
    suma_nulos = f'Suma valores nulos: {dataset.isnull().sum()}'
    suma_duplicados = f'suma de los duplicados: {dataset.duplicated().sum()}'

    print(titulo_info)
    dataset.info()

    return numero_filas_columnas,suma_nulos, suma_duplicados

