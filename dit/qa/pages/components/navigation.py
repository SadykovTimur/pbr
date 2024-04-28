from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Navigation']


class NavigationWrapper(ComponentWrapper):
    kno_settings = Component(css='[ng-reflect-router-link="kno-settings"]')
    users = Component(css='[ng-reflect-router-link="users"]')
    roles = Component(css='[ng-reflect-router-link="roles"]')
    envelopes = Component(css='[ng-reflect-router-link="envelopes"]')
    system_tasks = Component(css='[ng-reflect-router-link="system-tasks"]')
    appeals = Component(css='[ng-reflect-router-link="appeals"]')
    consultations = Component(css='[ng-reflect-router-link="consultations"]')
    initiation = Component(css='[ng-reflect-router-link="initiation"]')
    object_types = Component(css='[ng-reflect-router-link="object-types"]')
    dictionaries = Component(css='[ng-reflect-router-link="dictionaries"]')
    dictionaries_settings = Component(css='[ng-reflect-router-link="dictionaries-settings"]')
    number_templates = Component(css='[ng-reflect-router-link="number-templates"]')
    common_standards = Component(css='[ng-reflect-router-link="common-standards"]')
    standards_git = Component(css='[ng-reflect-router-link="standards-git"]')
    print_forms = Component(css='[ng-reflect-router-link="print-forms"]')
    notification_settings = Component(css='[ng-reflect-router-link="notification-settings"]')
    requests = Component(css='[ng-reflect-router-link="requests"]')
    subjects = Component(css='[ng-reflect-router-link="subjects"]')
    objects = Component(css='[ng-reflect-router-link="objects"]')
    objects_map = Component(css='[ng-reflect-router-link="objects-map"]')
    complaints = Component(css='[ng-reflect-router-link="complaints"]')
    helper = Component(css='[ng-reflect-router-link="helper"]')
    regulations = Component(css='[ng-reflect-router-link="meta-reglaments"]')
    collections_meta = Component(css='[ng-reflect-router-link="collections-meta"]')
    permissions = Component(css='[ng-reflect-router-link="permissions"]')
    methods = Component(css='[ng-reflect-router-link="methods"]')
    applications = Component(css='[ng-reflect-router-link="applications"]')
    notification_types = Component(css='[ng-reflect-router-link="notification-types"]')
    notification_kinds = Component(css='[ng-reflect-router-link="notification-kinds"]')
    service_scripts = Component(css='[ng-reflect-router-link="service-scripts"]')
    registers = Component(css='[ng-reflect-router-link="registers"]')
    plans = Component(css='[ng-reflect-router-link="plans"]')
    organizations = Component(css='[ng-reflect-router-link="organizations"]')
    settings = Component(css='[ng-reflect-router-link="settings"]')
    history = Component(css='[ng-reflect-router-link="history"]')
    collections_groups = Component(css='[ng-reflect-router-link="collections-groups"]')
    system_messages = Component(css='[ng-reflect-router-link="system-messages"]')


class Navigation(Component):
    def __get__(self, instance, owner) -> NavigationWrapper:
        return NavigationWrapper(instance.app, self.find(instance), self._locator)
