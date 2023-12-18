FROM python:3.7

WORKDIR /

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m pip install -r /tmp/requirements.txt
ADD ./templates ./templates
ADD main.py main.py
ADD requirements.txt requirements.txt

ENTRYPOINT ["python3"]
CMD ["main.py"]
