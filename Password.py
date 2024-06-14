import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    
    # Randomly select characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

# Run the main function
if __name__ == "__main__":
    main()
