import os
import time
import tempfile
from distutils.dir_util import copy_tree
from pathlib import Path

from . projectconfigparser import ProjectConfigParser


class ProjectDatabase:
    def __init__(self, config_data, connection):
        self.config_data = config_data
        self.tmp_dir = tempfile.gettempdir()
        self.connection = connection
        self.config_filename = 'wp-config.php'

    def update_sql_dir(self, location='local'):
        """
        This overwrites the SQL folter with the database export
        """
        if location == 'local':
            files_dir = 'tmp' + self.config_data['remote_sql_folder']
            return copy_tree(files_dir, 'SQL')

    def get_filename(self, database_name, timestamp):
        if timestamp:
            t = time.localtime()
            stamp = time.strftime('-%b-%d-%Y_%H%M', t)

        sql_filename = database_name

        if timestamp:
            sql_filename += stamp

        return sql_filename + '.sql'

    def create(self, location='remote'):
        if location == 'remote':
            return True
        else:
            return True

    def drop(self, location='remote'):
        if location == 'remote':
            return True
        else:
            return True

    def update(self, sql_filepath, location='remote'):
        if location == 'remote':
            return True
        else:
            return True

    def export(self, location='remote', timestamp=False):
        wp_config = ProjectConfigParser(self.config_data, self.connection)

        if location == 'remote':
            print("Exporting remote database.")

            wp_config_variables = wp_config.read('remote')

            remote_sql_file_path = self.config_data['remote_sql_folder'] + '/' \
                + self.get_filename(wp_config_variables['DB_NAME'], timestamp)

            command = 'mysqldump -h ' + wp_config_variables['DB_HOST'] + ' -u' + wp_config_variables['DB_USER'] \
                      + ' -p' + wp_config_variables['DB_PASSWORD'] + ' ' + wp_config_variables['DB_NAME'] \
                      + ' > ' + remote_sql_file_path

            stdin, stdout, stderr = self.connection.exec_command(command)
            errors = stderr.readlines()

            if errors:
                return False
            else:
                return remote_sql_file_path

        else:
            print("Exporting local database.")

            wp_config_variables = wp_config.read('local')

            local_sql_file_path = Path('SQL') / self.get_filename(wp_config_variables['DB_NAME'], timestamp)
            # TODO make this cross platform
            mysqldump_path = Path(self.config_data['mysql_path']) / 'mysqldump'

            command = str(mysqldump_path) + ' -h ' + wp_config_variables['DB_HOST'] + ' -u' + wp_config_variables['DB_USER'] \
                      + ' -p' + wp_config_variables['DB_PASSWORD'] + ' ' + wp_config_variables['DB_NAME'] \
                      + ' > ' + str(local_sql_file_path)

            os.system(command)

            return str(local_sql_file_path)

            # return False
