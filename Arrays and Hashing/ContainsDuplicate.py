def ContainsDuplicate(nums):

    hashset = set()

    for i in nums:

        if i in hashset:
            return True
        hashset.add(i)

    return False


def main():
    print(ContainsDuplicate([1,2,3,1]))


if __name__ == "__main__":
    main()
