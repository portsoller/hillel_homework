from playwright.sync_api import Page, expect
from pages.garage_page import GaragePage

def test_create_car(garage_page: GaragePage):
    add_modal = garage_page.open_add_car_modal()
    add_modal.add_car("155000")
    expect(garage_page.car_list).to_contain_text("Audi TT")
    expect(garage_page.mileage).to_have_value("155000")

def test_update_mileage(garage_page: GaragePage):
    edit_modal = garage_page.open_edit_car_modal()
    edit_modal.fill_mileage("255000")
    edit_modal.click_save()
    expect(garage_page.mileage).to_have_value("255000")

def test_delete_car(garage_page: GaragePage):
    edit_modal = garage_page.open_edit_car_modal()
    edit_modal.remove_car()
    expect(garage_page.page.locator("app-alert", has_text="Car removed")).to_be_visible()
