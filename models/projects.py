from sys import maxsize


class Projects:
    def __init__(self, name=None, status=None, inherit_global=None,
                 view_state=None, enabled=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.enabled = enabled

    def __repr__(self):
        return "%s:%s;%s;%s;" % (self.name, self.status, self.inherit_global,
                                self.view_state)

    def sorted_name(self):
        if self.name:
            return self.name