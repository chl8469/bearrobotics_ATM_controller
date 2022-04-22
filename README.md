# bearrobotics custom task
simple ATM controller Implementation. 

atm.py &#8594; ATM Implementation  
test_atm.py &#8594; test code(using pytest)  
testcase.py &#8594; test case
```plane text
test_users = {"card pin"(str): "password"(str)}
test_accounts = {"card pin"(str): balance(int)}
```
you can add test case if you want

<br>

# Requirements
* python 3.8+

<br>

# run project
you can test project manually
```bash
python main.py
```

or test automatically using pytest
```bash
$ pip install pytest==7.1.1
$ cd bearrobotics_ATM_controller
$ pytest -s -vv # -vv argument is optional
```

