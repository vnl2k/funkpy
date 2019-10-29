## Installation

These are the libraries required by the package:
```
funkpy
Jinja2
MarkupSafe
nltk
six
```
The code was tested with Python 3.6 and requires at least version 3.5.

Installation using pip3:
```bash
pip3 install -r /path/to/requirements.txt
```

Run this command prior to running the main script:
```bash
python3 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```
NLTK has to download locally datasets which are not apart of the standard installation. For more information see [here](http://www.nltk.org/api/nltk.tokenize.html#module-nltk.tokenize.punkt).

# Running the code
The main code in _main.py_ requires three variables to run properly, i.e. `PATH_TO_DOCS`, `DOCUMENTS` and `SORT_BY`. They are defined in __init__.py. `PATH_TO_DOCS` tells he script where the documents to process are located and `DOCUMENTS` is a list with the names of the files (excluding file extensions). `SORT_BY` determines how the final results are ordered and the possible values are `'alphabetical'` and `'word-count'`. The default value is `word-count` which returns the most common words first.

Execute the code:
```bash
python3 main.py
```

The output is a file called `answer.html` which can be opened with any browser. The final result contains ALL the words in the documents. 

# Known issues
1. In some cases, highlighting words in sentences results in highlighting entire sentences instead of just the word itself, e.g. _comes_ will be highlighted when _come_ is selected.
