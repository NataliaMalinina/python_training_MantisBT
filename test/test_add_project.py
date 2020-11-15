from models.projects import Projects
from random import randint

def test_add_project(app):
    project_name = str(randint(-999999999, 999999999))
    add_project = Projects(name=project_name,
                           status='development',
                           view_state='public',
                           description="test element")
    app.session.login("administrator", "root")
    old_list_of_projects = app.mantis_projects.get_project_list()
    old_list_count = app.mantis_projects.count()
    app.mantis_projects.create_new_project(add_project)
    assert old_list_count+1 == app.mantis_projects.count()
    new_list_of_projects = app.mantis_projects.get_project_list()
    old_list_of_projects.append(add_project)
    assert sorted(old_list_of_projects, key=Projects.name_or_max) == sorted(new_list_of_projects,
                                                                            key=Projects.name_or_max)
