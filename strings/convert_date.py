

from calendar import isleap
print(isleap(2019))

def convert_date(date: str) -> str:
    
    date_list_str = date.split("/")
    date_list_str.reverse()
    print(date_list_str)
    date_list_int = list(map(int, date_list_str))
    print(date_list_int)
    day = date_list_int[0]
    month = date_list_int[1]
    year = date_list_int[2]
    
#use calendar or datetime module...


print("Example:")
print(convert_date("29/02/2020"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

#print("The mission is done! Click 'Check Solution' to earn rewards!")