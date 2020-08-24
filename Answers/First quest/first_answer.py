import string

with open('names.txt', 'r') as f:
    names = f.read().split(',')
    name_list = {}
    alphabet = string.ascii_lowercase + ''
    names.sort()
    most_sum = 0

    for i in range(len(names)):
        names[i] = names[i].replace('"', '').lower()

        sum_symbols = 0

        for j in names[i]:
            for k in range(len(alphabet)):
                if j == alphabet[k]:
                    sum_symbols += (k+1)

        most_sum += (i+1)*sum_symbols


    print(most_sum)