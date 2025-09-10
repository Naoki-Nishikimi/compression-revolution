# examples/compression_demo.py

# Define deletion candidates (5 categories)
deletion_candidates = [
    "Old LEVEL definitions",
    "Redundant Caesar analyses",
    "Short-term small talk (weather, schedules)",
    "Temporary emotional reactions",
    "One-time experimental notes"
]

def compress_log(entry: str) -> str:
    """
    Simple demo: mark entries as 'delete' if they match candidates,
    otherwise 'preserve'.
    """
    for pattern in deletion_candidates:
        if pattern.lower() in entry.lower():
            return f"DELETE >> {entry}"
    return f"PRESERVE >> {entry}"

# Example usage
logs = [
    "Old LEVEL definitions should be updated",
    "Contract evidence for July 2025",
    "Weather was rainy yesterday"
]

for log in logs:
    print(compress_log(log))
