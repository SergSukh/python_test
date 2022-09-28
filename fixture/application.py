from selenium import webdriver
from fixture.session import SessionHelper
from fixture.client_info.group import GroupHelper
from fixture.client_info.contact import ContactHelper
from fixture.client_info.passport import PassportHelper
from fixture.client_info.parent import ParentHelper
from fixture.client_info.address import AddressHelper
from fixture.client_info.information import InformationHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.passport = PassportHelper(self)
        self.parent = ParentHelper(self)
        self.address = AddressHelper(self)
        self.information = InformationHelper(self)

    def open_homepage(self):
        wd = self.wd
        # wd.get("https://stablev10.ci.dental-pro.online/")
        # wd.get("https://betav10.ci.dental-pro.online/")
        # wd.get("https://stndnextlite.dm.dental-pro.online/dashboard/widgets/index")
        wd.get("https://stablev10.dm.dental-pro.online/")
        wd.set_window_size(1920, 1080)

    def destroy(self):
        wd = self.wd
        wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
