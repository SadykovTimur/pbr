from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.constants import WEB_DRIVER_WAIT
from coms.qa.frontend.helpers.custom_wait_conditions import ElementToBeClickable
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from dit.qa.pages.start_system_page.components.application import Application
from dit.qa.pages.start_system_page.components.header import Header
from dit.qa.pages.start_system_page.components.modal import Modal

__all__ = ['StartSystemPage']


class StartSystemPage(Page):
    header = Header(class_name="header")
    application = Application(class_name="applications-wrapper")
    modal = Modal(class_name="modal-content")

    def open_page(self, name: str) -> None:
        wait = WebDriverWait(self.driver, WEB_DRIVER_WAIT)
        el = self.driver.find_element(By.XPATH, f'//div[text()="{name}"]')
        wait.until(ElementToBeClickable(element=el))
        el.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title.visible
                assert self.header.messages.visible
                assert self.header.notifications.visible
                assert self.header.profile.visible
                assert self.header.help.visible
                assert self.header.logout.visible

                return self.application.box[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
