FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY InionBlog /app/InionBlog

EXPOSE 8000

CMD ["python", "/app/InionBlog/manage.py", "runserver", "0.0.0.0:80"]
