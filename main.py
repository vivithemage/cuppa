import sys
from pathlib import Path

from cuppa.config import Config
from cuppa.cuppa_ssh import CuppaSSH
from cuppa.filemanager import FileManager
from cuppa.filetransport import FileTransport
from cuppa.init import Init

config = Config(sys.argv)
config_data = config.read_file()

ssh_connector = CuppaSSH(config_data)
connection = ssh_connector.open_connection()

transport = FileTransport(config_data)

init = Init(config_data, connection)


def cuppa():
    init.startup()
    arguments = config.get_cli_args()

    if arguments['primary_action'] == 'archive':
        """
        Bundles up the remote site into a zip and downloads to current directory
        """
        file_manager = FileManager(config_data, connection)
        remote_archive_path = file_manager.archive()

        if remote_archive_path:
            """
            Something up with zipping to tmp folder and then sshing in again to download.
            Use a tmp folder in the home folder instead of the system tmp one.
            """

            local_path = Path('tmp') / 'cuppa-archive.zip'
            remote_path = config_data['remote_temporary_folder'] + '/cuppa-archive.zip'

            print("Zipped up project to remote path: ")
            print(remote_archive_path)

            print("Downloading to: ")
            print(local_path)

            transport.download(remote_path, local_path)

        print('Download complete')

    if arguments['primary_action'] == 'pull':

        print('pulling ')
        if arguments['secondary_action'] == 'db':
            print('database')

        if arguments['secondary_action'] == 'files':
            print('files...')

    if arguments['primary_action'] == 'push':
        print('pushing...')
        if arguments['secondary_action'] == 'db':
            print('db...')

        if arguments['secondary_action'] == 'files':
            print('files...')


if __name__ == '__main__':
    cuppa()
