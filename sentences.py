import random

def main():
    print(get_determiner(1).title(), get_noun(1), get_verb(1,"past") + '.')
    print(get_determiner(2).title(), get_noun(2), get_verb(1,"past") + '.')
    print(get_determiner(1).title(), get_noun(1), get_verb(1,"present")+ '.')
    print(get_determiner(2).title(), get_noun(2), get_verb(2,"present")+'.')
    print(get_determiner(1).title(), get_noun(1), get_verb(1,"future")+ '.')
    print(get_determiner(2).title(), get_noun(2), get_verb(1,"future")+ '.')
    print(get_determiner(1).title(), get_noun(1), get_verb(1,"past"), get_prepositional_phrase(1)+'.')
    print(get_determiner(2).title(), get_noun(2), get_verb(1,"past"),  get_prepositional_phrase(2)+'.')
    print(get_determiner(1).title(), get_noun(1), get_verb(1,"present"), get_prepositional_phrase(1)+'.')
    print(get_determiner(2).title(), get_noun(2), get_verb(2,"present"), get_prepositional_phrase(2)+'.')
    print(get_determiner(1).title(), get_noun(1), get_verb(1,"future"), get_prepositional_phrase(1)+'.')
    print(get_determiner(2).title(), get_noun(2), get_verb(1,"future"), get_prepositional_phrase(2)+'.')

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    # Randomly choose and return a determiner.
    noun = random.choice(words)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if quantity == 1 and tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity == 2 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif quantity == 1 and tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]    

    # Randomly choose and return a determiner.
    verb = random.choice(words)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(words)
    return preposition    

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        prepositional_phrase = get_preposition() + " " + get_determiner(1)+ " "+ get_noun(1)
    else:
        prepositional_phrase = get_preposition()+ " " + get_determiner(2)+ " " + get_noun(2)

    return prepositional_phrase                

main()