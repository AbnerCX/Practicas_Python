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

    def show_information(self):
        print(f'''
        Name: {self._name}
        Age: {self._age}
        Address: {self._address}
        E-mail: {self._email}
        Token: {self._token}
        ''')

    def get_token(self):
        return self._token


class Transactions:

    def __init__(self, balance):
        self._balance = balance

    def _verification_token(self, token):
        verification = token.get_token()
        if verification is not None:
            print('Verification successful')
        else:
            print('Please, create account')

    def _transaction(self, balance):
        try:
            option = int(input('Do you want to make a deposit?'))
            print('1- Yes')
            print('2- Nope')
            if option == 1:
                amount = int(input('How much amount do you want to deposit?'))
                balance += amount
                balance = self._balance
        except ValueError:
            logger.info('Error, use a correct option')


if __name__ == "__main__":
    prueba = Customers()
    prueba._create_account()

    logger.info(f'El token es: {prueba.get_token()}')

    tokensito = Transactions()
    tokensito._verification_token(prueba)
