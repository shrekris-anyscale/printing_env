class Printer:

    def __init__(self):
        print("Creating a printer")

    def __call__(self, request):
        print(f"Printer received a request: {request}")
        return "PC LOAD LETTER"
