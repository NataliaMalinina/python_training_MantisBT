from models.projects import Projects
from selenium.webdriver.support.ui import Select
from time import sleep


class ProjectHelper:

    project_cache = None

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def autorization(self):
        wd = self.app.wd
        self.open_home_page()
        login = wd.find_element_by_name("username")
        login.send_keys("administrator")
        password = wd.find_element_by_name("password")
        password.send_keys("root")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def manage(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("Manage").click()

    def manage_projects(self):
        wd = self.app.wd
        self.manage()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, projects):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_in_form_project(Projects(name=projects.name, status=projects.status,
                                           view_state=projects.view_state, description=projects.description))
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        if wd.find_elements_by_css_selector("body > div:nth-child(5) > table > tbody > tr:nth-child(1) > td"):
            self.manage_projects()
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()
            self.fill_in_form_project(Projects(name=projects.name, status=projects.status,
                inherit_global=projects.inherit_global, view_state=projects.view_state, description=projects.description))
            wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_home_page()
        self.project_cache = None


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
        # self.select_by_value("status", projects.status)
        # self.change_field_value("inherit_global", projects.inherit_global)
        # self.select_by_value("view_state", projects.view_state)
        # self.change_field_value("description", projects.description)

    def select_by_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_value('10')

    def get_project_list(self, reset_cache=False):
        if reset_cache:
            self.project_cache = None
        if self.project_cache is None:
            wd = self.app.wd
            self.manage_projects()
            self.project_cache = []
            elements = wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")
            for element in elements:
                if element.get_attribute("class") not in ('', 'row-category'):
                    cells = element.find_elements_by_tag_name("td")
                    name = cells[0].text
                    status = cells[1].text
                    enabled = cells[2].text
                    view_state = cells[3].text
                    description = cells[4].text
                    self.project_cache.append(Projects(name=name, status=status, enabled=enabled,
                                        view_state=view_state, description=description))
        return list(filter(None, self.project_cache))

    def get_project_from_row(self, project):
        wd = self.app.wd
        name = project.name
        try:
            wd.find_elements_by_css_selector("body > table:nth-child(6)")
            wd.find_element_by_link_text(name).click()                                                                        #("body > table:nth-child(6) > tbody > tr:nth-child(3) > td:nth-child(1) [href]")
        finally:
            pass

    def delete_project(self, project):
        wd = self.app.wd
        #element = wd.find_element_by_id("%s" % id).click()
        #element = wd.find_element_by_xpath("/html/body/table[3]/tbody/tr[3]")
        element = project
        # if element.get_attribute("class") not in ('', 'row-category'):
        #     cells = element.find_elements_by_tag_name("td")
        #     name = cells[0].text
        #     status = cells[1].text
        #     enabled = cells[2].text
        #     view_state = cells[3].text
        #     description = cells[4].text
        self.get_project_from_row(element)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        #return Projects(name=name, status=status, enabled=enabled,view_state=view_state, description=description)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        self.manage_projects()
        return len(wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr"))

















