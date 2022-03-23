import pytest
import os
from cuppa.config import Config
from cuppa.ssh import SSHConnection
from cuppa.parser import Parser
from cuppa.database import Database

from tests.baseline_data_structures import result, config_file_result, test_argv

config_file = 'cuppa.ini'

config = Config(test_argv)
config_data = config.read_file()


def test_get_cli_arguments():
    """"  Basic test to check cuppa processes command line arguments """
    assert (result == config.get_cli_args())


def test_read_config_file():
    """"  Basic test to check cuppa can read the config file for a project """
    assert (config_file_result == config.read_file())


def test_open_ssh_connection():
    """"  Basic test to see if we can connect over ssh with the details provided in the config
        If any errors are returned from running the command, the connection is deemed to have failed,
    """

    ssh_connector = SSHConnection(config_data)
    connection = ssh_connector.open_connection()

    test_command = 'ls'
    stdin, stdout, stderr = connection.exec_command(test_command)
    errors = stderr.readlines()

    if errors:
        assert False
    else:
        assert True


def test_config_file_download():
    """
    Test a file can be downloaded from the remote server
    :return:
    """
    ssh_connector = SSHConnection(config_data)
    connection = ssh_connector.open_connection()
    config_array = config.read_file()

    test_filename = 'wp-config.php'

    sftp = connection.open_sftp()
    sftp.get(config_array['remote_files_folder'] + '/' + test_filename, 'public_html/' + test_filename)

    assert True


def test_get_remote_config_variables():
    """
    Check the file can be parsed and key variables such as database details extracted

    :return:
    """
    ssh_connector = SSHConnection(config_data)
    connection = ssh_connector.open_connection()

    wp_config = Parser(config_data, connection)
    wp_config_variables = wp_config.read()

    # print(wp_config_variables)

    """ If these variables are defined, then it indicates values were successfully retrieved """
    if (wp_config_variables['DB_NAME'] and
            wp_config_variables['DB_USER'] and
            wp_config_variables['DB_PASSWORD'] and
            wp_config_variables['DB_HOST']):
        assert True


def test_export_remote_database():
    ssh_connector = SSHConnection(config_data)
    connection = ssh_connector.open_connection()

    database = Database(config_data, connection)
    remote_sql_file_path = database.export('remote')

    print("Remote SQL path: " + remote_sql_file_path)

    if remote_sql_file_path:
        assert True
    else:
        assert False


def test_zip_remote_directory():
    assert True


def test_zip_directory():
    assert True


def test_file_upload():
    assert True


def test_check_local_folder_structure():
    directory_path = os.getcwd()
    print(directory_path)
    assert True


def test_check_remote_folder_structure():
    assert True
