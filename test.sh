#!/bin/bash

services=("UserComponent" "ProductComponent")

for service in "${services[@]}"
do
  chmod -x "$service/tests.py"
  python3 -m pytest "$service/tests.py"
done