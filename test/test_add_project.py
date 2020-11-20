from models.projects import Projects
import string
import random
#from random import randint


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project_name = random_project_name("project", 7)
    add_project = Projects(name=project_name, status="development", view_state='public', description='test element')
    app.mantis_projects.autorization()
    app.mantis_projects.manage_projects()
    old_list = app.mantis_projects.get_project_list()
    app.mantis_projects.create_new_project(add_project)
    new_list = app.mantis_projects.get_project_list()
    assert len(old_list) + 1 == len(new_list)
    assert app.soap.get_list_from_soap("administrator", "root")
    pass






















