import itertools
import string
import time

# Function to simulate a password check (replace with your own logic for testing)
def check_password(attempt):
    # Example: The correct password is "secret"
    correct_password = "secret"
    return attempt == correct_password







def brute_force_password(length):
    
    chars = string.ascii_letters + string.digits + string.punctuation




    # all possible combinations


    for attempt in itertools.product(chars, repeat=length):
        attempt = ''.join(attempt)  
        print(f"Trying: {attempt}")






        # Check if the attempt matches the password
        if check_password(attempt):
            print(f"Password found: {attempt}")
            return attempt
        
    print("Password not found.")
    return None

# Main function
if __name__ == "__main__":
   
    password_length = 6

    # Start the brute-force attack
    print(f"Starting brute-force attack for passwords of length {password_length}...")
    start_time = time.time()
    brute_force_password(password_length)
    end_time = time.time()

    
    print(f"Time taken: {end_time - start_time:.2f} seconds")