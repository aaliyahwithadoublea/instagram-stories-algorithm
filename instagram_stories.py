# Instagram Stories Manager
# Data Structure : Circular Doubly Linked List
# Filter        : Linear Search  - O(n)
# Sort          : Merge Sort     - O(n log n)
# Language      : Python 3


class Node:
    """Represents a single Instagram story."""

    def __init__(self, user, story_type, duration, timestamp):
        self.user       = user
        self.story_type = story_type
        self.duration   = duration
        self.timestamp  = timestamp
        self.next       = None
        self.prev       = None


class InstagramStories:
    """
    Circular Doubly Linked List implementation of an Instagram Stories feed.

    Stories loop back to the beginning when the end is reached,
    matching the natural behavior of Instagram Stories.
    """

    def __init__(self):
        self.head = None  # first story in the feed
        self.tail = None  # last story in the feed
        self.size = 0     # total number of stories


    def prefill(self):
        """Load 5 default stories with different values."""
        self.add_story("Alice", "promotion", 15, "09:00")
        self.add_story("Bob",   "caption",    8, "09:30")
        self.add_story("Carol", "feedback",  12, "10:00")
        self.add_story("Dave",  "promotion",  5, "10:30")
        self.add_story("Eve",   "caption",   20, "11:00")