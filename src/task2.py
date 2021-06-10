def get_month_decorator(func):
    """ checks that number being passed as month argument is valid. i.e betweeen 1 - 12"""
    
    #   Inner function which would access func value/arguement
    def inner(x):
        month = func(x)     #   Accessing the value of func

        #   Dictionary storing the months in a year and their index
        months = {
            1 : "January",
            2 : "February",
            3 : "March",
            4 : "April",
            5 : "May",
            6 : "June",
            7 : "July",
            8 : "August",
            9 : "September",
            10 : "October",
            11 : "November",
            12 : "December"
        }

        if month in months:
            return months[month]
        else:
            return "Sorry, you entered an invalid month"
        
    return inner



# calling the decorator unto the function
@get_month_decorator
def get_month(month):
    """ 
        returns the expected month string based on the valid month integer passed as an argument 
    """
    return month


try:
    value = int(input("Please enter any value of the mont between 1 to 12:  "))
    print(get_month(value))
except ValueError:
    print("Invalid input, please enter a number")


