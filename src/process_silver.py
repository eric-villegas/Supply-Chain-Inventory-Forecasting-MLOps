import boto3
import pandas as pd
import io
import os

def process_retail_to_silver():
    # 1. Configuración - CAMBIA EL NOMBRE DE TU BUCKET AQUÍ
    BUCKET_NAME = "tu-nombre-de-bucket-aqui" 
    s3 = boto3.client('s3')
    
    print(f"Reading from s3://{BUCKET_NAME}/bronze/...")
    
    try:
        # 2. Descargar el archivo (Capa Bronze)
        # Asegúrate de que el nombre del archivo coincida con el que subiste
        response = s3.get_object(Bucket=BUCKET_NAME, Key='bronze/online_retail_II.xlsx')
        data = response['Body'].read()
        
        # 3. Procesamiento con Pandas
        # Usamos engine='openpyxl' porque es un archivo .xlsx
        df = pd.read_excel(io.BytesIO(data), engine='openpyxl')
        
        # Limpieza profesional (Estándar MLOps)
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        
        # En el dataset de UCI, las columnas clave son 'customer_id', 'quantity' y 'price'
        df_clean = df.dropna(subset=['customer_id'])
        df_clean = df_clean[(df_clean['quantity'] > 0) & (df_clean['price'] > 0)]
        
        print(f"Cleaned data: {len(df_clean)} records. Converting to Parquet...")

        # 4. Guardar en formato Parquet (Ahorra 80% de espacio y es más rápido)
        parquet_buffer = io.BytesIO()
        df_clean.to_parquet(parquet_buffer, index=False)
        
        # 5. Subir a la Capa Silver
        s3.put_object(
            Bucket=BUCKET_NAME, 
            Key='silver/retail_cleaned.parquet', 
            Body=parquet_buffer.getvalue()
        )
        print("✅ Success: Data saved to Silver Layer in Parquet format.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    process_retail_to_silver()
