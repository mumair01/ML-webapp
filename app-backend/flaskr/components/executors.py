# Standard imports
from typing import Dict, Any
from abc import ABC, abstractmethod
# Third party imports
from transformers import pipeline


class Executor(ABC):

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        pass


class TransformerExecutor:

    TASKS = [
        "feature-extraction",
        "text-classification",
        "sentiment-analysis",
        "token-classification",
        "ner",
        "question-answering",
        "fill-mask",
        "summarization",
        "translation_xx_to_yy",
        "text2text-generation",
        "text-generation",
        "zero-shot-classification",
        "conversational"
    ]

    def execute(self, model: Any, tokenizer: Any, task: str,
                input_data: Dict) -> Any:
        if not task in self.TASKS:
            raise Exception("Task not supported: {}".format(task))
        # TODO: Use the specific model for the specific task
        task_pipeline = pipeline(task)
        return task_pipeline(input_data)
