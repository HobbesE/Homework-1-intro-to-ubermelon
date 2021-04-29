log_file = open("um-server-01.txt")         #open the specified file and name it "log_file"

def sales_reports(log_file):                #start a function that takes the newly named file as an argument
    for line in log_file:                   #divide the contents of log_file into lines
        line = line.rstrip()                #redefine "line" to eliminate any/all trailing blank spaces at the end of the line
        day = line[0:3]                     #define "day" as the first to fourth character of each line
        if day == "Mon":                    #loop through the "day" in each line and if the day reads "Tue"
            print(line)                     #then print that whole line.


sales_reports(log_file)                     #calls the function with log_file as the argument


