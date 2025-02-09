#@ Param : secretWord (string) - kata yang akan ditebak pemain
#Referensi : OS Clear (https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def updateText(secretWord):
    letterGuessed = set()
    chances = len(set(secretWord)) + 2
    print("\n" + "="*30)
    print(" " * 5 + "Welcome to Hangman")
    print("="*30 + "\n")
    
    while chances > 0:
        text = ""
        for char in secretWord:
            if char in letterGuessed:
                text += char + " "
            else:
                text += "_ "
        
        print("Tebakan Sejauh ini: ", text.strip())
        print(f"Sisa Kesempatan: {chances}")
        
        guess = input("Masukkan Huruf: ").lower()
        if len(guess) != 1:
            print("Masukin huruf 1 doang ya!") 
            continue
        if guess.isalpha() == False:
            print("Gaboleh Angka!") 
            continue
        
        
        if guess in secretWord:
            if guess not in letterGuessed:
                letterGuessed.add(guess)
                print(f"Bagus! Huruf '{guess}' ada dalam kata.")
                letterGuessed.add(guess)
                chances -= 1
            else:
                print(f"Anda sudah menebak huruf '{guess}'.")
        else:
            chances -= 1
            print(f"Sayang sekali! Huruf '{guess}' tidak ada dalam kata. Kesempatan berkurang.")
        
        if all(char in letterGuessed for char in secretWord):
            clear_terminal()
            print(f"GG Banget! Anda Menang! Secret Wordnya adalah: {secretWord}")
            break

    if chances == 0:
        clear_terminal()
        print(f"Noob Banget kamu Kalah! Secret Wordnya adalah: {secretWord}, kamu hanya berhasil menebak {len(letterGuessed)} huruf dari {len(set(secretWord))} huruf yang ada {letterGuessed}.")

# Start the game
updateText("indonesia")
