from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    messages = Component(css='[class*="admin-messages"]')
    notifications = Component(css='[class*="notifications-widget"]')
    profile = Component(class_name="settings")
    help = Component(css='[class*="help-widget"]')
    logout = Component(class_name="logout")
    breadcrumbs = Text(class_name="breadcrumbs")
    search = Component(class_name="global-search")
    first = Button(xpath="//a[text()='Главная'] ")
    save = Component(xpath="//button[text()=' Сохранить ']")
    navbar_title = Component(xpath="//h4[text()=' Редактирование организации ']")
    main_btn = Button(xpath="//button[text()=' Добавить дело ']")
    directory = Component(xpath="//span[text()='Справочники']")
    create_users = Button(xpath="//button[text()=' Создать пользователя ']")
    all_case = Component(xpath="//span[text()=' Все дела ']")
    new_directory = Component(xpath="//button[text()=' Новый справочник ']")
    statement = Component(xpath="//button[text()=' Добавить заявление ']")
    plane = Component(xpath="//button[text()=' Добавить план ']")
    create_case = Component(xpath="//span[text()=' Создание дела ']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
