# `tarot-doc` Utilities

This folder contains utilities intended to ease development of the Tarot documentation. It is not intended to ultimately ship with the final Debian package.

## `learn-tarot.py`

A bootstrapping script called [`learn-tarot.py`](learn-tarot.py) is provided here that writes an initial `mdoc(7)`-style manual page for each individual card in the Tarot. The script "learns" about the Tarot by scraping the [LearnTarot.com](http://learntarot.com/) website.

To use the script for development purposes, first change to the root directory of this repository and then perform the following invocations:

```sh
virtualenv dev                        # Create a virtual environment called dev(elopment).
source dev/bin/activate               # Activate the virtual environment.
pip install -r utils/requirements.txt # Install the requirements.
./utils/learn-tarot.py                # Invoke the magic inscription!
```

The result should be a filesystem `tree(1)` with the following contents:

```sh
tarot-doc maymay$ tree -I dev
.
├── README.markdown
├── ace-of-cups.7
├── ace-of-pentacles.7
├── ace-of-swords.7
├── ace-of-wands.7
├── death.7
├── eight-of-cups.7
├── eight-of-pentacles.7
├── eight-of-swords.7
├── eight-of-wands.7
├── five-of-cups.7
├── five-of-pentacles.7
├── five-of-swords.7
├── five-of-wands.7
├── four-of-cups.7
├── four-of-pentacles.7
├── four-of-swords.7
├── four-of-wands.7
├── judgement.7
├── justice.7
├── king-of-cups.7
├── king-of-pentacles.7
├── king-of-swords.7
├── king-of-wands.7
├── knight-of-cups.7
├── knight-of-pentacles.7
├── knight-of-swords.7
├── knight-of-wands.7
├── nine-of-cups.7
├── nine-of-pentacles.7
├── nine-of-swords.7
├── nine-of-wands.7
├── page-of-cups.7
├── page-of-pentacles.7
├── page-of-swords.7
├── page-of-wands.7
├── queen-of-cups.7
├── queen-of-pentacles.7
├── queen-of-swords.7
├── queen-of-wands.7
├── seven-of-cups.7
├── seven-of-pentacles.7
├── seven-of-swords.7
├── seven-of-wands.7
├── six-of-cups.7
├── six-of-pentacles.7
├── six-of-swords.7
├── six-of-wands.7
├── strength.7
├── temperance.7
├── ten-of-cups.7
├── ten-of-pentacles.7
├── ten-of-swords.7
├── ten-of-wands.7
├── the-chariot.7
├── the-devil.7
├── the-emperor.7
├── the-empress.7
├── the-fool.7
├── the-hanged-man.7
├── the-hermit.7
├── the-hierophant.7
├── the-high-priestess.7
├── the-lovers.7
├── the-magician.7
├── the-star.7
├── the-tower.7
├── the-world.7
├── three-of-cups.7
├── three-of-pentacles.7
├── three-of-swords.7
├── three-of-wands.7
├── two-of-cups.7
├── two-of-pentacles.7
├── two-of-swords.7
├── two-of-wands.7
├── utils
│   ├── README.md
│   ├── learn-tarot.py
│   └── requirements.txt
└── wheel-of-fortune.7

1 directory, 80 files
```

From this point, you can use `man ./seven-of-wands.7` to view the basic information for the Seven of Wands. When you're done developing, say `deactivate` to your shell to leave the virtual environment.
