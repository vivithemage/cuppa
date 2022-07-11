import os
import time
import tempfile
import uuid
from distutils.dir_util import copy_tree
from pathlib import Path
from sys import platform

from . projectconfigparser import ProjectConfigParser


class ProjectDatabase:
    def __init__(self, config_data, connection):
        self.config_data = config_data
        self.tmp_dir = tempfile.gettempdir()
        self.connection = connection
        self.config_filename = 'wp-config.php'

    def get_mysql_exe_path(self):
        if platform == "linux" or platform == "linux2":
            return 'mysql'
        elif platform == "win32":
            return self.config_data['mysql_path']
        else:
            return 'mysql'

    def search_and_replace_on_file(self, file_path, search_text, replace_text):
        amended_file_path = Path('SQL') / (str(uuid.uuid4()) + '.sql')

        print("Starting replace of " + search_text + " with " + replace_text + " in " + file_path)
        print("New sql file with replaced text is: " + str(amended_file_path))
        print("This may take some time.")

        original_file = open(file_path, encoding='utf-8')
        amended_file = open(amended_file_path, 'a', encoding='utf-8')

        """ Go through the original sql file and do a text replace if a match is found
        Large SQL files could become an issue, so this line by line method should be less
        resource intensive than loading everything into RAM. """
        for line in original_file:
            if search_text in line:
                amended_line = line.replace(search_text, replace_text)
            else:
                amended_line = line

            amended_file.write(amended_line)

        original_file.close()
        amended_file.close()

        print("Search and replace process complete")

        return str(amended_file_path)

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

    def create(self, db_name, wp_config_variables, location='remote'):
        if location == 'remote':
            return True
        else:
            command = self.get_mysql_exe_path() + ' -u ' + wp_config_variables['DB_USER'] + ' -p' \
                      + wp_config_variables['DB_PASSWORD'] + ' -e ' + '"create database ' + db_name + '"'

            errors = os.system(command)

            if errors:
                return False
            else:
                return True

    def drop(self, db_name, wp_config_variables, location='remote'):
        if location == 'remote':
            return True
        else:
            command = self.get_mysql_exe_path() + ' -u' + wp_config_variables['DB_USER'] + ' -p' \
                      + wp_config_variables['DB_PASSWORD'] + ' -e ' + '"drop database ' + db_name + '"'

            errors = os.system(command)

            if errors:
                return False
            else:
                return True


    def update(self, sql_filepath, location='remote'):
        wp_config = ProjectConfigParser(self.config_data, self.connection)

        if location == 'remote':
            return True
        else:
            wp_config_variables = wp_config.read('local')

            """ Get rid of existing db and recreate """
            self.drop(wp_config_variables['DB_NAME'], wp_config_variables, 'local')
            self.create(wp_config_variables['DB_NAME'], wp_config_variables, 'local')

            local_sql_path = sql_filepath

            command = self.get_mysql_exe_path() + ' -u ' + wp_config_variables['DB_USER'] + ' -p' + wp_config_variables['DB_PASSWORD'] \
                      + ' ' + wp_config_variables['DB_NAME'] + ' < ' + local_sql_path

            errors = os.system(command)

            if errors:
                return False
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
