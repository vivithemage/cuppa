from os.path import exists
from configparser import ConfigParser


class Config:
    def __init__(self, argv):
        self.file_name = 'cuppa.yml'
        self.argv = argv

    def _valid_args(self):
        """ Check there are enough arguments to do anything

        :return: Bool Whether the arguments are valid
        """
        if self.argv[1] != 'archive':
            if len(self.argv) <= 2:
                return False

        return True

    def get_cli_args(self):
        """ Retrieves the command line arguments

        :return : dict Lets cuppa know which actions to take
        """

        actions = {
            'primary_action': False,
            'secondary_action': False,
        }

        if self._valid_args() is False:
            print("Not enough arguments. try cuppa pull db")
            exit()

        actions['primary_action'] = self.argv[1]

        """ Check the commands are know """
        if (actions['primary_action'] != 'pull') and \
                (actions['primary_action'] != 'push') and \
                (actions['primary_action'] != 'archive'):
            print(f"'{actions['primary_action']}' is an unknown primary action. Try 'pull' or 'push'")
            return False

        if actions['primary_action'] != 'archive':
            actions['secondary_action'] = self.argv[2]
            if (actions['secondary_action'] != 'db') and (actions['secondary_action'] != 'files'):
                print(f"{actions['secondary_action']} is an unknown secondary action. Try 'db' or 'files'")
                return False

        return actions

    def config_present_in_dir(self):
        return exists('cuppa_config.ini')

    def read_file(self):
        """
        Reads the config file which includes info such as hostname, username, password etc.

        :return dict
        """

        if not self.config_present_in_dir():
            print("Config (cuppa_config.ini) is not present. Please add one to this directory.")
            exit()

        try:
            config_parser = ConfigParser()
            if exists('cuppa_config.ini'):
                config_parser.read('cuppa_config.ini')

                result = {
                    'hostname': config_parser.get('general', 'hostname'),
                    'username': config_parser.get('general', 'username'),
                    'password': config_parser.get('general', 'password'),
                    'remote_files_folder': config_parser.get('general', 'remote_files_folder'),
                    'remote_sql_folder': config_parser.get('general', 'remote_sql_folder'),
                    'remote_temporary_folder': config_parser.get('general', 'remote_temporary_folder'),
                }

                return result
            else:
                print("config file does is not present.")
        except:
            print("Exception thrown when reading config file. Please see Config class, read_file ")
            return False
