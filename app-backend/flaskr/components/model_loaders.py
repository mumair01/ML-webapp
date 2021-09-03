from typing import Any, Dict
from abc import ABC, abstractmethod
from transformers import AutoModel, AutoTokenizer


class ModelLoader(ABC):

    @abstractmethod
    def load(self, *args, **kwargs) -> Dict:
        pass


class HuggingFaceLoader(ModelLoader):

    def load(self, model_name: str) -> Dict:
        return {
            "model": AutoModel.from_pretrained(model_name),
            "tokenizer": AutoTokenizer.from_pretrained(model_name)}
