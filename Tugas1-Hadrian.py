answer = ""
def guess(secretWord):
    counter = 0
    global answer
    i = 0
    while i != len(secretWord):
        if(counter == 5):
            print("\nKesempatan Habis")
            break
        userInput = input(f"Masukan Huruf {i + 1} :")
        if(userInput):
            counter +=1
        if(userInput.strip() != ""):
              if(len(userInput) == 1):
                if(userInput == secretWord[i]):
                    print(f"Huruf {i + 1} Anda Benar")
                    i+=1
                    answer += userInput
                else:
                    if(userInput.lower() != secretWord[i].lower()):
                        print("Jawaban Salah !")
                    elif(userInput < secretWord[i]):
                        print("Huruf Kecil!")
                    elif(userInput > secretWord[i]):
                        print("Huruf Kapital!")
                    # elif(userInput != secretWord[i]):
                    #     print(f"Huruf {i+1} Salah")
              else:
                print("Tidak boleh lebih dari 1 huruf")
        else:
            print("Jawaban tidak boleh kosong!")
    if(len(answer) == len(secretWord)):
        print(f"Jawaban anda benar ({answer})")
    elif(len(answer) < len(secretWord) and answer != ""):
        print(f"Jawaban anda kurang tepat ({answer})")
    elif(answer == ""):
        print("Ups... Belum ada yang kejawab nih")
guess("Duren")
                

