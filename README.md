# ChatGPT3 Python Voice Chat
Small voice chat to talk with chatGPT using python.

![Screenshot main menu](https://github.com/lavradodosilicio/cobra/blob/main/screenshots/Captura%20de%20tela%20de%202021-01-07%2018-02-55.png)

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
pip install -r openai re openai speech_recognition pyttsx3 winsound
```

## Windows (10)
Install pip in the Python environment
```
py -m ensurepip --upgrade
```
Then,
```
pip install -r openai re openai speech_recognition pyttsx3 winsound
```

# Compile and Run

Once you have the dependencies (see above), download, unzip and navigate to this respository and run the following commands in your terminal.

## Linux (Ubuntu)
```
python chatVoice.py
```

## Windows (10)
```
python chatVoice.py
```

# Chatting

* Talk to chatgpt when the message "Listening" appears, say something and start your sentence with the word "Computer". Example: Computer, how are you?

# Dependencies

* openai
* speech_recognition 
* pyttsx3
