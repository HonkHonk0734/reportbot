class reportedUsers:
    """A sample Employee class"""

    def __init__(self, reported, reason, date, report):
        self.reported = reported,
        self.reason = reason,
        self.date = date,
        self.report = report

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)