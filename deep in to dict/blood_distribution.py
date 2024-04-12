import pprint

def distribute_blood(blood_avail: dict[str, int], blood_needs: dict[str, int]) -> dict[str, dict[str, int]]:
    
    res = {}
    
    def matches(blood_type):
        if blood_type == "A": match_rule = {"A" : 1, "B" : 0, "AB" : 1, "O" : 0}
        elif blood_type == "B": match_rule = {"A" : 0, "B" : 1, "AB" : 1, "O" : 0}
        elif blood_type == "AB": match_rule = {"A" : 0, "B" : 0, "AB" : 1, "O" : 0}
        elif blood_type == "O": match_rule = {"A" : 1, "B" : 1, "AB" : 1, "O" : 1}
        return match_rule    
        
    for ak, av in blood_avail.items():
        match = matches(ak)
        blood_used = {}
 
        for nk, nv in blood_needs.items():
            if match[nk] and av >= nv:
                blood_used.update({nk : nv})
                av -= nv
                blood_needs[nk] = 0
            elif match[nk] and av < nv:
                blood_used.update({nk : av})
                blood_needs[nk] = nv - av
                av = 0
            else:
                blood_used.update({nk : 0})
                
        res.update({ak : blood_used})   
        
    return res
    
    
pprint.pp(distribute_blood({"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}))


