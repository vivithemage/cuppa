import os
from pathlib import Path
from . generic import CommandGeneric
from cuppa.projectdatabase import ProjectDatabase
from cuppa.utils import tmp_directory_cleanup
from cuppa.filemanager import FileManager
from ..projectconfigparser import ProjectConfigParser


class CommandPull(CommandGeneric):
    def run(self):
        if self.args[0] == 'db':
            print("pulling db")
            """ Exporting database on remote server """
            database = ProjectDatabase(self.config_data, self.connection)
            remote_sql_file_path = database.export('remote')

            """ Download SQL file to tmp folder """
            sql_file_name = os.path.basename(remote_sql_file_path)
            local_sql_path = Path('SQL') / sql_file_name
            self.file_transport.download(remote_sql_file_path, local_sql_path)

            """ Export local database """
            local_backup_sql_path = database.export('local', True)

            # """ Extract database credentials from config """
            wp_config = ProjectConfigParser(self.config_data, self.connection)
            wp_config_variables = wp_config.read('local')

            # print(wp_config_variables)
            """ Make new database """

            """ Import SQL file """
            database.update(local_sql_path, 'local')

            """ Change wp-config to use new database. """

        if self.args[0] == 'files':
            print("Pulling files")
            archive_filename = 'cuppa-archive.zip'

            """ Bundle up files remotely alone - similar to archive but exclude the sql """
            file_manager = FileManager(self.config_data, self.connection)
            remote_archive_path = file_manager.archive()
            local_path = Path('tmp') / archive_filename
            remote_path = self.config_data['remote_temporary_folder'] + '/' + archive_filename

            print("Zipped up project to remote path: " + remote_archive_path)
            print("Downloading to: " + str(local_path))

            self.file_transport.download(remote_path, local_path)

            """ Extract and move all files other than config to public_html """
            file_manager.extract('local')
            file_manager.update_files_dir('local')

            tmp_directory_cleanup()
            print("Pulling files complete")


