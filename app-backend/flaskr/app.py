from typing import Dict, List, Any
# Local imports
from .components import ModelFactory
# Third party imports
from transformers import pipeline


class App:

    def __init__(self) -> None:
        self.model_factory = ModelFactory()

    def register_model(self, model_name: str, tasks: List[str],
                       load_kwargs: Dict) -> None:
        return self.model_factory.register_model(model_name, tasks, load_kwargs)

    def get_task_model_names(self, task: str) -> List[str]:
        return self.model_factory.get_tasks_model_names().get(
            task, default=list())

    def execute_model(self, task: str, model_name: str, input_data: Any) -> Any:
        res = self.model_factory.get_task_model(task, model_name)
        if res == None:
            return
        # NOTE: Assuming that the model is from HuggingFace.
        try:
            task_pipeline = pipeline(
                task)
            return task_pipeline(input_data)
        except Exception as e:
            print(e)
