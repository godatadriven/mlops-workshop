FROM python:3.10-slim-buster

RUN pip install mlflow

EXPOSE 5000

# remove `"--backend-store-uri", "sqlite:///mlruns/mlruns.db"` to remove sqlite
CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "sqlite:///mlruns/mlruns.db"]
