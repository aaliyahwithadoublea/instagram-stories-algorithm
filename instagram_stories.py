# Instagram Stories Manager
# Data Structure : Circular Doubly Linked List
# Filter        : Linear Search  - O(n)
# Sort          : Merge Sort     - O(n log n)
# Language      : Python 3


class Node:
    """Represents a single Instagram story."""

    def __init__(self, user, story_type, duration, timestamp):
        self.user       = user          # who posted the story
        self.story_type = story_type    # caption | feedback | promotion
        self.duration   = duration      # length in seconds
        self.timestamp  = timestamp     # time posted, e.g. "09:00"
        self.next       = None          # pointer to next node
        self.prev       = None          # pointer to previous node