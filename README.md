
# Specmatic Sample: Flask BFF calling Domain API

* [Specmatic Website](https://specmatic.in)
* [Specmatic Documenation](https://specmatic.in/documentation.html)

This sample project demonstrates how we can practice contract-driven development and contract testing in a Flask (Python) application that depends on an external domain service. Here, Specmatic is used to stub calls to domain API services based on its OpenAPI specification.

Here is the domain api [contract/open api spec](https://github.com/znsio/specmatic-order-contracts/blob/main/in/specmatic/examples/store/api_order_v3.yaml)

## Definitions

* BFF: Backend for Front End
* Domain API: API managing the domain model
* Specmatic Stub/Mock Server: Create a server that can act as a real service using its OpenAPI or AsyncAPI spec

## Background

A typical web application might look like this. We can use Specmatic to practice contract-driven development and test all the components mentioned below. In this sample project, we look at how to do this for Flask BFF, which is dependent on the Domain API Service, demonstrating OpenAPI support in **Specmatic**.

![HTML client talks to client API which talks to backend API](assets/specmatic-order-bff-architecture.gif)

## Tech

1. Flask
2. Specmatic
3. PyTest
4. Coverage

## Setup

1. Install [Python 3.12](https://www.python.org/)
2. Install JRE 17 or later.

## Setup Virtual Environment

1. ### Create a virtual environment named **.venv** by running this in project's root folder

   ```shell
    python -m venv .venv
    ```

2. ### Activate virtual environment by running

   * **on MacOS and Linux**

      ```shell
      source .venv/bin/activate
      ```

   * **on Windows CMD**

     ```cmd
     .venv\Scripts\activate.bat
     ```

   * **on Windows Powershell ( might  have  to  modify ExecutionPolicy )**

     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

## Install Dependencies

To install all the required dependencies for this project, from a terminal window in the project's root folder, run:

```shell
pip install -r requirements.txt
```

## Run Tests and Validate Contracts using Specmatic

This will start the specmatic stub server for domain api using the information in specmatic.json and run the pytest tests on Flask that expects the domain api at port 8080.

```shell
pytest test -v -s
```
