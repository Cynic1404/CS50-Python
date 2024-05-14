from seasons import convert
import pytest
import datetime


@pytest.mark.parametrize("period", ([365, "Five hundred twenty-five thousand, six hundred minutes"],[730,"One million, fifty-one thousand, two hundred minutes"]))
def test_year(period):
    today=datetime.date.today().strftime("%Y-%m-%d")
    start_from=(datetime.date.today()-datetime.timedelta(days=period[0])).strftime("%Y-%m-%d")
    assert convert(time=today, start_from=start_from)==period[1]
