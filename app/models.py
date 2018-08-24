class Question(object):
    """This class represents the Questions in the app"""

    def __init__(self, ask, language,date_posted):
        self.ask = ask
        self.language = language
        self.date_posted = date_posted


class Answer(object):
    """This class represents the Answers the app."""

    def __init__(self, answer, date_posted):
        self.answer = answer
        self.date_posted = date_posted


class User(object):
    """This class represents the Users in the app."""

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password