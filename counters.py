import Counter
import Mystem
import re

def verbs_statistics(text):
    '''
    Выделяет из текста данные о частотности глаголов, их лемм, вида и совершенности
    :param text: текст
    :return: словари с частотностью
    '''
    m = Mystem()  # создаем экземпляр класса-анализатора
    ana = m.analyze(text)
    pos = [i['analysis'][0]['gr'].split('=')[0].split(',')[0] for i in ana if
           i['text'].strip() and 'analysis' in i and i['analysis']]

def pos_counter(pos):
    '''
    Считает части речи, глаголы и долю глаголов в тексте.
    :param pos: список с частеречными тегами Mystem для всех слов в тексте
    :type pos: list
    :return: all_pos - количество всех частей речи (слов) в тексте
             v - количество глаголов в тексте
             ratio - доля глаголов в тексте
    '''
    c_pos = Counter(pos)
    return c_pos

def punct_counter(text):
    punct = ['!', '?']
    c_punc = re.findall('[!?]')

def emoji_pos_counter:


def emoji_neg_counter:

def smile_pos_counter:
    pos_smiles =  (':)', ':D',': @', ';)' ':-)', '=)', ':*', ':3')

def smile_neg_counter:
    neg_smiles = (':(', ';(', ': @', '=(', ':-(')