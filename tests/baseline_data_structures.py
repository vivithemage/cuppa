result = {
    'primary_action': 'pull',
    'secondary_action': 'db',
}

config_file_result = {
    'hostname': 'example.com',
    'username': 'user',
    'password': 'password',
    'remote_files_folder': '/home/user/example_project/public_html',
    'remote_sql_folder': '/home/user/example_project/SQL',
    'remote_temporary_folder': '/home/remote_user/example_project/cuppa_tmp'
}

test_argv = [
    '/home/vivi/workspace/cuppa/cuppa/main.py',
    'pull',
    'db']
