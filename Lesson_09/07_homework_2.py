# each social channel has a type
# and the current number of followers
# each post has a message and the timestamp when it should be posted


# class SocialChannel:
#     def __init__(self, channel: str, followers: int):
#         self.channel = channel
#         self.followers = followers


# class Post:
#     def __init__(self, message: str, timestamp: int):
#         self.message = message
#         self.timestamp = timestamp

#     def post_a_message(channel: SocialChannel, message: str):
#         type, _ = channel
#         if type == "youtube":
#             post_to_youtube(channel, message)
#         elif type == "facebook":
#             post_to_facebook(channel, message)
#         elif type == "twitter":
#             post_to_twitter(channel, message)

#     def process_schedule(
#         posts: list[Post], channels: list[SocialChannel]
#     ) -> None:
#         for post in posts:
#             message, timestamp = post
#             for channel in channels:
#                 if timestamp <= time():
#                     post_a_message(channel, message)
