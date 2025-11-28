students = {}
items = {}

def admin_login():
    password = input("Enter Password: ")
    return password == "admin"

def admin_menu():
    while True:
        print("===== ADMIN DASHBOARD =====")
        print("1. View All Lost Items")
        print("2. Add a New Lost Item")
        print("3. Mark an Item as Claimed")
        print("4. Register New Student")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_lost_items()
        elif choice == "2":
            add_lost_item()
        elif choice == "3":
            mark_item_claimed()
        elif choice == "4":
            register_student()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")

def view_lost_items():
    if not items:
        print("No lost items yet.")
    else:
        print("===== LOST ITEMS =====")
        for item_id, item in items.items():
            print(f"ID: {item_id}")
            print(f"Name: {item['name']}")
            print(f"Description: {item['description']}")
            print(f"Location Found: {item['location_found']}")
            print(f"Date Found: {item['date_found']}")
            print(f"Status: {item['status']}")
            print(f"Claimed By: {item['claimed_by']}")

def add_lost_item():
    item_id = len(items) + 1
    item = {
        "id": item_id,
        "name": input("Enter item name: "), "description": input("Enter item description: "), 
        "location_found": input("Enter where it was found: "), 
        "date_found": input("Enter date found (YYYY-MM-DD): "), 
        "status": "Unclaimed", 
        "claimed_by": None
    }
    items[item_id] = item
    print("Item added successfully!")

def mark_item_claimed():
    if not items:
        print("No items to mark as claimed.")
        return
    try:
        item_id = int(input("Enter the ID of the item to mark as claimed: "))
        if item_id in items:
            items[item_id]["status"] = "Claimed"
            items[item_id]["claimed_by"] = input("Enter name of claimer: ")
            print("Item marked as claimed.")
        else:
            print("Item not found.")
    except ValueError:
        print("Invalid input. Please enter a valid item ID.")

def register_student():
    print("===== Student Registration =====")
    username = int(input("Enter your Student ID: "))
    if username in students:
        print("Student ID already registered.")
        return
    password = input("Enter your password: ")
    students[username] = password
    print("Registration complete!")

def student_login():
    username = int(input("Enter Student ID: "))
    if username not in students:
        print("Invalid Student ID.")
        return None

    password = input("Enter password: ")

    if students[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid password.")
        return None

def student_menu(username):
    while True:
        print(f"===== STUDENT DASHBOARD ({username}) =====")
        print(f"Welcome ({username})!!!")
        print("\n1. Search for Item")
        print("2. View Lost and Found Items")
        print("3. View Lost and Not Found Items")
        print("4. Claim an Item")
        print("5. Report Lost and Not Found Item")
        print("6. Log Out")

        choice = input("Enter your choice: ")

        if choice == "1":
            search()
        elif choice == "2":
            view_lost_and_found_item()
        elif choice == "3":
            view_lost_not_found_item()
        elif choice == "4":
            claim_item(username)
        elif choice == "5":
            report_not_found_item(username)
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice! Try again.")

def search():
    print("===== SEARCH FOR ITEM =====")
    if not items:
        print("No items found.")
        return

    item_search = input("Enter item name: ").lower()
    found = False

    for item in items.values():
        if item_search in item['name'].lower() or item_search in item['description'].lower():
            print(f"Found: {item['name']} - (Description: {item['description']} - (Status: {item['status']})")
            found = True

    if not found:
        print("No matching items found.")

def view_lost_and_found_item():
    print("===== LOST AND FOUND ITEMS =====")
    found_any = False
    for item in items.values():
        if item["status"] == "Unclaimed":
            print(f"ID: {item['id']} | {item['name']} | {item['description']} | Found at: {item['location_found']}")
            found_any = True
    if not found_any:
        print("No items currently unclaimed.")

def view_lost_not_found_item():
    print("===== LOST BUT NOT FOUND ITEMS =====")
    not_found_any = False
    for item in items.values():
        if item["status"] == "Reported Missing":
            print(f"ID: {item['id']} | {item['name']} | Description: {item['description']}")
            not_found_any = True
    if not not_found_any:
        print("No items reported missing yet.")

def claim_item(username):
    print("===== CLAIM ITEM =====")
    if not items:
        print("No items available to claim.")
        return

    try:
        item_id = int(input("Enter the ID of the item you want to claim: "))
        if item_id in items and items[item_id]["status"] == "Unclaimed":
            items[item_id]["status"] = "Claimed"
            items[item_id]["claimed_by"] = username
            print("Item successfully claimed!")
        else:
            print("Item not found or already claimed.")
    except ValueError:
        print("Invalid ID entered.")

def report_not_found_item(username):
    print("===== REPORT LOST ITEM =====")
    item_id = len(items) + 1
    item_name = input("Enter the name of your lost item: ")
    description = input("Enter a brief description: ")

    items[item_id] = {
        "id": item_id,
        "name": item_name,
        "description": description,
        "location_found": "Unknown",
        "date_found": "N/A",
        "status": "Reported Missing",
        "claimed_by": username
    }
    print(f"Thank you, {username}. Your lost item '{item_name}' has been reported and is now visible to the admin.")

def main():
    while True:
        print("===== LOST AND FOUND SYSTEM =====")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if admin_login():
                print("Admin login successful!")
                admin_menu()
            else:
                print("Incorrect admin password!")
        elif choice == "2":
            username = student_login()
            if username:
                student_menu(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main()
