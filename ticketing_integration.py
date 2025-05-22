
def simulate_ticket_api(entry_log):
    return [{"member": m["id"], "scans": len(m["scans"])} for m in entry_log]
