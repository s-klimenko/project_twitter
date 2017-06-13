from pymystem3 import Mystem  # импортируем майстем
from collections import Counter
import re
import string

def word_counter(text):
    '''
    Считаем слова
    :param text:
    :return:
    '''
    text = text.split()
    text = text.strip(string.punctuation)
    text = [i for i in text if i != '']
    return(len(text))

def pos_counter(text):
    '''
    Считаем части речи
    :param text: текст
    :return: словари с частотностью
    '''
    m = Mystem()  # создаем экземпляр класса-анализатора
    ana = m.analyze(text)
    pos = [i['analysis'][0]['gr'].split('=')[0].split(',')[0] for i in ana if
           i['text'].strip() and 'analysis' in i and i['analysis']]
    c_pos = Counter(pos)
    return c_pos

def punct_counter(text):
    punct = re.findall('[!?]', text)
    c_punct = (Counter(punct))
    return c_punct

def emoji_counter(text):
    '''
    Считаю емодзи
    :param emoji:
    :return:
    '''
    with open ('em_neg.txt', 'r') as em_neg:
        neg_emoji = [line.strip() for line in em_neg]
        ne = '[' + '|'.join(neg_emoji) + ']'
    emoji_n = re.findall(ne, text)
    c_neg_em = {'neg_em': sum(Counter(emoji_n).values())}
    with open('em_neg.txt', 'r') as em_pos:
        pos_emoji = [line.strip() for line in em_pos]
        pe = '[' + '|'.join(pos_emoji) + ']'
    emoji_p = re.findall(pe, text)
    c_pos_em = {'pos_em': sum(Counter(emoji_p).values())}
    return c_neg_em, c_pos_em

def smile_counter(text):
    '''
    Считает смайлики
    :param smiles:
    :return:
    '''
    sm_n = re.findall(r'(:\(|;\(||=\(|:-\()', text)
    c_neg_smiles = {'neg_sm' : sum(Counter(sm_n).values())}
    sm_p =  re.findall(r'(:\)|:D|: @|;\)|:-\)|=\)|:\*|:3)')
    c_pos_smiles = {'pos_sm' : sum(Counter(sm_p).values())}
    return c_neg_smiles, c_pos_smiles

