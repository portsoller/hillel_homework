# tests/record.py
from playwright.sync_api import Page

def test_record_actions(login_ui: Page):
    # Фикстура login_ui залогинит вас и приведет в Гараж
    login_ui.pause()  # Здесь откроется инспектор

    import re
    from playwright.sync_api import Page, expect

    def test_example(page: Page) -> None:
        page.get_by_role("button", name="Add car").click()
        page.get_by_role("spinbutton", name="Mileage").click()
        page.get_by_role("spinbutton", name="Mileage").fill("338180")
        page.get_by_role("button", name="Add").click()
        expect(page.get_by_role("list")).to_contain_text("Audi TT")
        expect(page.get_by_role("spinbutton").first).to_have_value("338180");
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("spinbutton").first.press("ArrowRight")
        page.get_by_role("spinbutton").first.press("ArrowRight")
        page.get_by_role("spinbutton").first.fill("155000")
        expect(page.get_by_role("spinbutton").first).to_have_value("338180");
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("spinbutton").first.press("ArrowRight")
        page.get_by_role("spinbutton").first.press("ArrowRight")
        page.get_by_role("spinbutton").first.press("ArrowRight")
        page.get_by_role("spinbutton").first.press("ArrowRight")
        page.get_by_role("spinbutton").first.fill("155000")
        page.get_by_role("spinbutton").first.press("Enter")
        page.get_by_role("spinbutton").first.press("Enter")
        page.get_by_role("spinbutton").first.click()
        page.get_by_role("button").nth(2).click()
        page.get_by_role("spinbutton", name="Mileage").click()
        page.get_by_role("spinbutton", name="Mileage").fill("155555")
        page.get_by_role("button", name="Save").click()
        page.get_by_role("spinbutton", name="Mileage").click()
        page.get_by_role("spinbutton", name="Mileage").click()
        page.get_by_role("spinbutton", name="Mileage").press("ArrowLeft")
        page.get_by_role("spinbutton", name="Mileage").press("ArrowLeft")
        page.get_by_role("spinbutton", name="Mileage").press("ArrowLeft")
        page.get_by_role("spinbutton", name="Mileage").press("ArrowLeft")
        page.get_by_role("spinbutton", name="Mileage").press("ArrowLeft")
        page.get_by_role("spinbutton", name="Mileage").fill("455555")
        page.get_by_role("button", name="Save").click()
        expect(page.get_by_role("spinbutton").first).to_have_value("455555");
        page.get_by_role("button").nth(2).click()
        page.get_by_role("button", name="Remove car").click()
        expect(page.locator("app-remove-car-modal")).to_contain_text(
            "Do you really want to remove Audi TT from your account?")
        page.get_by_role("button", name="Remove").click()
        expect(page.locator("app-alert")).to_contain_text("Car removed")
