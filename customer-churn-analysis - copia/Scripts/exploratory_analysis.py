import pandas as pd

import pandas as pd

# Cargar datos
data_for_exploratory = pd.read_csv(r'Data\cleaned_data.csv')
data_for_exploratory.columns = data_for_exploratory.columns.str.strip()  # Eliminar espacios

def datos_exploratory_completo(data):
    """Calcula suma y porcentaje de churn por variables clave."""
    
    # Normalizar texto
    data['Churn'] = data['Churn'].str.lower().str.strip()
    data['Churn_numeric'] = data['Churn'].map({'yes': 1, 'no': 0})
    
    # Función auxiliar para calcular porcentaje
    def churn_percentage(group):
        return round(group.mean() * 100, 2) # Convertir a porcentaje
    
    # Churn por tipo de contrato
    churn_contract_sum = data.groupby('Contract')['Churn_numeric'].sum().sort_values(ascending=False)
    churn_contract_pct = data.groupby('Contract')['Churn_numeric'].apply(churn_percentage).sort_values(ascending=False)
    
    # Churn por método de pago
    churn_payment_sum = data.groupby('PaymentMethod')['Churn_numeric'].sum().sort_values(ascending=False)
    churn_payment_pct = data.groupby('PaymentMethod')['Churn_numeric'].apply(churn_percentage).sort_values(ascending=False)
    
    # Churn por servicios contratados
    churn_service_sum = data.groupby(['InternetService', 'OnlineSecurity', 'StreamingMovies'])['Churn_numeric'].sum().sort_values(ascending=False)
    churn_service_pct = data.groupby(['InternetService', 'OnlineSecurity', 'StreamingMovies'])['Churn_numeric'].apply(churn_percentage).sort_values(ascending=False)
    
    # Churn vs. antigüedad del cliente
    churn_tenure_sum = data.groupby('tenure')['Churn_numeric'].sum()
    churn_tenure_pct = data.groupby('tenure')['Churn_numeric'].apply(churn_percentage)
    
    return {
        'Contract': {'sum': churn_contract_sum, 'pct': churn_contract_pct},
        'PaymentMethod': {'sum': churn_payment_sum, 'pct': churn_payment_pct},
        'Services': {'sum': churn_service_sum, 'pct': churn_service_pct},
        'Tenure': {'sum': churn_tenure_sum, 'pct': churn_tenure_pct}
    }

# Ejecutar análisis exploratorio
resultados_churn = datos_exploratory_completo(data_for_exploratory)

# Ejemplo de cómo ver resultados
#print("Churn por contrato (porcentaje):")
#print(resultados_churn['Contract']['pct'])
#print("\nChurn por contrato (suma):")
#print(resultados_churn['Contract']['sum'])