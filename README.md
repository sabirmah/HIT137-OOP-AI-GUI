# 🎨 AI Studio - Hugging Face Model Interface

> A modern, object-oriented GUI application for AI-powered Object Detection and Image Generation

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![Hugging Face](https://img.shields.io/badge/AI-Hugging%20Face-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 Project Overview

**AI Studio** is a sophisticated desktop application that brings the power of Hugging Face's AI models to your fingertips through an elegant, user-friendly interface. This project demonstrates professional software development practices by implementing core Object-Oriented Programming (OOP) principles in Python, combined with a beautifully styled Tkinter GUI.

### 🎯 Key Capabilities

1. **🔍 Object Detection**: Analyze images and detect objects with bounding boxes, confidence scores, and precise location data
2. **🎨 Image Generation**: Create stunning images from text descriptions using state-of-the-art AI models

### 👥 Development Team

This project was developed by:
- **Anish Regmi**
- **Sabir Pudasaini**
- And two other talented contributors

### 🏆 What Makes This Special

- **Professional OOP Architecture**: Demonstrates inheritance, encapsulation, polymorphism, decorators, and modularization
- **Modern GUI Design**: Intuitive card-based interface with color-coded actions and visual feedback
- **Production-Ready Code**: Clean, maintainable, and well-documented codebase
- **Educational Value**: Built-in OOP concepts explanation window for learning purposes

---

## ✨ Features

### 🤖 AI Models Integration

- **Object Detection Model**: Powered by Hugging Face's advanced computer vision models
  - Detect multiple objects in images
  - View confidence scores and bounding box coordinates
  - Support for various image formats (PNG, JPG, JPEG, BMP)

- **Text-to-Image Generation**: Create images from natural language descriptions
  - Generate high-quality images from text prompts
  - Powered by FLUX.1-dev model
  - Instant preview and save functionality

### 🎨 User Interface

- **Modern Card-Based Design**: Visual model selection with descriptive cards
- **Professional Color Scheme**: Blue-themed interface with color-coded action buttons
- **Intuitive Layout**: Organized sections for model selection, input, and output
- **Responsive Controls**: Radio buttons, file browsers, and scrollable text areas
- **Visual Feedback**: Highlighted selections and status indicators

### 📚 Educational Component

- **OOP Concepts Explained**: Dedicated window explaining all OOP principles used
- **Code Examples**: Direct references to implementation in the codebase
- **Comprehensive Coverage**: Classes, inheritance, encapsulation, polymorphism, decorators, and more

### 🏗️ Technical Architecture

```
ai_studio_ani/
├── main.py              # Application entry point
├── gui.py               # GUI implementation with AppGUI and OOPExplanationWindow classes
├── models.py            # AI model classes (BaseModel, ObjectDetectionModel, TextToImageModel)
├── decorators.py        # Custom decorators (@log_call, @validate_input)
├── explanations.py      # OOP concept explanations for educational window
├── requirements.txt     # Project dependencies
├── README.md           # This file
├── INSTALLATION.md     # Detailed installation guide
└── USAGE_GUIDE.md      # Step-by-step usage instructions
```

### 🎓 OOP Principles Demonstrated

1. **Classes and Objects**: Multiple class definitions with clear responsibilities
2. **Inheritance**: `BaseModel` parent class with specialized child classes
3. **Encapsulation**: Private attributes (`_model_name`, `_api_key`) and protected methods
4. **Polymorphism**: Unified `run()` method interface across different model types
5. **Decorators**: `@log_call` and `@validate_input` for cross-cutting concerns
6. **Modularization**: Clean separation of concerns across multiple modules

---

## 🚀 Installation Guide

Follow these steps to set up AI Studio on your computer. This guide ensures all dependencies are properly installed and the application runs smoothly.

### Prerequisites

Before you begin, ensure you have:
- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager) - usually comes with Python
- **Internet connection** for downloading models and dependencies

