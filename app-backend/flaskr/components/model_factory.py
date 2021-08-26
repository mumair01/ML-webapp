from typing import List, Dict, Any
from .model_loaders import ModelLoader, HuggingFaceLoader


class ModelFactory:

    LOADERS: List[ModelLoader] = [
        HuggingFaceLoader()
    ]

    def __init__(self) -> None:
        self.models: Dict[str, Dict] = dict()

    def register_model(self, model_name: str, tasks: List[str],
                       load_kwargs: Dict) -> bool:
        if model_name in self.models:
            return False
        for loader in self.LOADERS:
            try:
                res = loader.load(**load_kwargs)
                model = res["model"]
                tokenizer = res["tokenizer"]
                # Model has been loaded in this case.
                if model != None:
                    self.models[model_name] = {
                        "tasks": tasks,
                        "model": model,
                        "tokenizer": tokenizer}
                    return True
            except Exception as e:
                print("Exception raised when registering: {}".format(e))
        return False

    def get_tasks_model_names(self) -> Dict[str, List[str]]:
        task_model_names = dict()
        for model_name, details in self.models.items():
            details: Dict
            tasks = details.get("tasks")
            for task in tasks:
                if task in task_model_names:
                    task_model_names[task].append(model_name)
                else:
                    task_model_names[task] = [model_name]
        return task_model_names

    def get_task_model(self, task: str, model_name: str) -> Dict:
        if not model_name in self.models:
            return
        details = self.models.get(model_name)
        if task in details.get("tasks"):
            return {
                "model": details.get("model"),
                "tokenizer": details.get("tokenizer")
            }
