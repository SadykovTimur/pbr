from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper

__all__ = ['Application']


class ApplicationWrapper(ComponentWrapper):
    box = Components(class_name="application-text-block")


class Application(Component):
    def __get__(self, instance, owner) -> ApplicationWrapper:
        return ApplicationWrapper(instance.app, self.find(instance), self._locator)
