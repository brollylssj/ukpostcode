import pytest
from ukpostcode import UKPostcode


@pytest.fixture
def valid_postcodes():
    return [
        "EC1A 1BB", "W1A 0AX", "M1 1AE", "B33 8TH", "CR2 6XH", "DN55 1PT",
        "SW1W 0NY", "PO16 7GZ", "GU16 7HF", "L1 8JQ"
    ]


@pytest.fixture
def invalid_postcodes():
    return ["INVALID", "12345", "A1 1XDA", "ZZ999ZZ"]


@pytest.fixture
def special_cases():
    return [
        "ASCN 1ZZ", "STHL 1ZZ", "TDCU 1ZZ", "BBND 1ZZ", "BIQQ 1ZZ", "FIQQ 1ZZ",
        "PCRN 1ZZ", "TKCA 1ZZ", "BFPO 1234", "KY1-1101", "MSR 1234", "VG 2345",
        "AI-2640", "SAN TA1", "GE CX", "GIR 0AA"
    ]


def test_valid_postcodes(valid_postcodes):
    for pc in valid_postcodes:
        assert UKPostcode.validate(pc)
        uk_postcode = UKPostcode(pc)
        assert str(uk_postcode) == UKPostcode.format(pc)


def test_invalid_postcodes(invalid_postcodes):
    for pc in invalid_postcodes:
        assert not UKPostcode.validate(pc)
        with pytest.raises(ValueError):
            UKPostcode(pc)


def test_get_outward_code():
    uk_postcode = UKPostcode("EC1A 1BB")
    assert uk_postcode.get_outward_code() == "EC1A"


def test_get_inward_code():
    uk_postcode = UKPostcode("EC1A 1BB")
    assert uk_postcode.get_inward_code() == "1BB"


def test_special_cases(special_cases):
    for pc in special_cases:
        assert UKPostcode.validate(pc)
        uk_postcode = UKPostcode(pc)
        assert str(uk_postcode) == UKPostcode.format(pc)


def test_postcode_with_space():
    pc = "EC1A  1BB"
    assert UKPostcode.validate(pc)
    uk_postcode = UKPostcode(pc)
    assert str(uk_postcode) == "EC1A 1BB"


def test_postcode_without_space():
    pc = "EC1A1BB"
    assert UKPostcode.validate(pc)
    uk_postcode = UKPostcode(pc)
    assert str(uk_postcode) == "EC1A 1BB"
