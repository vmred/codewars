def toJadenCase(string):
    return ' '.join(x.capitalize() for x in string.split())


print(toJadenCase('How can mirrors be real if our eyes aren\'t real'))
