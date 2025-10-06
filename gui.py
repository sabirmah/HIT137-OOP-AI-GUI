import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image
from models import ObjectDetectionModel, TextToImageModel
from explanations import get_oop_explanation


class OOPExplanationWindow:
    """Dedicated window for displaying OOP concept explanations"""
    
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("OOP Concepts Explanation")
        self.window.geometry("900x700")
        self.window.configure(bg="#f0f4f8")
        
        # Make window modal
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.window, bg="#2c5aa0", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text=" Object-Oriented Programming Concepts",
            font=("Segoe UI", 18, "bold"),
            bg="#2c5aa0",
            fg="white"
        )
        title_label.pack(pady=25)
        
        # Content frame
        content_frame = tk.Frame(self.window, bg="#f0f4f8")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Scrolled text widget for explanations with bigger font
        self.text_widget = scrolledtext.ScrolledText(
            content_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),  # Increased from 10 to 11
            bg="white",
            fg="#2d3748",
            relief=tk.FLAT,
            borderwidth=0,
            padx=15,
            pady=15
        )
        self.text_widget.pack(fill="both", expand=True)
        
        # Insert explanation text
        explanation = get_oop_explanation()
        self.text_widget.insert("1.0", explanation)
        self.text_widget.config(state=tk.DISABLED)  # Make read-only
        
        # Configure text tags for formatting
        self.text_widget.tag_configure("header", font=("Segoe UI", 13, "bold"), foreground="#2c5aa0")  # Increased from 12 to 13
        
        # Button frame
        button_frame = tk.Frame(self.window, bg="#f0f4f8")
        button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        close_btn = tk.Button(
            button_frame,
            text="Close",
            command=self.window.destroy,
            font=("Segoe UI", 11),
            bg="#e53e3e",
            fg="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2",
            activebackground="#c53030",
            activeforeground="white"
        )
        close_btn.pack(side="right")


