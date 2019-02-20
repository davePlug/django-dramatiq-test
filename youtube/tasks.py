import dramatiq


@dramatiq.actor
def get_videos(channel):
    print(channel)
    print("hello")