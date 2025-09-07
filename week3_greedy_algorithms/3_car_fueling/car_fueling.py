from sys import stdin
def min_refills(distance, tank, stops):
    # Add the destination as a final "stop" but without mutating the input
    stops = stops + [distance]  
    
    refills = 0
    current_stop = 0
    last_refill_stop = 0
    i = 0
    
    while current_stop < distance:
        last_refill_stop = current_stop
        
        # Move as far as possible without running out of fuel
        while i < len(stops) and stops[i] - last_refill_stop <= tank:
            current_stop = stops[i]
            i += 1

        # If it is not possible to refill at any other stops to complete the journey, journey is impossible
        if current_stop == last_refill_stop:
            return -1
        
        # Count refill if we haven't reached the destination
        if current_stop < distance:
            refills += 1
        
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
