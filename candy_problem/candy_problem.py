'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.
'''
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]


def get_friends_favorite_candy_count(favorites):
    candy_count = {}
    for name in favorites:
        candy_list = name[1]
        for candy in candy_list:
            if candy in candy_count:
                candy_count[candy] += 1
            else:
                candy_count[candy] = 1
    return candy_count

    

'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 
'''
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

def create_new_candy_data_structure(data):
    candy_favorites = {}
    for friend in data:
        for candy in friend[1]:
            if candy in candy_favorites:
                candy_favorites[candy].append(friend[0])
            else:
                candy_favorites[candy] = []
                candy_favorites[candy].append(friend[0])
    return candy_favorites
# print(create_new_candy_data_structure(friend_favorites))

'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    pass

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    pass 

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

