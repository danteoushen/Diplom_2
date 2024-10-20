from faker import Faker

def generate_user():

    fake = Faker('ru_RU')

    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }

    return user_data