

class Config:
    def __init__(self, argv):
        self.file_name = 'cuppa.yml'
        self.argv = argv

    def get_cli_args(self):
        """ Retrieves the command line arguments

        :return : dict Lets cuppa know which actions to take
        """

        primary_action = self.argv[1]
        secondary_action = self.argv[2]

        """ Check the commands are know """
        if (primary_action != 'pull') and (primary_action != 'push'):
            print(f"'{primary_action}' is an unknown primary action. Try 'pull' or 'push'")
            return False

        if (secondary_action != 'db') and (primary_action != 'files'):
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
        result = {
            'primary_action': 'pull',
            'hostname': 'example.com',
            'username': 'test',
            'password': 'password123',
        }

        return result

    def save_file(self):
        return True

