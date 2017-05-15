#!/usr/bin/env python
"""
Create a manual page for each Tarot card from LearnTarot.com.

"Learn" the Tarot by scraping the LearnTarot.com website and writing
``mandoc``-formatted pages for each of the individual Tarot cards.
"""

import requests, re, datetime
from bs4 import BeautifulSoup

class TarotCard:
    """
    An individual card in the Tarot deck.
    """

    name   = None # The name of the card.
    suit   = None # The suit of the card, if it's a minor Arcana.
    number = None # Numerical value of the card.
    keywords = [] # A few words that this card evokes.
    examples = [] # A list of phrases evoking this card.
    description = None # A textual description of the card.

    def toManDocFile(self, style='mdoc'):
        """
        Writes out a mandoc formatted file of itself.

        The name of the file will be a slugified version of the card
        name with an extension of ``.7``.

        Args:
            style (string): The style of ``man`` formating. Default is ``mdoc``.
        """

        # Construct a filename based on the card name.
        filename = self.name.lower().replace(' ', '-') + '.7' # Always section 7.

        # Open the file for writing.
        f = open(filename, 'w')

        # Write the mdoc-style header.
        now = datetime.datetime.now()
        f.write('.\" Automatically generated using the learn-tarot.py utility.' + "\n")
        f.write(".Dd {} {}, {}\n".format(
            now.strftime('%B'), now.day, now.year))
        f.write(".Os\n")

        # Write the card-specific documentation.
        f.write(".Dt \"{}\" 7\n".format(self.name))
        f.write(".Sh NAME\n")
        f.write(".Nm {}\n".format(self.name))
        f.write('.Nd Tarot card with numeric value {}'.format(self.number))
        if self.suit is not None:
            f.write(' and suit of {}'.format(self.suit))
        f.write(".\n")
        f.write(".Sh SYNOPSIS\n")
        f.write(', '.join(self.keywords) + ".\n")
        f.write(".Sh DESCRIPTION\n")
        f.write(self.description + "\n")

        # Close the opened file.
        f.close()

class LearnTarotCardPage:
    """
    A Tarot card page scraped from the LearnTarot.com website.
    """

    card = None
    html = None

    def __init__(self, url):
        """
        Constructor.

        Args:
            url (string): The Web address as a URL of the Tarot card.
        """
        self.url = url

    def toManDocFile(self):
        """
        Converts the (expected) Tarot HTML into a ``ManDoc``-formatted file.
        """
        if self.card is None:
            self.getCardFromURL(self.url)

        self.card.toManDocFile()

    def getCardFromURL(self, url):
        """
        Makes a Web (HTTP) request to download a given Tarot card page.

        Once downloaded, the HTML is parsed and a ``TarotCard`` object
        is constructed from the parsed data.

        Args:
            url (string): The Web address as a URL of the Tarot card.
        """
        r = requests.get(url)
        self.html = r.text
        card = TarotCard()
        soup = BeautifulSoup(self.html, 'html.parser')

        # Cleanup as much as possible.
        soup = BeautifulSoup(soup.prettify(), 'html.parser')

        card.name = soup.title.string.title().strip()

        base_len = len(url_base)
        if url.startswith('maj', base_len):
            # A major arcana card.
            card.number = int(url[base_len+3:base_len+3+2])
        else:
            # A minor arcana card.
            if url.startswith('w', base_len):
                card.suit = 'Wands'
            elif url.startswith('c', base_len):
                card.suit = 'Cups'
            elif url.startswith('s', base_len):
                card.suit = 'Swords'
            elif url.startswith('p', base_len):
                card.suit = 'Pentacles'

            number = url[base_len+1:base_len+1+2]
            if number == 'a.':
                card.number = 1 # an Ace is a 1, basically
            elif number == 'pg':
                card.number = 11 # a Page is an 11, basically
            elif number == 'kn':
                card.number = 12 # a Knight is a 12, basically
            elif number == 'qn':
                card.number = 13 # a Queen is a 13, basically
            elif number == 'kg':
                card.number = 14 # a King is a 14, basically
            else:
                card.number = int(number[0:1])

        # Extract the "keywords" from the page source.
        card.keywords = [word.string.strip().title() for word in soup.find('ul').find_all('b')]

        # Parse the horrifically formed "Description" section.
        desc = soup.find('a', href=re.compile('howdesc')).find_next(
            'p').text.split('[ Home ]')[0].strip().replace("\n", '')
        desc = ' '.join(desc.split()).replace('[ note ]', '')
        card.description = desc

        self.card = card

# TODO: These globals are pretty ugly but...whatevers.
url_base = 'http://learntarot.com/' # Note trailing slash.
url_paths = [
    # Major Arcana paths.
    'maj00',
    'maj01',
    'maj02',
    'maj03',
    'maj04',
    'maj05',
    'maj06',
    'maj07',
    'maj08',
    'maj09',
    'maj10',
    'maj11',
    'maj12',
    'maj13',
    'maj14',
    'maj15',
    'maj16',
    'maj17',
    'maj20',
    'maj21',

    # Wands
    'wa',
    'w2',
    'w3',
    'w4',
    'w5',
    'w6',
    'w7',
    'w8',
    'w9',
    'w10',
    'wpg',
    'wkn',
    'wqn',
    'wkg',

    # Cups
    'ca',
    'c2',
    'c3',
    'c4',
    'c5',
    'c6',
    'c7',
    'c8',
    'c9',
    'c10',
    'cpg',
    'ckn',
    'cqn',
    'ckg',

    # Swords
    'sa',
    's2',
    's3',
    's4',
    's5',
    's6',
    's7',
    's8',
    's9',
    's10',
    'spg',
    'skn',
    'sqn',
    'skg',

    # Pentacles
    'pa',
    'p2',
    'p3',
    'p4',
    'p5',
    'p6',
    'p7',
    'p8',
    'p9',
    'p10',
    'ppg',
    'pkn',
    'pqn',
    'pkg',
]
url_ext = '.htm'

if __name__ == "__main__":
    for i in range(0, len(url_paths)):
        # Get the page's data.
        page = LearnTarotCardPage(url_base +  url_paths[i] + url_ext)

        # Tell the page to print a mandoc of itself.
        page.toManDocFile()
