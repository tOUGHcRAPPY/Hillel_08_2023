from datetime import datetime
import time



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
    def process_schedule(self, year, month, day, hour, minute: int):
        self.scheduled_time = datetime(year, month, day, hour, minute)
        print(self.scheduled_time)
        return self.scheduled_time

    def post_a_message(self, channel: SocialChannel, message: str, scheduled_time: int):
        current_time = datetime.now()
        time_difference = scheduled_time - current_time
        time_in_seconds = time_difference.total_seconds()
        time.sleep(time_in_seconds)
        if isinstance(channel, Youtube):
            greeting = channel.greeting_message()
            print(f"{greeting}\n{message}\nPosted at:{current_time}.")
        elif isinstance(channel, Facebook):
            greeting = channel.greeting_message()
            print(f"{greeting}\n{message}\nPosted at:{current_time}.")
        elif isinstance(channel, Twitter):
            greeting = channel.greeting_message()
            print(f"{greeting}\n{message}\nPosted at:{current_time}.")
        else:
            print("nothing to share...")


youtube_channel = Youtube("Youtube", 1000)
facebook_channel = Facebook("Facebook", 100)
twitter_channel = Twitter("Twitter", 10000)

social_post = Post()

social_post.process_schedule(2023, 10, 4, 21, 55)

# social_post.post_a_message(youtube_channel, "Hello, World!", social_post.scheduled_time)
# social_post.post_a_message(twitter_channel, "Hello, World!", social_post.scheduled_time)
social_post.post_a_message(facebook_channel, "Hello, World!", social_post.scheduled_time)
