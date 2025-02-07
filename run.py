import nltk
from nltk.corpus import wordnet
import spacy
import random


print("Loading data....")
# Load spaCy model
nlp = spacy.load('en_core_web_lg')
# List of English words (could be expanded or replaced)
word_list = ["quick", "fox", "jumps", "over", "lazy", "dog", "cat", "happy",
             "silent", "run", "beautiful", "fast", "slow", "sits", "under",
             "table", "sky", "clouds", "mountain", "river", "walks", "city",
             "night", "apple", "book", "running", "game", "plays", "reading",
             "set"]


class TextProcessor:
    """
    Creating Assistant Procedures for Generating Random Phrases,
    Analyzing Phrases and Words
    """
    def generate_random_phrase(self, length):
        """
        Generate a random phrase with a specific number of words
        """
        random.shuffle(word_list)
        if length <= len(word_list):
            return " ".join(word_list[:length])
        else:
            return " ".join(word_list)

    def get_words(self, phrase):
        """
        Return the set of words contained in the sentence.
        """
        return phrase.split()

    def get_pos_tag(self, phrase):
        """
        Return the part of speach tag of the phrase' words
        """
        pos_tags = {}
        for token in nlp(phrase):
            pos_tags[token.text] = spacy.explain(token.tag_)
        return pos_tags

    def get_word_meaning(self, word):
        """
        Get the meaning of a word
        """
        # Get all the synsets (different meanings)
        synsets = wordnet.synsets(word)
        if synsets:
            # Get the first meaning from the synsets
            return synsets[0].definition()
        else:
            return "Meaning not found."


class MysteryWord(TextProcessor):
    """
    Create word object with some properties and functions
    """
    def __init__(self, word, pos_tag):
        self.word = word
        self.length = len(word)
        self.start_with = word[0]
        self.pos_tag = pos_tag
        self.meaning = self.get_word_meaning(word)
        self.is_guessed = False
        self.available_attempts = 3

    def describe(self):
        print(f"This word is {self.length} carachter(s) long.")
        print(f"starts with {self.start_with}.")
        print(f"POS_TAG for this word is: {self.pos_tag}")
        print(f"Words meaning: {self.meaning}")

    def validate(self, word):
        number_attempts = f"{self.available_attempts-1} more attempts" \
                            if self.available_attempts > 1 \
                            else "no more attempt"
        self.available_attempts -= 1
        if not word.isalpha():
            return "\nThe word contains other characters not only letters." \
                   f"\nYou have {number_attempts}.\n"
        elif self.word.lower() != word.lower():
            return "\nThe word was not guessed. The entered word is" \
                   f"\nincorrect.You have {number_attempts}.\n"

        self.is_guessed = True
        return f"\nCongratulations!! you have guessed the word.\n"

    def print_result(self):
        print(f'{self.word:{15}} \t {self.is_guessed:{6}} \t \
        {3-self.available_attempts:{6}}')


class MysteryPhrase(TextProcessor):
    """
    Create a random phrase and define the properties of the words it contains,
    then establish a set of procedures to handle them."
    """
    def __init__(self):
        """
        Get a random sentence with a subject, predicate,
        direct object and adjective
        """
        self.phrase = self.generate_random_phrase(4)
        self.pos_tags = []
        self.words = []

    def define_words(self):
        # get all words from the phrase without ponctuations
        word_list = self.get_words(self.phrase)
        # get all pos tags for each words
        self.pos_tags = self.get_pos_tag(self.phrase)
        # generate defined word object list
        self.words = [MysteryWord(word, self.pos_tags[word])
                      for word in word_list]

    def describe(self):
        print(f"The generated phrase contains {len(self.words)} words.\n")

    def display_current_state(self):
        displayed_phrase = [word.word if word.is_guessed
                            else "?" for word in self.words]
        print(f"The current state of the phrase: {displayed_phrase}\n")


class Game(MysteryPhrase):
    """
    Initiate the game and interact with user
    """
    def __init__(self):
        super().__init__()

    def start_game(self):
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        print("Welcome to Mystery Phrase ^_^ ")
        print("We will see your ability to discover the hidden words!\n")
        print("Start generating the phrase...\n\n")
        print("defining words....\n\n")
        self.define_words()
        print("The phrase has been generated for you.")
        self.describe()
        print("Let's go..... \n")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    def play(self):
        self.display_current_state()
        for word in self.words:
            print("-------------------------------------------------"
                  "------------\n")
            while word.available_attempts and not word.is_guessed:
                word.describe()
                user_word = input("Please enter a word: ")
                validation = word.validate(user_word)
                print(validation)
            print("-------------------------------------------------"
                  "------------\n")
            self.display_current_state()

    def get_final_result(self):
        print("Summery for your guessing scroe")
        print(f'{"word":{15}} \t {"guessed":>{6}} \t \
        {"number of used attempts":{6}}')
        print("---------------------------------------------------------------"
              "------------------")
        for word in self.words:
            word.print_result()
        print("---------------------------------------------------------------"
              "------------------\n")
        print("The correct phrase is:")
        print(f"{self.phrase}\n")
        guessed_word = [word for word in self.words if word.is_guessed]
        if len(guessed_word) == len(self.words):
            print("Congratulations!! you have guessed all the words.\n")


def main():
    """
    Create a game object and start and play the game.
    """
    game = Game()
    game.start_game()
    game.play()
    game.get_final_result()


main()
