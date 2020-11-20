from models.projects import Projects
import random

def test_delete_project(app):
    app.mantis_projects.autorization()
    app.mantis_projects.manage_projects()
    if len(app.mantis_projects.get_project_list()) == 0:
        app.mantis_projects.create_new_project()
    old_list = app.mantis_projects.get_project_list()
    project = random.choice(old_list)
    app.mantis_projects.delete_project(project)
    new_list = app.mantis_projects.get_project_list(reset_cache=True)
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list, key=Projects.name_or_max) == sorted(new_list, key=Projects.name_or_max)




