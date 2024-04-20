import re
def clear_title(title):
    return re.sub(r'[^a-zA-Z0-9\s]+', '', title)

