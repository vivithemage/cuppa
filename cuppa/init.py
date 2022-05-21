import os

class Init:
    def __init__(self):
        self.local_tmp_dir = 'tmp'

    def startup(self):
        if not os.path.exists(self.local_tmp_dir):
            os.makedirs(self.local_tmp_dir)