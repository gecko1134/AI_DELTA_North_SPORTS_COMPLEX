
def track_roi(impressions, spend):
    if spend == 0:
        return 0
    return round(impressions / spend, 2)
