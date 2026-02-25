FROM python:3.13-slim

WORKDIR /app
COPY server.py .

RUN mkdir -p /srv/images

EXPOSE 6969

CMD ["python", "server.py"]
