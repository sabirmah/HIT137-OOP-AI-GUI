# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from models import TextToImageModel, AudioToTextModel
from decorators import error_handler

class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HIT137 AI GUI Assignment")
        self.geometry("600x400")

        self.input_type = tk.StringVar()
        self.model_choice = tk.StringVar()
        self.file_path = None

        # Dropdowns
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

    @error_handler
    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
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
