
def get_contract_alerts(contracts):
    alerts = []
    for c in contracts:
        if c['days_to_expiry'] <= 30:
            alerts.append(f"{c['sponsor']} contract expires in {c['days_to_expiry']} days.")
    return alerts
