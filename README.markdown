# `tarot-doc` - Documentation for The Tarot

The `tarot-doc` package is an (aspirational) Debian package that provides information about the Tarot and various Tarot decks as `man(1)`-formatted documentation.

Currently, this repository houses [utilities](utils/) and source files from which to manifest the desired output. However, that desired output is not entirely certain. :)

## Developing

In this repository you will find a [`src`](src/) directory. This directory holds more contemporary versions of source material that is later used, through various incantations, for manifesting the ultimately desired output. In this way, human editors can more easily contribute to and read the source material itself. We use [`md2man`](https://github.com/sunaku/md2man) for the translation between contemporary human scripts and the arcane syntaxes of various UNIX-like manual page formats.

### Prerequisites

First, ensure you have installed the following, in the following order:

* [Git](https://git-scm.com/)
    * Test this by asking your system to report its Git version number: `git --version`
* [Ruby](https://www.ruby-lang.org/) (version 2.0 or later is recommended)
    * Test this by asking your system to report its Ruby version number: `ruby --version`
* [Bundler](https://bundler.io/)
    * Test this by asking your system to report its Bundler versio number: `bundler --version`

### Set up

Once the prerequisites are installed, clone the repository from GitHub (or a mirror), and then use `bundler` to install the development dependencies. An example installation, with output, is shown below:

```sh
$ cd tarot-doc                         # Change to the tarot-doc folder.
$ bundle install --path vendor/bundle  # Install the listed dependencies.
Fetching gem metadata from https://rubygems.org/...
Fetching version metadata from https://rubygems.org/.
Resolving dependencies...
Rubygems 2.0.14 is not threadsafe, so your gems will be installed one at a time. Upgrade to Rubygems 2.1.0 or higher to enable parallel gem installation.
Installing opener 0.1.0
Installing redcarpet 3.4.0 with native extensions
Installing rouge 1.11.1
Using bundler 1.14.2
Installing binman 5.1.0
Installing md2man 5.1.1
Bundle complete! 1 Gemfile dependency, 6 gems now installed.
Bundled gems are installed into ./vendor/bundle.
```

Once installed, you can generate individual manual pages from the files in the `src` directory and view them in your manual page viewer as follows:

```sh
$ ./utils/build.sh --force-clean # Use the build script to clean and regenerate the docs.
$ man ./build/the-fool.7         # View generated documentation with the man page viewer.
```
