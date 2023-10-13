#!/bin/sh -f

set -e
mvn clean package
cp target/StoreWebService-0.0.1-SNAPSHOT.jar ../..
