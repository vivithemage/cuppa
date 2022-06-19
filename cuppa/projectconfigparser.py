import tempfile
import sys
import re
from pathlib import Path

from . filetransport import FileTransport


class ProjectConfigParser:
    def __init__(self, config_data, connection):
        self.config_data = config_data
        self.tmp_dir = tempfile.gettempdir()
        self.connection = connection
        self.config_filename = 'wp-config.php'
        self.transport = FileTransport(self.config_data)

    def _get_variable(self, key, content):
        try:
            regex_key = r'define\(\s*?\'' + key + r'\'\s*?,\s*?\'(.*?)\'\s*?'
            value = re.search(regex_key, content).group(1)
            return value
        except:
            print("Unable to read config variable: " + key)
            print("Check this exists and is correct in both remote and local configs. Exiting...")
            exit(1)

    def _remote_file(self):
        local_filepath = self.tmp_dir + '/' + self.config_filename
        remote_filepath = self.config_data['remote_files_folder'] + '/' + self.config_filename
        self.transport.download(remote_filepath, local_filepath)

        return local_filepath

    def _local_file(self):
        local_filepath = Path('public_html') / self.config_filename
        return local_filepath

    def _valid_variables(self, config_variables):
        """ Check to see all variables at least have a value before continuing"""
        for variable in config_variables:
            if (type(variable) != str) or (len(variable) <= 0):
                return False

        return True

    def read(self, location='remote'):

        if location == 'remote':
            config_file = self._remote_file
        else:
            config_file = self._local_file

        try:
            with open(config_file()) as f:
                content = f.read()

                config_variables = {
                    'DB_USER':  self._get_variable('DB_USER', content),
                    'DB_PASSWORD': self._get_variable('DB_PASSWORD', content),
                    'DB_HOST': self._get_variable('DB_HOST', content),
                    'DB_NAME': self._get_variable('DB_NAME', content),
                    'WP_HOME': self._get_variable('WP_HOME', content),
                    'WP_SITEURL': self._get_variable('WP_SITEURL', content)
                }

                if self._valid_variables(config_variables):
                    return config_variables
                else:
                    print("Unable to read config, exiting...")
                    exit(1)

        except FileNotFoundError:
            print('File Not Found')
            sys.exit(1)
