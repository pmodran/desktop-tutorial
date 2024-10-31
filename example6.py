
while True:
    scanner = input('>')
    cuvinte = scanner.split(' ')

    emojis = {
    ':(':'😞',
    ':)':'🙂',
    ":D":'😁',
    ':P':'😝'
}
    output=''
    for cuvant in cuvinte:
        output += emojis.get(cuvant, cuvant) + ' '
    print(output)
    

