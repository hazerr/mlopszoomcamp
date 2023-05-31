import mlflow

# Ruta al archivo Python que deseas ejecutar
file_path = "/home/jovyan/register_model_modif.py"

# Ejecuta el archivo dentro del contexto de mlflow.start_run()
with mlflow.start_run():
    exec(open(file_path).read())
