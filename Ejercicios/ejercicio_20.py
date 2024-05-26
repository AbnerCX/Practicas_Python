import logging
import uuid

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] [%(funcName)s:%(lineno)d] [%(message)s]",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


class Customers:
    def __init__(self):
        self._name = None
        self._age = None
        self._address = None
        self._email = None
        self._token = None
        self._balance = 0

    def _generate_token(self):
        self._token = uuid.uuid4().hex

    def _create_account(self):
        print('----Please fill the form----')
        while True:
            self._name = input('Please introduce your name: ')
            try:
                self._age = int(input('Please introduce your age: '))
                if self._age < 18:
                    print('Error: You are not of age....')
                    continue
                else:
                    break
            except ValueError:
                print('Error: Please introduce a correct answer')

        self._address = input('Please introduce your address: ')
        self._email = input('Please introduce your e-mail:')

        self._generate_token()

    def _transaction(self):
        try:
            print('Do you want to make a deposit?')
            print('1- Yes')
            print('2- Nope')
            option = int(input('Choose an option: '))
            if option == 1:
                amount = int(input('How much amount do you want to deposit? '))
                self._balance += amount
            else:
                print('Thanks')
        except ValueError:
            logger.warn('Error, use a correct option')

    def _whithdrawal_of_money(self):
        try:
            print('Do you want to make a whithdrawal? ')
            print('1- Yes')
            print('2- Nope')
            option = int(input('Choose an option: '))
            if option == 1:
                amount = int(input('How much amount do you want to whithdrawal? '))
                if amount > self._balance:
                    print('You dont have enough money')
                else:
                    self._balance -= amount
            else:
                print('Thanks')
        except ValueError:
            logger.warn('Error, use a correct option')

    def show_information(self):
        print(f'''
        Name: {self._name}
        Age: {self._age}
        Address: {self._address}
        E-mail: {self._email}
        Token: {self._token}
        ''')

    def show_cash(self):
        print(f'The money in your account is: {self._balance}')

    def get_token(self):
        return self._token


class Transactions:

    def _verification_token(self, token):
        verification = token.get_token()
        if verification is not None:
            print('Verification successful')
        else:
            print('Please, create account')


if __name__=="__main__":

    prueba = Customers()
    prueba._create_account()

    tokensito = Transactions()
    tokensito._verification_token(prueba)

    prueba.show_information()
    prueba._transaction()
    prueba.show_cash()
    prueba._whithdrawal_of_money()
    prueba.show_cash()

    logger.info(f'El token es: {prueba.geejhert_token()}')