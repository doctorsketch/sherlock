Sherlock
========

Extract interesting information about redditors from their submissions and comments. Outputs data in JSON format.

Dependencies
------------
* [pytz](https://pypi.python.org/pypi/pytz/)
* [TextBlob 0.9.0](http://textblob.readthedocs.org/en/dev/)

Setup
-----
* Run `pip install -r requirements.txt` to install dependencies.
* Run `python -m textblob.download_corpora` to download TextBlob corpora.
* Create .env file in the root containing:

    REDDIT_CLIENT_ID=blahblahblah
    REDDIT_SECRET=BlahBlahBlah
    REDDIT_USER_AGENT="snoosnoop by /u/MemoryEmptyAgain"


Usage
-----
    python sherlock.py <reddit-username>
    
Example
-------
Command:

    python sherlock.py MemoryEmptyAgain

Output:

    Processing user MemoryEmptyAgain
    Data saved to MemoryEmptyAgain.json
    Processing complete... 0:00:05.465406


License
-------
MIT License