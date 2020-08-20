dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

input_ = input().split()

incorrect_words = [word for word in input_ if word not in dictionary]

if len(incorrect_words) > 0:
    for word in incorrect_words:
        print(word)
else:
    print("OK")