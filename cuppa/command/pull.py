from . generic import CommandGeneric
from cuppa.projectdatabase import ProjectDatabase


class CommandPull(CommandGeneric):
    def run(self):
        if self.args[0] == 'db':
            print("pulling db")
            """ Exporting database on remote server """
            database = ProjectDatabase(self.config_data, self.connection)
            # remote_sql_file_path = database.export('remote')
            # self.file_transport.download(local_path, remote_path)

            """ Download SQL file to tmp folder """

            """ Extract database credentials from config """

            """ Make new database """

            """ Import SQL file """

            """ Change wp-config to use new database. """

        if self.args[0] == 'files':
            print("pulling files")

            """ Download archive """

            """ Move all files other than wp-config to public_html """


