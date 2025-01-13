# syntax=docker/dockerfile:experimental
FROM python:3.9.19-bullseye

RUN apt-get -qy update && \
    apt-get -qy full-upgrade && \
    apt-get -qy install pip
	
WORKDIR /app

COPY setup.py .
COPY requirements.txt .
COPY LICENSE .
COPY *.md .
COPY asyncapi.yaml .
COPY C2_treatment_beneficense_valuator/ C2_treatment_beneficense_valuator/

RUN --mount=type=cache,target=/root/.cache/pip pip install -e .

ENV RABBITMQ_HOST=mov-mq
ENV RABBITMQ_PORT=5672.
ENV RABBITMQ_USERNAME=mov.
ENV RABBITMQ_PASSWORD=password
ENV RABBITMQ_MAX_RETRIES=100
ENV RABBITMQ_RETRY_SLEEP=3

ENV LOG_CONSOLE_LEVEL=DEBUG
ENV LOG_FILE_LEVEL=DEBUG
ENV LOG_FILE_MAX_BYTES=1000000
ENV LOG_FILE_BACKUP_COUNT=5

HEALTHCHECK CMD test -s /app/{$LOG_DIR:-logs}/{$COMPONET_ID_FILE_NAME:-component_id.json}

CMD ["python", "C2_treatment_beneficense_valuator"]