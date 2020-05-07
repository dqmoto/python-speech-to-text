#!/usr/bin/env python3

import speech_recognition as sr

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 400
        print(r.energy_threshold) 
        
        r.dynamic_energy_threshold = False
        print('Please say something...')
        audio = r.listen(source, timeout=10)

        try:
            print('You said:  \n ' + r.recognize_google(audio))
        except Exception as e:
            print('Error: ' + str(e))

if __name__ == "__main__":
    main()