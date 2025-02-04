from wonderwords import RandomSentence


class MysteryPhrase:
    """
    Create a random phrase and define the properties of the words it contains,
    then establish a set of procedures to handle them."
    """
    def __init__(self):
        s = RandomSentence()
        # Get a random sentence with a subject, predicate, direct object and adjective
        self.phrase = s.sentence()



def main():
    """
    Create phrase and call the procedures so that the game can begin.
    """
    print("Welcome to phrase chalnge")
    mystery_phrase = MysteryPhrase()
    print(mystery_phrase.phrase)


main()