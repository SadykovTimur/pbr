from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_auth_sudir_page, open_start_page, open_start_system_page, redirect_complaint, sign_in


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('PKND')
@allure.story('Перенаправление на страницу "Жалобы"')
@allure.title('Cтраница КНД "Жалобы"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_redirect_complaint(request: FixtureRequest,
                            make_app: Callable[..., Application],
                            browser: str, device_type: str) -> None:

    app = make_app(browser, device_type)

    open_start_page(app, request)

    open_auth_sudir_page(app)
    sign_in(app, request.config.option.username, request.config.option.password)
    open_start_system_page(app)

    redirect_complaint(app)
