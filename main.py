import sys
from cuppa.config import Config
from cuppa.cuppa_ssh import CuppaSSH
from cuppa.projectdatabase import ProjectDatabase

config = Config(sys.argv)
config_data = config.read_file()

ssh_connector = CuppaSSH(config_data)
connection = ssh_connector.open_connection()


def cuppa():
    arguments = config.get_cli_args()

    if arguments['primary_action'] == 'archive':
        database = ProjectDatabase(config_data, connection)
        remote_sql_file_path = database.export('remote')
        print(remote_sql_file_path)
        print('archiving')

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
