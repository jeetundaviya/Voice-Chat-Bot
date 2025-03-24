import openai
import whisper
import pyttsx3
import whisper
import sounddevice as sd
import soundfile as sf
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Initialize OpenAI key
openai.api_key = "OPEN-AI-KEY"

# Initialize speech recognition and text-to-speech
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()


def transcribe_audio():
    model = whisper.load_model("base")
    print("Listening...")

    # Record audio (5 seconds, 16kHz sample rate)
    duration = 5
    sample_rate = 16000
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()

    # Convert to 16-bit PCM format for Whisper
    audio = (recording * 32767).astype(np.int16)

    # Save audio to file using soundfile
    file_path = "temp_audio.wav"
    sf.write(file_path, audio, sample_rate)

    # Transcribe using Whisper
    result = model.transcribe(file_path)
    return result["text"]

def get_response(question):
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use this if GPT-4 is not available
    messages=[{"role": "user", "content": question}]
)
    return response.choices[0].message.content

def main():
    print("Start speaking...")
    question = transcribe_audio()
    if question:
        print(f"User: {question}")
        response = get_response(question)
        print(f"ChatGPT: {response}")
        speak(response)

if __name__ == "__main__":
    main()
