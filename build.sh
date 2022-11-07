#!/bin/bash

services=("BankingComponent" "FoodComponent")

for service in $services
do
    s=$(echo "$service" | tr '[:upper:]' '[:lower:]')
    image="ghcr.io/lassebirk96/$s:latest"
    docker build -t $image . --build-arg COMPONENT_PATH=$service
    docker push $image
done