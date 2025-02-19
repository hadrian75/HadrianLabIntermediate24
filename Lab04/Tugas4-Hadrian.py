import random
import os

listOfWords = ["Indonesia", "Malaysia", "Singapura", "Thailand", "Vietnam", "Filipina", "Brunei", "Laos", "Myanmar", "Kamboja"]
guessedWords = []
scores = 0

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def updateText(choicesWord):
    global scores
    choicesWord = random.choice(listOfWords).lower()
    letterGuessed = set()
    chances = round(len(set(choicesWord))/2) + 2
    print("\n" + "="*30)
    print(" " * 5 + "Welcome to Hangman")
    print("="*30 + "\n")
    
    while True:

        text = ""
        for char in choicesWord:
            if char in letterGuessed:
                text += char + " "
            else:
                text += "_ "
        
        print("Tebakan Sejauh ini: ", text.strip())
        print(f"Sisa Kesempatan: {chances}")
        
        guess = input("Masukkan Huruf: ").lower()
        if len(guess) < 1:
            print("Tolong Masukan Tebakan!") 
            continue
        if len(guess) > 1:
            print("Masukin huruf 1 doang ya!") 
            continue
        if not guess.isalpha():
            print("Gaboleh Angka!") 
            continue
        
        if guess in choicesWord:
            if guess not in letterGuessed:
                letterGuessed.add(guess)
                print(f"Bagus! Huruf '{guess}' ada dalam kata.")
            else:
                print(f"Anda sudah menebak huruf '{guess}'.")
        else:
            chances -= 1
            print(f"Sayang sekali! Huruf '{guess}' tidak ada dalam kata. Kesempatan berkurang.")
        
        if all(char in letterGuessed for char in choicesWord):
            clear_terminal()
            print(f"GG Banget! Anda Menang! Secret Wordnya adalah: {choicesWord}")
            guessedWords.append(choicesWord.capitalize())
            listOfWords.remove(choicesWord.capitalize())
            scores += 1
            print(f"Your Score now: {scores}")
            break  

        if chances == 0:
            clear_terminal()
            print(f"Noob Banget kamu Kalah! Secret Wordnya adalah: {choicesWord}, kamu hanya berhasil menebak {len(letterGuessed)} huruf dari {len(set(choicesWord))} huruf yang ada {letterGuessed}.")
            print(f"Your Score now: {scores}")
            break  
 
    if len(listOfWords) == 0:
        print("Semua kata sudah ditebak! Permainan selesai.")
        print(f"Your Score: {scores}")
        print(f"kata yang sudah ditebak: {guessedWords}")
        return
    else:
        print(f"Ingin Bermain Lagi? Y/N")
        inputUser  = input()
        if inputUser .lower() == "y":
            clear_terminal()
            updateText(random.choice(listOfWords).lower())  
        else:
            clear_terminal()
            print("Terima Kasih Telah Bermain!")
            print(f"Your Score: {scores} from {len(listOfWords) - 1}")
            print(f"Kata yang belum ditebak: {listOfWords}")
            print(f"Kata yang sudah ditebak: {guessedWords}")
        

# Start the game
updateText(random.choice(listOfWords).lower())