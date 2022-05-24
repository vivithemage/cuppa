import os
import tempfile
import shutil


from cuppa.config import Config
from cuppa.cuppa_ssh import CuppaSSH
from cuppa.filemanager import FileManager

from cuppa.filetransport import FileTransport
from cuppa.projectdatabase import ProjectDatabase
from cuppa.projectconfigparser import ProjectConfigParser
from cuppa.init import Init


from tests.baseline_data_structures import result, config_file_result, test_argv

config_file = 'cuppa.ini'

config = Config(test_argv)
config_data = config.read_file()

ssh_connector = CuppaSSH(config_data)
connection = ssh_connector.open_connection()

transport = FileTransport(config_data)


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
    config_array = config.read_file()

    test_filename = 'wp-config.php'
    local_path = 'tmp/' + test_filename
    remote_path = config_array['remote_files_folder'] + '/' + test_filename

    transport.download(remote_path, local_path)

    assert True


def test_get_remote_config_variables():
    """
    Check the file can be parsed and key variables such as database details extracted

    :return:
    """
    wp_config = ProjectConfigParser(config_data, connection)
    wp_config_variables = wp_config.read()

    # print(wp_config_variables)

    """ If these variables are defined, then it indicates values were successfully retrieved """
    if (wp_config_variables['DB_NAME'] and
            wp_config_variables['DB_USER'] and
            wp_config_variables['DB_PASSWORD'] and
            wp_config_variables['DB_HOST']):
        assert True


def test_export_remote_database():
    database = ProjectDatabase(config_data, connection)
    remote_sql_file_path = database.export('remote')

    if remote_sql_file_path:
        print("Remote SQL path: " + remote_sql_file_path)
        assert True
    else:
        assert False


def test_zip_remote_directory():
    file_manager = FileManager(config_data, connection)
    remote_archive_path = file_manager.archive()

    if remote_archive_path:
        print("Zipped up project to: " + remote_archive_path)
        assert True
    else:
        assert False


def test_remote_zip_archive_download():
    file_manager = FileManager(config_data, connection)
    remote_archive_path = file_manager.archive()

    if remote_archive_path:
        local_archive_path = tempfile.gettempdir() + '/cuppa-archive.zip'

        print("Zipped up project to remote path: " + remote_archive_path)
        print("Downloading to: " + local_archive_path)

        # Something up with zipping to tmp folder and then sshing in again to download.
        # Use a tmp folder in the home folder instead of the system tmp one.
        local_path = 'tmp/cuppa-archive.zip'
        remote_path = config_data['remote_temporary_folder'] + '/cuppa-archive.zip'

        transport.download(remote_path, local_path)

        assert True
    else:
        assert False


def test_file_upload():
    test_filename = 'wp-config.php'
    local_path = 'tmp/' + test_filename
    remote_path = config_data['remote_files_folder'] + '/' + test_filename

    transport.upload(local_path, remote_path)

    assert True


def test_extract_archive():
    file_manager = FileManager(config_data, connection)
    assert file_manager.extract('local')


def test_move_to_public_html():
    file_manager = FileManager(config_data, connection)
    assert file_manager.update_files_dir('local')


def test_move_to_sql():
    database = ProjectDatabase(config_data, connection)
    assert database.update_sql_dir('local')


def test_change_host_in_database():
    # database = ProjectDatabase(config_data, connection)
    # database.update_hostname('localhost')
    assert True


def test_check_remote_folder_structure_incorrect_config():
    print(config_data)

    dummy_incorrect_config_data = config_data

    dummy_incorrect_config_data['remote_files_folder'] = 'test123'
    dummy_incorrect_config_data['remote_sql_folder'] = 'test123'
    dummy_incorrect_config_data['remote_temporary_folder'] = 'test123'

    initialize = Init(dummy_incorrect_config_data, transport)

    if initialize.check_directories('remote') is False:
        assert True


def test_check_remote_folder_structure_correct_config():
    initialize = Init(config_data, transport)
    if initialize.check_directories('remote'):
        assert True


def test_check_local_folder_structure():
    initialize = Init(config_data, transport)

    if initialize.check_directories('local'):
        assert True


def test_cleanup_local_tmp_files():
    temporary_directory = 'tmp'
    shutil.rmtree(temporary_directory)
    os.mkdir(temporary_directory)

    assert True
