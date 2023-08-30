# Restaurant Review System


## Introduction

This repo contains code for a restaurant review system for Phase 3 Week 2 Code Challenge based on python classes and instances, class and instance methods, variable scope, object relationships, and lists and list methods working with a Yelp-style domain.

This project utilizes the `pytest` library for testing purposes. The `pytest framework` makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

*The test suite encompases all deliverables for this code challenge. All tests should be passing.*

## Table of Contents
- [Technologiesused](#technologiesused)
- [Installation](#installation)
- [Usage](#usage)

- [Author & License](#author--license)

## Technologies used
![python version](https://img.shields.io/badge/python-3.10.12+-blue.svg)
![pytest version](https://img.shields.io/badge/pytest-7.1.3+-cyan.svg)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JOY19ANYANGO/phase3-wk2-challenge.git
```

### 2. Navigate to the project's directory

```bash
cd phase3-wk2-challenge
```

### 3. Install all the required dependencies

The root directory of this repository contains the `Pipfile` with all the required Python libraries for this project and restricts them to this repository.

To install `pytest` and any other required libraries, run:

```python
pipenv install
```

### 4. Enter the pipenv shell

```python
pipenv shell
```

### 5. Use pytest to run the test suite

```python
 pytest restaurants/test.py 
``` 

## Usage

You can use the Restaurant Review System to simulate interactions between customers, restaurants, and reviews. Follow these steps to get started:
Do this in main.py file
1. Create customer and restaurant instances.
2. Add reviews using the add_review method.
3. Retrieve information about customers, restaurants, and reviews using the provided methods.
4. Run `python3 main.py` in your terminal to see the output


## Author & License

Authored by [Joy Anyango](https://github.com/JOY19ANYANGO).

Licensed under the [MIT License]((https://choosealicense.com/licenses/mit/)) 