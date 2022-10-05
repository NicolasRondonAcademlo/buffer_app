#
FROM python:3.9

WORKDIR /code

COPY ./requirements /code/requirement

RUN pip install --no-cache-dir --upgrade -r /code/requirement/base.txt

#
COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
