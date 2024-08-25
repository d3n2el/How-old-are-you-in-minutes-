import pytest
from seasons import get_date
def test_getdate():
    assert get_date("1999-01-01") == "Thirteen million, four hundred eighty-nine thousand, nine hundred twenty minutes"
    assert get_date("2001-09-11") == "Twelve million, seventy-two thousand, nine hundred sixty minutes"
    assert get_date("0335-01-11") == "Eight hundred eighty-eight million, six hundred fifty-five thousand, six hundred eighty minutes"
