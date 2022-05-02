""" 'Melon Delivery Report' 

INSTRUCTIONS: 
        - Refactor the code to make it more readable and less repetitive.
        - Walk through the code and add comments explaining each line of code as well as you can. """


# Create a function to reduce repetition
# Our function will take in 2 arguments- the day_number and the text file for that day

def get_daily_delivery_info(day_number, file_for_that_day):
    """ Prints melon delivery info for day number entered and the text file passed in.
    
    States day number, opens the text file, reads through each line and prints report. 
    
    Report dislplays:
        - number delivered of the melon type, 
        - specific name of that melon type,
        - and the total amount in sales for the melon type."""
    
    # Helpful to print a line of dashes-- in terminal this quickly indicates to reader a separate section
    #  f-string prints the start of report and day_number (that will be passed in when the function is called)  
    print("-" * 35 + f"START OF DAY {day_number} REPORT" + "-" * 35)

    #   created a variable that opens the text file (that will be passed in when the function is called)
    file_open = open(file_for_that_day)

    #   started a for loop to iterate through each line of the text file
    for line in file_open:          #   for each line of the file passed in, 
        line = line.rstrip()        #   remove the white space to the right for each line, and assign this to the variable line
        words = line.split('|')     #   split line by the | sign, which creates a list; assign this to the variable words

        melon = words[0]            #   assign the variable melon to index 0 of words
        count = words[1]            #   assign the variable count to index 1 of words
        amount = words[2]           #   assign the variable amount to index 2 of words

        # for each line, we print out information for our report (using an f-string and the variables melon, count and amount)
        print(f"Delivered {count} {melon}s for total of ${amount}")
    
    #   close the text file
    file_open.close()

    #  f-string prints the end of report and day_number so reader knows report is finished for that day
    print("-" * 35 + f"END OF DAY {day_number} REPORT" + "-" * 35)

#   here we call our functions, passing in different arguments with each function call
get_daily_delivery_info(1, "um-deliveries-day-1.txt")
get_daily_delivery_info(2, "um-deliveries-day-2.txt")
get_daily_delivery_info(3, "um-deliveries-day-3.txt")
