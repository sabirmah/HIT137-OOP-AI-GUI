# models.py
from huggingface_hub import InferenceClient
from decorators import log_action

# Base Class
class AIModel:
    def __init__(self, model_name):
        self._model_name = model_name    # Encapsulation
        self.client = InferenceClient(model_name)

    def run_model(self, input_data):
        raise NotImplementedError("Subclass must override run_model()")

    def get_info(self):
        return f"Model: {self._model_name}"

# Subclass 1 (Polymorphism + Method Overriding)
class TextToImageModel(AIModel):
    @log_action
    def run_model(self, input_data):
        return self.client.text_to_image(input_data)

# Subclass 2
class AudioToTextModel(AIModel):
    @log_action
    def run_model(self, input_data):
        with open(input_data, "rb") as f:
            return self.client.audio_to_text(f) 
