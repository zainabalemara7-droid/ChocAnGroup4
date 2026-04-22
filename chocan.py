# Program Name: ChocAn System
# Programmer Name: Group 4
# Description: Partial implementation of the ChocAn system including
# member validation, service recording, provider directory request,
# and basic weekly report generation.
# Date Created: 04/19/2026

# Sample data used for current implementation
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

service_records = []


# Description: Validates a member ID and returns the validation result.
# Pre-condition: A member ID must be entered by the user.
# Post-condition: Returns whether the member is validated, invalid, or suspended.
def validate_member(member_id):
    if member_id == "" or not member_id.isdigit():
        return "Invalid member number"
    elif member_id not in members:
        return "Invalid member number"
    elif members[member_id] == "suspended":
        return "Member suspended"
    else:
        return "Validated"


# Description: Records a service if the member ID and service code are valid.
# Pre-condition: A valid member ID, service date, and service code must be entered.
# Post-condition: Stores the service record or returns an error message.
def record_service(member_id, service_date, service_code):
    member_result = validate_member(member_id)

    if member_result != "Validated":
        return member_result

    if service_code == "" or service_code not in services:
        return "Invalid service code"

    record = {
        "member_id": member_id,
        "date": service_date,
        "service_code": service_code,
        "service_name": services[service_code]
    }

    service_records.append(record)
    return "Service recorded successfully"


# Description: Displays the provider directory or an unavailable message.
# Pre-condition: The service directory must exist in the system.
# Post-condition: Returns the full provider directory or an error message.
def request_provider_directory():
    if len(services) == 0:
        return "Directory unavailable"

    directory = "Provider Directory:\n"
    for code, name in services.items():
        directory += f"{code} - {name}\n"

    return directory


# Description: Generates a simple weekly report based on recorded services.
# Pre-condition: Service records may or may not exist.
# Post-condition: Returns a report summary or a notice if no data exists.
def generate_weekly_reports():
    if len(service_records) == 0:
        return "Empty/notice report generated"

    report = "Weekly Reports Generated Successfully\n"
    report += "Recorded Services:\n"

    for record in service_records:
        report += (
            f"Member ID: {record['member_id']}, "
            f"Date: {record['date']}, "
            f"Service: {record['service_name']}\n"
        )

    return report


# Description: Main driver function for testing current system functionality.
# Pre-condition: Program must be run by user.
# Post-condition: Displays current ChocAn functionality results.
def main():
    print("ChocAn System")
    print()

    # Member validation examples
    print("Validation Test 1:", validate_member("123456789"))
    print("Validation Test 2:", validate_member("999999999"))
    print("Validation Test 3:", validate_member("222222222"))
    print()

    # Service recording examples
    print("Record Test 1:", record_service("123456789", "04-14-2026", "598470"))
    print("Record Test 2:", record_service("999999999", "04-14-2026", "598470"))
    print("Record Test 3:", record_service("123456789", "04-14-2026", "000000"))
    print()

    # Provider directory example
    print(request_provider_directory())
    print()

    # Report generation example
    print(generate_weekly_reports())


main()