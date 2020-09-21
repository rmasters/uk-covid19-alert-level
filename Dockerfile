FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . ./

ENV FLASK_APP=covid_alert_levels
ENV FLASK_ENV=production

EXPOSE 8000
CMD ["uwsgi", "--host=0.0.0.0", "--port=8000", ""]
