
# Bus Pass Management System
# Project Statement No. 54

import os

FILE = "buspass.txt"

# Pass types and their fees
PASS_TYPES = {
    "Monthly": (30, 500),
    "Quarterly": (90, 1350),
    "Yearly": (365, 4800)
}

CATEGORIES = ["General", "Student"]


# Load saved passes from file
def load_passes():
    passes = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                p = [x.strip() for x in line.split("|")]

                if len(p) >= 5 and p[3] in PASS_TYPES:
                    try:
                        fee = float(p[4].replace("Rs.", "").strip())
                        category = p[5] if len(p) > 5 else "General"

                        passes.append({
                            "id": p[0],
                            "name": p[1],
                            "route": p[2],
                            "type": p[3],
                            "fee": fee,
                            "category": category
                        })
                    except ValueError:
                        continue

    return passes


# Save passes in file
def save_passes(passes):
    with open(FILE, "w") as f:
        for p in passes:
            f.write(
                f'{p["id"]} | {p["name"]} | {p["route"]} | '
                f'{p["type"]} | Rs. {p["fee"]:g} | {p["category"]}\n'
            )


# Generate pass ID
def new_id(passes):
    numbers = []

    for p in passes:
        if p["id"].startswith("BP") and p["id"][2:].isdigit():
            numbers.append(int(p["id"][2:]))

    return "BP" + str(max(numbers, default=100) + 1)


# Get passenger details
def get_details():
    name = input("Enter name: ").strip()
    route = input("Enter route: ").strip()
    kind = input("Enter type (Monthly/Quarterly/Yearly): ").strip().title()
    category = input("Enter category (General/Student): ").strip().title()

    if not name or not route:
        print("Name and route cannot be empty.")
        return None

    if kind not in PASS_TYPES:
        print("Invalid pass type. Choose Monthly, Quarterly or Yearly.")
        return None

    if category not in CATEGORIES:
        print("Invalid category. Choose General or Student.")
        return None

    days, fee = PASS_TYPES[kind]

    if category == "Student":
        fee = fee * 0.75

    return {
        "name": name,
        "route": route,
        "type": kind,
        "category": category,
        "fee": fee,
        "validity": days
    }


# Display a pass
def show_pass(p):
    print(
        f'{p["id"]} | {p["name"]} | {p["route"]} | '
        f'{p["type"]} | Fee: Rs. {p["fee"]:g}'
    )


# Issue a new pass
def issue_pass(passes):
    p = get_details()

    if p is None:
        print("Pass not issued.")
        return

    p["id"] = new_id(passes)
    passes.append(p)
    save_passes(passes)

    print(
        f'Pass issued. ID: {p["id"]} | {p["name"]} | '
        f'{p["route"]} | {p["type"]} | Fee: Rs. {p["fee"]:g} '
        f'| Valid: {p["validity"]} days'
    )


# Renew an existing pass
def renew_pass(passes):
    pid = input("Enter pass ID to renew: ").strip().upper()

    for p in passes:
        if p["id"].upper() == pid:
            details = get_details()

            if details is None:
                print("Pass not renewed.")
                return

            p.update(details)
            save_passes(passes)

            print("Pass renewed successfully.")
            show_pass(p)
            return

    print("Pass ID not found.")


# Search pass by ID
def search_pass(passes):
    pid = input("Enter pass ID to search: ").strip().upper()

    for p in passes:
        if p["id"].upper() == pid:
            show_pass(p)
            return

    print("Pass not found.")


# Main program
def main():
    passes = load_passes()

    while True:
        print("\n===== BUS PASS MANAGEMENT SYSTEM =====")
        print("1. Issue New Pass")
        print("2. Renew Pass")
        print("3. Search Pass")
        print("4. View All Passes")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            issue_pass(passes)

        elif choice == "2":
            renew_pass(passes)

        elif choice == "3":
            search_pass(passes)

        elif choice == "4":
            if passes:
                for p in passes:
                    show_pass(p)
            else:
                print("No passes issued yet.")

        elif choice == "5":
            save_passes(passes)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid menu option. Try again.")


if __name__ == "__main__":
    main()
