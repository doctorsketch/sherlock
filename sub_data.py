# -*- coding: utf-8 -*-

import csv

subreddits = []

"""
CSV file has the following columns:
name            - Subreddit name
topic_level1    - Level 1 topic. For instance, Entertainment.
topic_level2    - Level 2 topic. For instance, TV Shows.
topic_level3    - Level 2 topic. For instance, Sherlock.
default         - Y if default sub, blank otherwise.
ignore_text     - Y if text in sub needs to be ignored, blank otherwise.
sub_attribute   - An attribute we can derive from this subreddit. 
                  For instance, gender, religion, gadget, etc.
sub_value       - Value for the above attribute. 
                  For instance, male, atheism, iPhone, etc.
"""

with open("subreddits.csv", "r", encoding='utf-8') as subreddits_file:
    reader = csv.reader(subreddits_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) != 8:
            print(f"Warning: Row has {len(row)} columns: {row}")
            continue
            
        name, topic_level1, topic_level2, topic_level3, default, ignore_text, sub_attribute, sub_value = row
        
        subreddit = {
            "name": name,
            "topic_level1": topic_level1,
            "topic_level2": topic_level2,
            "topic_level3": topic_level3,
            "default": default,
            "ignore_text": ignore_text,
            "attribute": sub_attribute.lower(),
            "value": sub_value.lower()
        }
        subreddits.append(subreddit)
