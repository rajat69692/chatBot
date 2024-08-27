FROM python:3.10-slim
 
WORKDIR /app
 
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080
 
COPY . .

CMD streamlit run --server.port 8080 --server.enableCORS false app.py
 