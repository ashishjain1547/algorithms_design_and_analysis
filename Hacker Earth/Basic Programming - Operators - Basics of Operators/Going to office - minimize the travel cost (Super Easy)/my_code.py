D = int(input())

oc, of, od = map(int, input().split())

ca, cb, cm, cd = map(int, input().split())

def online_cost(D, oc, of, od):
    if D <= of:
        return oc
    
    else:
        cost = oc

        rem_dist = D - of
        cost += (rem_dist * od)

        return cost

def offline_cost(D, ca, cb, cm, cd):
    cost = cb

    t = D/ca
    cost += ((t * cm) + (D * cd))
    return cost

on_cost = online_cost(D, oc, of, od)
off_cost = offline_cost(D, ca, cb, cm, cd)

if off_cost < on_cost:
    print("Classic Taxi")
else:
    print("Online Taxi")
