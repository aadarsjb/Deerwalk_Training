# a = 13
# b = 10

# print((a > b and "a>b") or (b > a and "b>a"))


# def func():
#     for x in range(22, 23, 24):
#         print(x)

# func()

# print(22 + "22" + 5000)  #error

import io
import pygame
from gtts import gTTS

def speak(text):
    #save sound to RAM
    with io.BytesIO() as file:
        gTTS(text = text, lang = "en").write_to_fp(file)
        file.seek(0)
        #play the sound
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

while True:
    if __name__ == '__main__':
        print('What should I say?')
        text = input(" >> ")
        speak(text)

    choice = input("Enter 1 to continue or 0 to exit \n")
    if choice == "1":
        continue
    else:
        break



