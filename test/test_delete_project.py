

def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.mantis_projects.get_project_list()) == 0:
        app.mantis_projects.create_new_project()
    app.mantis_projects.delete_project()
