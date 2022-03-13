import pytest
from cuppa.config import Config

config_file = 'cuppa.ini'

result = {
    'primary_action': 'pull',
    'secondary_action': 'db',
}

file_result = {
    'hostname': 'example.com',
    'username': 'user',
    'password': 'pass',
    'remote_files_folder': '/home/user/public_html'
}

test_argv = [
    '/home/vivi/workspace/cuppa/cuppa/cuppa.py',
    'pull',
    'db']


def test_get_cli_arguments():
    """"  Basic test to check cuppa processes command line arguments """

    config = Config(test_argv)
    assert(result == config.get_cli_args())


def test_read_config_file():
    """"  Basic test to check cuppa can read the config file for a project """
    config = Config(test_argv)
    assert (file_result == config.read_file())
