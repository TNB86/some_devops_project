FROM python:3.11
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . code
WORKDIR /code
EXPOSE 8000
ENTRYPOINT ["python3", "simple_web_app/manage.py"]
CMD ["runserver", "127.0.0.1:8000"]
