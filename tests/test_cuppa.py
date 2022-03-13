import pytest
from cuppa.config import Config

result = {
    'primary_action': 'pull',
    'secondary_action': 'db',
}

test_argv = [
    '/home/vivi/workspace/cuppa/cuppa/cuppa.py',
    'pull',
    'db']


def test_get_cli_arguments():
    """"  Testing command line arguments are in correct format

    """

    config = Config(test_argv)
    assert(result == config.get_cli_args())


# def test_read_config_file():
#     config = Config(test_argv)
#     assert (result == config.read_file())
#
#
# def test_save_config_file():
#     config = Config(test_argv)
#     assert (config.save_file())


