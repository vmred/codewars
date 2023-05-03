# Simple pig latin
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    return ' '.join([f"{i[1:]}{i[:1]}{'ay'}" if i.isalpha() else i for i in text.split()])
