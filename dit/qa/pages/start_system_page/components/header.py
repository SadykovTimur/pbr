from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Component(xpath='//span[text()=" Тестовая организация "]')
    messages = Component(css='[class*="admin-messages"]')
    notifications = Component(css='[class*="notifications-widget"]')
    profile = Component(class_name="settings")
    help = Component(css='[class*="help-widget"]')
    logout = Component(class_name="logout")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
