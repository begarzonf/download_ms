FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /download
WORKDIR /download
ADD . /download/
RUN pip install -r requirements.txt
CMD python manage.py runserver
EXPOSE 8005