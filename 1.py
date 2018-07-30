# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:58:16 2018

@author: JQ
"""

from data import data
from lexicon import Lexicon
from embedding_weights import Embedding_weights
lexicon,lexicon_reverse,lexicon_len=Lexicon(corpus_path)
train_data,val_data,train_label,val_label=data('corpus')
print(val_label.shape)
embedding_weights=Embedding_weights('corpus')

print(embedding_weights.shape)


from lexicon import Lexicon
lexicon,lexicon_reverse,lexicon_len=Lexicon('corpus')
print(lexicon_len)


import numpy as np
a=np.random.randint(1,2,size=(3,4))
b=a.shape
print('xingzhuang:',a)

a='jsjhhjdsj , .'
print(a.split())