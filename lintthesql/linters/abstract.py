class AbstractLinter:
    def __init__(self, rules):
        self.configure_rule(rules)

    def configure_rule(self, rules):
        pass

    def is_invalid(self, token):
        pass

    def get_invalid_message(self, line_number):
        pass
