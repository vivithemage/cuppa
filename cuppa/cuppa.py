import sys
from config import Config

config = Config(sys.argv)


def cuppa():
    arguments = config.get_cli_args()

    if arguments['primary_action'] == 'push':
        print('pushing...')
        if arguments['secondary_action'] == 'db':
            print('db...')

        if arguments['secondary_action'] == 'files':
            print('files...')

    if arguments['primary_action'] == 'pull':
        print('pulling...')
        if arguments['secondary_action'] == 'db':
            print('db...')

        if arguments['secondary_action'] == 'files':
            print('files...')


if __name__ == '__main__':
    cuppa()



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

