from wonderwords import RandomSentence
import re


class TextProcessor:
    """
    Creating Assistant Procedures for Analyzing Phrases and Words
    """

    def get_words(self, phrase):
        """
        Return the set of words contained in the sentence without punctuation marks.
        """
        phrase_without_punctuation = re.sub(r'[^\w\s]', '', phrase)
        return phrase_without_punctuation.split()
    



class MysteryWord(TextProcessor):
    """
    Create word object with som properies and functions
    """
    def __init__(self, word):
        self.word = word
        self.length = len(word)
        self.start_with = word[0]
    
    def describe(self):
        print(f" This word is {self.length} carachter(s) long, starts with {self.start_with}\n")



class MysteryPhrase(TextProcessor):
    """
    Create a random phrase and define the properties of the words it contains,
    then establish a set of procedures to handle them."
    """
    def __init__(self):
        s = RandomSentence()
        # Get a random sentence with a subject, predicate, direct object and adjective
        self.phrase = s.sentence()
        self.words = []
    
    def define_words(self):
        #get all words from the phrase without ponctuations
        word_list = self.get_words(self.phrase)
        #generate defined word object list
        self.words = [MysteryWord(word) for word in word_list]


    
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