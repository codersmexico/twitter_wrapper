from twitter import Twitter, OAuth


def get_twitter(access_key, access_secret, consumer_key, consumer_secret):
    """
    Returns an authenticated Twitter object
    :param access_key: access_key.
    :param access_secret: access_secret.
    :param consumer_key: consumer_key.
    :param consumer_secret: consumer_secret.
    :return: An authenticated Twitter object
    """
    return Twitter(auth=OAuth(access_key, access_secret, consumer_key, consumer_secret))


def post(twitter, message):
    """
    Posts a new message using the twitter account.
    :param twitter: An authenticated Twitter object.
    :param message: The message to be tweeted by the user.
    :return: Results of the status update.
    """
    return twitter.statuses.update(status=message)


def search(twitter, search_string):
    """
    Searches for something using Twitter's search API.
    :param twitter: An authenticated Twitter object.
    :param search_string: The query to search for.
    :return:
    """
    return twitter.search.tweets(q=search_string)
