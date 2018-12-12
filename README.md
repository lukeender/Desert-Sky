# Desert-Sky
This is a simple program I wrote using BeautifulSoup and genanki libraries in Python to create Anki flashcard decks from the vocabulary lists on http://arabic.desert-sky.net/vocab.html
Big thanks to github user kerrickstaley for creating ankigen, which makes this project possible. https://github.com/kerrickstaley/genanki

I created this project due to personal desire to have the Egyptian Arabic vocabularly lists provided at http://arabic.desert-sky.net/ as [Anki](https://apps.ankiweb.net/) decks to assist in learing the language.
The program scans all the links provided at the /vocab.html page and adds their contents to individual Anki decks.

## Known bugs
As it currently stands, the program cannot handle the entries which include only MSA entries (and hence have only 3 entries rather than 5) causing errors in some decks. Additionally, words with more than one entries are clipped to only one. I plan to fix these errors as I find time.
