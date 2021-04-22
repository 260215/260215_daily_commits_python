# Write a Python script to merge two Python dictionaries

def merge_dictionaries(dictionary_1, dictionary_2):
    return dictionary_1 | dictionary_2


if __name__ == '__main__':
    dictionary_1 = {'Hydrochloric_acid': 0, 'Vinegar': 2.8, 'Milk': 6.8}
    dictionary_2 = {'Sodium_hydroxide': 14.0, 'Pure_Water': 7.0, 'Ammonia': 11.0}
    print(merge_dictionaries(dictionary_1, dictionary_2))
