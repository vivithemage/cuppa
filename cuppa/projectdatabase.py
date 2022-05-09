import tempfile
from . projectconfigparser import ProjectConfigParser


class ProjectDatabase:
    def __init__(self, config_data, connection):
        self.config_data = config_data
        self.tmp_dir = tempfile.gettempdir()
        self.connection = connection
        self.config_filename = 'wp-config.php'

    def export(self, location='remote'):
        if location == 'remote':
            print("Exporting remote database.")

            wp_config = ProjectConfigParser(self.config_data, self.connection)
            wp_config_variables = wp_config.read()

            remote_sql_file_path = self.config_data['remote_sql_folder'] + '/' + wp_config_variables['DB_NAME'] + '.sql'

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
