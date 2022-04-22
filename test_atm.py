from atm import ATM
from testcase import test_users, test_accounts


def test_wrong_cardpin(capsys):
    atm = ATM()
    atm.insert_card(False)
    captured = capsys.readouterr()
    assert captured.out == "Not valid card. please check your card\n"

def test_wrong_passwd(capsys, monkeypatch):
    test_keys = [i for i in test_users.keys()]
    atm = ATM()
    wrong_passwd = iter([-1, -1, -1])
    monkeypatch.setattr('builtins.input', lambda x: next(wrong_passwd))

    error_msg = ('incorrect password. please check your password\n'
    'incorrect password. please check your password\n'
    'incorrect password. please check your password\n'
    'Authentification failed.\n')

    atm.insert_card(test_keys[0])
    captured = capsys.readouterr()
    assert captured.out == error_msg

def test_wrong_account(capsys, monkeypatch):
    test_keys = [i for i in test_users.keys()]
    atm = ATM()
    wrong_passwd = iter([-1, -1, -1])
    monkeypatch.setattr('builtins.input', lambda x: next(wrong_passwd))

    error_msg = ('incorrect password. please check your password\n'
    'incorrect password. please check your password\n'
    'incorrect password. please check your password\n'
    'Authentification failed.\n')

    atm.insert_card(test_keys[0])
    captured = capsys.readouterr()
    assert captured.out == error_msg

def test_balance(capsys, monkeypatch):
    test_keys = [key for key in test_users.keys()]
    atm = ATM()
    base_std = {key:make_stdout(key) for key in test_keys}

    for key in test_keys:
        idx = 1
        for acnt in test_accounts[key]:
            # make input iterator & stdout string
            user_info = iter([test_users[key], str(idx), '1'])
            balance = test_accounts[key][acnt]
            balance = [f"balance: {balance:,}\n"]
            idx += 1
            
            # start test
            monkeypatch.setattr('builtins.input', lambda _: next(user_info))
            std_out = base_std[key] + balance
            std_out = ''.join(std_out)

            atm.insert_card(key)
            captured = capsys.readouterr()
            assert captured.out == std_out

def test_deposit(capsys, monkeypatch):
    test_keys = [key for key in test_users.keys()]
    atm = ATM()
    base_std = {key:make_stdout(key) for key in test_keys}

    for key in test_keys:
        idx = 1
        for acnt in test_accounts[key]:
            # make input iterator & stdout string
            money = 1
            user_info = iter([test_users[key], str(idx), '2', str(money)])
            msg = ["result: success. \n"]
            balance = test_accounts[key][acnt] + money
            balance = msg + [f"balance: {balance:,}\n"]
            idx += 1
            
            # start test
            monkeypatch.setattr('builtins.input', lambda _: next(user_info))
            std_out = base_std[key] + balance
            std_out = ''.join(std_out)

            atm.insert_card(key)
            captured = capsys.readouterr()
            assert captured.out == std_out

def test_withdraw(capsys, monkeypatch):
    test_keys = [key for key in test_users.keys()]
    atm = ATM()
    base_std = {key:make_stdout(key) for key in test_keys}

    for key in test_keys:
        idx = 1
        for acnt in test_accounts[key]:
            # make input iterator & stdout string
            money = 1
            user_info = iter([test_users[key], str(idx), '3', str(money)])
            msg = ["result: success. \n"]
            balance = test_accounts[key][acnt]
            if balance > 0:
                balance -= money
            else:
                continue
            balance = msg + [f"balance: {balance:,}\n"]
            idx += 1
            
            # start test
            monkeypatch.setattr('builtins.input', lambda _: next(user_info))
            std_out = base_std[key] + balance
            std_out = ''.join(std_out)

            atm.insert_card(key)
            captured = capsys.readouterr()
            assert captured.out == std_out

def test_withdraw_fail(capsys, monkeypatch):
    test_keys = [key for key in test_users.keys()]
    atm = ATM()
    base_std = {key:make_stdout(key) for key in test_keys}

    for key in test_keys:
        idx = 1
        for acnt in test_accounts[key]:
            # make input iterator & stdout string
            balance = test_accounts[key][acnt]
            money = balance + 1
            user_info = iter([test_users[key], str(idx), '3', str(money)])
            msg = ["result: non sufficient funds. \n"]
            balance = msg + [f"balance: {balance:,}\n"]
            idx += 1
            
            # start test
            monkeypatch.setattr('builtins.input', lambda _: next(user_info))
            std_out = base_std[key] + balance
            std_out = ''.join(std_out)

            atm.insert_card(key)
            captured = capsys.readouterr()
            assert captured.out == std_out

def make_stdout(user):
    strings = []
    for idx, acnt in enumerate(test_accounts[user].keys()):
        string = f'{idx+1} : {acnt}\n'
        strings.append(string)
    
    strings += ['1 : balance\n',
    '2 : deposit\n',
    '3 : withdraw\n']

    return strings 

