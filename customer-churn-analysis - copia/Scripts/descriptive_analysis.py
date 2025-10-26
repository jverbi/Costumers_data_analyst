import pandas as pd


data = pd.read_csv(r'C:\Users\User\Documents\customer-churn-analysis\Data\cleaned_data.csv')


def descriptive_analysis(data_df):
    """
    Performs an initial descriptive analysis of the Telco Customer Churn dataset.
    Returns:
        dict: Key metrics and distributions including churn rate, customer status,
              contract types, payment methods, gender distribution, and tenure summary.
    """

    # Convertir columna 'Churn' a minúsculas para evitar errores de comparación
    data_df['Churn'] = data_df['Churn'].str.lower()
    data_df['Contract'] = data_df['Contract'].str.lower()

    #porcentaje total de clientes que abandonaron el servicio (churn)

    total_costomers = len(data_df)
    total_churn = len(data_df[data_df['Churn'] == 'yes'])
    churn_porcent = round((total_churn/total_costomers) * 100, 2)

    #clientes permanecen activos vs. los que se fueron
    active_costomer = len(data_df[data_df['Churn'] == 'no'])
    summary_customers = f'Hay {active_costomer} clientes activos y {total_churn} que se han ido'


    #distribucion del tipo de contrato (mensual, anual, bianual)
    distribution_contract = data_df['Contract'].value_counts()

    #métodos de pago son los más utilizados por los clientes

    payment_method  = data_df['PaymentMethod'].value_counts()      

    #distribuyen los clientes por género
    distribution_gender = data_df['gender'].value_counts()

    #rango de antigüedad (tenure) de los clientes
    tenure_summary = data_df['tenure'].describe().round(2)


    return {'porcentaje churn':churn_porcent, 
            'summary_customers':summary_customers, 
            'Distribucion_Contrato': distribution_contract,
            'Metodos_Pago': payment_method,
            'Distribucion_Genero': distribution_gender,
            'Resumen_Tenure': tenure_summary
    }

#results = descriptive_analysis(data)
#print("\n===== DESCRIPTIVE ANALYSIS REPORT =====")
#for key, value in results.items():
   # print(f"\n🔹 {key.upper()}:\n{value}")