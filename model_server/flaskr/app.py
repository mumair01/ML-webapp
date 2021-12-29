from typing import Dict, List, Any
# Local imports
from components import ModelFactory


class App:

    def __init__(self) -> None:
        self.model_factory = ModelFactory()

    ############################## MODIFIERS ##################################

    def register_model(self, model_name: str, tasks: List[str],
                       load_kwargs: Dict[str, Any]) -> None:
        self.model_factory.register_model(model_name, tasks, load_kwargs)

    def execute_model(self, model_name: str, task: str, execute_kwargs: Dict) \
            -> Any:
        return self.model_factory.execute_model(
            model_name, task, execute_kwargs)

    ################################# GETTERS #################################

    def is_registered(self, model_name: str) -> bool:
        return self.model_factory.is_registered(model_name)

    def is_registered_for_task(self, model_name: str, task: str) -> bool:
        return self.model_factory.is_registered_for_task(model_name, task)

    def get_model_tasks(self, model_name: str) -> List[str]:
        return self.model_factory.get_model_tasks(model_name)

    def get_models_for_task(self, task: str) -> List[str]:
        return self.model_factory.get_models_for_task(task)

    def get_models_by_task(self) -> Dict[str, str]:
        return self.model_factory.get_models_by_task()
