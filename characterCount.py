introString=input("Enter Your Introduction:")
characterCount=0
wordCount=1
for character in introString:
    characterCount=characterCount+1
    print(characterCount)
    if(character == " "):
        wordCount=wordCount+1
print("no of word in the string:")
print(wordCount)
print("no of characters in the string:")
print(characterCount)

