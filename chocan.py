# Program Name: ChocAn System
# Programmer Name: Group 4
# Description: Final ChocAn system with member validation, service recording,
# provider directory, and weekly report generation
# Date Created: 04/19/2026


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

    recorded_services.append((member_id, date, services[service_code]))
    return "Service recorded successfully"


# -----------------------------
# Function: Provider Directory
# Description: Displays available services
# -----------------------------
def display_provider_directory():
    print("\nProvider Directory:")
    for code, name in services.items():
        print(code, "-", name)


# -----------------------------
# Function: Generate Reports
# Description: Displays recorded services
# -----------------------------
def generate_reports():
    print("\nWeekly Reports Generated Successfully")
    print("Recorded Services:")

    if not recorded_services:
        print("No services recorded")
    else:
        for service in recorded_services:
            print("Member ID:", service[0], ", Date:", service[1], ", Service:", service[2])


# -----------------------------
# TEST EXECUTION (matches Test Plan)
# -----------------------------
print("ChocAn System\n")

# Member Validation Tests
print("Test 1 - Validate active member:", validate_member("123456789"))
print("Test 2 - Validate invalid member:", validate_member("999999999"))
print("Test 3 - Validate suspended member:", validate_member("222222222"))

# Service Recording Tests
print("\nTest 4 - Record valid service:",
      record_service("123456789", "04-14-2026", "598470"))

print("Test 5 - Record service with invalid member:",
      record_service("999999999", "04-14-2026", "598470"))

print("Test 6 - Record service with invalid code:",
      record_service("123456789", "04-14-2026", "000000"))

# Provider Directory
print("\nTest 7 - Provider directory request:")
display_provider_directory()

# Weekly Reports
print("\nTest 9 - Generate weekly reports:")
generate_reports()