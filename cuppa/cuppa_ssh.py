import paramiko


class CuppaSSH:

    def __init__(self, config):
        self.hostname = config['hostname']
        self.username = config['username']
        self.password = config['password']

    def open_connection(self):
        """  Opens up ssh client and returns client to execute commands

        :returns SSHClient
        """

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("connecting to " + str(self.hostname))

        try:
            client.connect(self.hostname, port=22, username=self.username, password=self.password,
                           allow_agent=True)

            return client
        except paramiko.AuthenticationException:
            raise Exception("Issue connecting to server over ssh, trying again")


