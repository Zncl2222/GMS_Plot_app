def is_numeric(string):
    try:
        int(string)
        float(string)
        return True
    except ValueError:
        return False
