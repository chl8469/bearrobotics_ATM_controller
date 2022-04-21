from atm import ATM

if __name__ == "__main__":
    atm = ATM()
    card = input("please insert your card: ")
    atm.insert_card(card)
