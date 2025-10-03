
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from huggingface_hub import InferenceClient


# Decorators for logging

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    return wrapper

# Base AI Model class

class AIModel:
    def __init__(self, model_name):
        self._model_name = model_name   # encapsulation (_model_name is private)
        self.client = InferenceClient(model_name)

    def run_model(self, input_data):
        raise NotImplementedError("Subclass must override run_model()")

    def get_info(self):
        return f"Model: {self._model_name}"

# Inheritance + Polymorphism

class TextToImageModel(AIModel):
    @log_action
    def run_model(self, input_data):
        return self.client.text_to_image(input_data)

class AudioToTextModel(AIModel):
    @log_action
    def run_model(self, input_data):
        with open(input_data, "rb") as f:
            return self.client.audio_to_text(f)


# GUI App

class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HIT137 AI GUI Assignment")
        self.geometry("600x400")

        # Dropdown to choose input type
        self.input_type = tk.StringVar()
        self.model_choice = tk.StringVar()

        tk.Label(self, text="Select Input Type:").pack(pady=5)
        input_menu = ttk.Combobox(self, textvariable=self.input_type, values=["Text", "Audio"])
        input_menu.pack()

        tk.Label(self, text="Select Model:").pack(pady=5)
        model_menu = ttk.Combobox(self, textvariable=self.model_choice,
                                  values=["Text-to-Image", "Audio-to-Text"])
        model_menu.pack()

        tk.Button(self, text="Browse File", command=self.browse_file).pack(pady=5)
        tk.Button(self, text="Run Model", command=self.run_selected_model).pack(pady=10)

        self.result_box = tk.Text(self, height=10, width=70)
        self.result_box.pack(pady=10)

        self.file_path = None

    @error_handler
    def browse_file(self):
        filetypes = [("All files", "*.*")]
        self.file_path = filedialog.askopenfilename(filetypes=filetypes)
        if self.file_path:
            self.result_box.insert(tk.END, f"Selected file: {self.file_path}\n")

    @error_handler
    def run_selected_model(self):
        choice = self.model_choice.get()
        input_type = self.input_type.get()

        if choice == "Text-to-Image" and input_type == "Text":
            model = TextToImageModel("stabilityai/stable-diffusion-2-1")
            result = model.run_model("A cute cat playing guitar")
            self.result_box.insert(tk.END, f"Generated Image: {result}\n")

        elif choice == "Audio-to-Text" and input_type == "Audio":
            if not self.file_path:
                raise ValueError("No audio file selected!")
            model = AudioToTextModel("openai/whisper-tiny")
            result = model.run_model(self.file_path)
            self.result_box.insert(tk.END, f"Transcription: {result}\n")

        else:
            raise ValueError("Invalid input/model combination!")

# Run GUI

if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()
