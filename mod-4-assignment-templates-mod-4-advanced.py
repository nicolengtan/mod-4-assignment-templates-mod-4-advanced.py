'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
'''
def relationship_status(from_member, to_member, social_graph):
    if from_member in social_graph and to_member in social_graph:
        if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
            return "friends"
        elif to_member in social_graph[from_member]["following"]:
            return "follower"
        elif from_member in social_graph[to_member]["following"]:
            return "followed by"
    return "no relationship"

social_graph = {
    "@bongolpoc": {"first_name": "Joselito", "last_name": "Olpoc", "following": []},
    "@joaquin": {"first_name": "Joaquin", "last_name": "Gonzales", "following": ["@chums", "@jobenilagan"]},
    "@chums": {"first_name": "Matthew", "last_name": "Uy", "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]},
    "@jobenilagan": {"first_name": "Joben", "last_name": "Ilagan", "following": ["@eeebeee", "@chums", "@joaquin", "@joeilagan"]},
    "@joeilagan": {"first_name": "Joe", "last_name": "Ilagan", "following": ["@eeebeee", "@jobenilagan", "@chums"]},
    "@eeebeee": {"first_name": "Elizabeth", "last_name": "Ilagan", "following": ["@jobenilagan", "@joeilagan"]},
}

from_member = str(input("Enter the username of the first/subject account:"))
to_member = str(input("Enter the username of the second/object account:"))
relationship = relationship_status(from_member, to_member, social_graph)

if relationship == "friends":
    print(f"{from_member} and {to_member} are friends.")
elif relationship == "follower":
    print(f"{from_member} follows {to_member}.")
elif relationship == "followed by":
    print(f"{to_member} follows {from_member}.")
else:
    print(f"There is no relationship between {from_member} and {to_member}.")
    
'''

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
        
'''

def tic_tac_toe(board):
    size = len(board)
    
    for i in range(size):
        row = set(board[i])
        column = set(board[j][i] for j in range(size))
        if len(row) == 1 and list(row)[0] != '.':
            return list(row)[0]
        if len(column) == 1 and list(column)[0] != '.':
            return  list(column)[0]
    
    diagonal1 = set(board[i][i] for i in range(size))
    diagonal2 = set(board[i][size - 1 - i] for i in range(size))
    if len(diagonal1) == 1 and list(diagonal1)[0] != '.':
        return list(diagonal1)[0]
    if len(diagonal2) == 1 and list(diagonal1)[0] != '.':
        return list(diagonal2)[0]
    
    return "NO WINNER"

print("Enter Tic Tac Toe Board:")
board = []
for i in range(3):
    row = str(input(f"Enter row {i + 1}:"))
    board.append(list(row))

winner = tic_tac_toe(board)
print(f"The winner is {winner}")

'''

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
        
'''

def eta(from_stop, to_stop, legs):
    current_stop = from_stop
    total_time = 0
    
    while current_stop != to_stop:
        if (current_stop, to_stop) in legs:
            total_time += legs[(current_stop, to_stop)]['travel_time_mins']
            break
        else:
            next_stops = [stop for stop, leg in legs. keys() if leg == current_stop]
            if not next_stops:
                return "NO ROUTE"
            next_stop = next_stops[0]
            leg_key = (current_stop, next_stop)
            if leg_key not in legs:
                return "NO ROUTE"
            total_time += legs[legs_key]['travel_time_mins']
            current_stop = next_stop
    
    return total_time

legs = {
    ("upd", "admu"): {
        "travel_time_mins": 10
    },
    ("admu", "dlsu"): {
        "travel_time_mins": 35
    },
    ("dlsu", "upd"): {
        "travel_time_mins": 55
    }
}

from_stop = str(input("Enter the starting stop:"))
to_stop = str(input("Enter the destination stop:"))
travel_time = eta(from_stop, to_stop, legs)

if travel_time == "NO ROUTE":
    print("There is no valid route.")
else:
    print(f"The estimated travel time from {from_stop} to {to_stop} is  {travel_time} minutes")

'''


