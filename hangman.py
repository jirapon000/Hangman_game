import random

def choose_word():
    words = [
        'python', 'variable', 'function', 'syntax', 'compile',
        'algorithm', 'boolean', 'integer', 'string', 'float',
        'class', 'object', 'inheritance', 'loop', 'recursion',
        'debug', 'binary', 'decimal', 'hexadecimal', 'module',
        'library', 'package', 'exception', 'thread', 'instance',
        'method', 'array', 'list', 'tuple', 'dictionary',
        'set', 'queue', 'stack', 'pointer', 'branch',
        'commit', 'merge', 'repository', 'clone', 'push',
        'pull', 'fork', 'feature', 'branching', 'terminal',
        'script', 'runtime', 'execute', 'input', 'output'
    ]
    return random.choice(words).upper()

def play_game():
    word = choose_word()
    guessed = set()
    attempts = 6
    display = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.\n")

    while attempts > 0 and '_' in display:
        print('Word: ' + ' '.join(display))
        print(f"Guessed letters: {', '.join(sorted(guessed))}")
        guess = input("Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.\n")
        elif guess in word:
            for idx, char in enumerate(word):
                if char == guess:
                    display[idx] = guess
            print("Correct!\n")
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}\n")

        guessed.add(guess)

    if '_' not in display:
        print(f"🎉 Congrats! You guessed the word: {word}")
    else:
        print(f"💀 Game Over. The word was: {word}")

if __name__ == "__main__":
    play_game()
