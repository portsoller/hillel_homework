from playwright.sync_api import Page, expect

def test_create_car(login_ui: Page):
    login_ui.get_by_role("button", name="Add car").click()
    login_ui.get_by_role("spinbutton", name="Mileage").click()
    login_ui.get_by_role("spinbutton", name="Mileage").fill("338180")
    login_ui.get_by_role("button", name="Add").click()
    expect(login_ui.get_by_role("list")).to_contain_text("Audi TT")
    expect(login_ui.get_by_role("spinbutton").first).to_have_value("338180")

def test_update_mileage(login_ui: Page):
    login_ui.get_by_role("button").nth(2).click()
    login_ui.get_by_role("spinbutton", name="Mileage").click()
    login_ui.get_by_role("spinbutton", name="Mileage").fill("400000")
    login_ui.get_by_role("button", name="Save").click()
    expect(login_ui.get_by_role("spinbutton").first).to_have_value("400000")

def test_delete_car(login_ui: Page):
    login_ui.get_by_role("button").nth(2).click()
    expect(login_ui.locator("app-edit-car-modal")).to_contain_text("Remove car")
    login_ui.get_by_role("button", name="Remove car").click()
    expect(login_ui.locator("app-remove-car-modal")).to_contain_text(
        "Do you really want to remove Audi TT from your account?"
    )
    expect(login_ui.get_by_role("heading")).to_contain_text("Remove car")
    login_ui.get_by_role("button", name="Remove").click()
    expect(login_ui.locator("app-alert", has_text="Car removed")).to_be_visible()


