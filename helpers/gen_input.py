from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker('ru_RU')

    def generate_name(self):
        """Генерирует случайное имя"""
        return self.fake.first_name()

    def generate_email(self):
        """Генерация почты"""
        return self.fake.email()

    def generate_password(self, length=10):
        """Генерация случайного пароля"""
        return self.fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)

