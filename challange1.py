dictionar = {
    '1': 'unu',
    '2': 'doi',
    '3': 'trei',
    '4':  'patru',
    '5':  'cinci',
    '6':  'sase',
    '7':  'SHEPTE',
    '8':  'opt',
    '9':  'noua',
    '0':  'zero'
}

x = input('Nr de telefon:')
y = ''

for i in x:
    y += dictionar.get(i, '!!!!!') + ' '


print (y)

