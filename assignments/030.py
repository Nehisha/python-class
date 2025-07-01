# Dictionary Key-Value Inverter (Dictionaries)
# Write a function invert_dict(d) that inverts a dictionary,
#  making keys into values and values into keys. If multiple
# keys have the same value, group those keys in a list as the
#  new value. For example, invert_dict({"a": 1, "b": 2, "c": 1})
#  returns {1: ["a", "c"], 2: ["b"]}. Use dictionary methods like items() and loops.

def invert_dict(d):
    inverted = {}

    for k, v in d.items():
        if v in inverted:
            inverted[v].append(k)
        else:
            inverted[v] = [k]
    return inverted


print(invert_dict({"a": 1, "b": 2, "c": 1}))
