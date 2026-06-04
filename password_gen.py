import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    
    char_pool = string.ascii_lowercase
    
 
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

   
    if not char_pool:
        return ""

    
    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("--- Robust Password Generator ---")
    
  
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 4:
            print("To ensure basic security, length must be at least 4.")
            return
    except ValueError:
        print("Please enter a valid whole number for the length.")
        return

    
    print("\nConfigure password settings:")
    include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters/symbols? (y/n): ").strip().lower() == 'y'

  
    generated_pwd = generate_password(length, include_upper, include_digits, include_special)
    
   
    print("\n" + "="*30)
    print(f"Generated Password: {generated_pwd}")
    print("="*30)

if __name__ == "__main__":
    main()
