from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    title = Component(xpath="//h1[text()=' КНД ']")
    description = Component(xpath="//div[text()=' Контрольно-надзорная деятельность '] ")
    sibmit_sudir = Button(xpath="//div[text()=' Вход через СУДИР ']")
    checkbox = Button(css='[for="сredentialsLoginSwitch"]')
    login = TextField(css='input[formcontrolname="login"]')
    password = TextField(css='input[formcontrolname="password"]')
    submit = Button(xpath="//div[text()=' Войти в систему ']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.description.visible
                assert self.sibmit_sudir.visible

                return self.checkbox.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_sudir(self) -> None:
        def condition() -> bool:
            try:
                assert self.login.visible
                assert self.password.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
