# Program Name: ChocAn System
# Programmer Name: Group 4
# Description: Final ChocAn system with member validation, service recording,
# provider directory, and weekly report generation
# Date Created: 04/19/2026

import os

# -----------------------------
# Sample Data
# -----------------------------
members = {
    "123456789": "active",
    "222222222": "suspended",
    "987654321": "active"
}

services = {
    "598470": "Dietitian Session",
    "883948": "Aerobics Session",
    "111111": "Therapy Session"
}

recorded_services = []


# -----------------------------
# Utility: Clear Screen
# -----------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# -----------------------------
# Utility: Pause for user
# -----------------------------
def pause():
    input("\nPress Enter to return to the main menu...")


# -----------------------------
# Function: Validate Member
# Description: Checks if member ID is valid and active
# Pre-condition: member_id is provided
# Post-condition: Returns validation message
# -----------------------------
def validate_member(member_id):
    if member_id not in members:
        return "Invalid member number"
    elif members[member_id] == "suspended":
        return "Member suspended"
    else:
        return "Validated"


# -----------------------------
# Function: Record Service
# Description: Records a service for a valid member
# Pre-condition: member_id and service_code provided
# Post-condition: Service recorded or error returned
# -----------------------------
def record_service(member_id, date, service_code):
    validation = validate_member(member_id)

    if validation != "Validated":
        return validation

    if service_code not in services:
        return "Invalid service code"

    service_name = services[service_code]
    print(f"\nService found: {service_name}")
    confirm = input("Confirm this service? (yes/no): ").strip().lower()
    if confirm != "yes":
        return "Service recording cancelled"

    recorded_services.append((member_id, date, service_name))
    return "Service recorded successfully"


# -----------------------------
# Function: Provider Directory
# Description: Displays available services
# -----------------------------
def display_provider_directory():
    clear()
    print("=" * 40)
    print("       Provider Directory")
    print("=" * 40)
    print(f"\n{'Code':<10} {'Service Name'}")
    print("-" * 30)
    for code, name in services.items():
        print(f"{code:<10} {name}")


# -----------------------------
# Function: Generate Reports
# Description: Displays recorded services
# -----------------------------
def generate_reports():
    clear()
    print("=" * 40)
    print("         Weekly Report")
    print("=" * 40)
    print("\nWeekly Reports Generated Successfully")
    print("\nRecorded Services:")
    print("-" * 50)
    if not recorded_services:
        print("No services recorded")
    else:
        for service in recorded_services:
            print(f"  Member ID : {service[0]}")
            print(f"  Date      : {service[1]}")
            print(f"  Service   : {service[2]}")
            print("-" * 50)
    print(f"\nTotal services recorded: {len(recorded_services)}")


# -----------------------------
# Function: Validate Member (interactive)
# -----------------------------
def interactive_validate_member():
    clear()
    print("=" * 40)
    print("       Member Validation")
    print("=" * 40)
    member_id = input("\nEnter member ID (9 digits): ").strip()
    result = validate_member(member_id)
    print(f"\nResult: {result}")
    pause()


# -----------------------------
# Function: Record Service (interactive)
# -----------------------------
def interactive_record_service():
    clear()
    print("=" * 40)
    print("         Record a Service")
    print("=" * 40)
    member_id = input("\nEnter member ID (9 digits): ").strip()
    date = input("Enter date of service (MM-DD-YYYY): ").strip()
    display_provider_directory()
    service_code = input("\nEnter service code (6 digits): ").strip()
    result = record_service(member_id, date, service_code)
    print(f"\nResult: {result}")
    pause()


# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        clear()
        print("=" * 40)
        print("   Welcome to the ChocAn System")
        print("=" * 40)
        print("\nMain Menu:")
        print("  1. Validate Member")
        print("  2. Record a Service")
        print("  3. View Provider Directory")
        print("  4. Generate Weekly Report")
        print("  5. Exit")
        print()

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            interactive_validate_member()

        elif choice == "2":
            interactive_record_service()

        elif choice == "3":
            display_provider_directory()
            pause()

        elif choice == "4":
            generate_reports()
            pause()

        elif choice == "5":
            clear()
            print("\nExiting ChocAn System. Goodbye!\n")
            break

        else:
            print("\nInvalid option. Please enter a number between 1 and 5.")
            pause()


if __name__ == "__main__":
    main()
