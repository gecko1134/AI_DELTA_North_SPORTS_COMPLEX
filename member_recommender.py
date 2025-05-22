
def recommend_tools(profile_tags):
    options = {
        "training": ["Goal Tracker", "Performance AI"],
        "youth": ["Camps", "Coach Assignments"],
        "inactive": ["Welcome Back Offer", "Quick Sign-up"]
    }
    recs = []
    for tag in profile_tags:
        recs.extend(options.get(tag, []))
    return list(set(recs))
