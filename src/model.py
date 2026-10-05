from src.log import logger

from transformers import pipeline
import sys 
from typing import Literal

MODELS = {
        "LOWER": "Qwen/Qwen3.5-0.8B-Instruct",
        "MEDIUM": "Qwen/Qwen3.5-4B-Instruct",
        "HIGH": "Qwen/Qwen3.5-9B-Instruct"
    }

class ModelControl:

    

    def __init__(self, type:Literal["LOWER", "MEDIUM", "HIGH"])-> None:

        self.type = type 
        

    def load(self) -> None:

        try:
            model = MODELS[self.type]
            logger.info(f"Carregando modelo {model}...")

            self.model = pipeline(model=model)

            logger.info(f"{model} carregado!")

        except Exception as error:

            logger.error(f"Houve um erro ao carregar: {error}")
            raise 

    

            