import re

# Constants
prefixes = set(['ي', 'ت', 'ب', 'ل','ف','س'])
sufixes = set(['هن', 'هم'])

# Used to check if the first letter is a prefix or part of the word
prefeix_conditions_dict = dict()
prefeix_conditions_dict['ي'] = ['ها', 'ون', 'هان','وا', 'ة']
prefeix_conditions_dict['ت'] = ['ها', 'ون','ين' ,'هان','وا', 'ة', 'ت']
prefeix_conditions_dict['ب'] = [ 'ه', 'ان', 'ات', 'ين', 'ها', 'ة']
prefeix_conditions_dict['ل'] = [ 'ة', 'ان', 'ات', 'ين', 'ها']
prefeix_conditions_dict['ف'] = ['ها', 'ين', 'ات', 'ان', 'ة']


# Remove هم and هن and associated suffixes
def hun_hum_sufix_removal(word):
    # Detect suffix presence
    if (word[-2:] in sufixes):
        # Search if the word begins with Alef_lam or Alef_lam and paired with a suffix
        alef_lam_search = re.search('ال', word)
        if(alef_lam_search != None and alef_lam_search.start() <= 1):
            if(word[0] in prefixes):
                return word[1:]
        else:
            if(word[0] in prefixes):
                return word[1:-2]
            else:
                return word[:-2]
    return word

def remove_prefixe_wsufixes(word):
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
    #assert type(sentence) == str
    output = list()
    for word in str(sentence).split():
        word = hun_hum_sufix_removal(word)
        word = remove_prefixe_wsufixes(word)
        output.append(word)
    return ' '.join(output)
