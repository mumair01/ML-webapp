# Local imports
from flaskr.components.model_factory import ModelFactory


def test_register_model() -> None:
    '''
    Tests:
        1. Register valid model for valid task.
        2. Register valid model for invalid task.
        3. Register model with invalid kwargs.
    '''
    factory = ModelFactory()
    factory.register_model()


def test_execute_model() -> None:
    pass


def test_is_registered() -> None:
    pass


def test_is_registered_for_task() -> None:
    pass


def test_get_model_tasks() -> None:
    pass


def test_get_models_for_task() -> None:
    pass


def test_get_models_by_task() -> None:
    pass


# def test_register_model() -> None:
#     factory = ModelFactory()
#     assert factory.register_model(
#         "t5_small", ["test_task"], {"model_name": "t5-small"})


# def test_get_tasks_model_names() -> None:
#     factory = ModelFactory()
#     factory.register_model(
#         "t5_small", ["test_task"], {"model_name": "t5-small"})
#     assert "test_task" in factory.get_tasks_model_names()
#     assert "t5_small" in factory.get_tasks_model_names().get("test_task")
