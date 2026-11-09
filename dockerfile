FROM python:3.13.11-slim
WORKDIR /Employee CRUD
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
