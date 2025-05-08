FROM python:3.6-slim
USER root
RUN apt update -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
