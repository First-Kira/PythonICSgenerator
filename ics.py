from datetime import datetime, timedelta

# Define the event start time
start_time = datetime(2025, 2, 5, 11, 0, 0)
end_time = start_time + timedelta(hours=2, minutes=30)

# Format the times for the ICS file
start_time_str = start_time.strftime("%Y%m%dT%H%M%SZ")
end_time_str = end_time.strftime("%Y%m%dT%H%M%SZ")

# Create the ICS file content
ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My Company//My Product//EN
BEGIN:VEVENT
UID:{start_time_str}-unique@mycompany.com
DTSTAMP:{datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}
DTSTART:{start_time_str}
DTEND:{end_time_str}
SUMMARY:Sample Event
DESCRIPTION:This is a sample event scheduled for 2 hours and 30 minutes.
LOCATION:Virtual
END:VEVENT
END:VCALENDAR"""

# Save the content to an ICS file
with open("event.ics", "w") as file:
    file.write(ics_content)

print("ICS file created successfully!")

