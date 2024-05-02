from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.components.navigation import Navigation
from dit.qa.pages.components.sidebar import Sidebar

__all__ = ['AccountingPage']


class AccountingPage(Page):
    header = Header(id="adaptive_navbar_pknd")
    navigation = Navigation(css='[class*="navigation"]')
    sidebar = Sidebar(css='[class*="sidebar-secondary"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.messages.visible
                assert self.header.notifications.visible
                assert self.header.profile.visible
                assert self.header.help.visible
                assert self.header.logout.visible
                assert 'Главная' in self.header.breadcrumbs
                assert 'Учет' in self.header.breadcrumbs
                assert 'Субъекты' in self.header.breadcrumbs
                assert 'Субъекты КНО' in self.header.breadcrumbs
                assert self.header.search

                assert self.navigation.subjects.visible
                assert self.navigation.objects.visible
                assert self.navigation.objects_map.visible

                assert self.sidebar.radio_block[0].visible
                assert self.sidebar.checkbox[0].visible

                return self.sidebar.group[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
