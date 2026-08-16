import pytest
from playwright.sync_api import Page, expect
from pages.garage_page import GaragePage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "http_credentials": {
            "username": "guest",
            "password": "welcome2qauto"
        }
    }

@pytest.fixture
def login_ui(page: Page) -> Page:
    page.goto("https://qauto2.forstudy.space/")
    page.get_by_role("button", name="Sign In").click()
    page.locator('#signinEmail').fill("nedzelnytskyidev+hillel02026@gmail.com")
    page.get_by_role("textbox", name="Password").fill("AYf3JtDQnAcMbnc")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.locator("app-signin-modal")).to_contain_text("Login")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator('//app-alert')).to_have_text('You have been successfully logged in')
    yield page

@pytest.fixture
def garage_page(login_ui) -> GaragePage:
  return GaragePage(login_ui)
