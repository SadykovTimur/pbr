from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.components.navigation import Navigation
from dit.qa.pages.components.panel import Panel
from dit.qa.pages.components.sidebar import Sidebar

__all__ = ['AdministrationCnoPage']


class AdministrationCnoPage(Page):
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
                assert 'Кабинет администратора КНО' in self.header.breadcrumbs
                assert 'Настройки КНО' in self.header.breadcrumbs
                assert self.header.save
                assert self.header.navbar_title

                assert self.navigation.kno_settings.visible
                assert self.navigation.users.visible
                assert self.navigation.roles.visible
                assert self.navigation.envelopes.visible
                assert self.navigation.system_tasks.visible

                assert self.sidebar.category_title[0].visible

                return self.panel.form_group[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
