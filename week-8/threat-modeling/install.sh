#!/bin/env bash

brew install pandoc java
pip3 install -r pytm/requirements-dev.txt
curl -L -O https://downloads.sourceforge.net/project/plantuml/plantuml.jar
