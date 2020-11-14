from models.projects import Projects
from selenium.webdriver.support.ui import Select

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/mantisbt-1.2.20/")) or not \
                (wd.current_url.endswith("/mantisbt-1.2.20/my_view_page.php")):
            wd.find_element_by_link_text("My View").click()

    def manage(self, password='root'):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("Manage").click()
        #wd.find_element_by_css_selector("a[href='/mantisbt-1.2.20/manage_overview_page.php']").click()
        #wd.find_element_by_name("password").send_keys("%s" % password)

    def manage_projects(self):
        wd = self.app.wd
        self.manage(password='root')
        wd.find_element_by_link_text("Manage Projects").click()
        #wd.find_element_by_css_selector("a[href='/mantisbt-1.2.20/manage_proj_page.php]").click()


    def create_new_project(self):
        wd = self.app.wd
        self.manage_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_in_form_project(Projects(name="uter", status="development",
                                           inherit_global="true", view_state="public", description="nani"))
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_home_page()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        element = wd.find_element_by_name(field_name)
        if not element.is_selected():
            element.click()
        if text is not None and field_name != 'inherit_global':
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_in_form_project(self, projects):
        wd = self.app.wd
        self.change_field_value("name", projects.name)
        self.select_by_value("status", projects.status)
        self.change_field_value("inherit_global", projects.inherit_global)
        self.select_by_value("view_state", projects.view_state)
        self.change_field_value("description", projects.description)

    def select_by_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_value('10')












