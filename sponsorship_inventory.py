
def get_zone_inventory(zones):
    inventory = {"available": [], "sold": [], "expiring": []}
    for zone in zones:
        if zone['status'] == "available":
            inventory["available"].append(zone)
        elif zone['status'] == "sold" and zone['days_left'] < 30:
            inventory["expiring"].append(zone)
        else:
            inventory["sold"].append(zone)
    return inventory
