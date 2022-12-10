class InvalidLanguageValue(Exception):
    def __init__(self, language, task):

        self.msg = f"{language} is not supported by {task}"

        super().__init__(self.msg)
