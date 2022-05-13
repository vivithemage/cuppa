import sys
import tempfile

from paramiko import transport

from cuppa.config import Config
from cuppa.cuppa_ssh import CuppaSSH
from cuppa.filemanager import FileManager
from cuppa.projectdatabase import ProjectDatabase
from cuppa.filetransport import FileTransport

config = Config(sys.argv)
config_data = config.read_file()

ssh_connector = CuppaSSH(config_data)
connection = ssh_connector.open_connection()

transport = FileTransport(config_data)


def cuppa():
    arguments = config.get_cli_args()

    if arguments['primary_action'] == 'archive':
        """
        Bundles up the remote site into a zip and downloads to current directory
        """
        file_manager = FileManager(config_data, connection)
        remote_archive_path = file_manager.archive()

        if remote_archive_path:
            local_archive_path = tempfile.gettempdir() + '/cuppa-archive.zip'

            print("Zipped up project to remote path: " + remote_archive_path)
            print("Downloading to: " + local_archive_path)

            # Something up with zipping to tmp folder and then sshing in again to download.
            # Use a tmp folder in the home folder instead of the system tmp one.
            local_path = 'tmp/cuppa-archive.zip'
            remote_path = config_data['remote_temporary_folder'] + '/cuppa-archive.zip'

            transport.download(remote_path, local_path)

        print('Download complete')

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
