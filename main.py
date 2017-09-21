import config
from twitter_wrapper import get_twitter, post, search

# Authenticated Twitter API object.
twitter = get_twitter(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret)

# Search mentions @RevisaMiGrieta
print("--------------------MENTIONS--------------------")
query = search(twitter, "@RevisaMiGrieta")
print("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))

# Print Results
for result in query["statuses"]:
    if 'Ayuda' in result["text"]:
        print("@%s: %s" % (result["user"]["screen_name"], result["text"]))

    # No one has replied to this message
    if result['in_reply_to_status_id'] is None:
        print(">>> %s <<<" % ("@%s: %s" % (result["user"]["screen_name"], result["text"]),))

print("--------------------HASHTAGS--------------------")
# Search for hashtags
query = search(twitter, "#RevisaMiGrieta")
# Print Results
for result in query["statuses"]:
    if 'Ayuda' in result["text"]:
        print()

    # No one has replied to this message
    if result['in_reply_to_status_id'] is None:
        print(">>> %s <<<" % ("@%s: %s" % (result["user"]["screen_name"], result["text"]),))

# Post something:
# results = post(twitter, "Testing 123.")
