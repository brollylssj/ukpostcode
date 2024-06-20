import re


class UKPostcode:
    """
    A class to validate and format UK postcodes.
    """

    POSTCODE_REGEX = re.compile(
        r'^(GIR ?0AA|'
        r'([A-PR-UWYZ][0-9][0-9]?|'
        r'[A-PR-UWYZ][A-HK-Y][0-9][0-9]?|'
        r'[A-PR-UWYZ][0-9][A-HJKPSTUW]|'
        r'[A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])'
        r' ?[0-9][ABD-HJLNP-UW-Z]{2}|'
        r'BFPO ?[0-9]{1,4}|'
        r'(ASCN|STHL|TDCU|BBND|FIQQ|BIQQ|PCRN|TKCA) ?1ZZ|'
        r'(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|'
        r'[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$',
        re.IGNORECASE
    )

    def __init__(self, postcode: str):
        """
        Initialize the UKPostcode object with a given postcode.

        Args:
            postcode (str): The postcode to validate and format.

        Raises:
            ValueError: If the postcode is invalid.
        """
        self.raw_postcode = postcode.strip().upper()
        if not self.validate(self.raw_postcode):
            raise ValueError(f"Invalid UK postcode: {postcode}")
        self.formatted_postcode = self.format(self.raw_postcode)

    @classmethod
    def validate(cls, postcode: str) -> bool:
        """
        Validate a UK postcode.

        Args:
            postcode (str): The postcode to validate.

        Returns:
            bool: True if the postcode is valid, False otherwise.
        """
        if not postcode:
            return False
        postcode = postcode.strip().upper().replace(' ', '')
        return bool(cls.POSTCODE_REGEX.match(postcode))

    @staticmethod
    def format(postcode: str) -> str:
        """
        Format a UK postcode to the standard format with a single space separating
        the outward and inward parts.

        Args:
            postcode (str): The postcode to format.

        Returns:
            str: The formatted postcode.
        """
        postcode = postcode.strip().upper().replace(' ', '')
        outward = postcode[:-3]
        inward = postcode[-3:]
        return f"{outward} {inward}"

    def get_outward_code(self) -> str:
        """
        Get the outward code part of the postcode.

        Returns:
            str: The outward code.
        """
        return self.formatted_postcode.split()[0]

    def get_inward_code(self) -> str:
        """
        Get the inward code part of the postcode.

        Returns:
            str: The inward code.
        """
        return self.formatted_postcode.split()[1]

    def __str__(self):
        return self.formatted_postcode
