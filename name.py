import ray
from ray import serve
from ray.util.state import get_actor

@serve.deployment
def f():
    actor_id = ray.get_runtime_context().get_actor_id()
    actor_state = get_actor(actor_id, timeout=5)
    return actor_state.name

@serve.deployment
async def g(request):
    # requests.get("http://localhost:8000", json={"code": 'import ray;print(ray.get_runtime_context().get_actor_id())'})

    code = (await request.json())["code"]
    exec(code)

app1 = f.bind()
app2 = g.bind()
