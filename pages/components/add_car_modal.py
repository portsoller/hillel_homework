from playwright.sync_api import Page

class AddCarModal:
    def __init__(self, page: Page):
        self.page = page
        self.mileage_input = self.page.get_by_role("spinbutton", name="Mileage")
        self.add_button = self.page.get_by_role("button", name="Add")

    def fill_mileage(self, mileage: str):
        self.mileage_input.fill(mileage)

    def click_add(self):
        self.add_button.click()

    def add_car(self, mileage: str):
        self.fill_mileage(mileage)
        self.click_add()
