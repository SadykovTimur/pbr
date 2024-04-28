from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_auth_sudir_page, open_start_page


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('PBR')
@allure.story('Проверка работы СУДИР')
@allure.title('Пройти по кнопке "Вход через СУДИР"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_work_sudir(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_start_page(app, request)

    open_auth_sudir_page(app)
