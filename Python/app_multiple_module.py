import sys

from admin import Admin

def main():
    ad_raj = Admin('Raj', 'kumar')

    ad_raj.add_privilege('can add post')
    ad_raj.add_privilege('can delete post')
    ad_raj.add_privilege('can ban user')

    ad_raj.privileges.show_privileges()

if __name__ == '__main__':
     main()
     sys.exit(1)
