
def match_sponsors(assets, sponsors):
    matches = []
    for sponsor in sponsors:
        for asset in assets:
            if sponsor['target'] in asset['tags']:
                matches.append({'sponsor': sponsor['name'], 'asset': asset['id']})
    return matches
