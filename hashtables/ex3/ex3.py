def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dict = {}
    result = []
    #first i need to loop through the list of lists and make a
    for index in range(0, len(arrays[0])):
        dict[arrays[0][index]] = index
    print(dict)
    arrays.pop(0)
    for array in arrays:
        for item in array:
            if item in dict:
                result.append(item)

    return item




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
