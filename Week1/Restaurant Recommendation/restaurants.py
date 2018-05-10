"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    # read the whole file and save it in a list called restaurants"""
    with open (file, 'r') as f:
        restaurants = f.read()

    # rearrange the list to remove '' and newlines
    st = ''
    restaurants = restaurants.splitlines()
    for element in restaurants:
        if(element == ''):
            restaurants.remove(element)
        if('%' in element):
            st = element[:-1]
            restaurants[restaurants.index(element)] = st
            
    #print(restaurants)

    # converting the list into list of lists where every inner list is a restaurant 
    n = 4           #number of inner list items
    restaurants = [restaurants[n*i : n*(i+1)] for i in range(len(restaurants)//4)]

    # rating
    name_to_rating = {}

    # slicing the first and second element - name and rate - from restaurants info
    for i in range (len(restaurants)):
            name_to_rating.update({restaurants[i][0] : int(restaurants[i][1])})

    #print(name_to_rating)

    # pricing

    # create empty lists to hold the price ranges
    rating = ''
    List_1 = []
    List_2 = []
    List_3 = []
    List_4 = []

    for i in range(len(restaurants)): 
        rating = restaurants[i][2]
        if (rating == '$'):
            List_1.append(restaurants[i][0])
        elif (rating == '$$'):
            List_2.append(restaurants[i][0])
        elif (rating == '$$$'):
            List_3.append(restaurants[i][0])
        elif (rating == '$$$$'):
            List_4.append(restaurants[i][0])

    price_to_names = {'$': List_1, '$$': List_2, '$$$': List_3, '$$$$': List_4}

    #print(price_to_names)

    # cuisine

    # spliting the cuisines if the restaurant has more than one and add them to a list of strings
    c = []
    
    for i in range(len(restaurants)):
        if(',' in restaurants[i][3]):
            restaurants[i][3] = restaurants[i][3].split(',')
        c.append(restaurants[i][3])

    # add those lists of strings to the other cuisines in one large list
    cu = []
    
    for element in c:
        if type(element) is list:
            cu += element
        else:
            cu.append(element)

    # remove the similar cuisines
    cuisines = []
    for element in cu:
        if element not in cuisines: 
            cuisines.append(element)

    # create the cuisine to names dictionary
    cuisine_to_names = {}

    for element in cuisines:
        Lst = []
        for restaurant in restaurants:
            if element in restaurant[3]:
                Lst.append(restaurant[0])    

        cuisine_to_names[element] = Lst
        
    #print(cuisine_to_names)

    return (name_to_rating, price_to_names, cuisine_to_names)

    
