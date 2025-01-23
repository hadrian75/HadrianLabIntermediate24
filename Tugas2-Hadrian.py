def hangman(secretWord):
    wordSet = set(secretWord) 
    guesses = set()  
    chances = 6
    
    while chances > 0:
        guess = input("Masukan Huruf : ").lower()
        if guess in wordSet and guess not in guesses:
            guesses.add(guess)  
            chances -= 1
        else:
            chances -= 1  
        if wordSet == guesses:
            print(f"GG Banget! Anda Menang! Secret Wordnya adalah: {secretWord}")
            break
        print(f"Sisa kesempatan: {chances}")
    if chances == 0:
        print(f"Noob Banget kamu Kalah! Secret Wordnya adalah: {secretWord}")
hangman("nanan")
