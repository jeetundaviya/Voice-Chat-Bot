# 🎙️ Voice-Chat-Bot

A Python-based voice chatbot that leverages **Whisper** for speech-to-text, **Ollama** for AI-generated responses, and **pyttsx3** for text-to-speech conversion. This project allows users to have a natural, real-time conversation with an AI model using voice commands.

---

## 🚀 Features
✅ **Speech Recognition** – Uses Whisper to transcribe audio to text.  
✅ **AI Responses** – Generates responses using an LLM (like LLaMA) via Ollama.  
✅ **Voice Output** – Converts AI-generated responses to speech using pyttsx3.  
✅ **Simple & Fast** – Lightweight and efficient for real-time interaction.  

---

## 🛠️ Installation

### 1. Clone the repository:
```bash
git clone https://github.com/jeetundaviya/Voice-Chat-Bot.git
cd Voice-Chat-Bot
```

### 2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Install Whisper:
```bash
pip install git+https://github.com/openai/whisper.git
```

### 5. Install and run Ollama:
- Install Ollama from [https://ollama.com](https://ollama.com).
- Download the Mistral model:
```bash
ollama pull mistral
```

---

## ▶️ Usage
1. Start the chatbot:
```bash
python chatbot_with_ollama.py
```
2. Speak into your microphone.
3. The chatbot will respond using voice output.

---

## 📂 Project Structure
```
├── README.md                  # Project documentation  
├── chatbot_with_chatgpt.py    # Chatbot using OpenAI GPT models  
├── chatbot_with_ollama.py     # Chatbot using Ollama with LLaMA models  
├── env/                       # Virtual environment (ignored in .gitignore)  
├── requirements.txt           # Required Python packages  
└── temp_audio.wav             # Temporary audio file for transcription  
```

---

## 🌟 Future Improvements
- Add multi-language support.  
- Improve response latency.  
- Add more model options for enhanced responses.  

---

## 🤝 Contributing
Feel free to open issues or create pull requests. Contributions are always welcome!

---

## 🏆 Credits
Developed by [Jeet Undaviya](https://github.com/jeetundaviya)  

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).