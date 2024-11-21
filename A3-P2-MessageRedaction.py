#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:    W0443556
#Student Name:  Kyle Preston

def redact_phrase(phraseInput):
    redactedphrase =""                                  #function is referencing the while statement in the main function, the purpose of this function is to split letters that are being redacted and in the case where theres no letters being redacted it would add the letters back
    redactedcount  = 0                                  # continuing from comment above ^. the end of the statement prints out how many redacted letters there were and prints new redactedphrase
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
    phraseInput = ""                                                    # main function serves as a while command and the starting input. basically the user has the option to break it with "quit". in the if statement
    while phraseInput.lower() !="quit":                                 # else statement works as calling the function above to run the phrased made in input to potentially redacted and at the end will restart the program
        phraseInput=input("Type a phrase (or quit to exit program): ")
        if phraseInput.lower() =="quit":
            break
        else:
            redact_phrase(phraseInput)
            print('\n')

main()