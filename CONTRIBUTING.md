This document describes best practices and suggestions for new contributors to `tarot-doc`. While these are not strict rules, we appreciate consistency and find that appropriate conventions aid in making sense of the world. If your contributions are initially rejected, please consider whether you can accomplish your goal while more closely adhering to these guidelines.

# Writing conventions

We borrow heavily from the [GNU/Linux `man-pages(7)` project](http://man7.org/linux/man-pages/man7/man-pages.7.html), but at times also use BSD-style manual page conventions when appropriate. Unless otherwise noted here, consider the `man-pages(7)` documentation to be an authoritative source of suggested conventions to use when writing `tarot-doc` manual pages.

# Manual page sections

The following manual page sections are *required*:

* [`NAME`](#name)
* [`SYNOPSIS`](#synopsis)
* [`DESCRIPTION`](#description)
* [`IN A READING`](#in-a-reading)
* [`AUTHORS`](#authors)

In addition to the above, the following manual page sections are *optional*, but recommended:

* [`ENVIRONMENT`](#environment)
* [`SEE ALSO`](#see-also)
* [`NOTES`](#notes)

If present, these sections should be written in the following order:

1. `NAME`
1. `SYNOPSIS`
1. `DESCRIPTION`
1. `IN A READING`
1. `ENVIRONMENT`
1. `NOTES`
1. `SEE ALSO`
1. `AUTHORS`

## `NAME`

This section should include the name of the card and a single sentence alternative name useful for identifying it, set apart from the name with a single dash surrounded by single spaces. For example:

```markdown
## NAME

Three of Cups - Tarot card with numeric value 3 and suit of Cups.
```

## `SYNOPSIS`

This section should provide a brief (one or two sentence) description of the most important elements of the card. For example:

```markdown
## SYNOPSIS

Friends gather with a sense of belonging, togetherness, and solidarity.
```

## `DESCRIPTION`

This section should go into greater detail about the card and may include any information you feel is appropriate to convey the card's meaning. Include textual descriptions of common visual depictions, elaborations on the history or storytelling attributes of its meaning, and so on.

## `IN A READING`

This section should offer guidance to a querent who is faced with the card in a specific reading. As such, this section should be explicit about the context in which the card was drawn; many cards may mean different things or have subtle differences in their connotation when the query is a divinatory one versus a meditative one.

## `ENVIRONMENT`

This section should describe the card in relation to its environment; other cards in the spread (reinforcing or opposing cards, for instance), position in the spread, further details about the card's relationship to the query or the querent, and so on.

## `NOTES`

This section should provide additional, related information to the card's meaning. This additional information need not be directly related to The Tarot, tarotology, or cartomancy. This section may also include references in the form of hyperlinks to other resources that may help the querent contextualize their reading by using supplementary tools beyond those contained within The Tarot.

## `SEE ALSO`

This section should provide direct references to other important manual pages that offer additional context as a comma-separated list. For example:

```markdown
## SEE ALSO

the-world(7), king-of-cups(7).
```

## `AUTHORS`

This section should include the names, pseudonyms, or credits of the authors of the manual page itself.
