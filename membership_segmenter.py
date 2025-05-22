
def segment_members(members):
    segments = {}
    for m in members:
        visits = m['visits']
        if visits > 15:
            segments[m['name']] = "Gold"
        elif visits > 8:
            segments[m['name']] = "Silver"
        else:
            segments[m['name']] = "Bronze"
    return segments
