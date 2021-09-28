import random

def get_word(wordlist="/usr/share/dict/words"): # Dependency injection
    f = open(wordlist)
    words = []
    for w in f:
        w = w.strip()
        if not w.isalpha():
            continue
        if not w.islower():
            continue
        if len(w) < 7:
            continue
        words.append(w.strip())
    return random.choice(words)

def mask_word(word, guesses):
    letters = []
    for i in word:
        if i in guesses:
            letters.append(i)
        else:
            letters.append("-")
    return "".join(letters)
    

def get_status(secret_word, guesses, turns_left):
    masked_word = mask_word(secret_word, guesses)
    return f"""Word : {masked_word}
Turns left : {turns_left}"""

def evaluate_input(secret_word, guesses, turns_left, input_):
    if input_ in guesses:
        return f"You already guessed '{input_}'", turns_left
    
    if "-" not in mask_word(secret_word, guesses+[input_]):
        return "word has been guessed", turns_left

    if input_ in secret_word:
        guesses.append(input_)
        return "good guess", turns_left

    if input_ not in secret_word:
        if turns_left == 1:
            return "game is over", turns_left
        else:
            guesses.append(input_)
            return "bad guess", turns_left - 1

def main():
    secret_word = get_word()
    print (secret_word)
    guesses = []
    turns_left = 7
    status = ""
    while status not in ["word has been guessed", "game is over"]:
        print ("\n", status)
        print (get_status(secret_word, guesses, turns_left))
        guess = input("Enter a letter ")
        print (f'"{guess}"')
        status, turns_left = evaluate_input(secret_word, guesses, turns_left, guess)

if __name__ == "__main__":
    main()

        
