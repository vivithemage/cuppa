import tempfile
import sys
import re


class Parser:
    def __init__(self, config_data, connection):
        self.config_data = config_data
        self.tmp_dir = tempfile.gettempdir()
        self.connection = connection
        self.config_filename = 'wp-config.php'

    def _get_variable(self, key, content):
        regex_key = r'define\(\s*?\'' + key + r'\'\s*?,\s*?\'(.*?)\'\s*?'
        value = re.search(regex_key, content).group(1)
        return value

    def _remote_file(self):
        sftp = self.connection.open_sftp()
        local_filepath = self.tmp_dir + '/' + self.config_filename
        remote_filepath = self.config_data['remote_files_folder'] + '/' + self.config_filename
        sftp.get(remote_filepath, local_filepath)

        return local_filepath

    def read(self):
        try:
            with open(self._remote_file()) as f:
                content = f.read()

                return {
                    'DB_USER':  self._get_variable('DB_USER', content),
                    'DB_PASSWORD': self._get_variable('DB_PASSWORD', content),
                    'DB_HOST': self._get_variable('DB_HOST', content),
                    'DB_NAME': self._get_variable('DB_NAME', content)
                }

        except FileNotFoundError:
            print('File Not Found')
            sys.exit(1)
