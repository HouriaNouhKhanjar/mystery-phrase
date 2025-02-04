from wonderwords import RandomSentence
import re


class TextProcessor:
    """
    Creating Assistant Procedures for Analyzing Phrases and Words
    """
    def get_words(self):
        """
        Return the set of words contained in the sentence without punctuation marks.
        """
        phrase_without_punctuation = re.sub(r'[^\w\s]', '', self.phrase)
        return phrase_without_punctuation.split()



class MysteryPhrase(TextProcessor):
    """
    Create a random phrase and define the properties of the words it contains,
    then establish a set of procedures to handle them."
    """
    def __init__(self):
        s = RandomSentence()
        # Get a random sentence with a subject, predicate, direct object and adjective
        self.phrase = s.sentence()
    
    def descripe(self):
        print(f"   The generated phrase contains {len(self.get_words())} words.")



def main():
    """
    Create phrase and call the procedures so that the game can begin.
    """
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("   Welcome to Mystery Phrase ^_^ ")
    print("   We will see your ability to discover the hidden words!\n")
    mystery_phrase = MysteryPhrase()
    print("   The phrase has been generated for you.")
    mystery_phrase.descripe()
    print("   Let's go..... \n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(mystery_phrase.phrase)
    print(mystery_phrase.get_words())


main()