from cuppa.ssh import SSHConnection


class Transport:
    def __init__(self, config):
        config_data = config.read_file()

        ssh_connector = SSHConnection(config_data)
        self.connection = ssh_connector.open_connection()
        self.sftp = self.connection.open_sftp()

    def upload(self, local_filepath, remote_filepath):
        return self.sftp.put(local_filepath, remote_filepath)

    def download(self, remote_filepath, local_filepath):
        return self.sftp.get(remote_filepath, local_filepath)


