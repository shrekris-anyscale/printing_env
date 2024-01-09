import logging

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from ray import serve
from starlette.responses import JSONResponse

logger = logging.getLogger("ray.serve")

app = FastAPI()


@serve.deployment
@serve.ingress(app)
class ModelServer:

    def __init__(self):
        logger.info("Initialized")


    @app.post("/inference")
    async def inference(self, request: Request) -> JSONResponse:

        response = {
            "result": "OK"
        }

        return JSONResponse(content=jsonable_encoder(response))

esp_model_app = ModelServer.bind()
