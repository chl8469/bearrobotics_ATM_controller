from bank_api import BankApi


class ATM:
    def insert_card(self, card_pin:str):
        result = BankApi.valid_card(card_pin)
        if result:
            self.card_pin = card_pin
            self._valid_passwd()
        else:
            print("Not valid card. please check your card")
    
    def _valid_passwd(self, count = 1):
        if count > 3:
            print("Authentification failed.")
            return 0
    
        passwd = input("Password:")
        result = BankApi.valid_passwd(self.card_pin, passwd)
        if result:
            self.passwd = passwd
            self._select_account()
        else:
            print("incorrect password. please check your password")
            self._valid_passwd(count + 1)

    def _select_account(self):
        accounts = BankApi.get_accounts(self.card_pin)
        ac_rng = [i + 1 for i in range(len(accounts))]
        ac_rng_str = ", ".join([str(i) for i in ac_rng])

        for idx, acnt in enumerate(accounts):
            print(idx+1, ":", acnt)
        
        while True:
            selected = input("please select your account: ")
            try:
                selected = int(selected)
                if selected in ac_rng:
                    break
            except ValueError:
                pass
            print(f"please select one of {ac_rng_str}")
                
        self.account = accounts[selected - 1]
        self._select_bdw()
    
    def _select_bdw(self):
        bdw = {"1":"balance",
               "2":"deposit",
               "3":"withdraw"}
        
        for key in bdw:
            print(key, ":", bdw[key])
        
        while True:
            selected = input("please select one of 1, 2, 3: ")
            try:
                if selected in bdw.keys():
                    break
            except ValueError:
                print("please select one of 1, 2, 3: ")

        self._action(selected)
    
    def _action(self, action:str):
        bdw = {"1":BankApi.get_balance,
               "2":BankApi.deposit_money,
               "3":BankApi.withdraw_balance}

        if action == "1":
            result = bdw[action](self.card_pin, self.account)
            print(f"balance: {result:,}")
        else:
            while True:
                money = input("please enter the amount of money: ")
                try:
                    money = int(money)
                    break
                except ValueError:
                    print("input must be a number")
            result = bdw[action](self.card_pin, self.account, money)
            print(f"result: {result[0]} \nbalance: {result[1]:,}")