import random

print("Welcome to Hangman Game")
words=["python","words","books","apples","orange"]
selected_word= random.choice(words) 
wrong_count=0
max_wrong=6
guessed_letters=[]

hidden=["_"]*len(selected_word)

print("word: "," ".join(hidden))

while wrong_count<max_wrong:
    letter=input("guess a letter\n").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if letter in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(letter)

    if letter in selected_word:
     print("present")
     for i in range(len(selected_word)):
         if selected_word[i]==letter:
             hidden[i]=letter
    else:
     print("wrong guess") 
     wrong_count+=1
    print("attempts left:", max_wrong - wrong_count)
    print("word: "," ".join(hidden))
    
    if "_" not in hidden:
      print("Congratulations! You guessed the word:", selected_word)
      break



if wrong_count==max_wrong:
 print("Game Over! The word was:", selected_word)
     
