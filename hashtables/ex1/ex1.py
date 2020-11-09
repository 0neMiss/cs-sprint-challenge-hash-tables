
def get_indices_of_item_weights(weights, length, limit):
    dict = {}
    #if the lenth of the list is greater than 1
    if len(weights) > 1:
        #iterate through the list using range so we can use the index for the key
        for index in range(0, len(weights)):
            #set weight equal to the value at the index we are currently on
            weight = weights[index]
            print(weight)
            #if the value is currently in the dictionary
            if weight in dict:
                #set the value for the index of the weight
                value = dict[weight]
                print(value)
                return [index, value]
            #find the difference of the limit and the weight and then find the index of the other value
            difference = limit - weight
            dict[difference] = index
        return []
    else:
        return None
