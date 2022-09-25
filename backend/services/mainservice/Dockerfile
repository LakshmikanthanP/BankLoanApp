FROM python:3.8

WORKDIR /app

EXPOSE 5000

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "mainservice.py"]