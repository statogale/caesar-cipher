def text_shift(alphabets, job):
    """ Text and shift inputs from user after validation """
   
    while True:     
        try:  
            if 'text' not in locals(): 
                text = input("\nPlease enter the text: ")                
                for letter in text:                         
                    if letter != " " and letter not in alphabets: 
                        uppercase = " uppercase " if all(char.isupper() for char in alphabets) else " "
                        del text
                        raise ValueError(f"For Caesar cipher, text should only include{uppercase}letters of \
                        \nthe 26 English Alphabets or space characters")                           
            
            if 'shift' not in locals():
                try: 
                    shift = input("\nPlease enter the secret key or shift parameter. \
                \nLeft shift should be negative number:  ").replace(" ", "")
                    
                    if shift == "":
                        shift = -3 # Use default shift                     
                        
                    shift = int(shift)
                    
                    if shift not in range(-25, 25):
                        raise ValueError("Secret should only be numbers between 0 and 25")
                except ValueError as e:
                    del shift
                    raise ValueError(f"{e}")
            break         
        except ValueError as e:
            print(f"😞 Input is not valid. {e}")
        except Exception as e:
            # Handling other exceptions
            print(f"An unexpected error occurred: {e}")
    
    return text, shift


def ask_user(job):
    """ Ask user if they want to do an encryption or a decryption. """
    try:
        user = input(f"\nDo you want to perform {job}?  \
                      \nEnter Y or y for Yes or any other value to end the program:  ")
        return user
    except Exception as e:
        print(f"An unexpected error occurred: {e}")