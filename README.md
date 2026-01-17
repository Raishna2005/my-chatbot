# 🤖 My First AI Chatbot

A simple AI chatbot built using Python, Gradio, and the Hugging Face Inference API.  
This project demonstrates how to create a functional chatbot without needing a local GPU, while following basic security practices.

---

## 📌 Project Objective

The objective of this project was to build a functional AI chatbot that can accept user input and generate meaningful responses using a large language model.  
This project helped me understand API-based AI inference and simple web-based deployment.

---

## 🛠️ Tools & Technologies Used

- Python  
- Gradio (for the web UI)  
- Hugging Face Inference API  
- Model: Qwen/Qwen2.5-7B-Instruct  
- python-dotenv (for environment variables)  
- Git & GitHub  

---

## ⚙️ Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up the .env file

Create a file named .env in the project root and add your Hugging Face API token:

```
HF_API_TOKEN=your_huggingface_api_token_here
```


The .env file is added to .gitignore to prevent accidental exposure of sensitive data.

### 4. Run the application
```bash
python app.py
```

After running the command, Gradio will provide a local URL to access the chatbot in your browser.

---

## 🧠 Approach

This project uses the Hugging Face Inference API so the chatbot can run without requiring a GPU on the local machine.
Gradio was chosen because it allows quick creation of a simple and interactive web interface with minimal code.

---

## 🚧 Challenges Faced

Encountered StopIteration errors with an initial model, which were resolved by switching to Qwen/Qwen2.5-7B-Instruct.

Faced GitHub Push Protection issues when an API key was detected, which highlighted the importance of using .env files and .gitignore.
