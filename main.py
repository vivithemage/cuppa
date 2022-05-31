import sys

from cuppa.config import Config
from cuppa.init import Init
from cuppa.cuppa_ssh import CuppaSSH
from cuppa.filetransport import FileTransport

from cuppa.command.archive import CommandArchive
from cuppa.command.push import CommandPush
from cuppa.command.pull import CommandPull


def cuppa():
    config = Config(sys.argv)
    config_data = config.read_file()

    arguments = config.get_cli_args()

    ssh_connector = CuppaSSH(config_data)
    connection = ssh_connector.open_connection()
    file_transport = FileTransport(config_data)

    init = Init(config_data, file_transport)
    init.startup()

    if arguments['primary_action'] == 'archive':
        command = CommandArchive(config_data, connection, file_transport)

    if arguments['primary_action'] == 'pull':
        if arguments['secondary_action'] == 'db':
            command = CommandPull(config_data, connection, file_transport, ['db'])

        if arguments['secondary_action'] == 'files':
            command = CommandPull(config_data, connection, file_transport, ['files'])

    if arguments['primary_action'] == 'push':
        if arguments['secondary_action'] == 'db':
            command = CommandPush(config_data, connection, file_transport, ['db'])

        if arguments['secondary_action'] == 'files':
            command = CommandPush(config_data, connection, file_transport, ['files'])

    command.run()


if __name__ == '__main__':
    cuppa()
