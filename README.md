# ChatGPT3 Python Voice Chat
Small voice chat to talk with chatGPT using python.

![Screenshot main menu](https://github.com/engjango/chatgpt-python-voice/blob/main/screenshot.png)

# Features

- [x] ChatGPT3 API
- [x] Auto Translate
- [x] Speach to Text

# Install Dependencies

## Linux (Ubuntu)
Install pip in the Python environment
```
python -m ensurepip --upgrade
```
Then,
```
pip install -r openai re openai speech_recognition pyttsx3
```

## Windows (10)
Install pip in the Python environment
```
py -m ensurepip --upgrade
```
Then,
```
pip install -r openai re openai speech_recognition pyttsx3
```
# Get an OpenAI API Key
Register at "openai.com" and generate your api key.

# Compile and Run

Once you have the dependencies (see above) and the api key, download, unzip and navigate to this respository and change the openai api key in chatVoice.py (Line 16).

Then run the following commands in your terminal.

## Linux (Ubuntu)
```
python chatVoice.py
```

## Windows (10)
```
python chatVoice.py
```

# Talk to ChatGPT

* Talk to chatgpt when the message "Listening" appears, say something and start your sentence with the word "Computer". Example: Computer, how are you?

# Dependencies

* openai
* speech_recognition 
* pyttsx3
