FROM python:alpine
USER root
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache dos2unix
RUN chmod +x ./test_runner.sh
RUN dos2unix test_runner.sh
CMD ["sh", "./test_runner.sh"]