def parse_flags(func):
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            raise ValueError("Function must have at least one argument which is the command string.")
        
        command = args[0]
        flags = {}
        parts = command.split()
        
        for part in parts:
            if part.startswith('-'):
                flag, *value = part[1:].split('=')
                flags[flag] = '='.join(value) if value else None
        
        kwargs['flags'] = flags
        return func(*args, **kwargs)
    
    return wrapper
