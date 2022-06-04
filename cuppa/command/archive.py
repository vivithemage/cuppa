from pathlib import Path
from . generic import CommandGeneric
from cuppa.filemanager import FileManager
from cuppa.projectdatabase import ProjectDatabase


class CommandArchive(CommandGeneric):
    def export_db(self):
        database = ProjectDatabase(self.config_data, self.connection)
        remote_sql_file_path = database.export('remote')

        return remote_sql_file_path

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

            self.export_db()
            local_path = Path('tmp') / 'cuppa-archive.zip'
            remote_path = self.config_data['remote_temporary_folder'] + '/cuppa-archive.zip'

            print("Zipped up project to remote path: " + remote_archive_path)

            print("Downloading to: " + str(local_path))

            self.file_transport.download(remote_path, local_path)

        print('Download complete')

