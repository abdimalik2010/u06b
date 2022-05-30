FROM python:3.8

ADD linux.py .

ADD Linuxhotd.db .

ADD Linux-Logo-1996-present.png .

COPY requirments.txt .

RUN pip install -r ./requirments.txt


CMD ["python", "./linux.py"]


