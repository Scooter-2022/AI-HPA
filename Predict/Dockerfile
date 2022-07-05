FROM python:3.8.10
 
WORKDIR /model
COPY ./requirements.txt /model/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /model/requirements.txt 

COPY ./model.py /model/model.py
COPY ./server.py /model/server.py

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "4000"]

