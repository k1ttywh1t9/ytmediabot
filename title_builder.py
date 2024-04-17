def clear_title(title):
    import re
    return re.sub(r'[^a-zA-Z0-9\s]+', '', title)

