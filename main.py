"""Converts an input in english into morse code

    Returns:
        list: list with string elements representing morse code
"""
morse_code_rules = {
    'a': '·-',
    'b': '-···',
    'c': '-·-·',
    'd': '-··',
    'e': '·',
    'f': '··-·',
    'g': '-·',
    'h': '····',
    'i': '··',
    'j': '·-',
    'k': '-·-',
    'l': '·-··',
    'm': '--',
    'n': '-·',
    'o': '---',
    'p': '·-·',
    'q': '-·-',
    'r': '·-·',
    's': '···',
    't': '-',
    'u': '··-',
    'v': '···-',
    'w': '·-',
    'x': '-··-',
    'y': '-·-',
    'z': '-··',
    '0': '-----',
    '1': '·-',
    '2': '··-',
    '3': '···-',
    '4': '····-',
    '5': '·····',
    '6': '-····',
    '7': '-···',
    '8': '-··',
    '9': '-·',
    ' ': '/'
}
def eng_to_morse(morse):
    return morse_code_rules.get(morse)

english_msg = input("Enter a message in english:\n").lower()
morse = [eng_to_morse(eng) for eng in english_msg]
