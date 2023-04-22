#!/usr/bin/env bash

PYTEST_CMD="pytest --alluredir=results --reruns 5 ./tests/"

echo "Running tests..."
$PYTEST_CMD