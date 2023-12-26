#Purna Chhetri
#CPT 101 Lab 11 Part 2
#This program proceses sales data

#Main function
def main():
    #Introduction
    print("Welcome to my sales data summary program")
    #Variables
    line_count = 0
    total_sales = 0
    try:
        #Filename input
        file_name = input("What is the name of the file that you want to open?(.txt required)  ")
    
        #Opening the file in write mode
        file_contents = open(file_name,'r')
        
        #Reading the lines 
        line = file_contents.readline()
        
        #Output statement
        print("Here are all the sales in this file:")
        #Processing the line
        while line!='':
            #counting the amount of lines in file
            line_count += 1
            #converting to float
            sales_amount = float(line)
            #adding to total
            total_sales += sales_amount
            #displaying the value
            print(f'${sales_amount:,.2f}')
            #reading the next line
            line = file_contents.readline()
        #function call to find average
        average_sales = get_average(total_sales,line_count)
        
        #output 
        print(f'The total amount of transcations: {line_count}')
        print(f'The total of the sales: ${total_sales:,.2f}')
        print(f'The average of the sales: ${average_sales:,.2f}')

        #Closing the file
        file_contents.close()
    except FileNotFoundError:
        print("That file doesn't exist, please try an another file") 
        file_name = input("What is the name of the file that you want to open? ")

#This function returns the average based on the total sales and the amount of sales
def get_average(total_sales,sales_amount):
    average = total_sales/sales_amount
    return average

#Calling main function
if __name__ == '__main__':
    main()


