from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Modal']


class ModalWrapper(ComponentWrapper):
    close = Button(css='[class*="close"]')


class Modal(Component):
    def __get__(self, instance, owner) -> ModalWrapper:
        return ModalWrapper(instance.app, self.find(instance), self._locator)
