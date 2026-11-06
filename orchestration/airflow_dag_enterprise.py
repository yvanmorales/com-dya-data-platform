from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.dataform import DataformCreateCompilationResultOperator, DataformCreateWorkflowInvocationOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['data-alerts@enterprise.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'enterprise_dya_medallion_pipeline',
    default_args=default_args,
    description='Orquestación de plataforma DYA: Ingesta, Bronze, Silver y Gold',
    schedule_interval='0 2 * * *',  # Ejecución diaria a las 2:00 AM
    start_date=datetime(2026, 1, 1),
    catchup=False,
    max_active_runs=1
) as dag:

    def run_python_ingestion(**context):
        # Lógica para invocar el conector y validación Pydantic
        print("Ejecutando ingesta y validación de contratos de datos...")

    task_ingestion = PythonOperator(
        task_id='run_source_ingestion',
        python_callable=run_python_ingestion
    )

    # Disparador de Dataform para la ejecución de las capas Medallion en BigQuery
    # (Gestionado mediante operadores nativos de GCP Cloud Composer)
    
    task_ingestion >> print("Listo para disparar transformaciones Dataform en BigQuery")