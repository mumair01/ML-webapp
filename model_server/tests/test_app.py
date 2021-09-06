# Local imports
from flaskr.app import App


def test_register_model() -> None:
    pass


def test_get_task_model_names() -> None:
    pass


def test_execute_model() -> None:
    app = App()
    app.register_model(
        "distilbert-base-cased-distilled-squad",
        ["question-answering"],
        {"model_name": "distilbert-base-cased-distilled-squad"})
    data = {
        "question": 'What is the name of the repository ?',
        "context": "Pipeline has been included in the huggingface/transformers repository"
    }
    res = app.execute_model(
        'question-answering', "distilbert-base-cased-distilled-squad",
        data)
    print(res)
