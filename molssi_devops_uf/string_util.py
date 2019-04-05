"""
string_util.py
A sample repo for the MolSSI workshop at UF

Misc. string processing functions 
"""

def title_case(sentence):
    """
    convert a string to a title case.

    Parameters
    __________
    sentence: string
         string to be converted to title case
    
    Returns
    _______
    
    title_case_sentence : string
         String converted to title case

    Example
    _______
    
    >>> title_case('This Is A String To Be Converted.')
        'This Is A String To Be Converted.'

    """
    # check that input is a string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input must be string type' %(sentence))
    # error if empty string
    if len(sentence) == 0:
        raise ValueError('cannot apply title funtion to empty string')
    ret = sentence[0].upper()
    for i in range(1, len(sentence)):
            if sentence[i - 1] == ' ':
                  ret += sentence[i].upper()
            else:
                  ret +=sentence[i].lower()
    return ret

