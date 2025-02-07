from nltk.corpus import wordnet
import nltk
import spacy
import random
import re



print("Loading data....")
# Load spaCy model
nlp = spacy.load('en_core_web_lg')
# List of English words (could be expanded or replaced)
word_list = [
    "quick", "fox", "jumps", "over", "lazy", "dog", "cat", "happy", 
    "silent", "run", "beautiful", "fast", "slow","sits", "under", 
    "table", "sky", "clouds", "mountain", "river", "walks", "city", "night",
    "apple", "book", "running", "game", "plays", "reading", "set"
]


class TextProcessor:
    """
    Creating Assistant Procedures for Generating Random Phrases, Analyzing Phrases and Words
    """

    def generate_random_phrase(self, length):
        """
        Generate a random phrase with a specific number of words
        """
        random.shuffle(word_list)
        if length <= len (word_list):
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
        synsets = wordnet.synsets(word)  # Get all the synsets (different meanings)
        
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
        print(f"This word is {self.length} carachter(s) long, starts with {self.start_with}")
        print(f"POS_TAG for this word is: {self.pos_tag}")
        print(f"Words meaning: {self.meaning}")



class MysteryPhrase(TextProcessor):
    """
    Create a random phrase and define the properties of the words it contains,
    then establish a set of procedures to handle them."
    """
    def __init__(self):
        # Get a random sentence with a subject, predicate, direct object and adjective
        self.phrase = self.generate_random_phrase(4)
        self.pos_tags = []
        self.words = []
    
    def define_words(self):
        #get all words from the phrase without ponctuations
        word_list = self.get_words(self.phrase)
        #get all pos tags for each words
        self.pos_tags = self.get_pos_tag(self.phrase)
        #generate defined word object list
        self.words = [MysteryWord(word, self.pos_tags[word]) for word in word_list]


    
    def describe(self):
        print(f"The generated phrase contains {len(self.words)} words.\n")
    
    def display_current_state(self):
        displayed_phrase = [word.word if word.is_guessed else "?" for word in self.words]
        print (f"The current state of the phras: {displayed_phrase}\n")


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
        self.display_current_state()
        print(self.phrase)


def main():
    """
    Create a game object and start and play the game.
    """
    game= Game()
    game.start_game()


main()