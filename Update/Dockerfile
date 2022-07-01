FROM python:3.8.13-alpine 

WORKDIR /aihpa
COPY utils.py .
COPY workflow.py .
COPY ./pkg ./pkg
WORKDIR ./pkg/requests-2.28.0
RUN python3 setup.py install

WORKDIR /aihpa
CMD ["python3", "./workflow.py"]

