#!/bin/bash

services=("ProductComponent" "UserComponent")

for service in "${services[@]}"
do
  chmod -x "$service/tests.py"
  python3 "$service/tests.py"
done