def TwoSum(nums, target):

    dictionary = {}

    for i, j in enumerate(nums):

        difference = target - j

        if difference in dictionary:
            return [dictionary[difference], i]

        dictionary[j] = i


def main():
    print(TwoSum([2,7,11,15], 9))


if __name__ == "__main__":
    main()