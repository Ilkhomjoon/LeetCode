def countMatches(items, ruleKey, ruleValue):    
    a = {"type": 0,
        "color": 1,
        "name": 2
        }
    count = 0
    for i in items:
        if i[a[ruleKey]] == ruleValue:
            count += 1
    return count





items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(countMatches(items, ruleKey, ruleValue))