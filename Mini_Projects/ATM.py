
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(f"Need ₹{amount} but only ₹{balance} available!")

class WrongPINError(Exception):
    def __init__(self, attempts_left):
        self.attempts_left = attempts_left
        super().__init__(f"Worng pin enter attempts left {attempts_left}!")

class AccountLockedError(Exception):
    def __init__(self):
        super().__init__("Your account was locked!")

class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin
        self.__attempts = 3
        self.__locked = False

    def withdraw(self, amount, pin):
        try:
            if self.__locked:
                raise AccountLockedError()
            
            if pin != self.__pin:
                self.__attempts -= 1
                if self.__attempts == 0:
                    self.__locked = True
                raise WrongPINError(self.__attempts)
            
            if amount > self.__balance:
                raise InsufficientFundsError(self.balance, amount)
            else:
                self.__balance -= amount

        except (AccountLockedError, WrongPINError, InsufficientFundsError) as e:
            print("Error : {e}")
        else:
            print("Transaction successful!")
        finally:
            print("transaction ended.")