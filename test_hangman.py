import hangman
import pytest

# 1. No special characters (only alphabet)
# 2. No capital letters
# 3. Atleast 7 characters long

def test_get_word_no_special():
    # 1. No special characters (only alphabet)
    f = open("/tmp/my_words.txt", "w")
    f.write("aeroplane\n")
    f.write("submarine's\n")
    f.write("battle ship\n")
    f.close()
    for i in range(10):
        word = hangman.get_word("/tmp/my_words.txt")
        assert word == "aeroplane"

def test_get_word_no_special_none():
    f = open("/tmp/my_words.txt", "w")
    f.write("submarine's\n")
    f.write("battle ship\n")
    f.close()
    for i in range(10):
        with pytest.raises(IndexError): 
            word = hangman.get_word("/tmp/my_words.txt")


def test_no_capitals():
    f = open("/tmp/my_words.txt", "w")
    f.write("Peter\n")
    f.write("Paul\n")
    f.write("aeroplane\n")
    f.write("John\n")
    f.close()
    for i in range(10):
        word = hangman.get_word("/tmp/my_words.txt")
        assert word == "aeroplane"

def test_min_length_7():
    f = open("/tmp/my_words.txt", "w")
    f.write("cat\n")
    f.write("dog\n")
    f.write("aeroplane\n")
    f.write("bunny\n")
    f.close()
    for i in range(10):
        word = hangman.get_word("/tmp/my_words.txt")
        assert word == "aeroplane"
        

def test_mask_word():
    word = "aeroplane"
    guesses = ['x', 't', 'p', 'a']
    assert hangman.mask_word(word, guesses) == "a---p-a--"
    

def test_get_status():
    secret_word = "aeroplane"
    guesses = ['x', 't', 'p', 'a']
    status = hangman.get_status(secret_word, guesses, 5)
    assert status == f"""Word : a---p-a--
Turns left : 5"""

# Word has been guessed
# Bad guess
# Last turn over
# Repeat guess

def test_evaluate_input_word_guessed():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 5
    input_ = "t"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert turns_left == 5
    assert resp == "word has been guessed"
    
def test_evaluate_input_bad_guess():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 5
    input_ = "q"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert resp == "bad guess"
    assert guesses == ["c", "a", "x", "m", "q"]
    assert turns_left == 4

    
def test_evaluate_input_game_over():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 1
    input_ = "q"
    resp, _ = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert resp == "game is over"

def test_evaluate_input_repeat_guess():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 5
    input_ = "c"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert turns_left == 5
    assert resp == "You already guessed 'c'"

def test_evaluate_input_good_guess():
    secret_word = "cat"
    guesses = ["c", "x", "m"]
    turns_left = 5
    input_ = "a"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert resp == "good guess"
    assert turns_left == 5


    
