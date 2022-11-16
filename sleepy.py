from ray import serve
import logging

logger = logging.getLogger("ray.serve")

@serve.deployment(user_config={"time": 15})
class Sleeper:

    def __init__(self):
        logger.info("I am initializing!")
    
    def reconfigure(self, config):
        import time
        time.sleep(config.get("time", 15))
    
    def __call__(self, *args):
        logger.info("pre-import print statement!")
        import os
        logger.info(f"PID {os.getpid()} | I got called with args: {args}")
        return os.getpid()

app = Sleeper.bind()
