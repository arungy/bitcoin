"""A class than can be used to represent administrator"""

import sys

from users import Users
from privileges import Privileges

class Admin(Users):
    """An attempt to model the admin"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(first_name, last_name)

    def add_privilege(self, privilege):
        self.privileges.privileges_data.append(privilege)

