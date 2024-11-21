#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:    W0443556
#Student Name:  Kyle Preston

def redact_phrase(phraseInput):
    redactedphrase =""
    redactedcount  = 0
    letterInput=input("Type a comma-separated list of letters to redact: ")   
    redactedLetters= letterInput.split(",")
    for letter in phraseInput:
        if letter.lower() in redactedLetters:
            redactedcount += 1
            redactedphrase += "_"
                
        else: 
            redactedphrase += letter
        
            
            

    print(f"Number of letters redacted: {redactedLetters}")
    print(f"Redacted phrase: {redactedphrase}")




def main():
    phraseInput = ""
    while phraseInput.lower() !="quit":
        phraseInput=input("Type a phrase (or quit to exit program): ")
        if phraseInput.lower() =="quit":
            break
        else:
            redact_phrase(phraseInput)
            print('\n')

main()