def new_sighting(kinds: list[str], counts_seen: list[int], sighting: str) -> None:
    """Adds a new sighting to the list of sightings

    Args:
        kinds (list[str]): _description_
        counts_seen (list[int]): _description_
        sighting (str): _description_
    """
    
    if sighting not in kinds:
        kinds.append(sighting)
        counts_seen.append(1)
    else:
        index = kinds.index(sighting)
        counts_seen[index] += 1

kinds = ["Monarch", "Painted Lady", "Red Admiral", "Peacock", "Small Tortoiseshell"]
counts_seen = [3, 7, 2, 5, 8]

for i in range(len(kinds)):
    print(f"I have seen {counts_seen[i]} {kinds[i]} butterflies.")

new_sighting(kinds, counts_seen, "Peacock")
new_sighting(kinds, counts_seen, "Peacock")
new_sighting(kinds, counts_seen, "Red Admiral")
new_sighting(kinds, counts_seen, "Small White")

for i in range(len(kinds)):
    print(f"I have seen {counts_seen[i]} {kinds[i]} butterflies.")


# Now with a dictionary
butterflies = {
    "Monarch": 3,
    "Painted Lady": 7,
    "Red Admiral": 2,
    "Peacock": 5,
    "Small Tortoiseshell": 8
}

for kind, count in butterflies.items():
    print(f"I have seen {count} {kind} butterflies.")

def new_add_sighting(butterflies: dict[str, int], sighting: str) -> None:
    """Adds a new sighting to the dictionary of sightings

    Args:
        butterflies (dict[str, int]): _description_
        sighting (str): _description_
    """
    
    if sighting not in butterflies:
        butterflies[sighting] = 1
    else:
        butterflies[sighting] += 1

new_add_sighting(butterflies, "Peacock")
new_add_sighting(butterflies, "Peacock")
new_add_sighting(butterflies, "Red Admiral")
new_add_sighting(butterflies, "Small White")

for kind, count in butterflies.items():
    print(f"I have seen {count} {kind} butterflies.")


def combine(d1: dict, d2: dict) -> dict:
    """Combines two dictionaries
    key in both d1 and d2
    the value associated with each key in
    the new dictionary is the sum of all the new integers 
    associated with that key in d1 and d2.
    """
    
    new_dict = {}
    for key in d1:
        if key in d2:
            lst_d1 = d1[key]
            lst_d2 = d2[key]
            new_dict[key] = sum(lst_d1 + lst_d2)
    return new_dict

d1 = {"a": [1, 2, 3], "b": [4, 5, 6]}
d2 = {"a": [7, 8, 9], "b": [10, 11, 12]}

print(combine(d1, d2))


def combine2(d1, d2):
    """
    return dictionary where each ley is a key that is a key in the values of d1 and d2
    The value associated with each key in the new dictionary is the sum of all the new integers
    associated with that key in d1 and d2.

    >>> combine2({"a": {3: [2], 4: [5,6]}}, {"a": {3:[8,12]}})
    {3: 22}
    
    """


d1 = {"a": {3: [2], 4: [5, 6]}, "b":{7:[2, 7, 9], 4: [5, 6]}}
d2 = {"a": {3: {8, 12}}, "b": {7: [7, 33]}}