def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if len(original) != len(other):
        return False
    for i in range(len(original)):
        if type(original[i]) != type(other[i]):
            if  type(original[i]) != list and type(other[i]) != list:
                return True
            return False
        if isinstance(original[i],list) and isinstance(original[i], list):
            if len(original[i]) != len(other[i]):
                return False
            for j in range(len(original[i])):
                if type(original[i][j]) != type(other[i][j]):
                    return False
    return True