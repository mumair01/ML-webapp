
from flaskr.components.model_factory import ModelFactory


def test_register_model() -> None:
    factory = ModelFactory()
    assert factory.register_model(
        "t5_small", ["test_task"], {"model_name": "t5-small"})


def test_get_tasks_model_names() -> None:
    factory = ModelFactory()
    factory.register_model(
        "t5_small", ["test_task"], {"model_name": "t5-small"})
    assert "test_task" in factory.get_tasks_model_names()
    assert "t5_small" in factory.get_tasks_model_names().get("test_task")
