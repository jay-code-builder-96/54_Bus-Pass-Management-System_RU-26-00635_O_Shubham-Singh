# Bus Pass Management System (PS No. 54)
# Concepts: Lists, Dictionaries, Functions, File Handling

FILE_NAME = "buspass.txt"
STUDENT_DISCOUNT = 0.25

# Pass types with fee and validity
PASS_TYPES = {
    "Monthly": {"fee": 500, "days": 30},
    "Quarterly": {"fee": 1350, "days": 90},
    "Yearly": {"fee": 4800, "days": 365},
}
CATEGORIES = ["General", "Student"]

# List of all passes
passes = []

# Calculate fee (25% discount for students)
def calculate_fee(pass_type, category):
    fee = PASS_TYPES[pass_type]["fee"]
    if category == "Student":
        fee = fee * (1 - STUDENT_DISCOUNT)
    return int(round(fee))

# Generate the next pass ID
def generate_id():
    if not passes:
        return "BP101"
    # Last number + 1
    return "BP" + str(max(int(p["id"][2:]) for p in passes) + 1)

# Return a pass as one line of text
def format_pass(p):
    return (p["id"] + " | " + p["name"] + " | " + p["route"] + " | "
            + p["type"] + " | Fee: Rs. " + str(p["fee"]))

# Check the pass type or category
def validate(text, valid_options):
    text = text.strip().capitalize()
    return text if text in valid_options else None

# Find a pass by ID
def find_pass(pass_id):
    for p in passes:
        if p["id"].upper() == pass_id.strip().upper():
            return p
    return None

# Save all passes to the file
def save_passes():
    try:
        with open(FILE_NAME, "w") as f:
            for p in passes:
                line = " | ".join([p["id"], p["name"], p["route"], p["type"],
                                   p["category"], str(p["fee"]),
                                   str(p["days"]), str(p["renewals"])])
                f.write(line + "\n")
    except IOError:
        print("Error: could not save passes to file.")

# Load passes from the file
def load_passes():
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = [x.strip() for x in line.strip().split("|")]
                # Skip invalid lines
                if len(parts) < 5 or parts[3] not in PASS_TYPES:
                    continue
                if len(parts) >= 8:
                    # Full format
                    category, fee = parts[4], int(parts[5])
                    days, renewals = int(parts[6]), int(parts[7])
                else:
                    # Short format
                    category = "General"
                    fee = int(parts[4].replace("Rs.", "").strip())
                    days, renewals = PASS_TYPES[parts[3]]["days"], 0
                passes.append({"id": parts[0], "name": parts[1],
                               "route": parts[2], "type": parts[3],
                               "category": category, "fee": fee,
                               "days": days, "renewals": renewals})
    except FileNotFoundError:
        pass  # File not found
    except (IOError, ValueError):
        print("Warning: some saved data could not be read.")

# Issue a new pass
def issue_pass():
    name = input("Name: ").strip()
    route = input("Route: ").strip()
    pass_type = validate(input("Type: "), PASS_TYPES)
    category = validate(input("Category: "), CATEGORIES)

    # Check input
    if not name or not route:
        print("Name and route cannot be empty. Pass not issued.")
        return
    if pass_type is None:
        print("Invalid pass type. Choose Monthly, Quarterly or Yearly. "
              "Pass not issued.")
        return
    if category is None:
        print("Invalid category. Choose General or Student. Pass not issued.")
        return

    new_pass = {
        "id": generate_id(), "name": name, "route": route,
        "type": pass_type, "category": category,
        "fee": calculate_fee(pass_type, category),
        "days": PASS_TYPES[pass_type]["days"], "renewals": 0,
    }
    passes.append(new_pass)
    save_passes()
    print("Pass issued. ID: " + format_pass(new_pass)
          + " | Valid: " + str(new_pass["days"]) + " days")

# Renew an existing pass
def renew_pass():
    p = find_pass(input("Enter pass ID to renew: "))
    if p is None:
        print("Pass not found.")
        return
    pass_type = validate(input("Renew as (Monthly/Quarterly/Yearly): "),
                         PASS_TYPES)
    if pass_type is None:
        print("Invalid pass type. Choose Monthly, Quarterly or Yearly. "
              "Pass not renewed.")
        return

    # Update the pass
    p["type"] = pass_type
    p["fee"] = calculate_fee(pass_type, p["category"])
    p["days"] = PASS_TYPES[pass_type]["days"]
    p["renewals"] += 1
    save_passes()
    print("Pass renewed. " + format_pass(p) + " | Valid: " + str(p["days"])
          + " days | Renewals: " + str(p["renewals"]))

# Search a pass by ID
def search_pass():
    p = find_pass(input("Enter pass ID: "))
    print("Pass not found." if p is None else format_pass(p))

# View all passes
def view_all():
    if not passes:
        print("No passes issued yet.")
        return
    print("--- All Bus Passes ---")
    for p in passes:
        print(format_pass(p))
    print("Total passes: " + str(len(passes)))

# Main program
def main():
    # Load saved passes
    load_passes()
    # Menu options
    actions = {"1": issue_pass, "2": renew_pass,
               "3": search_pass, "4": view_all}
    while True:
        print("\n===== BUS PASS MANAGEMENT SYSTEM =====")
        print("1. Issue new pass\n2. Renew pass\n3. Search pass by ID")
        print("4. View all passes\n5. Exit")
        choice = input("Menu option: ").strip()
        if choice == "5":
            print("Thank you. Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
