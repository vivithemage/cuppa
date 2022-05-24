import sys

from cuppa.config import Config
from cuppa.init import Init
from cuppa.cuppa_ssh import CuppaSSH
from cuppa.filetransport import FileTransport

from cuppa.command.archive import CommandArchive
from cuppa.command.push import CommandPush
from cuppa.command.pull import CommandPush


def cuppa():
    config = Config(sys.argv)
    config_data = config.read_file()

    ssh_connector = CuppaSSH(config_data)
    connection = ssh_connector.open_connection()
    file_transport = FileTransport(config_data)

    init = Init(config_data, file_transport)
    init.startup()

    arguments = config.get_cli_args()

    if arguments['primary_action'] == 'archive':
        command = CommandArchive(config_data, connection, file_transport)

    if arguments['primary_action'] == 'pull':
        print('pulling ')
        if arguments['secondary_action'] == 'db':
            command = CommandPush(config_data, connection, file_transport, ['db'])

        if arguments['secondary_action'] == 'files':
            command = CommandPush(config_data, connection, file_transport, ['files'])

    if arguments['primary_action'] == 'push':
        print('pushing...')
        if arguments['secondary_action'] == 'db':
            command = CommandPush(config_data, connection, file_transport, ['db'])

        if arguments['secondary_action'] == 'files':
            command = CommandPush(config_data, connection, file_transport, ['db'])

    command.run()


if __name__ == '__main__':
    cuppa()
