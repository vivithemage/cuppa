import os
from pathlib import Path
from . generic import CommandGeneric
from cuppa.projectdatabase import ProjectDatabase
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

            """ Export local database """
            database.export('local')

            # """ Extract database credentials from config """
            # wp_config = ProjectConfigParser(self.config_data, self.connection)
            # wp_config_variables = wp_config.read('local')

            # print(wp_config_variables)


            """ Make new database """

            """ Import SQL file """

            """ Change wp-config to use new database. """

        if self.args[0] == 'files':
            print("pulling files")

            """ Bundle up files remotely alone - similar to archive but exclude the sql """

            """ Move all files other than config to public_html """


