FROM python:3.12.2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

# EXPOSE 8000
WORKDIR /app

# Shouldn't need to set --app-dir, but was failing
CMD ["uvicorn", "main:app", "--reload", "--app-dir", "app"]