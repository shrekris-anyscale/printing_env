from ray import serve

@serve.deployment
class Turtle:

    def __call__(self, *args):
        return "Sup!"

graph = Turtle.bind()

