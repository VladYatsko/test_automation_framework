FROM python:alpine
ENV PATH="/app:${PATH}"
USER root
RUN apk add --no-cache curl gnupg
RUN curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --import
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apk/repositories'
RUN apk update && apk upgrade
RUN apk add --no-cache chromium
RUN apk add --no-cache chromium-chromedriver
ENV PATH="/usr/bin/chromedriver:${PATH}"
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache dos2unix
RUN chmod +x ./docker_runner.sh
RUN dos2unix docker_runner.sh
CMD ["sh", "./docker_runner.sh"]