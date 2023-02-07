



def input_checker(og_input):
    #convert og_input string into a list
    og_input_list = list(og_input)

    #check if list is at least 5 items in length
    if len(og_input_list) >= 5:

    else:
        return "Not enough items"


input("Enter number of cycles: ")
input_checker(input("Enter input list: "))
og_input = "0,1,0,1,1,0,1,1,0,0"