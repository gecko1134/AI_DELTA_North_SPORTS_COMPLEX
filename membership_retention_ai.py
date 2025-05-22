
def flag_at_risk(members):
    return [m['name'] for m in members if m['attendance'] < 5 and m['months'] > 2]
