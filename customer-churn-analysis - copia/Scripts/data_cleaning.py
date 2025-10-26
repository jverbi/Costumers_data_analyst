import pandas as pd
import data_preprocessing as d
import numpy as np

dataset = d.data.copy()

def clean_data(data):
    #Sustituir los espacios en blanco (' ') por el valor nulo estándar de Pandas (np.nan)
    data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)

    #Convertir la columna al tipo numérico (float)
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'])

    # Simplificar categorías
    replace_cols = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies']
    for col in replace_cols:
        if col in data.columns:
            data[col] = data[col].replace({'No internet service': 'No'})

    # Manipular valores null
    data = data.dropna()

    data = data.reset_index(drop=True)

    # Eliminar duplicados
    data = data.drop_duplicates()

    # pasar a un archivo csv
    data.to_csv(r'C:\Users\User\Documents\customer-churn-analysis\Data\cleaned_data')

    return data

