# Standard imports
from typing import List, Dict, Any
from copy import deepcopy
# Local imports
from .loaded_model import LoadedModel
from .model_loaders import ModelLoader, HuggingFaceLoader
from .executors import Executor, TransformerExecutor


class ModelFactory:

    LOADERS: List[ModelLoader] = [
        HuggingFaceLoader()
    ]
    EXECUTORS: List[Executor] = [
        TransformerExecutor()
    ]

    def __init__(self) -> None:
        self.loaded_models: Dict[str, LoadedModel] = dict()

    ############################## MODIFIERS ################################

    def register_model(self, model_name: str, tasks: List[str],
                       load_kwargs: Dict[str, Any]) -> None:
        if model_name in self.loaded_models:
            raise Exception("Model already exists: {}".format(model_name))
        for loader in self.LOADERS:
            try:
                loader_result = loader.load(**load_kwargs)
                # Considered loaded
                if loader_result != None:
                    self.loaded_models[model_name] = LoadedModel(
                        model_name, tasks, loader_result)
                    return
            except Exception as e:
                print(e)
        raise Exception("No loader found for model: {}".format(model_name))

    def execute_model(self, model_name: str, task: str, execute_kwargs: Dict) \
            -> Any:
        if not self.is_registered_for_task(model_name, task):
            raise Exception("Model not registered for task: {} --> {}".format(
                model_name, task))
        for executor in self.EXECUTORS:
            try:
                kwargs = deepcopy(self.loaded_models.get(
                    model_name).execute_kwargs)
                kwargs.update(execute_kwargs)
                print(kwargs)
                return executor.execute(**kwargs)
            except Exception as e:
                print(e)
        raise Exception("No executor found for model with task: {} --> {}".
                        format(model_name, task))

    ################################# GETTERS #################################

    def is_registered(self, model_name: str) -> bool:
        return model_name in self.loaded_models

    def is_registered_for_task(self, model_name: str, task: str) -> bool:
        return self.is_registered(model_name) and \
            task in self.loaded_models.get(model_name).tasks

    def get_model_tasks(self, model_name: str) -> List[str]:
        if not self.is_registered(model_name):
            raise Exception("Model not registered: {}".format(model_name))
        return self.loaded_models.get(model_name).tasks

    def get_models_for_task(self, task: str) -> List[str]:
        return [model_name for model_name, loaded_model
                in self.loaded_models.items() if task in loaded_model.tasks]

    def get_models_by_task(self) -> Dict[str, str]:
        task_models = dict()
        for model_name, loaded_model in self.loaded_models.items():
            for task in loaded_model.tasks:
                if task in task_models:
                    task_models[task].append(model_name)
                else:
                    task_models[task] = [model_name]
        return task_models

    ################################# SETTERS #################################
