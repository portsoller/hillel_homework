from playwright.sync_api import Page

class EditCarModal:
    def __init__(self, page: Page):
        self.page = page
        self.mileage_input = self.page.get_by_role("spinbutton", name="Mileage")
        self.save_button = self.page.get_by_role("button", name="Save")
        self.remove_car_button = self.page.get_by_role("button", name="Remove car")
        self.confirm_remove_button = self.page.get_by_role("button", name="Remove")

    def fill_mileage(self, mileage: str):
        self.mileage_input.fill(mileage)

    def click_save(self):
        self.save_button.click()

    def remove_car(self):
        self.remove_car_button.click()
        self.confirm_remove_button.click()
