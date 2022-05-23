

class Validation:
    def __init__(self, check_type):
        self.check_type = check_type

    def can_zip(self):
        print('can zip')

    def validate(self):
        if self.check_type == 'initial':
            print("initial checks")


