from typing import List, Union
from testcase import test_users, test_accounts


class BankApi:
    def valid_card(card_pin:str) -> bool:
        if card_pin in test_users.keys():
            return True
        else:
            return False
    
    def valid_passwd(card_pin:str, passwd:str) -> bool:
        password = test_users[card_pin]
        if passwd == password:
            return True
        else:
            return False

    def get_accounts(card_pin:str) -> List[str]:
        accounts = test_accounts[card_pin]
        return [i for i in accounts.keys()]

    def get_balance(card_pin:str, account:str) -> int:
        account_list = test_accounts[card_pin]
        balance = account_list[account]
        return balance
    
    def deposit_money(card_pin:str, account:str, money:int) -> List[Union[str, int]]:
        account_list = test_accounts[card_pin]
        account_list[account] = account_list[account] + money
        balance = account_list[account]
        return ["success.", balance]
    
    def withdraw_balance(card_pin:str, account:str, money:int) -> List[Union[str, int]]:
        account_list = test_accounts[card_pin]
        balance = account_list[account]

        if money <= balance:
            account_list[account] = balance - money
            return ["success.", account_list[account]]
        else:
            return ["non sufficient funds.", account_list[account]]
        