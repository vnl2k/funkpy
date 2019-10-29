# standard python3 libraries
import os
import builtins 
from typing import Dict, List, Any
from uuid import uuid4 as uuid
import re

import nltk

# assumes `stopwords` dataset is available locally
from nltk.corpus import stopwords

# HTML templating library
from jinja2 import Environment, FileSystemLoader

# functional python3 library
from funkpy import Collection as _
from funkpy.utils import curry, compose

# path to the documents for the exercise
from __init__ import PATH_TO_DOCS, DOCUMENTS, SORT_BY

# dictionary of stopwords not covered by the standard NLTK stopwords
EXTRA_STOPWORDS = {
  '.': True, ',': True, "I": True, 
  '\'s': True, "n't": True, 
  ";": True, 'us': True, 'let': True, '-': True,
  "'ve": True, "'re": True, ":": True, '"': True,
  '?': True, "``": True, '--': True, 'ca': True,
  "$": True, "%": True, "'": True, '"': True, "'d": True,
  "'em": True, "'ll": True, '...': True, "'m": True,
  "!": True, ",": True, '“': True, '‘': True, '’': True, 
  '”': True, "''": True
}

# dictionary with stopwords from NLTK extended with EXTRA_STOPWORDS
STOPWORD_DICT = _.reduce(lambda a, i: a.update({i: True}) or a, stopwords.words('english'), EXTRA_STOPWORDS)

# global lookup for all words in the six documents
LOOKUP = {}

# global lookup mapping unique IDs to each sentence
SENTENCE_LOOKUP = {}

def updateLookup(doc_name: str, sentence_uuid: str, word: str):
  if word in LOOKUP:
    o = LOOKUP[word]
    o['cnt'] += 1
    
    o['dox'].add(doc_name)
    
    # words store reference to the sentence they came from in order to minimise the memory ussage by LOOKUP variable
    o['uuids'].append(sentence_uuid)

  else:
    LOOKUP.update({word.lower(): {'cnt': 1, 'dox': {doc_name}, 'uuids': [sentence_uuid]}})


def sentencePipe(doc_name: str, sentence: str):
  
  # generate unique ID for each sentence
  sentence_uuid = uuid().hex
  SENTENCE_LOOKUP.update({sentence_uuid: sentence})

  cUpdateLookup = curry(updateLookup)(doc_name, sentence_uuid)

  compose(
    curry(_.strictMap)(cUpdateLookup),
    curry(_.filter)(lambda i: STOPWORD_DICT.get(i.lower()) is not True),
    nltk.tokenize.word_tokenize
  )(sentence)

def readFile(file_name: str, doc_name: str) -> None:
  with open(file_name, 'r', encoding='utf-8', newline=os.linesep) as file:
    for paragraph in file:
      sentenceS = nltk.tokenize.sent_tokenize(paragraph)
      _.map(curry(sentencePipe)(doc_name), sentenceS)

for i in DOCUMENTS:
  readFile(PATH_TO_DOCS + i + '.txt', i)


def boldWord(text: str, word: str):
  pattern_before = ''.join([r'(?<=\W)', r'(?=', word, ')'])
  pattern_after = ''.join([r'(?<=', word, ')', r'(?=\W)'])

  return re.subn(
    pattern_after,
    '</b>',
    re.subn(pattern_before, '<b>', text, flags=re.IGNORECASE)[0],
    flags=re.IGNORECASE
  )[0]

if __name__ == '__main__':
  template = Environment(loader=FileSystemLoader('./')).get_template('html_template.html')


  items = []

  if SORT_BY == 'word-count':
    keys = sorted(LOOKUP.items(), key=lambda i: i[1]['cnt'], reverse=True)

  elif SORT_BY == 'aphabetical':
    keys = sorted(LOOKUP.items(), key=lambda i: i[0])

  for key, value in keys:
    items.append([key, ', '.join(sorted(value['dox'])), boldWord('<br>'.join(_.map(lambda i: SENTENCE_LOOKUP[i], value['uuids'])), key)])

  output = template.render(items=items)

  with open('answer.html', 'w', encoding='utf-8') as file:
    file.write(output)

  print('Done!')