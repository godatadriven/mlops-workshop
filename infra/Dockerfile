FROM python:3.10-slim-buster

RUN pip install mlflow

EXPOSE 5000

RUN mkdir mlruns
RUN mkdir mlartifacts

CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "sqlite:///mlruns/mlruns.db"]
