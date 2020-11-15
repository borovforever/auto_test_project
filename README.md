Put the chromedriver file in project root folder

To run the test in chrome type in terminal:

pytest --browser_name=chrome --language=en test_file_name.py

To change languages use:
 - en
 - ru
 - es
 e t.c.
 
 --------
 
To run the test in firefox type in terminal:


pytest --browser_name=firefox --language=en test_file_name.py

Language's parameters are the same as for chrome.

---------

To run tests with allure reports generating:

pytest -s -v --tb=line --language=en --alluredir reports test_file_name.py