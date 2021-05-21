def flatten(S):
    if S == []: # return the array directly if the length is 0
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])   # recursively return each element if it's a list
    return S[:1] + flatten(S[1:])