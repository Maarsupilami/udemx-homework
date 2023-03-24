FROM python:3.12.0a6-alpine3.17

WORKDIR /app
COPY src/ .

RUN pip install -r requirements.txt

RUN apk update && \
    apk add --no-cache curl

HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -f http://localhost:8080/status || exit 1

EXPOSE 5000

CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:5000 app:app"]