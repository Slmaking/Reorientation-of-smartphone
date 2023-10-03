import datetime

from datetime import datetime

# Convert milliseconds timestamp to seconds by dividing by 1000
timestamp_in_milliseconds = int("1681591751148")
timestamp_in_seconds = timestamp_in_milliseconds / 1000

# Convert Unix timestamp to a human-readable date and time format
formatted_datetime = datetime.utcfromtimestamp(timestamp_in_seconds).strftime('%Y-%m-%d %H:%M:%S')

print(formatted_datetime)



def convert_to_datetime(timestamp_ms):
    timestamp_seconds = timestamp_ms / 1000  # Convert milliseconds to seconds
    return datetime.utcfromtimestamp(timestamp_seconds).strftime('%Y-%m-%d %H:%M:%S')

# Apply the function to create a new 'datetime' column
df['Commence_time'] = df['start_time'].apply(convert_to_datetime)

# Display the DataFrame
print(df)
