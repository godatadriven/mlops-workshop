FROM python:3.10-slim-buster

# Install python packages
RUN pip install mlflow

EXPOSE 5000

CMD ["mlflow", "server", "--host", "0.0.0.0"]