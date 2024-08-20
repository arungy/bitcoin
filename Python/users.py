"""A class that can be used to represent users"""

import sys

class Users:
    """A simple attempt to represent a users"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is joined to our group.")

    def greet_user(self, message):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, Welcome to {message.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is attempted to login {self.login_attempts} times!")

"""
def main():
    mac_user = Users('arun', 'kumar')
    win_user = Users('rajesh', 'kanna')
    linux_user = Users('richard', 'stallman')
    oracle_user = Users('gopal', 'ram')

    #mac_user.describe_user()
    #mac_user.greet_user("mac")
    #
    #win_user.describe_user()
    #win_user.greet_user("windows")
    #
    #linux_user.describe_user()
    #linux_user.greet_user("ubuntu linux")
    #
    #oracle_user.describe_user()
    #oracle_user.greet_user("oracle")

    mac_user.describe_user()
    mac_user.greet_user("mac")

    mac_user.increment_login_attempts()
    mac_user.increment_login_attempts()
    mac_user.increment_login_attempts()
    mac_user.increment_login_attempts()
    mac_user.increment_login_attempts()
    mac_user.increment_login_attempts()
    mac_user.read_login_attempts()

    mac_user.reset_login_attempts()
    mac_user.read_login_attempts()

if __name__ == '__main__':
    main()
    sys.exit(1)
"""
