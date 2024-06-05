import os
from selene import browser, be, have


def test_demoqa_form():
    browser.open("/automation-practice-form")

    # Заполнение текстовых полей
    browser.element("#firstName").type("Yulia")
    browser.element("#lastName").type("Vdovina")
    browser.element("#userEmail").type("yulya_vdovina@mail.ru")
    browser.element("#userNumber").type("0123456789")
    browser.element("#currentAddress").type("Penza, st. Ladoga 1234")

    # Установка даты (Date of Birth)
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select option[value="11"]').click()
    browser.element('.react-datepicker__year-select option[value="2000"]').click()
    browser.all(".react-datepicker__day--028").second.click()

    # Проверка поля subjects
    browser.element("#subjectsInput").type("Social")
    browser.element(".subjects-auto-complete__menu").click()
    browser.element(
        ".subjects-auto-complete__indicators .subjects-auto-complete__clear-indicator"
    ).click()
    browser.element("#subjectsInput").should(be.blank)

    browser.element("#subjectsInput").type("Eco").press_tab()
    # browser.element('.subjects-auto-complete__multi-value .subjects-auto-complete__multi-value__remove').click()

    browser.element("#subjectsInput").type("En").press_tab()

    # Радиокнопка (Gender)
    browser.element('[for="gender-radio-2"]').click()

    # Радиокнопка (Hobbies)
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click().click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Выбор файла (Picture)
    browser.element(".form-file").click().element("#uploadPicture").send_keys(
        os.path.abspath("data/kit.jpg")
    )

    # Выбор из выпадающего списка (State and City)
    browser.element("#state").click().element("#react-select-3-option-2").click()
    browser.element("#city").click().element("#react-select-4-option-0").click()

    # Отправка
    browser.element("#submit").click()

    # Проверка
    browser.element(".modal-content").element("table").all("tr").all("td").even.should(
        have.exact_texts(
            "Yulia Vdovina",
            "yulya_vdovina@mail.ru",
            "Female",
            "0123456789",
            "28 December,2000",
            "Economics, English",
            "Sports, Music",
            "kit.jpg",
            "Penza, st. Ladoga 1234",
            "Haryana Karnal",
        )
    )
