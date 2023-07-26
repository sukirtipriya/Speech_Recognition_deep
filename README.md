# Speech_Recognition_deep

Speech Recognition incorporates computer science and linguistics to identify spoken words and converts them into text. It allows computers to understand human language.
![image](https://github.com/sukirtipriya/Speech_Recognition_deep/assets/88479900/3a573e4b-8d5a-4e3e-83c4-f4126e07c45b)

Speech recognition is a machine's ability to listen to spoken words and identify them. You can then use speech recognition in Python to convert the spoken words into text, make a query or give a reply. You can even program some devices to respond to these spoken words. You can do speech recognition in python with the help of computer programs that take in input from the microphone, process it, and convert it into a suitable form.

Speech recognition seems highly futuristic, but it is present all around you. Automated phone calls allow you to speak out your query or the query you wish to be assisted on; your virtual assistants like Siri or Alexa also use speech recognition to talk to you seamlessly.

How Does Speech Recognition work?

Speech recognition in Python works with algorithms that perform linguistic and acoustic modeling. Acoustic modeling is used to recognize phenones/phonetics in our speech to get the more significant part of speech, as words and sentences.

![image](https://github.com/sukirtipriya/Speech_Recognition_deep/assets/88479900/7c6e2a17-3061-4305-ab43-f76801cf06bc)
Speech recognition starts by taking the sound energy produced by the person speaking and converting it into electrical energy with the help of a microphone. It then converts this electrical energy from analog to digital, and finally to text. 

It breaks the audio data down into sounds, and it analyzes the sounds using algorithms to find the most probable word that fits that audio. All of this is done using Natural Language Processing and Neural Networks. Hidden Markov models can be used to find temporal patterns in speech and improve accuracy.


Picking and Installing a Speech Recognition Package

To perform speech recognition in Python, you need to install a speech recognition package to use with Python. There are multiple packages available online. The table below outlines some of these packages and highlights their specialty.

Package                           Functionality                                                                 Installation      
 
Apiai                     Includes natural language processing for identifying a speaker’s intent               $ pip install apiai

Google-cloud-speech       Offers basic speech to text conversion                                                $pip install virtualenv
 
virtualenv <your-env>     <your-env>\Scripts\activate                                                           <your-env>\Scripts\pip.exe install google-cloud-speech

Speech Recognition       Offers easy audio processing and microphone accessibility                              pip install SpeechRecognition

Watson-developer-cloud    Watson developer cloud is an Artificial Intelligence API that makes creating, debugging,
                          running, and deploying APIs easy. It can be used to perform basic speech recognition tasks.      pip install-upgrade watson-developer-cloud

Picking and installing a speech recognition package

For this implementation, you will use the Speech Recognition package. It allows:

    Easy speech recognition from the microphone.
    Makes it easy to transcribe an audio file.
    It also lets us save audio data into an audio file.
    It also shows us recognition results in an easy-to-understand format
