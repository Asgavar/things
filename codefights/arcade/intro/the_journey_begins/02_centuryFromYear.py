def centuryFromYear(year):
    naive_century = (year // 100) + 1
    first_year_modifier = -1 if (year % 100) == (year % 10) == 0 else 0
    return naive_century + first_year_modifier
