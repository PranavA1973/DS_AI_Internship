contacts = {
    "Pranav": "9876543210",
    "bhnaush": "9123456789",
    "Gagan": "9988776655"
}

contacts["Pranav"] = "9012345678"
contacts["bhanush"] = "9000000000"

existing_contact = contacts.get("sathwik", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")

print("Safe Lookup Results:")
print("sathwik:", existing_contact)
print("Eve:", missing_contact)

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
