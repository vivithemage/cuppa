# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# Open ssh connection


"""
generate name for backup (backup-randomid.zip)
apt install zip
rm -rf /home/thrive/SQL/*
rm -rf /home/thrive/public_html/.git ## probably not needed
mysqldump -u root -p crownmickleton > crownmickleton.sql
zip -r backup-0C5P5qPrlQhm.zip /home/thrive/public_html/ /home/thrive/SQL/
echo zip file

"""


"""
Downloads repository
logs in to server and downloads latest files
downloads database
sets up database
configures wp-config
"""

