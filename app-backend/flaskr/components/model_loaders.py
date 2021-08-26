from abc import ABC, abstractmethod
from transformers import AutoModel, AutoTokenizer


class ModelLoader(ABC):

    @abstractmethod
    def load(self, *args, **kwargs) -> None:
        pass


class HuggingFaceLoader(ModelLoader):

    def load(self, model_name: str) -> None:
        return {
            "model": AutoModel.from_pretrained(model_name),
            "tokenizer": AutoTokenizer.from_pretrained(model_name)}
