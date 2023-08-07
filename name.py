import ray
from ray import serve
from ray.util.state import get_actor

@serve.deployment
def f():
    actor_id = ray.get_runtime_context().get_actor_id()
    actor_state = get_actor(actor_id, timeout=5)
    return actor_state.name

app = f.bind()
