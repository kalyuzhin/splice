FROM python:3.12-slim
WORKDIR backend/
COPY ./requirements.txt /backend/
RUN pip3 install -U pip && pip3 install -Ur requirements.txt
COPY . /backend/
EXPOSE 8080

CMD ["scripts/startup.sh"]
