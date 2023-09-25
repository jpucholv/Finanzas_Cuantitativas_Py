import pandas as pd

path = r'.\2024_1_data\^VIX.csv'

# Cargar el archivo CSV
df = pd.read_csv(path)

# Convertir la columna de fechas al formato deseado
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')

# Guardar el DataFrame de nuevo en un archivo CSV
df.to_csv(path, index=False)