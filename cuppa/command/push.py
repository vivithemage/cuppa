import os
from . generic import CommandGeneric
from cuppa.projectdatabase import ProjectDatabase
from cuppa.projectconfigparser import ProjectConfigParser


class CommandPush(CommandGeneric):
    def run(self):
        if self.args[0] == 'db':
            print("pushing db")
            """ Export the database locally """
            database = ProjectDatabase(self.config_data, self.connection)
            local_sql_path = database.export('local')

            """ Get remote url and replace dev url with live in sql file """
            config_parser = ProjectConfigParser(self.config_data, self.connection)
            local_config_variables = config_parser.read('local')
            remote_config_variables = config_parser.read('remote')

            updated_sql_file = database.search_and_replace_on_file(str(local_sql_path),
                                                                   local_config_variables['WP_SITEURL'],
                                                                   remote_config_variables['WP_SITEURL'])

            """ Upload updated SQL file to the temporary directory on the remote server """
            remote_sql_path = self.config_data['remote_sql_folder'] + '/' + os.path.basename(updated_sql_file)
            self.file_transport.upload(updated_sql_file, remote_sql_path)

            """ Update database with new sql file """
            database.update(remote_sql_path, 'remote')

        if self.args[0] == 'files':
            print("pushing files")

            """ Zip up files locally alone - similar to archive but exclude the sql """

            """ Upload the zip file """

            """ Extract and copy (without config file)"""
