FROM python:3.10-slim-buster

RUN pip install mlflow

EXPOSE 5000

CMD ["mlflow", "server", "--backend-store-uri", "sqlite:////mlflow/mlflow.db", "--default-artifact-root", "/mlflow", "--host", "0.0.0.0"]
