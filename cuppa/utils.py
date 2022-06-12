import os
import shutil


def tmp_directory_cleanup():
    tmp_directory = 'tmp'

    try:
        shutil.rmtree(tmp_directory)
        os.mkdir(tmp_directory)
    except OSError as e:
        print("Error: %s : %s" % (tmp_directory, e.strerror))

