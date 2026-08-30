from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.components.add_car_modal import AddCarModal
from pages.components.edit_car_modal import EditCarModal

class GaragePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_car_button = page.get_by_role("button", name="Add car")
        self.edit_car_button = page.get_by_role("button").nth(2)
        self.car_list = self.page.get_by_role("list")
        self.mileage = self.page.get_by_role("spinbutton").first

    def open_add_car_modal(self) -> AddCarModal:
        self.add_car_button.click()
        return AddCarModal(self.page)

    def open_edit_car_modal(self) -> EditCarModal:
        self.edit_car_button.click()
        return EditCarModal(self.page)
