answer = ""
def guess(secretWord):
    global answer
    i = 0
    while i != len(secretWord):
        userInput = input(f"Masukan Huruf {i + 1} :")
        if(userInput != " "):
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
    print(f"Jawaban anda benar ({answer})")
guess("Duren")
                
