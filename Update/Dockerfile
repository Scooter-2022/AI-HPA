FROM python:3.8.13-alpine 

COPY request-metrics.py /
COPY ./pkg /pkg
WORKDIR /pkg/requests-2.28.0
RUN python3 setup.py install

CMD ["python3", "/request-metrics.py"]

