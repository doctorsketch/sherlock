import sys
import datetime
import json

from reddit_user import RedditUser, UserNotFoundError, NoDataError

# Ensure the user has provided a username argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py <username>")
    sys.exit(1)

username = sys.argv[1]
print(f"Processing user {username}")
start = datetime.datetime.now()
try:
    u = RedditUser(username)
    # Assuming u is JSON formatted as a string, load it to a dictionary
    user_data = json.loads(str(u))  # Use str(u) if u.__str__() returns a JSON string
    # Write the user_data to a file named username.json
    with open(f"{username}.json", "w") as file:
        json.dump(user_data, file, indent=4)  # Pretty-print with an indent of 4 spaces
except UserNotFoundError:
    print(f"User {username} not found")
except NoDataError:
    print(f"No data available for user {username}")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Processing complete... {datetime.datetime.now() - start}")
