from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Panel']


class PanelWrapper(ComponentWrapper):
    form_group = Components(css='[class*="form-group"]')
    # item = Components(css='[class="list-item-data"]')
    list = Components(class_name='list-item-data')
    create_btn = Button(css='button[class*="btn btn-primary"]')
    title = Component(xpath="//span[contains(text(),'Профилактика. Профилактический визит. Федеральный ')]")


class Panel(Component):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)
