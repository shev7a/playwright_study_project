import pytest
from playwright.sync_api import Playwright


def test_add_todo_generated(playwright: Playwright) -> None:

    """
    Сгенерированный код
    playwright codegen https://playwright-todomvc.antonzimaiev.repl.co/#/

    Узнать дополнительные опции:
    playwright codegen --help
    """

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="Создать первый сценарий playwright").get_by_role("checkbox").check()

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.new
def test_add_todo(page):

    """
     Аналогичный тест с использованием pytest и фикстуры page из аддона pytest-playwright
     По умолчанию pytest-playwright делает браузер headless
     Если нужно выполнить в режиме headed:
     pytest --headed
    """

    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
