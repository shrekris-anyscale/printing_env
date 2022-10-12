from ray import serve
import logging

logger = logging.getLogger("ray.serve")

@serve.deployment
class Loud:

    def __init__(self):
        logger.info("I am initializing!")
    
    def __call__(self, *args):
        logger.info("pre-import print statement!")
        import os
        logger.info(f"PID {os.getpid()} | I got called with args: {args}")
        return os.getpid()

app = Loud.bind()