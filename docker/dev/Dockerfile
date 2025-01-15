# syntax=docker/dockerfile:experimental
FROM python:3.13.1-bullseye

ENV RABBITMQ_HOST=host.docker.internal
	
RUN pip install hatch

WORKDIR /app
COPY pyproject.toml .
COPY LICENSE .
COPY *.md .
COPY src/ src/
RUN pip install -e .
RUN pip install -e .[test]

RUN echo "PS1='\[\033[01;32m\]c2_treatment_beneficense_valuator@dev\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\] \$ '" >> /root/.bashrc
RUN echo "alias run=\"RABBITMQ_HOST=host.docker.internal python src/c2_treatment_beneficence_valuator\"" >> /root/.bashrc
RUN echo "alias testAll=\"hatch test\"" >> /root/.bashrc
RUN echo "alias coverage=\"hatch test --cover\"" >> /root/.bashrc
RUN echo "alias test=\"hatch test -vv \"" >> /root/.bashrc
