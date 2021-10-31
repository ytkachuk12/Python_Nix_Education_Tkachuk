"""exceptions example"""


actor = {"name": "John Cleese", "rank": "awesome"}


def get_last_name():
    """Get actors family name. raise Error if we have only actors first name"""
    if actor["name"].split() == -1:
        raise NameError
    return actor["name"].split()[1]


get_last_name()
print("All exceptions caught! Good job!")
print(f"The actor's last name is {get_last_name()}")
