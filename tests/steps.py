import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.accounting_page import AccountingPage
from dit.qa.pages.adiminstaration_cno_page import AdministrationCnoPage
from dit.qa.pages.auth_page import AuthPage
from dit.qa.pages.cnm_pm_page import CnmPmPage
from dit.qa.pages.complaint_page import ComplaintPage
from dit.qa.pages.developer_office_page import DeveloperOfficePage
from dit.qa.pages.licensing_page import LicensingPage
from dit.qa.pages.methodology_cno_page import MethodologyCnoPage
from dit.qa.pages.methodology_system_page import MethodologySystemPage
from dit.qa.pages.nsi_page import NsiPage
from dit.qa.pages.plane_ncm_page import PlaneCnmPage
from dit.qa.pages.security_page import SecurityPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.start_system_page import StartSystemPage

__all__ = [
    'open_start_page',
    'open_auth_sudir_page',
    'sign_in',
    'open_start_system_page',
    'redirect_administration_cno',
    'redirect_start_system_page',
    'redirect_security',
    'redirect_cnm_pm',
    'redirect_methodology_cno',
    'redirect_methodology_system',
    'redirect_accounting',
    'redirect_nsi',
    'redirect_complaint',
    'redirect_developer_office',
    'redirect_licensing_office',
    'redirect_plane_cnm',
    'add_case',
    'add_case_choice_standard',
]


