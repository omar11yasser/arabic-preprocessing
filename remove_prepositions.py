import re

# Constants
PREFIXES = set(['ي', 'ت', 'ب', 'ل','ف','س'])
SUFIXES = set(['هن', 'هم'])
PREFIXES_OF_WAW_ALEF = set(['ب', 'ا', 'ي'])

# Used to check if the first letter is a prefix or part of the word
prefeix_conditions_dict = dict()
prefeix_conditions_dict['ي'] = ['ها', 'ون', 'هان','وا', 'ة']
prefeix_conditions_dict['ت'] = ['ها', 'ون','ين' ,'هان','وا', 'ة', 'ت']
prefeix_conditions_dict['ب'] = [ 'ه', 'ان', 'ات', 'ين', 'ها', 'ة']
prefeix_conditions_dict['ل'] = [ 'ة', 'ان', 'ات', 'ين', 'ها']
prefeix_conditions_dict['ف'] = ['ها', 'ين', 'ات', 'ان', 'ة']

def hun_hum_sufix_removal(word):
    '''
    Remove هم and هن and associated suffixes

    Args:
        String - word.
    Returns:
        String - word with هم or هن removed.
    '''
    # Detect suffix presence
    if (word[-2:] in SUFIXES):
        # Search if the word begins with Alef_lam or Alef_lam and paired with a suffix
        alef_lam_search = re.search('ال', word)
        if(alef_lam_search != None and alef_lam_search.start() <= 1):
            if(word[0] in PREFIXES):
                return word[1:]
        else:
            if(word[0] in PREFIXES):
                return word[1:-2]
            else:
                return word[:-2]
    return word

def remove_sufixe_waw_alef(word):
    if len(word) > 3 and word[-2:0] == 'وا' and word[0] in PREFIXES_OF_WAW_ALEF:
        return word[1:-2]
    return word

def remove_prefix_sin(word):
    '''
    Remove prefix س as it follows a diffrent logic from the prfixes listed in the dictionary
    Args:
        String - word.
    Returns:
        String - word with prefix س and the following prefix (ي or ب)removed.
    '''
    if len(word) > 2 and word[0] == 'س' and (word [1] == 'ي' or word [1] == 'ت'):
        for sufix in prefeix_conditions_dict['ب']:
            sufix = re.search(sufix + '$', word)
            if sufix != None:
                return word[2:sufix.start()]
    return word

def remove_prefixe_wsufixes(word):
    '''
    Args:
        String - word.
    Returns:
        String - word with prefixes and sufixes removed.
    '''
    for prefix in prefeix_conditions_dict.keys():
        if len(word) > 0 and word[0] == prefix:
            sufix = None
            for sufix in prefeix_conditions_dict[prefix]:
                sufix = re.search(sufix + '$', word)
                if sufix != None:
                    word = word[1:sufix.start()]
                    return word
    return word

def remove_propositions_from_sentences(sentence):
    '''
    Args:
        A String - sentnece.
    Returns:
        A string containing Sentence with prefixes remove.
    '''
    #assert type(sentence) == str
    output = list()
    for word in str(sentence).split():
        word = hun_hum_sufix_removal(word)
        word = remove_sufixe_waw_alef(word)
        word = remove_prefix_sin(word)
        word = remove_prefixe_wsufixes(word)
        output.append(word)
    return ' '.join(output)
