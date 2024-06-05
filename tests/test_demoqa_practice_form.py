from data.users import User
from pages.registration_page import RegistrationPage


def test_demoqa_form():
    page = RegistrationPage()
    user = User(
            "Yulia",
            "Vdovina",
            "yulya_vdovina@mail.ru",
            "Female",
            "0123456789",
            "December", "28", "2000",
            "Economics",
            "Sports",
            "kit.jpg",
            "Penza, st. Ladoga 1234",
            "Haryana",
            "Karnal"
        )
    page.open_browser()
    page.register(user)
    page.registered_user_with(user)
