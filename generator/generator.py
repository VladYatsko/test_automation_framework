from faker import Faker

from data.data import Person

faker_en = Faker('en-US')
Faker.seed()


def generated_data():
    yield Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        address=faker_en.address(),
        city=faker_en.city(),
        state=faker_en.state(),
        zip_code=faker_en.zipcode(),
        phone_number=faker_en.phone_number(),
        social_security_num=faker_en.ssn(),
        username=faker_en.user_name(),
        password=faker_en.password()
    )
