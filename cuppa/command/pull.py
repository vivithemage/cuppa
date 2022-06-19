import os
from pathlib import Path
from . generic import CommandGeneric
from cuppa.projectdatabase import ProjectDatabase
from cuppa.utils import tmp_directory_cleanup
from cuppa.filemanager import FileManager
from cuppa.projectconfigparser import ProjectConfigParser


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

            """ Export local database for backup purposes """
            local_backup_sql_path = database.export('local', True)

            """ Extract database credentials from local config """
            config_parser = ProjectConfigParser(self.config_data, self.connection)
            local_config_variables = config_parser.read('local')
            remote_config_variables = config_parser.read('remote')

            """ Get domain url from exported config file (may not be in config) """
            database.search_and_replace_on_file(str(local_sql_path),
                                                remote_config_variables['WP_SITEURL'],
                                                local_config_variables['WP_SITEURL'])

            """ Search and replace on the domain url """

            # print(wp_config_variables)
            """ Make new database """

            """ Import SQL file into new mysql database """
            database.update(local_sql_path, 'local')

            """ Change wp-config to use new database. """


            """ Done """

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


