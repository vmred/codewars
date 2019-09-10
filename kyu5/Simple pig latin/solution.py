# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
from asserts.Asserts import assert_true


def pig_it(text):
    text = text.split()
    return ' '.join(['{}{}{}'.format(i[1:], i[:1], 'ay') if i.isalpha() else i for i in text])


assert_true(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
assert_true(pig_it('This is my string'), 'hisTay siay ymay tringsay')
assert_true(pig_it('Quis custodiet ipsos custodes ?'), 'uisQay ustodietcay psosiay ustodescay ?')
