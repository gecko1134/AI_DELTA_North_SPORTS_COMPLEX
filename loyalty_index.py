
def calculate_loyalty(visits, months):
    return round((visits / months) * 10, 2) if months else 0
