from datetime import datetime


# each social channel has a type
# and the current number of followers
class SocialChannel:
    def __init__(self, channel: str, followers: int):
        self.channel: str = channel
        self.followers: int = followers


class Youtube(SocialChannel):
    def greeting_message(self):
        self.greeting = "To all my dear youtubers..."
        return self.greeting


class Facebook(SocialChannel):
    def greeting_message(self):
        self.greeting = (
            "Read this lines, users of Lizardman's Social Network..."
        )
        return self.greeting


class Twitter(SocialChannel):
    def greeting_message(self):
        self.greeting = "Twit-twit, twit-twit..."
        return self.greeting


# each post has a message and the timestamp when it should be posted
class Post:
    def process_schedule(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return timestamp

    def post_a_message(self, channel: SocialChannel, message: str):
        timestamp = self.process_schedule()
        if isinstance(channel, Youtube):
            greeting = channel.greeting_message()
            print(f"{greeting}\n{message}\nPosted at: {timestamp}")
        elif isinstance(channel, Facebook):
            greeting = channel.greeting_message()
            print(f"{greeting}\n{message}\nPosted at: {timestamp}")
        elif isinstance(channel, Twitter):
            greeting = channel.greeting_message()
            print(f"{greeting}\n{message}\nPosted at: {timestamp}")
        else:
            print("nothing to share...")


youtube_channel = Youtube("Youtube", 1000)
facebook_channel = Facebook("Facebook", 100)
twitter_channel = Twitter("Twitter", 10000)

social_post = Post()

social_post.post_a_message(youtube_channel, "FUCK YOU!")
social_post.post_a_message(twitter_channel, "FUCK YOU!")
social_post.post_a_message(facebook_channel, "FUCK YOU!")
