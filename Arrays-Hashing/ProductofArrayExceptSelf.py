nums = [1, 2, 3, 4]

def ProductofArrayExceptSelf(nums):

    result = [1] * (len(nums))
    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    print(result)
    postfix = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result




if __name__ == "__main__":
    print(ProductofArrayExceptSelf(nums))