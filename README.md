# Sherlock
-----
Extract interesting information about redditors from their submissions and comments. Outputs data in JSON format.

## Setup
-----
* Run `pip install -r requirements.txt` to install dependencies.
* Create .env file in the root containing:

```
REDDIT_CLIENT_ID=blahblahblah
REDDIT_SECRET=BlahBlahBlah
REDDIT_USER_AGENT="snoosnoop by /u/MemoryEmptyAgain"
```

## Usage
-----
```
python sherlock.py <reddit-username>
```

## Example
-------

### Command:
```
python sherlock.py MemoryEmptyAgain
```

### Output:
```
Processing user MemoryEmptyAgain
Data saved to MemoryEmptyAgain.json
Processing complete... 0:00:05.465406
```

## License
-------
MIT License
