from selene import browser, be, have, command
import os
import tests
from data.users import User


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')
        self.city = browser.element('#city')

    def open_browser(self):
        browser.open("/automation-practice-form")

    def _fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def _fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def _fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def _fill_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def _fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def _fill_date_of_birth(self, month, day, year):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.all(f'.react-datepicker__day--0{day}').second.click()
        return self

    def _fill_subject(self, value):
        browser.element("#subjectsInput").type(f"{value}")
        browser.element(".subjects-auto-complete__menu").click()
        browser.element(
            ".subjects-auto-complete__indicators .subjects-auto-complete__clear-indicator"
        ).click()
        browser.element("#subjectsInput").should(be.blank)
        browser.element("#subjectsInput").type(f"{value}").press_tab()

        return self

    def _fill_gender(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()
        return self

    def _fill_hobbies(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()
        return self

    def _upload_file(self, file_name):
        browser.element(".form-file").click().element("#uploadPicture").send_keys(
            os.path.abspath(f"data/{file_name}")
        )
        return self

    def _fill_state(self, value):
        self.state.perform(command.js.scroll_into_view).click()
        self.state.all('[id^=react-select-3-option]').element_by(
            have.text(value)
        ).click()

        return self

    def _fill_city(self, value):
        self.city.click()
        self.city.all('[id^=react-select-4-option]').element_by(
            have.text(value)
        ).click()

        return self

    def _submit(self):
        browser.element("#submit").click()
        return self

    def register(self, student: User):
        (
            self._fill_first_name(student.name)
            ._fill_last_name(student.surname)
            ._fill_email(student.email)
            ._fill_gender(student.gender)
            ._fill_number(student.phone)
            ._fill_date_of_birth(student.date_month, student.date_day, student.date_year)
            ._fill_subject(student.subject)
            ._fill_hobbies(student.hobby)
            ._upload_file(student.file)
            ._fill_address(student.address)
            ._fill_state(student.state)
            ._fill_city(student.city)
            ._submit()
        )
        return self

    def registered_user_with(self, student: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.name} {student.surname}',
                student.email,
                student.gender,
                student.phone,
                f'{student.date_day} {student.date_month},{student.date_year}',
                student.subject,
                student.hobby,
                student.file,
                student.address,
                f'{student.state} {student.city}'
            )
        )
