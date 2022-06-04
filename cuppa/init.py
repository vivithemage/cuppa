import os


class Init:
    def __init__(self, config_data, connection, transport):
        self.local_tmp_dir = 'tmp'
        self.config_data = config_data
        self.transport = transport
        self.connection = connection

    def check_available_commands(self, location='remote'):
        """ Check required command line tools are installed on the
         remote server """

        if location == 'remote':
            command = 'zip --help'

            stdin, stdout, stderr = self.connection.exec_command(command)
            errors = stderr.readlines()
            output = stdout.readlines()

            if errors or len(output) == 0:
                return False

            return True

    def check_directories(self, location='remote'):
        """ Check if all the directories specified in the config files are present along
         with the implicit ones (e.g. SQL, tmp) on the local machine """
        missing_directory = False

        if location == 'remote':
            remote_directories = [
                self.config_data['remote_files_folder'],
                self.config_data['remote_sql_folder'],
                self.config_data['remote_temporary_folder']
            ]

            for remote_dir in remote_directories:
                if not self.transport.folder_exists(remote_dir):
                    print("Local directories are incorrect, please check " + remote_dir +
                          " directory before proceeding. ")
                    missing_directory = True
        else:
            local_directories = [
                'public_html',
                'SQL',
                'tmp'
            ]

            for local_dir in local_directories:
                if not os.path.isdir(local_dir):
                    print("Missing directory " + local_dir)
                    missing_directory = True

        if missing_directory:
            return False

        return True

    def startup(self):
        if not self.check_directories('remote'):
            print("Incorrect directory structure, some folders do not exist. please check cuppa_config.ini")
            exit()

        if not self.check_directories('local'):
            print("Please make relevant local directories before proceeding.")
            exit()

        if not self.check_available_commands('remote'):
            print("Some commands are not available, check remote server has zip installed.")
            exit()

        # Make the tmp directory if it does not exist.
        if not os.path.exists(self.local_tmp_dir):
            os.makedirs(self.local_tmp_dir)