class AppGUI:
    """Enhanced AI GUI with modern design and improved UX"""
    
    # Color scheme
    COLORS = {
        'primary': '#2c5aa0',      # Professional blue
        'secondary': '#4299e1',    # Light blue
        'success': '#48bb78',      # Green
        'danger': '#e53e3e',       # Red
        'warning': '#ed8936',      # Orange
        'bg_main': '#f7fafc',      # Light gray background
        'bg_card': '#ffffff',      # White cards
        'text_primary': '#2d3748', # Dark gray text
        'text_secondary': '#718096', # Medium gray text
        'border': '#e2e8f0'        # Light border
    }
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Studio - Hugging Face Model Interface")
        self.root.geometry("1000x750")
        self.root.configure(bg=self.COLORS['bg_main'])
        
        # Configure styles
        self.setup_styles()

        # Initializing the models
        self.model1 = ObjectDetectionModel("facebook/detr-resnet-50")
        self.model2 = TextToImageModel("black-forest-labs/FLUX.1-dev")

        self.selected_model = None
        self.input_type = tk.StringVar(value="Text")
        self.input_text = tk.StringVar()
        self.input_image_path = tk.StringVar()
        
        # Initialize attribute placeholders
        self.model_cards = {}
        self.input_entry = None
        self.output_display = None
        self.model_info_label = None
        self.main_action_btn = None  # Main action button that changes based on model
        self.input_instruction_label = None  # Instructions for input
        self.canvas = None  # Canvas for scrolling
        self.scrollable_frame = None  # Frame inside canvas
        self.canvas_window = None  # Canvas window ID

        self.setup_menu()
        self.setup_layout()
    
    def setup_styles(self):
        """Configure ttk styles for modern look"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button styles
        style.configure(
            'Primary.TButton',
            font=('Segoe UI', 10),
            borderwidth=0,
            relief='flat',
            padding=10
        )
        
        style.configure(
            'Card.TFrame',
            background=self.COLORS['bg_card'],
            relief='flat'
        )


    def setup_menu(self):
        """Setup enhanced menu bar"""
        menu_bar = tk.Menu(self.root, bg=self.COLORS['bg_card'], fg=self.COLORS['text_primary'])
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0, bg=self.COLORS['bg_card'], fg=self.COLORS['text_primary'])
        file_menu.add_command(label=" Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0, bg=self.COLORS['bg_card'], fg=self.COLORS['text_primary'])
        help_menu.add_command(label=" OOP Concepts", command=self.show_oop_explanation)
        help_menu.add_separator()
        help_menu.add_command(label=" About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def show_about(self):
        messagebox.showinfo(
            "About AI Studio",
            "AI Studio - Hugging Face Model Interface\n\n"
            "Version 2.0\n"
            "A modern GUI for AI model interaction\n\n"
            "Features:\n"
            "• Object Detection (Identify objects in images)\n"
            "• Text to Image Generation\n"
            "• OOP Principles Demonstration\n\n"
            "© 2025 - Group Assignment 3"
        )
    
    def show_oop_explanation(self):
        """Open the OOP explanation window"""
        OOPExplanationWindow(self.root)

    def setup_layout(self):
        """Setup enhanced main layout"""
        # Header
        self.create_header()
        
        # Create a canvas with scrollbar for scrollable content
        canvas_frame = tk.Frame(self.root, bg=self.COLORS['bg_main'])
        canvas_frame.pack(fill="both", expand=True)
        
        # Create canvas
        self.canvas = tk.Canvas(canvas_frame, bg=self.COLORS['bg_main'], highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Create scrollbar
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        
        # Configure canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create frame inside canvas for all content
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.COLORS['bg_main'])
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Bind canvas to update scroll region
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        # Bind mousewheel for scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Make canvas window expand to canvas width
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        # Main container with padding (now inside scrollable frame)
        main_container = tk.Frame(self.scrollable_frame, bg=self.COLORS['bg_main'])
        main_container.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        # Model selection section
        self.create_model_selection_section(main_container)
        
        # Input section
        self.create_input_section(main_container)
        
        # Output section
        self.create_output_section(main_container)
        
        # Clear button (standalone)
        self.create_clear_button(main_container)
        
        # Info section (without OOP explanation)
        self.create_info_section(main_container)
    
    def _on_mousewheel(self, event):
        """Handle mousewheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_canvas_configure(self, event):
        """Adjust the canvas window to match canvas width"""
        self.canvas.itemconfig(self.canvas_window, width=event.width)
    
    def create_header(self):
        """Create modern header section"""
        header = tk.Frame(self.root, bg=self.COLORS['primary'], height=100)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text=" AI Studio",
            font=("Segoe UI", 24, "bold"),
            bg=self.COLORS['primary'],
            fg="white"
        )
        title.pack(side="left", padx=30, pady=30)
        
        subtitle = tk.Label(
            header,
            text="Hugging Face Model Interface",
            font=("Segoe UI", 12),
            bg=self.COLORS['primary'],
            fg="#e6f2ff"
        )
        subtitle.pack(side="left", padx=(0, 30), pady=30)
        
        # OOP Explanation button in header
        oop_btn = tk.Button(
            header,
            text=" View OOP Concepts",
            command=self.show_oop_explanation,
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg=self.COLORS['primary'],
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            activebackground="#e6f2ff",
            activeforeground=self.COLORS['primary']
        )
        oop_btn.pack(side="right", padx=30)
    
    def create_model_selection_section(self, parent):
        """Create enhanced model selection with cards"""
        section_frame = tk.Frame(parent, bg=self.COLORS['bg_main'])
        section_frame.pack(fill="x", pady=(0, 15))
        
        # Section title
        title_label = tk.Label(
            section_frame,
            text="Select AI Model",
            font=("Segoe UI", 14, "bold"),
            bg=self.COLORS['bg_main'],
            fg=self.COLORS['text_primary']
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Card container
        cards_container = tk.Frame(section_frame, bg=self.COLORS['bg_main'])
        cards_container.pack(fill="x")
        
        # Model 1 Card (Object Detection)
        model1_card = self.create_model_card(
            cards_container,
            " Object Detection",
            "Detect and identify objects in images",
            "facebook/detr-resnet-50",
            lambda: self.select_model_card(1)
        )
        model1_card.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Model 2 Card (Text to Image)
        model2_card = self.create_model_card(
            cards_container,
            " Text to Image",
            "Generate images from text descriptions",
            "black-forest-labs/FLUX.1-dev",
            lambda: self.select_model_card(2)
        )
        model2_card.pack(side="left", fill="both", expand=True)
        
        self.model_cards = {1: model1_card, 2: model2_card}
    
    def create_model_card(self, parent, title, description, model_name, command):
        """Create a stylish model selection card"""
        card = tk.Frame(
            parent,
            bg=self.COLORS['bg_card'],
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=2,
            highlightbackground=self.COLORS['border'],
            highlightcolor=self.COLORS['border']
        )
        
        # Card content
        content_frame = tk.Frame(card, bg=self.COLORS['bg_card'])
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            content_frame,
            text=title,
            font=("Segoe UI", 13, "bold"),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary']
        )
        title_label.pack(anchor="w")
        
        # Description
        desc_label = tk.Label(
            content_frame,
            text=description,
            font=("Segoe UI", 9),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_secondary'],
            wraplength=250,
            justify="left"
        )
        desc_label.pack(anchor="w", pady=(5, 10))
        
        # Model name
        model_label = tk.Label(
            content_frame,
            text=f"Model: {model_name}",
            font=("Consolas", 8),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_secondary']
        )
        model_label.pack(anchor="w", pady=(0, 10))
        
        # Select button
        select_btn = tk.Button(
            content_frame,
            text="Select Model",
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg=self.COLORS['primary'],
            fg="white",
            relief=tk.FLAT,
            padx=15,
            pady=8,
            cursor="hand2",
            activebackground=self.COLORS['secondary'],
            activeforeground="white"
        )
        select_btn.pack(anchor="w")
        
        return card
    
    def select_model_card(self, model_num):
        """Handle model selection with visual feedback"""
        if model_num == 1:
            self.selected_model = self.model1
            # Highlight selected card
            self.model_cards[1].configure(
                highlightbackground=self.COLORS['success'],
                highlightcolor=self.COLORS['success'],
                highlightthickness=3
            )
            self.model_cards[2].configure(
                highlightbackground=self.COLORS['border'],
                highlightcolor=self.COLORS['border'],
                highlightthickness=2
            )
            # Update main action button for Object Detection
            if self.main_action_btn:
                self.main_action_btn.config(
                    text=" ACTION\n(Detect Objects)",
                    bg=self.COLORS['success'],
                    state=tk.NORMAL
                )
        else:
            self.selected_model = self.model2
            # Highlight selected card
            self.model_cards[2].configure(
                highlightbackground=self.COLORS['success'],
                highlightcolor=self.COLORS['success'],
                highlightthickness=3
            )
            self.model_cards[1].configure(
                highlightbackground=self.COLORS['border'],
                highlightcolor=self.COLORS['border'],
                highlightthickness=2
            )
            # Update main action button for Text-to-Image
            if self.main_action_btn:
                self.main_action_btn.config(
                    text=" ACTION\n(Generate Image)",
                    bg=self.COLORS['warning'],
                    state=tk.NORMAL
                )
        
        self.display_model_info()
        messagebox.showinfo(
            "Model Selected", 
            f"Model {model_num} has been loaded successfully!\n\n"
            " Action button is now ready!\n\n"
            "Next steps:\n"
            f"{'1. Click Browse Image to select a file' if model_num == 1 else '1. Type your text description in the input box'}\n"
            "2. Click the ACTION button to run the model"
        )
    
    def run_selected_model(self):
        """Run the currently selected model"""
        if not self.selected_model:
            messagebox.showwarning(
                "No Model Selected",
                "Please select a model first by clicking on one of the model cards above."
            )
            return
        
        if self.selected_model == self.model1:
            self.run_model1()
        else:
            self.run_model2()
    
    def create_input_section(self, parent):
        """Create enhanced input section"""
        section_frame = tk.Frame(parent, bg=self.COLORS['bg_card'], relief=tk.FLAT)
        section_frame.pack(fill="x", pady=(0, 15))
        
        # Inner padding
        inner_frame = tk.Frame(section_frame, bg=self.COLORS['bg_card'])
        inner_frame.pack(fill="both", padx=20, pady=20)
        
        # Section title with instructions
        title_label = tk.Label(
            inner_frame,
            text="Input Your Data",
            font=("Segoe UI", 14, "bold"),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary']
        )
        title_label.pack(anchor="w", pady=(0, 5))
        
        # Radio buttons for showcase (no functional effect)
        radio_frame = tk.Frame(inner_frame, bg=self.COLORS['bg_card'])
        radio_frame.pack(anchor="w", pady=(5, 10))
        
        radio_label = tk.Label(
            radio_frame,
            text="Your input is:",
            font=("Segoe UI", 10),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary']
        )
        radio_label.pack(side="left", padx=(0, 10))
        
        # Radio button variable (for showcase only)
        self.input_type_var = tk.StringVar(value="image")
        
        radio_image = tk.Radiobutton(
            radio_frame,
            text="Image",
            variable=self.input_type_var,
            value="image",
            font=("Segoe UI", 10),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary'],
            selectcolor="white",
            activebackground=self.COLORS['bg_card']
        )
        radio_image.pack(side="left", padx=(0, 15))
        
        radio_text = tk.Radiobutton(
            radio_frame,
            text="Text",
            variable=self.input_type_var,
            value="text",
            font=("Segoe UI", 10),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary'],
            selectcolor="white",
            activebackground=self.COLORS['bg_card']
        )
        radio_text.pack(side="left")
        
        # Instructions label
        self.input_instruction_label = tk.Label(
            inner_frame,
            text=" For Text-to-Image: Enter your text description below\n For Object Detection: Click 'Browse Image' to select an image file",
            font=("Segoe UI", 9),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_secondary'],
            justify="left"
        )
        self.input_instruction_label.pack(anchor="w", pady=(0, 15))
        
        # Input entry and buttons
        input_container = tk.Frame(inner_frame, bg=self.COLORS['bg_card'])
        input_container.pack(fill="x")
        
        # Text entry field (larger for better visibility)
        self.input_entry = tk.Text(
            input_container,
            height=3,
            font=("Segoe UI", 11),
            bg="white",
            fg=self.COLORS['text_primary'],
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=2,
            highlightbackground=self.COLORS['border'],
            highlightcolor=self.COLORS['secondary'],
            padx=10,
            pady=10,
            wrap=tk.WORD
        )
        self.input_entry.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Buttons container (vertical stack)
        buttons_container = tk.Frame(input_container, bg=self.COLORS['bg_card'])
        buttons_container.pack(side="left", fill="y")
        
        # Browse button (for image selection)
        browse_btn = tk.Button(
            buttons_container,
            text=" Browse Image",
            command=self.browse_image,
            font=("Segoe UI", 10, "bold"),
            bg=self.COLORS['secondary'],
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            width=15,
            activebackground=self.COLORS['primary'],
            activeforeground="white"
        )
        browse_btn.pack(pady=(0, 8))
        
        # ACTION button (main action button integrated here!)
        self.main_action_btn = tk.Button(
            buttons_container,
            text=" ACTION\n(Select Model First)",
            command=self.run_selected_model,
            font=("Segoe UI", 11, "bold"),
            bg=self.COLORS['text_secondary'],
            fg="white",
            relief=tk.FLAT,
            padx=15,
            pady=10,
            cursor="hand2",
            width=15,
            state=tk.DISABLED,
            activebackground=self.COLORS['success'],
            activeforeground="white"
        )
        self.main_action_btn.pack()
    
    def create_output_section(self, parent):
        """Create enhanced output section"""
        section_frame = tk.Frame(parent, bg=self.COLORS['bg_card'], relief=tk.FLAT)
        section_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        # Inner padding
        inner_frame = tk.Frame(section_frame, bg=self.COLORS['bg_card'])
        inner_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Section title
        title_label = tk.Label(
            inner_frame,
            text="Model Output",
            font=("Segoe UI", 14, "bold"),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary']
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Output text widget with scrollbar
        output_container = tk.Frame(inner_frame, bg=self.COLORS['bg_card'])
        output_container.pack(fill="both", expand=True)
        
        self.output_display = tk.Text(
            output_container,
            height=8,
            font=("Consolas", 10),
            bg="white",
            fg=self.COLORS['text_primary'],
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=1,
            highlightbackground=self.COLORS['border'],
            highlightcolor=self.COLORS['secondary'],
            padx=10,
            pady=10,
            wrap=tk.WORD
        )
        self.output_display.pack(fill="both", expand=True)
    
    def create_clear_button(self, parent):
        """Create clear output button"""
        button_frame = tk.Frame(parent, bg=self.COLORS['bg_main'])
        button_frame.pack(fill="x", pady=(0, 15))
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text=" Clear Output",
            command=self.clear_output,
            font=("Segoe UI", 11),
            bg=self.COLORS['danger'],
            fg="white",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            cursor="hand2",
            activebackground="#c53030",
            activeforeground="white"
        )
        clear_btn.pack(side="left")
    
    def create_info_section(self, parent):
        """Create info section (without OOP explanation)"""
        section_frame = tk.Frame(parent, bg=self.COLORS['bg_card'], relief=tk.FLAT)
        section_frame.pack(fill="x")
        
        # Inner padding
        inner_frame = tk.Frame(section_frame, bg=self.COLORS['bg_card'])
        inner_frame.pack(fill="both", padx=20, pady=15)
        
        # Section title
        title_label = tk.Label(
            inner_frame,
            text="Model Information",
            font=("Segoe UI", 12, "bold"),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_primary']
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Model info display
        self.model_info_label = tk.Label(
            inner_frame,
            text="Select a model to view its information",
            font=("Segoe UI", 9),
            bg=self.COLORS['bg_card'],
            fg=self.COLORS['text_secondary'],
            anchor="w",
            justify="left",
            wraplength=900
        )
        self.model_info_label.pack(fill="x")


    def browse_image(self):
        """Handle image file selection"""
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.input_image_path.set(file_path)
            # Clear and update text input
            self.input_entry.delete("1.0", tk.END)
            self.input_entry.insert("1.0", f"Selected image: {file_path}")
            messagebox.showinfo("Image Selected", f"Image loaded successfully!\n\nPath: {file_path}\n\nClick the action button to extract text.")

    def display_model_info(self):
        """Display information about the selected model"""
        if self.selected_model:
            info = self.selected_model.get_info()
            self.model_info_label.config(text=info)

    def run_model1(self):
        """Run the Object Detection model"""
        if not self.selected_model or self.selected_model != self.model1:
            messagebox.showwarning(
                "Wrong Model",
                "Please select the Object Detection model first!"
            )
            return
        
        try:
            input_data = self.get_input()
            if not input_data or len(input_data.strip()) == 0:
                messagebox.showwarning(
                    "No Input Provided", 
                    "Please browse and select an image file first!\n\nClick the ' Browse Image' button to choose an image."
                )
                return
            
            # Validate it's a file path
            import os
            if not os.path.exists(input_data):
                messagebox.showerror(
                    "Invalid Image",
                    f"The file does not exist:\n{input_data}\n\nPlease select a valid image file."
                )
                return
            
            # Show processing message
            self.output_display.delete("1.0", tk.END)
            self.output_display.insert(tk.END, "⏳ Analyzing image... Please wait...\n\nDetecting objects in the image...")
            self.root.update()
            
            result = self.model1.run(input_data)
            self.output_display.delete("1.0", tk.END)
            
            if result and len(str(result).strip()) > 0:
                self.output_display.insert(
                    tk.END,
                    f" OBJECT DETECTION COMPLETED!\n\n"
                    f"{'='*60}\n"
                    f"{str(result)}\n"
                    f"{'='*60}\n\n"
                    f"Source: {input_data}"
                )
                messagebox.showinfo("Success!", "Objects detected successfully in the image!")
            else:
                self.output_display.insert(
                    tk.END,
                    " No objects were detected in the image.\n\n"
                    "This could mean:\n"
                    "• The image has no recognizable objects\n"
                    "• The objects are too small or unclear\n"
                    "• The image quality is too low\n\n"
                    "Try using a clearer image with visible objects."
                )
        except FileNotFoundError:
            self.output_display.delete("1.0", tk.END)
            self.output_display.insert(tk.END, " Error: Image file not found!\n\nPlease select a valid image file.")
            messagebox.showerror("File Not Found", "The selected image file could not be found.")
        except ValueError as ve:
            self.output_display.delete("1.0", tk.END)
            self.output_display.insert(tk.END, f" Validation Error:\n\n{str(ve)}\n\nPlease check your input and try again.")
            messagebox.showerror("Validation Error", str(ve))
        except Exception as e:
            self.output_display.delete("1.0", tk.END)
            error_msg = str(e)
            self.output_display.insert(
                tk.END,
                f" Error occurred:\n\n{error_msg}\n\n"
                "Possible causes:\n"
                "• Invalid image file or format\n"
                "• Network connectivity issues\n"
                "• API service temporarily unavailable\n"
                "• Model processing error\n\n"
                "Troubleshooting:\n"
                "1. Try a different image (PNG, JPG recommended)\n"
                "2. Check your internet connection\n"
                "3. Wait a moment and try again\n"
                "4. Ensure image contains clear objects\n"
            )
            messagebox.showerror("Error", f"Failed to process image:\n\n{error_msg}")

    def run_model2(self):
        """Run the Text-to-Image model"""
        if not self.selected_model or self.selected_model != self.model2:
            messagebox.showwarning(
                "Wrong Model",
                "Please select the Text-to-Image model first!"
            )
            return
        
        try:
            input_data = self.get_input()
            if not input_data or len(input_data.strip()) == 0:
                messagebox.showwarning(
                    "No Input Provided",
                    "Please enter a text description first!\n\nType what you want to generate in the text box.\n\nExample: 'A cute robot reading a book in a cozy library'"
                )
                return
            
            # Make sure it's not an image path
            if input_data.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                messagebox.showwarning(
                    "Wrong Input Type",
                    "For Text-to-Image, please enter a TEXT DESCRIPTION, not an image file!\n\nClear the input and type your description."
                )
                return
            
            # Show processing message
            self.output_display.delete("1.0", tk.END)
            self.output_display.insert(
                tk.END,
                " Generating image... This may take 10-30 seconds...\n\n"
                f"Your prompt: '{input_data}'\n\n"
                "Please wait while the AI creates your image..."
            )
            self.root.update()
            
            result = self.model2.run(input_data)
            self.output_display.delete("1.0", tk.END)
            
            # Check if result is a PIL Image object
            if hasattr(result, 'save') and hasattr(result, 'size'):
                # Save and display image
                output_path = "output_image.png"
                result.save(output_path)
                self.output_display.insert(
                    tk.END,
                    f" IMAGE GENERATED SUCCESSFULLY!\n\n"
                    f"{'='*60}\n"
                    f" Saved as: {output_path}\n"
                    f" Size: {result.size[0]} x {result.size[1]} pixels\n"
                    f" Prompt: {input_data}\n"
                    f"{'='*60}\n\n"
                    f" Your image has been saved in the current directory!\n"
                    f"You can find it at: {output_path}"
                )
                messagebox.showinfo(
                    "Success!",
                    f"Image generated and saved successfully!\n\n"
                    f" File: {output_path}\n"
                    f" Size: {result.size[0]} x {result.size[1]} pixels\n\n"
                    f"Check the application folder to view your image!"
                )
            else:
                self.output_display.insert(tk.END, f"Generated result:\n\n{str(result)}")
        except Exception as e:
            self.output_display.delete("1.0", tk.END)
            self.output_display.insert(
                tk.END,
                f" Error occurred:\n\n{str(e)}\n\n"
                "Common issues:\n"
                "• Network connectivity problems\n"
                "• API rate limits\n"
                "• Invalid API token\n\n"
                "Please try again in a few moments."
            )
            messagebox.showerror("Error", f"Failed to generate image:\n\n{str(e)}")

    def get_input(self):
        """Get input from the text widget or image path"""
        # Check if we have an image path set
        image_path = self.input_image_path.get()
        if image_path:
            return image_path
        
        # Otherwise get text from the text widget
        text_content = self.input_entry.get("1.0", tk.END).strip()
        # Remove the "Selected image:" prefix if present
        if text_content.startswith("Selected image:"):
            return self.input_image_path.get()
        return text_content

    def clear_output(self):
        """Clear the output display"""
        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, "Output cleared. Ready for next operation.")

    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()
