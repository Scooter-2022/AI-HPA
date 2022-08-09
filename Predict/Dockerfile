FROM python:3.6.13
 
WORKDIR /model
COPY ./requirements.txt /model/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /model/requirements.txt 

COPY ./model.py /model/model.py
COPY ./server.py /model/server.py
COPY ./bi_lstm_model0.h5 /model/bi_lstm_model0.h5

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "4000"]

