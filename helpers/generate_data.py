import random
import string
from faker import Faker


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_email():
    fake = Faker()
    email = fake.email(domain='asdfg.com')
    return email
