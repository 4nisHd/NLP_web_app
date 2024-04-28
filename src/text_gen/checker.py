def is_valid(text):
    _range = (0x0600, 0x06FF)  
    _supplement_range = (0x0750, 0x077F) 
    _extended_range = (0x08A0, 0x08FF) 
    _presentation_forms_a_range = (0xFB50, 0xFDFF) 
    _presentation_forms_b_range = (0xFE70, 0xFEFF) 

    _ranges = [
        _range,
        _supplement_range,
        _extended_range,
        _presentation_forms_a_range,
        _presentation_forms_b_range,
    ]

    for char in text:
        if any(start <= ord(char) <= end for start, end in _ranges):
            return True

    return False