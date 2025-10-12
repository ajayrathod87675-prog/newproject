import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Enter the mobile number with country code
number = "+918767012177"  # Example: +91 for India

# Parse the number
phone = phonenumbers.parse(number)

# Get details
print("Country/Region:", geocoder.description_for_number(phone, "en"))
print("Carrier:", carrier.name_for_number(phone, "en"))
print("Time Zones:", timezone.time_zones_for_number(phone))
