import os
import pandas as pd

# Importar módulos
import data_preprocessing as dp
#import initial_inspection as ii
import descriptive_analysis as da
import exploratory_analysis as ea


def main():
    """Función principal para ejecutar el flujo completo de análisis de churn."""
    raw_path = r"Data\Raw\WA_Fn-UseC_-Telco-Customer-Churn.csv"
    cleaned_path = r"Data\cleaned_data.csv"

    # 1️⃣ --- Inspección inicial ---
    print("🔍 [1] INSPECCIÓN INICIAL DE LOS DATOS")
    raw_data = pd.read_csv(raw_path)
    filas_columnas, suma_nulos, suma_duplicados = dp.inicial_inspection(raw_data)
    print(filas_columnas)
    print(suma_nulos)
    print(suma_duplicados)
    print("-" * 60)

    # 2️⃣ --- Limpieza de datos ---
    print("🧹 [2] LIMPIEZA DE DATOS")
    if not os.path.exists(cleaned_path):
        cleaned_data = dp.clean_data(raw_data)
        print("✅ Datos limpiados y guardados en:", cleaned_path)
    else:
        cleaned_data = pd.read_csv(cleaned_path)
        print("📂 Datos limpios ya existen, cargados desde archivo.")
    print("-" * 60)

    # 3️⃣ --- Análisis descriptivo ---
    print("📊 [3] ANÁLISIS DESCRIPTIVO")
    descriptive_results = da.descriptive_analysis(cleaned_data)
    for key, value in descriptive_results.items():
        print(f"\n🔸 {key}:\n{value}")
    print("-" * 60)

    # 4️⃣ --- Análisis exploratorio ---
    print("📈 [4] ANÁLISIS EXPLORATORIO")
    exploratory_results = ea.datos_exploratory_completo(cleaned_data)

    print("\n📊 Churn por contrato (%):")
    print(exploratory_results['Contract']['pct'])
    print("\n📊 Churn por método de pago (%):")
    print(exploratory_results['PaymentMethod']['pct'])

    print("\n✅ Flujo completo ejecutado correctamente.")


if __name__ == "__main__":
    main()
