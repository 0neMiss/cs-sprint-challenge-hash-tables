# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #first use a dictionary to store the queries
    dict = {}
    result = []

    #make a list of each file path using split to divide them by / then use index -1 to check if the file matches the path

    for index in range(0, len(queries)):
        dict[queries[index]] = index
    for file in files:
        file_array = file.split("/")

        if file_array[-1] in dict:
            result.append(file)

    return(result)







if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
