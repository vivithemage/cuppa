from . generic import CommandGeneric


class CommandPush(CommandGeneric):
    def run(self):
        if self.args[0] == 'db':
            print("pushing db")
            """ Export the database locally """

            """ Upload it to the temporary directory on the remote server """

            """ Create new remote database with timestamp """
            
            """ Import SQL script to newly created database """

            """ Change config to match newly imported database """

            """ Delete uploaded database file """

        if self.args[0] == 'files':
            print("pushing files")

            """ Zip up files locally alone - similar to archive but exclude the sql """

            """ Upload the zip file """

            """ Extract and copy (without config file)"""
