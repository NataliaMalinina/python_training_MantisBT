from models.projects import Projects


def test_add_project(app):
    app.session.login("administrator", "root")
    app.mantis_projects.create_new_project()