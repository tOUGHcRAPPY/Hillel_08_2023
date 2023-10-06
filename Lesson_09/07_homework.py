import time
from datetime import datetime

# each social channel has a type
# and the current number of followers


class SocialChannel:
    def __init__(self, followers: int):
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
    def __init__(self, message: str, channel: SocialChannel) -> None:
        self.message = message
        self.channel = channel

    def process_schedule(self, year, month, day, hour, minute: int):
        self.scheduled_time = datetime(year, month, day, hour, minute)
        print(self.scheduled_time)
        return self.scheduled_time

    def post_a_message(self):
        current_time = datetime.now()
        time_difference = self.scheduled_time - current_time
        time_in_seconds = time_difference.total_seconds()
        if time_in_seconds > 0:
            time.sleep(time_in_seconds)
        greeting = self.channel.greeting_message()
        print(f"{greeting}\n{self.message}\nPosted at: {current_time}.")


youtube_channel = Youtube(followers=1000)
facebook_channel = Facebook(followers=100)
twitter_channel = Twitter(followers=10000)

social_post_1 = Post(message="Help me...", channel=twitter_channel)

social_post_1.process_schedule(2023, 10, 6, 20, 50)

social_post_1.post_a_message()
