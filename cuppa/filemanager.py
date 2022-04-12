import zipfile


class FileManager:
    def __init__(self, config_data, connection):
        self.config_data = config_data
        self.tmp_dir = config_data['remote_temporary_folder']
        self.connection = connection
        self.config_filename = 'wp-config.php'

    def archive(self, location='remote'):
        if location == 'remote':
            archive_path = self.tmp_dir + '/cuppa-archive.zip '
            command = 'zip -r ' + archive_path + self.config_data['remote_files_folder'] \
                      + ' ' + self.config_data['remote_sql_folder']

            stdin, stdout, stderr = self.connection.exec_command(command)
            errors = stderr.readlines()

            if errors:
                return False
            else:
                return archive_path

        else:
            command = ''


    def extract(self, location='remote'):
        print(location)

        if location == 'remote':
            print("todo")
        else:
            zip_file = "tmp/cuppa-archive.zip"

            try:
                with zipfile.ZipFile(zip_file) as z:
                    z.extractall('tmp')
                    print("Extracted all")
                    return True
            except:
                print("Invalid file")
                return False
