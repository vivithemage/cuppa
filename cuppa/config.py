from configparser import ConfigParser


class Config:
    def __init__(self, argv):
        self.file_name = 'cuppa.yml'
        self.argv = argv

    def _valid_args(self):
        """ Check there are enough arguments to do anything

        :return: Bool Whether the arguments are valid
        """
        if len(self.argv) <= 2:
            return False

        return True

    def get_cli_args(self):
        """ Retrieves the command line arguments

        :return : dict Lets cuppa know which actions to take
        """

        if self._valid_args() is False:
            print("Not enough arguments. try cuppa pull db")
            exit()

        primary_action = self.argv[1]
        secondary_action = self.argv[2]

        """ Check the commands are know """
        if (primary_action != 'pull') and (primary_action != 'push'):
            print(f"'{primary_action}' is an unknown primary action. Try 'pull' or 'push'")
            return False

        if (secondary_action != 'db') and (secondary_action != 'files'):
            print(f"{secondary_action} is an unknown secondary action. Try 'db' or 'files'")
            return False

        result = {
            'primary_action': primary_action,
            'secondary_action': secondary_action,
        }

        return result

    def read_file(self):
        """
        Reads the config file which includes info such as hostname, username, password etc.

        :return dict
        """

        try:
            config_parser = ConfigParser()
            config_parser.read('example_config.ini')

            result = {
                'hostname': config_parser.get('general', 'hostname'),
                'username': config_parser.get('general', 'username'),
                'password': config_parser.get('general', 'password'),
                'remote_files_folder': config_parser.get('general', 'remote_files_folder'),
                'remote_sql_folder': config_parser.get('general', 'remote_sql_folder'),
                'remote_temporary_folder': config_parser.get('general', 'remote_temporary_folder'),
            }

            return result
        except:
            print("Exception thrown when reading config file. Please see Config class, read_file ")
            return False


