import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file) #путь к файлу
        with open(config_file) as f: #переменная f содержит объект, который указывает на открытый файл
            target = json.load(f)
    return target


@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web'] #берем из конфигурации блок web
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, base_url=web_config['baseUrl']) #создаём фикстуру если она None или не валидная
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(end)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
