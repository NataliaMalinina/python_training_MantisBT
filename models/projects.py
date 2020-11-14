

class Projects:
    def __init__(self, name=None, status=None, inherit_global=None,
                 view_state=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s" % (self.id, self.name, self.status, self.inherit_global,
                                self.view_state, self.description)
