#!/bin/bash

services=("UserComponent" "ProductComponent")

for service in "${services[@]}"
do
  chmod -x "$service/tests.py"
  pytest "$service/tests.py"
done