### Step 1: Verify Python Installation

Open your terminal/command prompt and check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

You should see Python 3.8 or higher. If not, download and install Python from [python.org](https://www.python.org/downloads/).

### Step 2: Clone or Download the Project

**Option A: Clone with Git**
```bash
git clone https://github.com/60ani/aigui.git
cd aigui
```

**Option B: Download ZIP**
1. Download the project ZIP file
2. Extract it to your desired location
3. Open terminal/command prompt in that folder

### Step 3: Create a Virtual Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated:

**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal, indicating the virtual environment is active.

### Step 4: Install Required Dependencies

Install all necessary packages using pip:

```bash
pip install -r requirements.txt
```

This will install:
- `transformers` - Hugging Face transformers library
- `huggingface_hub` - For API access
- `torch` - PyTorch for model inference
- `Pillow` - Image processing library

**Note**: The installation might take a few minutes, especially for PyTorch (which can be large).

### Step 5: Verify Tkinter Installation

Tkinter usually comes with Python, but let's verify:

```bash
python -c "import tkinter; print('Tkinter is installed!')"
```

**If you get an error on Linux**, install tkinter:
```bash
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo yum install python3-tkinter  # Fedora/RHEL
```

### Step 6: Set Up Hugging Face API Token (Optional but Recommended)

For better rate limits and access:

1. Create a free account at [huggingface.co](https://huggingface.co/)
2. Go to Settings → Access Tokens
3. Create a new token
4. Set it as an environment variable:

**On Windows (PowerShell):**
```powershell
$env:HF_TOKEN="your_token_here"
```

**On macOS/Linux:**
```bash
export HF_TOKEN="your_token_here"
```

*Note: The application includes a fallback token for testing, but using your own is recommended for production use.*

### Step 7: Run the Application

Launch AI Studio:

```bash
python main.py
```

The application window should open immediately. If you see the interface, congratulations! 🎉

---

## 📘 How to Use AI Studio

### Getting Started

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Choose Your AI Model**
   
   You'll see two cards in the main window:
   - **🔍 Object Detection**: For analyzing images
   - **🎨 Image Generation**: For creating images from text

   Click on the card of the model you want to use. The selected card will be highlighted.

### Using Object Detection

**Step 1**: Select the Object Detection card

**Step 2**: Select input type
- Click the **"📁 Image File"** radio button

**Step 3**: Load your image
- Click **"Browse Image"** button
- Navigate to and select an image file (PNG, JPG, JPEG, BMP)
- The file path will be displayed

**Step 4**: Run detection
- Click the **"🚀 Run Model"** button
- Wait for processing (usually 5-15 seconds)
- Results will appear in the output area showing:
  - Detected objects
  - Confidence scores
  - Bounding box coordinates

### Using Image Generation

**Step 1**: Select the Image Generation card

**Step 2**: Select input type
- Click the **"✍️ Text Prompt"** radio button

**Step 3**: Enter your description
- Type your image description in the text box
- Example: "A serene mountain landscape at sunset with a lake"

**Step 4**: Generate image
- Click the **"🚀 Run Model"** button
- Wait for generation (may take 30-60 seconds)
- The generated image will be displayed
- Click **"💾 Save Output"** to save the image

### Additional Features

- **📋 View OOP Concepts**: Click the button in the header to learn about the OOP principles used in this project
- **ℹ️ View Model Info**: See details about the currently selected model
- **🗑️ Clear Output**: Clear the output area to start fresh
- **💾 Save Output**: Save generated images or detection results

---

## 🔧 Troubleshooting

### Common Issues and Solutions

**Issue**: "Module not found" error
- **Solution**: Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

**Issue**: Application window doesn't open
- **Solution**: Verify tkinter installation with `python -c "import tkinter"`

**Issue**: Slow model loading
- **Solution**: First-time model downloads can be large. Ensure stable internet connection. Models are cached after first use.

**Issue**: "API rate limit exceeded"
- **Solution**: Set up your own Hugging Face API token (see Installation Step 6)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Hugging Face** for providing amazing AI models and APIs
- **Python Software Foundation** for Python and Tkinter
- All contributors and testers who helped improve this project

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the `USAGE_GUIDE.md` for detailed instructions
3. Open an issue on GitHub

---

**Made with ❤️ by Anish Regmi, Sabir Pudasaini, and team**
- Easy maintenance and testing

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd aigui
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Hugging Face API token (optional but recommended):
```bash
# Windows PowerShell
$env:HF_TOKEN="your_token_here"

# Windows CMD
set HF_TOKEN=your_token_here

# Linux/Mac
export HF_TOKEN=your_token_here
```

### Running the Application

```bash
python main.py
```

## 📖 Usage Guide

### Using Image-to-Text (OCR)
1. Click the **"Image detection"** card to select the model
2. Choose **"Image Input"** radio button
3. Click **"Browse Image"** to select an image file
4. Click **"▶️ Action "** button
5. View extracted text in the output area

### Using Text-to-Image
1. Click the **"Text to Image"** card to select the model
2. Choose **"Text Input"** radio button
3. Enter your text description in the input field
4. Click **"▶️ Run Text-to-Image"** button
5. Generated image will be saved as `output_image.png`

### Viewing OOP Explanations
- Click **"📚 View OOP Concepts"** button in the header, OR
- Go to **Help → OOP Concepts** in the menu bar
- Read comprehensive explanations with code examples
- Close the window when finished

## 🔧 Technical Details

### Dependencies
- **tkinter**: GUI framework (included with Python)
- **Pillow (PIL)**: Image processing
- **transformers**: Hugging Face transformers library
- **huggingface_hub**: Hugging Face API client

### Supported Models
- **facebook/detr-resnet-50**:  Object Detection 
- **FLUX.1-dev** (black-forest-labs/FLUX.1-dev): Text-to-Image generation

### Supported Image Formats
- PNG (.png)
- JPEG (.jpg, .jpeg)
- BMP (.bmp)
- GIF (.gif)

## 🎓 Educational Value

This project serves as an excellent learning resource for:
- **Python Programming**: Intermediate to advanced concepts
- **GUI Development**: Tkinter framework usage
- **OOP Design**: Real-world application of OOP principles
- **API Integration**: Working with external AI services
- **Code Organization**: Project structure and modularization

## 📝 Assignment Requirements Met

✅ **Multiple Inheritance**: BaseModel as parent class  
✅ **Encapsulation**: Private attributes and methods  
✅ **Multiple Decorators**: @log_call, @validate_input  
✅ **Polymorphism**: Overridden run() methods  
✅ **Modularization**: Separate files for different concerns  
✅ **GUI Integration**: Tkinter-based interface  
✅ **AI Model Integration**: Hugging Face models  
✅ **Documentation**: Comprehensive explanations  

## 🆕 Version 2.0 Updates

### UI Enhancements
- Completely redesigned interface with modern aesthetics
- Professional color scheme (blues, greens, grays)
- Card-based model selection
- Enhanced visual hierarchy
- Improved spacing and padding

### UX Improvements
- Better error handling and user feedback
- Loading indicators for model operations
- Success/error messages with icons
- Intuitive navigation

### Documentation
- Dedicated OOP explanation window
- Bachelor's-level detailed explanations
- Code examples and references
- Formatted, scrollable content

## 🤝 Contributing

This is an educational project. For improvements:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is created for educational purposes as part of HIT137 coursework.

## 👥 Authors

- Group Assignment
- Anish Regmi
- Samir Pudasaini and 2 others.

## 🙏 Acknowledgments

- Hugging Face for AI model APIs
- Black Forest Labs for FLUX.1-dev model
- Python community for excellent libraries

---

**Note**: This application requires an internet connection to access Hugging Face models. Processing times may vary based on network speed and model complexity.
```
