FROM python:3.8

WORKDIR /app/accountingservice

EXPOSE 5002

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "accountingservice.py"]