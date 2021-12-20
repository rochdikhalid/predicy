# Predicy
A simple machine learning based web application built with **Flask** to predict real estate prices in New Delhi.
## Notebook Setup
* **1-** Go to the [Anaconda website](https://www.anaconda.com/) to install *Anaconda*, it's preferable to have the latest version of Python for the appropriate architecture.

* **2-** Use **Jupyter** or **Jupyter lab** to open up the notebook.
## Application Setup
* **1-** Use the **requirement.txt** file to install the dependencies:

         pip install -r requirements.txt
  ### Virtual Environment Configuration (optional)
  * **a-** Create a new virtual environment using the following command:
  
           python3 -m venv <name_of_virtualenv>
  * **b-** Install the dependencies as highlighted below using the **requirement.txt** file:
  
           pip install -r requirements.txt
  * **c-** Make sure all dependencies are installed correctly:
  
           pip freeze
* **2-** Run the **Flask** server using the following command:

         python run.py
* **3-** Navigate to **http://127.0.0.1:5000/** and start playing around with **Predicy**.
