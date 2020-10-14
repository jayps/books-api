FROM python:3.8.6-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
COPY ./requirements.txt /code
WORKDIR /code
# Add --no-cache to the line below to skip caching.
RUN pip install -r requirements.txt

COPY . /code
EXPOSE 8000
ENTRYPOINT sh entrypoint.sh
