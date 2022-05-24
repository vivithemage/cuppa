from . cuppa_ssh import CuppaSSH


class FileTransport:
    def __init__(self, config_data):

        ssh_connector = CuppaSSH(config_data)
        self.connection = ssh_connector.open_connection()
        self.sftp = self.connection.open_sftp()

    def upload(self, local_filepath, remote_filepath):
        return self.sftp.put(local_filepath, remote_filepath)

    def download(self, remote_filepath, local_filepath):
        return self.sftp.get(remote_filepath, local_filepath)

    def folder_exists(self, remote_filepath):
        try:
            self.sftp.stat(remote_filepath)
            return True
        except FileNotFoundError:
            return False


