class BrokenPrinter:

    def __init__(self):
        self.bug = 1/0

    def __call__(self):
        return "I'm a broken printer"
