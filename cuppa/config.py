

class Config:
    def __init__(self, argv):
        self.file_name = 'cuppa.yml'
        self.argv = argv

    def get_cli_args(self):
        result = {
            'primary_action': 'pull',
            'hostname': 'example.com',
            'username': 'test',
            'password': 'password123',
        }

        return result

    def read_file(self):
        result = {
            'primary_action': 'pull',
            'hostname': 'example.com',
            'username': 'test',
            'password': 'password123',
        }

        return result

    def save_file(self):
        return True

