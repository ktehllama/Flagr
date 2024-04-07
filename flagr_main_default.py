def parse_flags(command):
    flags = {}
    parts = command.split()
    
    for part in parts:
        if part.startswith('-'):
            flag, *value = part[1:].split('=')
            flags[flag] = '='.join(value) if value else None
    
    return flags
