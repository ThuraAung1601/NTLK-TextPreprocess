"""
Lemmatizating essay text file
Version 3
Nouns and adjective included 
input => input.txt
output => output_ver3.txt 
"""
contractions_dict = {     
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I had",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"isn't": "is not",
"it'd": "it had",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "iit will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that had",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there had",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they had",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have",
"Ain't": "am not",
"Aren't": "are not",
"Can't": "cannot",
"Can't've": "cannot have",
"'Cause": "because",
"Could've": "could have",
"Couldn't": "could not",
"Couldn't've": "could not have",
"Didn't": "did not",
"Doesn't": "does not",
"Don't": "do not",
"Hadn't": "had not",
"Hadn't've": "had not have",
"Hasn't": "has not",
"Haven't": "have not",
"He'd": "he had",
"He'd've": "he would have",
"He'll": "he will",
"He'll've": "he will have",
"He's": "he is",
"How'd": "how did",
"How'd'y": "how do you",
"How'll": "how will",
"How's": "how is",
"Isn't": "is not",
"It'd": "it had",
"It'd've": "it would have",
"It'll": "it will",
"It'll've": "iit will have",
"It's": "it is",
"Let's": "let us",
"Ma'am": "madam",
"Mayn't": "may not",
"Might've": "might have",
"Mightn't": "might not",
"Mightn't've": "might not have",
"Must've": "must have",
"Mustn't": "must not",
"Mustn't've": "must not have",
"Needn't": "need not",
"Needn't've": "need not have",
"Oughtn't": "ought not",
"Oughtn't've": "ought not have",
"Shan't": "shall not",
"Sha'n't": "shall not",
"Shan't've": "shall not have",
"She'd": "she had",
"She'd've": "she would have",
"She'll": "she will",
"She'll've": "she will have",
"She's": "she is",
"Should've": "should have",
"Shouldn't": "should not",
"Shouldn't've": "should not have",
"So've": "so have",
"So's": "so is",
"That'd": "that had",
"That'd've": "that would have",
"That's": "that is",
"There'd": "there had",
"There'd've": "there would have",
"There's": "there is",
"They'd": "they had",
"They'd've": "they would have",
"They'll": "they will",
"They'll've": "they will have",
"They're": "they are",
"They've": "they have",
"To've": "to have",
"Wasn't": "was not",
"We'd": "we had",
"We'd've": "we would have",
"We'll": "we will",
"We'll've": "we will have",
"We're": "we are",
"We've": "we have",
"Weren't": "were not",
"What'll": "what will",
"What'll've": "what will have",
"What're": "what are",
"What's": "what is",
"What've": "what have",
"When's": "when is",
"When've": "when have",
"Where'd": "where did",
"Where's": "where is",
"Where've": "where have",
"Who'll": "who will",
"Who'll've": "who will have",
"Who's": "who is",
"Who've": "who have",
"Why's": "why is",
"Why've": "why have",
"Will've": "will have",
"Won't": "will not",
"Won't've": "will not have",
"Would've": "would have",
"Wouldn't": "would not",
"Wouldn't've": "would not have",
"Y'all": "you all",
"Y'all'd": "you all would",
"Y'all'd've": "you all would have",
"Y'all're": "you all are",
"Y'all've": "you all have",
"You'd": "you had",
"You'd've": "you would have",
"You'll": "you will",
"You'll've": "you will have",
"You're": "you are",
"You've": "you have"
}
from nltk.corpus import wordnet as wn

# Just to make it a bit more readable
WN_NOUN = 'n'
WN_VERB = 'v'
WN_ADJECTIVE = 'a'
WN_ADJECTIVE_SATELLITE = 's'
WN_ADVERB = 'r'


def convert(word, from_pos, to_pos):    
    """ Transform words given from/to POS tags """

    synsets = wn.synsets(word, pos=from_pos)

    # Word not found
    if not synsets:
        return []

    # Get all lemmas of the word (consider 'a'and 's' equivalent)
    lemmas = []
    for s in synsets:
        for l in s.lemmas():
            if s.name().split('.')[1] == from_pos or from_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and s.name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                lemmas += [l]

    # Get related forms
    derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]

    # filter only the desired pos (consider 'a' and 's' equivalent)
    related_noun_lemmas = []

    for drf in derivationally_related_forms:
        for l in drf[1]:
            if l.synset().name().split('.')[1] == to_pos or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and l.synset().name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                related_noun_lemmas += [l]

    # Extract the words from the lemmas
    words = [l.name() for l in related_noun_lemmas]
    len_words = len(words)

    # Build the result in the form of a list containing tuples (word, probability)
    result = [(w, float(words.count(w)) / len_words) for w in set(words)]
    result.sort(key=lambda w:-w[1])

    # return all the possibilities sorted by probability
    return result
import string
import re
import nltk
from string import punctuation
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

lemmatizer = WordNetLemmatizer()


input_file = "text-files\input.txt"

def read_input(input_file):
    with open (input_file,"r+", encoding="utf-8") as fin:
        return fin.read()

get_text = read_input(input_file)
#print(get_text)
#print("\n")

get_text = get_text.split(" ")
if len(get_text) > 200:
    start = (len(get_text)-200)//2
    end = len(get_text) - start
    #print(start)
    #print(end)
    middle = get_text[start:end]

else:
    middle = get_text

text_list = middle
#print(text_list)
text = " "
text = text.join(text_list)

def expand_contractions(text, contractions_dict):
    contractions_pattern = re.compile('({})'.format('|'.join(contractions_dict.keys())),
                                      flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contractions_dict.get(match) \
            if contractions_dict.get(match) \
            else contractions_dict.get(match.lower())
        expanded_contraction = expanded_contraction
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

text = expand_contractions(text,contractions_dict)
#print(text)
#print("\n")

def remove_punct(text):
    """
    take string input and clean string without punctuations.
    use regex to remove the punctuations.
    """
    return ''.join(c for c in text if c not in punctuation)

text = remove_punct(text)
#print(text)
#print("\n")

lemmatizer = WordNetLemmatizer()

# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    elif nltk_tag.startswith('NP'):
        return None
    else:          
        return None

def lemmatize_sentence(sentence):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        word1 = word
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            if tag == wordnet.NOUN: 
                word_dict = dict(convert(word1,"n","v"))
                newlist = list()
                for i in word_dict.keys():
                    newlist.append(i)
                if newlist == []:
                    word1 = word
                else :
                    word1 = newlist[0]
                tag = wordnet.VERB
            elif tag == wordnet.ADJ:
                word1 = lemmatizer.lemmatize(word1,"a")
            lemmatized_sentence.append(lemmatizer.lemmatize(word1, tag))
    return " ".join(lemmatized_sentence)

lemm = lemmatize_sentence(text)
#print(lemm)

with open('text-files\output_ver3.txt', 'w') as f:
    for item in lemm:
        f.write("%s" % item)