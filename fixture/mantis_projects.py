from models.projects import Projects
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    project_cache = None

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/mantisbt-1.2.20/")) or not \
                (wd.current_url.endswith("/mantisbt-1.2.20/my_view_page.php")):
            wd.find_element_by_link_text("My View").click()

    def manage(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("Manage").click()

    def manage_projects(self, password='root'):
        wd = self.app.wd
        self.manage()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self):
        wd = self.app.wd
        self.manage_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_in_form_project(Projects(name="uter", status="development",
                                           inherit_global="true", view_state="public", description="nani"))
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
        self.select_by_value("status", projects.status)
        self.change_field_value("inherit_global", projects.inherit_global)
        self.select_by_value("view_state", projects.view_state)
        self.change_field_value("description", projects.description)

    def select_by_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_value('10')

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.manage_projects()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("body > table:nth-child(6) > tbody > tr.row-1"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                view_state = cells[3].text
                description = cells[4].text
                self.project_cache.append(Projects(name=name, status=status, enabled=enabled,
                                    view_state=view_state, description=description))
        return list(filter(None, self.project_cache))

    def get_project_from_row(self):
        wd = self.app.wd
        try:
            elements = wd.find_elements_by_css_selector("body > table:nth-child(6) > tbody > tr.row-1 [href]")
            for element in elements:
                element.click()
        finally:
            pass
        #wd.find_element_by_partial_link_text("/manage_proj_edit_page.php?project").click()

    def delete_project(self):
        wd = self.app.wd
        self.open_home_page()
        self.manage_projects()
        self.get_project_from_row()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

















