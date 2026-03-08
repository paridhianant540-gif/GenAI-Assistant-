# GenAI-Assistant
The goal of this project is to build a GenAI-powered chat assistant using Retrieval-Augmented Generation (RAG). It converts documents into embeddings, stores them for similarity search, and retrieves relevant context to generate accurate, reliable responses to user queries based on the provided documents.

# Tools and Technologies

- **Backend**: Python
- **Frontend**: Basic HTML
- **APIs**:
    - Large Language Model API (OpenAI / Gemini / Claude / Mistral)
    - Embeddings API
- **Vector Storage**: In-memory storage, SQLite, or a simple database
- **Development Environment**: Python 3.x, a code editor (like VSCode), and a web browser

  ### Hardware Requirements

- A computer with internet access
- Sufficient RAM (at least 8GB recommended for smooth operation)


Architecture diagram
<img width="455" height="684" alt="image" src="https://github.com/user-attachments/assets/d684c5fd-026c-41d0-ab0e-6bf8dcd24201" />



## Step-by-Step Instructions

# Set up Project Environment

1. **Install Python**: Ensure Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. **Create a Project Directory**:
    
    ```bash
    mkdir genai-chat-assistant
    cd genai-chat-assistant
    ```
    
3. **Set Up a Virtual Environment**:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    
4. **Install Required Packages**:
    
    ```bash
    pip install flask openai numpy
    ```
