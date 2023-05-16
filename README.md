This is a Python implementation of the [Specmatic Order BFF Service](https://github.com/znsio/specmatic-order-ui) project.  
The implementation is based on [Python Flask](https://flask.palletsprojects.com/en/2.3.x/)

The open api contract for the services is defined in the [Specmatic Central Contract Repository](https://github.com/znsio/specmatic-order-contracts/blob/main/in/specmatic/examples/store/api_order_v1.yaml)

The order bff service internally calls the order api service (on port 8080).

The purpose of this project is to demonstrate how specmatic can be used to validate the contract of the bff service while stubbing out the order api service at the same time.  

```Dev Setup```

- Install Python 3.11 ( use homebrew if you are on mac os)


- Install pip


- Install virtualenv by running:  
  ```pip install virtualenv```


- Clone the git repository


- **Virtual Environment Setup** 
  - Create a "virtual environment" named 'venv' by running:  
    ```virtualenv venv ```  

      This will create a virtual environment using the default python installation.  
      If you wish to provide a specific python installation, run:  
    ```virtualenv venv --python="/opt/homebrew/Cellar/python@3.11/3.11.3/libexec/bin/python"```  

  - To activate your virtual environment, execute this from a terminal window in your root folder:  
    ```source venv/bin/activate```  


- **Install project requirements**  
    From a terminal window in your root folder, run:  
    ``` pip install -r requirements.txt```  
    Reload the virtual env:  
    ```deactivate```   
    ```source venv/bin/activate```   

  
- **Run Tests**  
  Download the Specmatic standalone jar from the [specmatic website](https://specmatic.in/getting_started.html)  
  Open a terminal window in the root folder and run:  
  ```pytest test -v -s```
    
 