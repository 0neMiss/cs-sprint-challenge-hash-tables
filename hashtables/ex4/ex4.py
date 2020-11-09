def has_negatives(list):
    """
    YOUR CODE HERE
    """


    dict = {}
    result = []
    #for each number
    for num in list:
        # if the number is positive
        if num > 0:
            #set the value of the dictionary at the key of the number equal to the number
             dict[num] = num

    #iterate through the list again and run the abs function if the positive version of each nevgative number exists in the list
    result = [abs(num) for num in list if num * -1 in dict]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
