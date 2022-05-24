class CommandGeneric:
    def __init__(self, config_data, connection, file_transport, args=[]):
        self.connection = connection
        self.config_data = config_data
        self.file_transport = file_transport
        self.args = args

    def run(self):
        print("Running generic command")
