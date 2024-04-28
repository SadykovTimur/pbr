from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.components.navigation import Navigation
from dit.qa.pages.components.panel import Panel
from dit.qa.pages.components.sidebar import Sidebar

__all__ = ['CnmPmPage']


class CnmPmPage(Page):
    header = Header(id="adaptive_navbar_pknd")
    navigation = Navigation(css='[class*="navigation"]')
    sidebar = Sidebar(css='[class*="sidebar-secondary"]')
    panel = Panel(class_name="panel-body")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.messages.visible
                assert self.header.notifications.visible
                assert self.header.profile.visible
                assert self.header.help.visible
                assert self.header.logout.visible
                assert 'Главная' in self.header.breadcrumbs
                assert 'КНМ и ПМ' in self.header.breadcrumbs
                assert 'Список КНМ' in self.header.breadcrumbs
                assert self.header.main_btn
                assert self.header.search

                assert self.navigation.appeals.visible
                assert self.navigation.consultations.visible
                assert self.navigation.initiation.visible

                assert self.sidebar.group[0].visible

                return self.panel.item[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_case(self) -> None:
        def condition() -> bool:
            try:
                assert 'Главная' in self.header.breadcrumbs
                assert 'КНМ и ПМ' in self.header.breadcrumbs
                assert 'Список КНМ' in self.header.breadcrumbs
                assert 'Стандарты' in self.header.breadcrumbs

                assert self.sidebar.catalog.visible
                assert self.sidebar.checkbox[0].visible

                return self.sidebar.group[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_choice_standard(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.create_case.visible

                assert 'Главная' in self.header.breadcrumbs
                assert 'КНМ и ПМ' in self.header.breadcrumbs
                assert 'Список КНМ' in self.header.breadcrumbs
                assert 'Создание нового' in self.header.breadcrumbs

                assert self.panel.title.visible

                return self.sidebar.category_title[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
