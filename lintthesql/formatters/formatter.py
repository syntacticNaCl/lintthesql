import sys

class Formatter(object):

    def set_config(self, config):
        try:
            self.rules = config.get_rules()
        except:
            print('Please provide a valid Config object to the parser')
            sys.exit()

    def get_rule(self):
        pass

    def format(self):
        pass
