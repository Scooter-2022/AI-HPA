FROM python:3.8.13-alpine 

RUN pip install requests

WORKDIR /aihpa
COPY utils.py .
COPY workflow.py .

CMD ["python3", "./workflow.py"]

