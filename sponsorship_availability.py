
def filter_available_zones(zones, region=None, audience=None):
    return [z for z in zones if z['status'] == 'available' and 
            (region is None or z['region'] == region) and 
            (audience is None or audience in z['audience_targets'])]
