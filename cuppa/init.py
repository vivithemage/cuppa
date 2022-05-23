import os


class Init:
    def __init__(self, config_data, connection):
        self.local_tmp_dir = 'tmp'
        self.config_data = config_data
        self.connection = connection

    def startup(self):
        if not self.check_directories():
            print("Incorrect directory structure, some folders do not exist. please check cuppa_config.ini")

        if not os.path.exists(self.local_tmp_dir):
            os.makedirs(self.local_tmp_dir)

    def check_directories(self, location='remote'):
        """ Check if all the directories specified in the config files are present """
        if location == 'remote':
            print('TODO')
            # try:
            #     self.connection.sftp.stat(self.config_data['remote_files_folder'])
            #     self.connection.sftp.stat(self.config_data['remote_sql_folder'])
            #     self.connection.sftp.stat(self.config_data['remote_temporary_folder'])
            #     return True
            # except FileNotFoundError:
            #     return False
        else:
            if os.path.isdir('public_html') and os.path.isdir('SQL') and os.path.isdir('tmp'):
                return True
            else:
                raise Exception("Local directories are incorrect, please create public_html, "
                                "SQL and tmp before proceeding")
