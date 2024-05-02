from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.components.navigation import Navigation
from dit.qa.pages.components.panel import Panel
from dit.qa.pages.components.sidebar import Sidebar

__all__ = ['DeveloperOfficePage']


class DeveloperOfficePage(Page):
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
                assert 'Кабинет разработчика' in self.header.breadcrumbs
                assert 'Настройки справочников' in self.header.breadcrumbs
                assert self.header.search
                assert self.header.new_directory

                assert self.panel.list[0].visible

                assert self.navigation.dictionaries.visible
                assert self.navigation.dictionaries_settings.visible
                assert self.navigation.regulations.visible
                assert self.navigation.collections_meta.visible
                assert self.navigation.permissions.visible
                assert self.navigation.methods.visible
                assert self.navigation.applications.visible
                assert self.navigation.notification_types.visible
                assert self.navigation.notification_kinds.visible
                assert self.navigation.service_scripts.visible

                assert self.sidebar.checkbox[0].visible

                return self.sidebar.group[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
