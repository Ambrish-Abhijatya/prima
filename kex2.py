claim = ' Pluto is a planet. '
print(claim.upper())
print(claim.lower())
print(claim.title())
print(claim.strip())
print(f'Does the string "{claim}" start with " Pluto"? : ', claim.startswith(' Pluto'))
print(f'Does the string "{claim}" end with "planet. "? : ',claim.endswith('planet. '))
words = claim.split()
print(words)
date = '04-03-2021'
dd, mm, yyyy = date.split('-')
print(dd, mm, yyyy)
nfd = '/'.join([mm, dd, yyyy])
print(nfd)
print('👏'.join(word.upper() for word in words))
print(mm.isdigit())
print('15'.isdigit())
print(date.isdigit())