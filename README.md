# Red Badger Coding Challenge

## Introduction
A command line application that reads a data file to control virtual robots.

## Set Up
The following is the response for the backend role and was developed on Mac OS X (10.14.3).

### Prerequisites
The following software is needed to execute this application:
* Python Python 3.6.7

### Setup: Python Virtual Environment
Tend to deploy applications to their own virtual environment to provide isolation, therefore you will need to do the same. Install & Activate the virtualenv (this assumes you are in the root of the application folder using a cli):
```bash
python3 -m venv .ve
source .ve/bin/activate
```

### Setup: Install Python Packages
This assumes you are in the root of the application folder using cli (and the virual environment has been activated):
```bash
pip3 install -r requirements.txt
pip3 install -r requirements-for-test.txt
```

## Execution
### Execution: Unit Tests
This assumes you are in the root of the application folder using cli:
```bash
python3 setup.py develop
pytest
```
