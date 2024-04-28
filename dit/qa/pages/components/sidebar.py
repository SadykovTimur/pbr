from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper

__all__ = ['Sidebar']


class SidebarWrapper(ComponentWrapper):
    radio_block = Components(css='[class*="radio-block"]')
    category_title = Components(css='[class="category-title"]')
    group = Components(css='[class*="form-group"]')
    checkbox = Components(css='[class*="checkbox"]')
    catalog = Component(xpath="//span[text()=' Каталог ']")


class Sidebar(Component):
    def __get__(self, instance, owner) -> SidebarWrapper:
        return SidebarWrapper(instance.app, self.find(instance), self._locator)
