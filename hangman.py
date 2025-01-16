secretWord = "Duren"
answer = ""
def guess():
    global answer
    i = 0
    while i != len(secretWord):
        userInput = input(f"Masukan Huruf {i + 1} :")
        if(len(userInput) == 1):
            if(userInput == secretWord[i]):
                print(f"Huruf {i + 1} Anda Benar")
                i+=1
                answer += userInput
            else:
                if(userInput.islower()):
                    print("Huruf Kapital!")
                elif(userInput.isupper()):
                    print("Huruf Kecil!")
                else:
                    print("Jawaban Salah !")
                # elif(userInput != secretWord[i]):
                #     print(f"Huruf {i+1} Salah")
        else:
                
            print("Tidak boleh lebih dari 1 huruf")
    print(f"Jawabannya {answer}")
guess()
                
