from models.projects import Projects
import string
import random


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project_name = random_project_name("project", 13)
    add_project = Projects(name=project_name, status='development', view_state='public')
    app.mantis_projects.autorization()
    app.mantis_projects.manage_projects()
    old_list = app.mantis_projects.get_project_list()
    app.mantis_projects.create_new_project(add_project)
    new_list = app.mantis_projects.get_project_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(add_project)
    assert sorted(old_list, key=Projects.sorted_name) == sorted(new_list, key=Projects.sorted_name)
    soap_projects = app.soap.get_list_from_soap("administrator", "root")
    assert len(soap_projects) == len(new_list)





