def open_start_page(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Start page'):
        if request.config.option.block_urls:
            app.send_command('Network.setBlockedURLs', {'urls': ['unpkg.com']})
            app.send_command('Network.enable', {})

        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()
            page.checkbox.click()

            page.wait_for_loading_sudir()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def open_auth_sudir_page(app: Application) -> None:
    with allure.step('Opening Auth sudir page'):
        try:
            page = StartPage(app)
            page.checkbox.click()
            page.sibmit_sudir.click()

            AuthPage(app).wait_for_loading()

            screenshot_attach(app, 'auth_sudir_page')
        except Exception as e:
            screenshot_attach(app, 'auth_sudir_page_error')

            raise TimeoutError('Auth sudir page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = AuthPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_start_system_page(app: Application) -> None:
    with allure.step('Opening Start system page'):
        try:
            start = StartSystemPage(app)
            start.modal.close.click()

            start.wait_for_loading()

            screenshot_attach(app, 'start_system_page')
        except Exception as e:
            screenshot_attach(app, 'start_system_page_error')

            raise TimeoutError('Start system page was not loaded') from e


def redirect_administration_cno(app: Application) -> None:
    with allure.step('Opening Administration cno page'):
        try:
            StartSystemPage(app).open_page(" Кабинет администратора КНО ")

            AdministrationCnoPage(app).wait_for_loading()

            screenshot_attach(app, 'administration_cno_page')
        except Exception as e:
            screenshot_attach(app, 'administration_cno_page_error')

            raise TimeoutError('Administration cno page was not loaded') from e


def redirect_start_system_page(app: Application) -> None:
    with allure.step('Transition start system page'):
        try:
            AdministrationCnoPage(app)
            AdministrationCnoPage(app).header.first.click()

            StartSystemPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_start_page')
        except Exception as e:
            screenshot_attach(app, 'transition_start_page_error')

            raise TimeoutError('Transition start system page was not loaded') from e


def redirect_security(app: Application) -> None:
    with allure.step('Transition Security page'):
        try:
            StartSystemPage(app).open_page(" Безопасность ")

            SecurityPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_security_page')
        except Exception as e:
            screenshot_attach(app, 'transition_security_page_error')

            raise TimeoutError('Transition page was not loaded') from e


def redirect_cnm_pm(app: Application) -> None:
    with allure.step('Transition cnm pm page'):
        try:
            StartSystemPage(app).open_page(" КНМ и ПМ ")

            CnmPmPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_cnm_pm_page')
        except Exception as e:
            screenshot_attach(app, 'transition_cnm_pm_page_error')

            raise TimeoutError('Transition cnm pm page was not loaded') from e


def redirect_methodology_cno(app: Application) -> None:
    with allure.step('Transition methodology cno page'):
        try:
            StartSystemPage(app).open_page(" Кабинет методолога ")

            MethodologyCnoPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_methodology_cno_page')
        except Exception as e:
            screenshot_attach(app, 'transition_methodology_cno_page_error')

            raise TimeoutError('Transition methodology cno page was not loaded') from e


def redirect_methodology_system(app: Application) -> None:
    with allure.step('Transition methodology system page'):
        try:
            StartSystemPage(app).open_page(" Методолог системы ")

            MethodologySystemPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_methodology_system_page')
        except Exception as e:
            screenshot_attach(app, 'transition_methodology_system_page_error')

            raise TimeoutError('Transition methodology page was not loaded') from e


def redirect_accounting(app: Application) -> None:
    with allure.step('Transition accounting page'):
        try:
            StartSystemPage(app).open_page(" Учет ")

            AccountingPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_accounting_page')
        except Exception as e:
            screenshot_attach(app, 'transition_accounting_page_error')

            raise TimeoutError('Transition accounting page was not loaded') from e


def redirect_nsi(app: Application) -> None:
    with allure.step('Transition nsi page'):
        try:
            StartSystemPage(app).open_page(" НСИ ")

            NsiPage(app).wait_for_loading()

            screenshot_attach(app, 'transition_nsi_page')
        except Exception as e:
            screenshot_attach(app, 'transition_nsi_error')

            raise TimeoutError('Transition nsi page was not loaded') from e


def redirect_complaint(app: Application) -> None:
    with allure.step('Redirect complaint page'):
        try:
            StartSystemPage(app).open_page(" Жалобы ")

            ComplaintPage(app).wait_for_loading()

            screenshot_attach(app, 'redirect_complaint_page')
        except Exception as e:
            screenshot_attach(app, 'redirect_complaint_page_error')

            raise TimeoutError('Redirect complaint page was not loaded') from e


def redirect_developer_office(app: Application) -> None:
    with allure.step('Redirect developer office page'):
        try:
            StartSystemPage(app).open_page("Кабинет разработчика")

            DeveloperOfficePage(app).wait_for_loading()

            screenshot_attach(app, 'redirect_developer_page')
        except Exception as e:
            screenshot_attach(app, 'redirect_developer_page_error')

            raise TimeoutError('Redirect developer page was not loaded') from e


def redirect_licensing_office(app: Application) -> None:
    with allure.step('Redirect licensing office page'):
        try:
            StartSystemPage(app).open_page(" Лицензирование ")

            LicensingPage(app).wait_for_loading()

            screenshot_attach(app, 'redirect_licensing_page')
        except Exception as e:
            screenshot_attach(app, 'redirect_licensing_page_error')

            raise TimeoutError('Redirect licensing page was not loaded') from e


def redirect_plane_cnm(app: Application) -> None:
    with allure.step('Redirect plane ncm page'):
        try:
            StartSystemPage(app).open_page(" Планы КНМ ")

            PlaneCnmPage(app).wait_for_loading()

            screenshot_attach(app, 'redirect_plane_ncm_page')
        except Exception as e:
            screenshot_attach(app, 'redirect_plane_ncm_page_error')

            raise TimeoutError('Redirect licensing page was not loaded') from e


def add_case(app: Application) -> None:
    with allure.step('Add case page'):
        try:
            page = CnmPmPage(app)
            page.header.main_btn.click()

            page.wait_for_loading_case()

            screenshot_attach(app, 'add_case_page')
        except Exception as e:
            screenshot_attach(app, 'add_case_page_error')

            raise TimeoutError('Add case page was not loaded') from e


def add_case_choice_standard(app: Application) -> None:
    with allure.step('Add case choice standard page'):
        try:
            page = CnmPmPage(app)
            app.move_to_element(page.panel.list[0].webelement)
            page.panel.create_btn.click()

            page.wait_for_loading_choice_standard()

            screenshot_attach(app, 'add_choice_standard_page')
        except Exception as e:
            screenshot_attach(app, 'add_choice_standard_page_error')

            raise TimeoutError('Add case choice standard page was not loaded') from e
