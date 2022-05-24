from pathlib import Path
from cuppa.filemanager import FileManager


class CommandArchive:
    def __init__(self, config_data, connection, file_transport):
        self.connection = connection
        self.config_data = config_data
        self.file_transport = file_transport

    def run(self):
        """
        Bundles up the remote site into a zip and downloads to current directory
        """
        file_manager = FileManager(self.config_data, self.connection)
        remote_archive_path = file_manager.archive()

        if remote_archive_path:
            """
            Something up with zipping to tmp folder and then sshing in again to download.
            Use a tmp folder in the home folder instead of the system tmp one.
            """

            local_path = Path('tmp') / 'cuppa-archive.zip'
            remote_path = self.config_data['remote_temporary_folder'] + '/cuppa-archive.zip'

            print("Zipped up project to remote path: ")
            print(remote_archive_path)

            print("Downloading to: ")
            print(local_path)

            self.file_transport.download(remote_path, local_path)

        print('Download complete')

