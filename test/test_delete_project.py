from models.projects import Projects

def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.mantis_projects.get_project_list()) == 0:
        app.mantis_projects.create_new_project()
    old_list_count = app.mantis_projects.count()
    old_list_of_projects = app.mantis_projects.get_project_list()
    deleted_project = app.mantis_projects.delete_project()
    assert old_list_count - 1 == app.mantis_projects.count()
    new_list_of_projects = app.mantis_projects.get_project_list()
    old_list_of_projects.remove(deleted_project)
    assert sorted(old_list_of_projects, key=Projects.name_or_max) == sorted(new_list_of_projects,
                                                                            key=Projects.name_or_max)

