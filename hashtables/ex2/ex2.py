class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #setting up
    route = []
    dict = {}
    #for each index in the tickets array
    for ticket in tickets:
        #set the key to ticket.source, and the value to ticket.destination
        dict[ticket.source] = ticket.destination
    #append the ticket with the source "NONE" first since it is the first of the tickets
    print(dict["NONE"])
    route.append(dict["NONE"])
    #set the variable for last, so that the while loop runs
    last = dict["NONE"]
    #while loop runs as long as the destination is not "NONE"
    while last != "NONE":
        #if the destination is NONE then continue to the begining of the loop
        if last == "NONE":
            continue
        else:
            #while its value is not "NONE"
            #append that destiantion to the list
            route.append(dict[last])
            print(last)
            last = dict[last]
    return route
