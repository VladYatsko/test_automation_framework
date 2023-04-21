FROM python:alpine
USER root
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x test_runner.sh
CMD ["pytest", "./tests/test_api.py"]