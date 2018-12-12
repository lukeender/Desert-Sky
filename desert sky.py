import requests
from bs4 import BeautifulSoup
import genanki #from https://github.com/kerrickstaley/genanki
import random


toplevelurl = 'http://arabic.desert-sky.net/'


def makeModel(anki_ID, css = 'font-size:x-large;'):
    DSKY_model = genanki.Model(
    anki_ID,
    'Desert Sky',
    fields=[
        {'name': 'English'},
        {'name': 'MSA'},
        {'name': 'MSA_transl'},
        {'name': 'EGA'},
        {'name': 'EGA_transl'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{English}}',
        'afmt': '{{FrontSide}}<hr id="answer">MSA: {{MSA}}, {{MSA_transl}} EGA: {{EGA}}, {{EGA_transl}}',
        },
    ])
    return(DSKY_model)

def getsoup(pageurl): 
    page = requests.get(pageurl)
    soup = BeautifulSoup(page.content,'html.parser')
    return(soup)
                #Returns a bs4 "soup" object of the page
                #given in pageurl
def geturls():
    listpage = 'vocab.html'
    soup = getsoup(toplevelurl + listpage)
    url_table = soup.find('table')
    rows = url_table.find_all('tr')
    urls = [row.find('a',href = True) for row in rows]
    urls = [url['href'] for url in urls]
    return(urls)
                #Scans for a "table" html object
                #and returns a list of all the href
                #links

def gettable(url):
    soup = getsoup(toplevelurl + url)
    vocab_table = soup.find('table',attrs={'class':'vocab'})
    vocab_rows = vocab_table.find_all('tr')
    array = []
    for row in vocab_rows:
        cols = row.find_all('td')
        cols = [elm.text.strip() for elm in cols]
        array.append(cols)
    return(array[1:])
                #Returns any "table" html object
                #found with class "vocab" and 
                #returns it as a MxN list, where
                #M is the number of rows and N 
                #the number of columns

def createdeck(array,anki_ID,title):
    notes = [genanki.Note(model=makeModel(anki_ID), fields=row) for row in array]
    deck = genanki.Deck(anki_ID,'Dark Sky ' + title[:-5])
    for note in notes:
        deck.add_note(note)
    return(deck)
                #Makes a "note" object for each 
                #row of array passed in (representing
                # one word), adds each to a "deck",
                #and returns the deck

def createIDs(array):
    IDs = []
    for element in array:
        IDs.append(random.randrange(1 << 30, 1 << 31))
    return(IDs)
                #Creates a list of anki IDs having
                #the same length as the list of urls
                #to scan (and thus one per deck)

urls = geturls()
tables  = [gettable(url) for url in urls]
IDs = createIDs(urls)
decks = [createdeck(table,ID,url) for table,ID,url in zip(tables,IDs,urls)]
for deck,title in zip(decks,urls):
    genanki.Package(deck).write_to_file(title[:-5] + '.apkg')