#!/usr/bin/env python3

"""
Transliterador Harvard-Kyoto, IAST e Devanāgarī.
"""


def hkdv(entrada):

    '''
    :param entrada: str
    :return: str
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    i = -1
    # Dicionário de correspondências HK>>DV
    dict_unicode = {'M': '\u0902', 'H': '\u0903',
                    'a': '\u0905', 'A': '\u0906', 'i': '\u0907', 'I': '\u0908',
                    'u': '\u0909', 'U': '\u090A', 'R': '\u090B', 'RR': '\u0960', 'lR': '\u090C',
                    'e': '\u090F', 'ai': '\u0910', 'o': '\u0913', 'au': '\u0914',
                    'k': '\u0915', 'kh': '\u0916', 'g': '\u0917', 'gh': '\u0918', 'G': '\u0919',
                    'c': '\u091A', 'ch': '\u091B', 'j': '\u091C', 'jh': '\u091D', 'J': '\u091E',
                    'T': '\u091F', 'Th': '\u0920', 'D': '\u0921', 'Dh': '\u0922', 'N': '\u0923',
                    't': '\u0924', 'th': '\u0925', 'd': '\u0926', 'dh': '\u0927', 'n': '\u0928',
                    'p': '\u092A', 'ph': '\u092B', 'b': '\u092C', 'bh': '\u092D', 'm': '\u092E',
                    'y': '\u092F', 'r': '\u0930', 'l': '\u0932', 'v': '\u0935',
                    'z': '\u0936', 'S': '\u0937', 's': '\u0938', 'h': '\u0939',
                    "'": '\u093D', 'oM': '\u0950', ' ': ' ', '|': '\u0964', '||': '\u0964'
                    }

    # Dicionário específico para os diacríticos vocálicos.

    diacriticos_vogais = {'A': '\u093E', 'a': '',
                          'i': '\u093F', 'I': '\u0940',
                          'u': '\u0941', 'U': '\u0942',
                          'R': '\u0943', 'RR': '\u0944',
                          'lR': '\u0962',
                          'e': '\u0947', 'ai': '\u0948',
                          'o': '\u094b', 'au': '\u094C'}

    # Listas para especificidades do Devanagari.

    vogais = ['A', 'a', 'i', 'I', 'u', 'U',
              'R', 'RR',
              'lR', 'e', 'ai', 'o', 'au']
    consoantes = ['k', 'g', 'G', 'c', 'j', 'J',
                  'T', 'D', 'N', 't', 'd', 'n',
                  'p', 'b', 'm', 'y', 'r', 'l', 'v',
                  'z', 'S', 's', 'h']
    consoantes_especiais = ['G', 'J', 'N', 'n',
                            'm', 'y', 'r', 'l', 'v',
                            'z', 'S', 's']
    '''diacriticos = ['M', 'H', '\'']
    pontuacao = ['|', '||']'''

    for letra in entrada:
        i += 1
        if letra not in dict_unicode:
            saida.append(letra)
        else:
            if letra in vogais:
                if letra == 'a':
                    if entrada[i + 1] == 'i':
                        if entrada[i - 1] in consoantes:
                            saida.append(diacriticos_vogais['ai'])
                        else:
                            saida.append(dict_unicode['ai'])
                    elif entrada[i + 1] == 'u':
                        if entrada[i - 1] in consoantes:
                            saida.append(diacriticos_vogais['au'])
                        else:
                            saida.append(dict_unicode['au'])
                    else:
                        if entrada[i - 1] in consoantes:
                            saida.append('')
                        else:
                            saida.append(dict_unicode[letra])
                elif letra == 'i' or letra == 'u':
                    if entrada[i - 1] == 'a':
                        continue
                    else:
                        if entrada[i - 1] in consoantes:
                            saida.append(diacriticos_vogais[letra])
                        else:
                            saida.append(dict_unicode[letra])
                elif letra == 'R':
                    if entrada[i + 1] == 'R':
                        if entrada[i - 1] in consoantes:
                            saida.append(diacriticos_vogais['RR'])
                        else:
                            saida.append(dict_unicode['RR'])
                    elif entrada[i - 1] == 'R' or entrada[i - 1] == 'l':
                        continue
                    else:
                        if entrada[i - 1] in consoantes:
                            saida.append(diacriticos_vogais[letra])
                        else:
                            saida.append(dict_unicode[letra])
                else:
                    if entrada[i - 1] in consoantes:
                        saida.append(diacriticos_vogais[letra])
                    else:
                        saida.append(dict_unicode[letra])
            elif letra in consoantes:
                if letra == 'l' and entrada[i + 1] == 'R':
                    if entrada[i - 1] in consoantes:
                        saida.append(diacriticos_vogais['lR'])
                    else:
                        saida.append(dict_unicode['lR'])
                elif entrada[i + 1] == 'h' and letra not in consoantes_especiais:
                    saida.append(dict_unicode['%sh' % letra])
                elif entrada[i] == 'h' and entrada[i - 1] in consoantes:
                    continue
                elif entrada[i + 1] not in vogais:
                    saida.append(dict_unicode[letra])
                    saida.append('\u094D')
                else:
                    saida.append(dict_unicode[letra])
            else:
                saida.append(dict_unicode[letra])

    saida = "".join(saida)
    saida = saida.strip()
    return saida


def hkiast(entrada):
    '''
    
    :param entrada: str
    :return: str
    '''
    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []

    # Dicionário
    hk_iast_unicode = {
        'M': 'ṃ',
        'H': 'ḥ',
        'a': 'a',
        'A': 'ā',
        'i': 'i',
        'I': 'ī',
        'u': 'u',
        'U': 'ū',
        'R': 'ṛ',
        'lR': 'ḷ',
        'e': 'e',
        'o': 'o',
        'k': 'k',
        'g': 'g',
        'G': 'ṅ',
        'c': 'c',
        'j': 'j',
        'J': 'ñ',
        'T': 'ṭ',
        'D': 'ḍ',
        'N': 'ṇ',
        't': 't',
        'd': 'd',
        'n': 'n',
        'p': 'p',
        'b': 'b',
        'm': 'm',
        'y': 'y',
        'r': 'r',
        'l': 'l',
        'v': 'v',
        'z': 'ś',
        'S': 'ṣ',
        's': 's',
        'h': 'h',
        "'": '\'',
        ' ': ' ',
        '|': '\u0964',
        '||': '\u0964'
    }

    for i in range(len(entrada)):
        c = entrada[i]

        if c not in hk_iast_unicode.keys():
            saida.append(c)
            continue

        if c == 'l' and entrada[i + 1] == 'R':
            saida.append(hk_iast_unicode['lR'])
        elif c == 'R' and entrada[i - 1] == 'l':
            continue
        else:
            saida.append(hk_iast_unicode[c])
    saida = ''.join(saida)
    saida = saida.strip()
    return saida


def iastdv(entrada):

    '''
    :param entrada: str 
    :return: str 
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    i = -1
    # Dicionários
    iast_dv_unicode = {'ṃ': '\u0902', 'ḥ': '\u0903',
                       'a': '\u0905', 'ā': '\u0906',
                       'i': '\u0907', 'ī': '\u0908',
                       'u': '\u0909', 'ū': '\u090A',
                       'ṛ': '\u090B', 'ṝ': 'ॠ',
                       'ḷ': '\u090C',
                       'e': '\u090F', 'ai': '\u0910',
                       'o': '\u0913', 'au': '\u0914',
                       'k': '\u0915', 'kh': '\u0916', 'g': '\u0917', 'gh': '\u0918', 'ṅ': '\u0919',
                       'c': '\u091A', 'ch': '\u091B', 'j': '\u091C', 'jh': '\u091D', 'ñ': '\u091E',
                       'ṭ': '\u091F', 'ṭh': '\u0920', 'ḍ': '\u0921', 'ḍh': '\u0922', 'ṇ': '\u0923',
                       't': '\u0924', 'th': '\u0925', 'd': '\u0926', 'dh': '\u0927', 'n': '\u0928',
                       'p': '\u092A', 'ph': '\u092B', 'b': '\u092C', 'bh': '\u092D', 'm': '\u092E',
                       'y': '\u092F', 'r': '\u0930', 'l': '\u0932', 'v': '\u0935',
                       'ś': '\u0936', 'ṣ': '\u0937', 's': '\u0938', 'h': '\u0939',
                       "'": '\u093D', 'oṃ': '\u0950', ' ': ' ', '|': '\u0964', '||': '\u0964'
                       }

    # Dicionário específico para os diacríticos vocálicos.

    iast_c_vogais = {'ā': '\u093E', 'a': '',
                     'i': '\u093F', 'ī': '\u0940',
                     'u': '\u0941', 'ū': '\u0942',
                     'ṛ': '\u0943', 'ṝ': '\u0944',
                     'ḷ': '\u0962',
                     'e': '\u0947', 'ai': '\u0948',
                     'o': '\u094b', 'au': '\u094C'}

    # Listas para especificidades do Devanagari.

    iast_vogais = ['ā', 'a', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'e', 'ai', 'o', 'au']
    iast_consoantes = ['k', 'g', 'ṅ', 'c', 'j', 'ñ',
                       'ṭ', 'ḍ', 'ṇ', 't', 'd', 'n',
                       'p', 'b', 'm', 'y', 'r', 'l', 'v',
                       'ś', 'ṣ', 's', 'h']
    c_especiais = ['ṅ', 'ñ', 'ṇ', 'n',
                   'm', 'y', 'r', 'l', 'v',
                   'ś', 'ṣ', 's']
    iast_diacriticos = ['ṃ', 'ḥ', '\'']
    iast = ['|', '||']
    for letra in entrada:
            i += 1
            if letra not in iast_dv_unicode:
                saida.append(letra)
            else:
                if letra in iast_vogais:
                    if letra == 'a':
                        if entrada[i + 1] == 'i':
                            if entrada[i - 1] in iast_consoantes:
                                saida.append(iast_c_vogais['ai'])
                            else:
                                saida.append(iast_dv_unicode['ai'])
                        elif entrada[i + 1] == 'u':
                            if entrada[i - 1] in iast_consoantes:
                                saida.append(iast_c_vogais['au'])
                            else:
                                saida.append(iast_dv_unicode['au'])
                        else:
                            if entrada[i - 1] in iast_consoantes:
                                saida.append('')
                            else:
                                saida.append(iast_dv_unicode[letra])
                    elif letra == 'i' or letra == 'u':
                        if entrada[i - 1] == 'a':
                            continue
                        else:
                            if entrada[i - 1] in iast_consoantes:
                                saida.append(iast_c_vogais[letra])
                            else:
                                saida.append(iast_dv_unicode[letra])
                    else:
                        if entrada[i - 1] in iast_consoantes:
                            saida.append(iast_c_vogais[letra])
                        else:
                            saida.append(iast_dv_unicode[letra])
                elif letra in iast_consoantes:
                    if entrada[i + 1] == 'h' and letra not in c_especiais:
                        saida.append(iast_dv_unicode['%sh' % letra])
                    elif letra == 'h' and entrada[i - 1] in iast_consoantes:
                        continue
                    elif entrada[i + 1] not in iast_vogais:
                        saida.append(iast_dv_unicode[letra])
                        saida.append('\u094D')
                    else:
                        saida.append(iast_dv_unicode[letra])
                else:
                    saida.append(iast_dv_unicode[letra])

    saida = "".join(saida)
    saida = saida.strip()
    return saida


def iasthk(entrada):

    '''
    :param entrada: 
    :return: 
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    return None


def dviast(entrada):

    '''
    :param entrada: str
    :return: str
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    return None


def dvhk(entrada):

    '''
    :param entrada: 
    :return: 
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    return None