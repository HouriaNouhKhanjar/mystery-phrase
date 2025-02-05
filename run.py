from nltk.corpus import wordnet
import nltk
import spacy
import random
import re

# Load spaCy model
nlp = spacy.load('en_core_web_lg')
# List of English words (could be expanded or replaced)
word_list = [
    "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", "cat", "happy", 
    "silent", "run", "beautiful", "fast", "slow", "blue", "green", "sits", "under", 
    "table", "sky", "clouds", "mountain", "river", "walks", "city", "night"
]


class TextProcessor:
    """
    Creating Assistant Procedures for Generating Random Phrases, Analyzing Phrases and Words
    """

    def generate_random_phrase(self, length):
        """
        Generate a random phrase with a specific number of words
        """
        return " ".join(random.choice(word_list) for _ in range(length))


    def get_words(self, phrase):
        """
        Return the set of words contained in the sentence without punctuation marks.
        """
        phrase_without_punctuation = re.sub(r'[^\w\s]', '', phrase)
        return phrase_without_punctuation, phrase_without_punctuation.split()
    
    def get_pos_tag(self, phrase):
        """
        Return the part of speach tag of the phrase' words
        """
        pos_tags = {}
        for token in nlp(phrase):
            pos_tags[token.text] = spacy.explain(token.tag_)
        return pos_tags
    
    def get_synonyms(self, word):
        """
        Get synonyms for a word
        """
        synonyms = set()
        number_of_synonyms = 0
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                lemma_name = lemma.name() 
                if  lemma_name != word and word not in lemma_name and lemma_name not in word:
                    synonyms.add(lemma.name())  # Add synonym to set
                    number_of_synonyms += 1
                if number_of_synonyms == 2 :
                    break
            if number_of_synonyms == 2 :
                    break
        return list(synonyms)
    



class MysteryWord(TextProcessor):
    """
    Create word object with som properies and functions
    """
    def __init__(self, word, pos_tag):
        self.word = word
        self.length = len(word)
        self.start_with = word[0]
        self.pos_tag = pos_tag
        self.synonyms = self.get_synonyms(word)
    
    
    def describe(self):
        print(f" This word is {self.length} carachter(s) long, starts with {self.start_with}")
        print(f" POS_TAG for this word is: {self.pos_tag}")
        print(f" Synonyms for this word are: {self.synonyms}")



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
        phrase_without_punctuation, word_list = self.get_words(self.phrase)
        #get all pos tags for each words
        self.pos_tags = self.get_pos_tag(phrase_without_punctuation)
        #generate defined word object list
        self.words = [MysteryWord(word, self.pos_tags[word]) for word in word_list]


    
    def describe(self):
        print(f"   The generated phrase contains {len(self.words)} words.")



def main():
    """
    Create phrase and call the procedures so that the game can begin.
    """
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("   Welcome to Mystery Phrase ^_^ ")
    print("   We will see your ability to discover the hidden words!\n")
    mystery_phrase = MysteryPhrase()
    print("   The phrase has been generated for you.")
    mystery_phrase.describe()
    print("   Let's go..... \n")
    print("   defining words\n")
    mystery_phrase.define_words()
    for w in mystery_phrase.words:
        w.describe()
        print("..........................................\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(mystery_phrase.phrase)


main()