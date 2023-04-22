# test_automation_framework

## About this framework:
Current framework was created to test functionality of https://parabank.parasoft.com/parabank/index.htm web application. Current framework was created using Python + Selenium. Due to some issue with server please note that applicable time to run tests is after 4 p.m. UTC/GMT+2.

## How to run tests:
First of all it's required to clone this repository using:
```git
git clone https://github.com/VladYatsko/test_automation_framework.git
```

Then you need to install all the dependencies:
```
pip install -r requirements.txt
```

After all the actions above are performed you can run tests with three ways:
1) With default Python commands from framework root folder: 
```
pytest --alluredir=results --reruns 5 .\tests\   
```
After tests are finished you need to run:
```
allure serve results 
```
To generate allure report.

2) With running test_runner.bat for Windows to avoid typing commands 2 times.
3) For Unix/macOS there is test_runner.sh file, but to run it you need first run
```bash
chmod +x ./test_runner.sh
```
Then execute file with similar snippet as for Windows OS.

## How to run from Docker:
Current tests can be executed from docker in headless mode. To perform it you need to create your own image with running:
```
docker build . -t [image_name]
```
Then you need to run a container with test runner:
```
docker run --rm --name [container_name] [image_name]
```