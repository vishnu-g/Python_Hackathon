def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
def numbers_to_months(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    print func()