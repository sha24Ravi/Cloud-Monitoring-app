FROM python:3.13.0-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN  pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["python", "-m", "flask", "run"]
