import pytest
from cuppa.config import Config
from cuppa.ssh import SSHConnection

config_file = 'cuppa.ini'

result = {
    'primary_action': 'pull',
    'secondary_action': 'db',
}

file_result = {
    'hostname': 'example.com',
    'username': 'user',
    'password': 'pass',
    'remote_files_folder': '/home/user/public_html',
    'remote_sql_folder': '/home/user/SQL'
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


def test_open_ssh_connection():
    """"  Basic test to see if we can connect over ssh with the details provided in the config
        If any errors are returned from running the command, the connection is deemed to have failed,
    """

    config = Config(test_argv)
    config_data = config.read_file()

    ssh_connector = SSHConnection(config_data)
    connection = ssh_connector.open_connection()

    test_command = 'ls'
    stdin, stdout, stderr = connection.exec_command(test_command)
    errors = stderr.readlines()

    if errors:
        assert False
    else:
        assert True


def test_run_ssh_command():
    assert True


def test_file_upload():
    assert True


def test_file_download():
    assert True


def test_check_local_folder_structure():
    assert True


def test_check_remote_folder_structure():
    assert True

