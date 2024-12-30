FROM python:3.12-slim
WORKDIR app/
COPY ./requirements.txt /app/
RUN pip3 install -U pip && pip3 install -Ur requirements.txt
COPY . /app/
EXPOSE 8080

#CMD ["uvicorn","--reload",""]