def ValidAnagram(s, t):

    if len(s) != len(t):
        return False

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in t:
        freq[char] = freq.get(char, 0) - 1


    for i in freq:
        if freq[i] >= 0:
            return False

    return True



def main():
    print(ValidAnagram("anagram", "gramana"))




if __name__ == "__main__":
    main()