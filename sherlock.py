import sys
import datetime

from reddit_user import RedditUser, UserNotFoundError, NoDataError

print(f"Processing user {sys.argv[1]}")
start = datetime.datetime.now()
try:
    u = RedditUser(sys.argv[1])
    print(u)
except UserNotFoundError:
    print(f"User {sys.argv[1]} not found")
except NoDataError:
    print(f"No data available for user {sys.argv[1]}")

print(f"Processing complete... {datetime.datetime.now() - start}")
