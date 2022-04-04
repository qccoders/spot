FROM python:3.10

COPY ./server/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server /code

# TODO: Add frontend
RUN mkdir /static

WORKDIR /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
