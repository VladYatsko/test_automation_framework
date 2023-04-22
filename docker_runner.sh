#!/usr/bin/env bash

PYTEST_CMD="pytest --alluredir=alluredir=/app/test_automation_framework/results/ --reruns 5 ./tests/"

echo "Running tests..."
$PYTEST_CMD
