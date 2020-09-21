FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . ./

ENV FLASK_APP=covid_alert_levels
ENV FLASK_ENV=production

EXPOSE 8000
#CMD ["uwsgi", "--http=0.0.0.0:8000", "--manage-script-name", "--mount=/=covid_alert_levels.wsgi:application"]
CMD ["mypy", "covid_alert_levels"]
