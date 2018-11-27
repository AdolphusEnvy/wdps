'''
A sample code usage of the python package stanfordcorenlp to access a Stanford CoreNLP server.
Written as part of the blog post: https://www.khalidalnajjar.com/how-to-setup-and-use-stanford-corenlp-server-with-python/
'''

from stanfordcorenlp import StanfordCoreNLP
import logging
import json

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

if __name__ == '__main__':
    sNLP = StanfordNLP()
    text = 'A blog post using Stanford CoreNLP Server. Visit www.khalidalnajjar.com for more details.'
    test='''
Necole Bitchie: Page 1

Inappropriate? Coco Tweets Photo Of Herself Naked In Bed With Her Nephew
[Video] Whitney Houston Steps Out, Sings ‘Jesus Loves Me’ To Kelly...
Nicki Minaj Reveals Style Icons, Love For ‘Big Ang’ & New...
[Video] Brandy & Monica Rehearse For Special Pre-Grammy Night Performance
Who Owned The Look? Serena Williams vs. Angela Simmons In Giuseppe Zanotti Body...
Kobe Laughs While Fans Scream ‘She Wasn’t With You Shooting In The...
New Video: Jay-Z & Kanye West – “Ni**as In Paris”
EVE, Michelle Williams, Letoya Luckett, Dawn Richard & More Attend Essence...
Jen Gets Smacked Hard In Basketball Wives 4 Trailer
Lala Anthony Covers YRB:  Talks ‘Basketball Wife’ Label &...



Necole Bitchie: Page 2

Terrence J Tweets About Career, Selita & Connects: ‘I Can’t...
New Video: Raz B – “Na Na Na”
Ne-Yo and His Fiancee Make It Rain In A Strip Club
Khloe Kardashian Pictured With Her Real Father
Bitchie Or Not? Erykah Badu’s DSquared2 Ice Skate Boots
NY Giants Victor Cruz and Ashanti Get It In On The Dance Floor
Mob Wives Star Big Ang Hits The Streets [And Yes, She's All Woman -- Proof]
Solange Knowles Steps Out In Vera Wang For Runway To Win Party
Kelly Rowland Shows Off Her Boobies & Talks About Her ‘Good...
Beyonce Steps Out In Sexy Black Dress For 2nd Post-Baby Night Out



Necole Bitchie: Page 3

Chris Brown & Rihanna To Perform At The Grammys
New Video: Somaya Reece – “Classy Girl”
Meagan Good Covers Vibe Vixen: Talks Crazy Love, Gabrielle Union & Women...
Emily & Fabolous: ‘Don’t Sleep On Us’
[Video & Pics] Jay-z Performs At Carnegie Hall In NY With Special Guests...
Bitchie Or Not? Jessica White Steps Out In A Sheer Lace Jumpsuit @ Carnegie
Beyonce Steps Out In Red For The First Time Since Giving Birth
New Music: Monica & Brandy – ‘It All Belongs To Me’
Amar’e Stoudemire’s Brother Dies in Crash
    '''
    #print("Annotate:", sNLP.annotate(test))
    #print("POS:", sNLP.pos(text))
    #print("Tokens:", sNLP.word_tokenize(text))
    #print ("NER:", sNLP.ner(test))
    #print ("Parse:", sNLP.parse(text))
    #print ("Dep Parse:", sNLP.dependency_parse(text))