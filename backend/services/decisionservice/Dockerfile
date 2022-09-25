FROM python:3.8

WORKDIR /app/decisionservice

EXPOSE 5001

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "decisionengine.py"]