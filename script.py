from instabot import Bot
import re
import argparse
from pprint import pprint

def createParser():
    parser = argparse.ArgumentParser(description='Find users with right rules')
    parser.add_argument('post_link', help='The link of the post', default='https://www.instagram.com/p/B3lqfWLIO6w/')
    parser.add_argument('-l', '--post_author', help='Your account', default='kvartal_vocal')

    return parser


def get_user_name(input_string):
    return re.findall("(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)", input_string)


def is_user_exist(username):
    return bot.get_user_id_from_username(username) is not None


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    post_link = args.post_link
    post_author = args.post_author
    print(post_author)

    bot = Bot()
    bot.login(username="YOUR_LOGIN", password="YOUR_PASSWORD")

    media_id = bot.get_media_id_from_link(post_link)
    comments = bot.get_media_comments_all(media_id)
    likers = bot.get_media_likers(media_id)
    followers = bot.get_user_followers(post_author)

    users = []
    for comment in comments:
        user_id = comment['user_id']

        if str(user_id) in likers and str(user_id) in followers:
            user_friends = get_user_name(comment['text'])
            for friend in user_friends:
                if is_user_exist(friend):
                    users.append(comment['user']['username'])

    uniq_users = list(set(users))
    pprint(uniq_users)



