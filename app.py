
import africastalking as at
import hashlib
import random
import string


PORT = 30001
# Set up Africa's Talking API credentials
at_username = "userbyte"
at_api_key = "3f85007813969bb9bca60aa9b2d42f4068b7cfcc4ff8b6c40302fb076b9e04c7"

# Initialize Africa's Talking SMS service
at.initialize(at_username, at_api_key)
sms = at.SMS

# In-memory database for user registration data (Replace this with a proper database in production)
users_db = {}
entries_db = []
1
def generate_random_id():
    
    # Generate a random 6-character alphanumeric ID for anonymizing journal entries
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def register_user(phone_number):
    # Check if the user already exists
    if phone_number in users_db:
        return "User already registered."
    else:
        users_db[phone_number] = {}
        return "Registration successful. Welcome to the Confidant Journal!"

def create_journal_entry(phone_number, journal_entry):
    # Anonymize the journal entry before storing it
    entry_id = generate_random_id()
    entries_db.append({'phone': phone_number, 'id': entry_id, 'entry_text': journal_entry})

    return "Journal Entry saved successfully."

def view_all_journal_entries(phone_number):
    all_entries = [entry['entry_text'] for entry in entries_db if entry['phone'] == phone_number]
    if all_entries:
        return "\n".join(all_entries)
    else:
        return "You have no journal entries yet."

def search_journal_entries(phone_number, keyword):
    matching_entries = [entry['entry_text'] for entry in entries_db if entry['phone'] == phone_number and keyword.lower() in entry['entry_text'].lower()]
    if matching_entries:
        return "\n".join(matching_entries)
    else:
        return "No matching entries found."

def send_sms(phone_number, message):
    # Send an SMS message using Africa's Talking SMS API
    sms.send(message, [phone_number])

if __name__ == '__main__':
    
    print("Welcome to the Confidant Journal!")

    while True:
        print("\nChoose an option:")
        print("1. Register for the Confidant Journal")
        print("2. Create a Journal Entry")
        print("3. View All Journal Entries")
        print("4. Search Journal Entries")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            phone_number = input("Enter your phone number: ")
            response = register_user(phone_number)
            print(response)
        elif choice == '2':
            phone_number = input("Enter your phone number: ")
            if phone_number in users_db:
                journal_entry = input("Write your journal entry: ")
                response = create_journal_entry(phone_number, journal_entry)
                print(response)
            else:
                print("Invalid phone number. Please register first.")
        elif choice == '3':
            phone_number = input("Enter your phone number: ")
            if phone_number in users_db:
                entries = view_all_journal_entries(phone_number)
                print("All Journal Entries:")
                print(entries)
            else:
                print("Invalid phone number. Please register first.")
        elif choice == '4':
            phone_number = input("Enter your phone number: ")
            if phone_number in users_db:
                keyword = input("Enter a keyword to search for: ")
                entries = search_journal_entries(phone_number, keyword)
                print("Search Results:")
                print(entries)
            else:
                print("Invalid phone number. Please register first.")
        elif choice == '5':
            print("Goodbye! See you soon.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
