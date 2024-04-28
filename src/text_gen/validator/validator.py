class TextValidator:
    def __init__(self):
        self._range = (0x0600, 0x06FF)
        self._supplement_range = (0x0750, 0x077F)
        self._extended_range = (0x08A0, 0x08FF)
        self._presentation_forms_a_range = (0xFB50, 0xFDFF)
        self._presentation_forms_b_range = (0xFE70, 0xFEFF)
        self._ranges = [
            self._range,
            self._supplement_range,
            self._extended_range,
            self._presentation_forms_a_range,
            self._presentation_forms_b_range,
        ]

    def is_valid(self, text):
        for char in text:
            if any(start <= ord(char) <= end for start, end in self._ranges):
                return True
        return False
