

C**reated automated test script for Random Data API for three end points:-**</br>
**Credit Card-** </br>https://random-data-api.com/api/v2/credit_cards</br>
https://random-data-api.com/api/v2/beers</br>
https://random-data-api.com/api/v2/addresses

Result - Credit Card Endpoint

**Tech Stack**

Python 3.12</br>
Pytest Framework</br>
Using Request Module</br>
Reporting allure Report</br>
Test Cases generation</br>

**Install the required modules to run this framework**

-pip install requests pytest pytest-html allure-pytest

**How to run test cases parallel**

pip install pytest-xdist

**How to run single test cases**

pytest -s src/tests/test_sample.py --alluredir=allure_result

**To see the detailed allure report, run the below command-**

allure serve allure_result

![image](https://github.com/user-attachments/assets/dab9b985-c282-4936-9f38-a93e6b7461e2)
