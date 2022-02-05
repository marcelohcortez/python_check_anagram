def are_anagrams(first_word, second_word):
    freq1 = {}
    freq2 = {}

    if len(first_word) != len(second_word):
        print(f'{first_word} and {second_word} ARE NOT anagrams\n')
        return
  
    for char in first_word:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
  
    for char in second_word:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            print(f'{first_word} and {second_word} ARE NOT anagrams\n')
            return
        else:
            print(f'{first_word} and {second_word} ARE anagrams\n')
            return

if __name__ == '__main__':
    first_word = input('Define the first word:\n')
    second_word = input('Define the second word:\n')
    are_anagrams(first_word, second_word)