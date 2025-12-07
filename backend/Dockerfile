FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
jenkins@ip-172-31-84-79:~/workspace/NUEL-BANK-APP/backend$
