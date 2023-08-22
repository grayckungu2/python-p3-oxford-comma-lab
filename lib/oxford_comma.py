def oxford_comma(arr):
    if len(arr) == 0:
        return ""
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] + " and " + arr[1]
    else:
        return ", ".join(arr[:-1]) + ", and " + arr[-1]
    
    
    
print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))  
    
