import os


class Init:
    def __init__(self, config_data, transport):
        self.local_tmp_dir = 'tmp'
        self.config_data = config_data
        self.transport = transport

    def check_directories(self, location='remote'):
        """ Check if all the directories specified in the config files are present """
        if location == 'remote':
            if not self.transport.folder_exists(self.config_data['remote_files_folder']):
                print("Local directories are incorrect, please check files directory before proceeding. " +
                      self.config_data['remote_files_folder'])
                return False

            if not self.transport.folder_exists(self.config_data['remote_sql_folder']):
                print("Local directories are incorrect, please check SQL directory before proceeding. " +
                      self.config_data['remote_sql_folder'])
                return False

            if not self.transport.folder_exists(self.config_data['remote_temporary_folder']):
                print("Local directories are incorrect, please check tmp directory before proceeding. " +
                      self.config_data['remote_temporary_folder'])
                return False

            return True

        else:
            if os.path.isdir('public_html') and os.path.isdir('SQL') and os.path.isdir('tmp'):
                return True
            else:
                raise Exception("Local directories are incorrect, please create public_html, "
                                "SQL and tmp before proceeding")

    def startup(self):
        if not self.check_directories():
            print("Incorrect directory structure, some folders do not exist. please check cuppa_config.ini")

        if not os.path.exists(self.local_tmp_dir):
            os.makedirs(self.local_tmp_dir)
