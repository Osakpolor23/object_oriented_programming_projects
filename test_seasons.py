import pytest
from datetime import date
from seasons import get_dob, get_age_in_minutes


def test_get_dob_valid():
    assert get_dob("1997-04-09") == date(1997, 4, 9)
    with pytest.raises(SystemExit):
        get_dob("09apr1997") 

    with pytest.raises(SystemExit):
        get_dob("1997/04/09")

    with pytest.raises(SystemExit):
        get_dob("1997-04-31")


def test_get_age_in_minutes():
    # get a valid date of birth
    dob = date(1997, 4, 9)
    # calculate age in minutes with the function
    age_in_minutes = get_age_in_minutes(dob)
    # calculate expected age in minutes manually
    today_date = date.today()
    date_diff = (today_date - dob).days
    expected_minutes = date_diff * 24 * 60
    # assert that the calculated age in minutes matches the expected value
    assert age_in_minutes == expected_minutes