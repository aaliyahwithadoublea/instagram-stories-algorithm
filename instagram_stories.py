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
        self.head = None
        self.tail = None
        self.size = 0


    def prefill(self):
        """Load 5 default stories with different values."""
        self.add_story("Alice", "promotion", 15, "09:00")
        self.add_story("Bob",   "caption",    8, "09:30")
        self.add_story("Carol", "feedback",  12, "10:00")
        self.add_story("Dave",  "promotion",  5, "10:30")
        self.add_story("Eve",   "caption",   20, "11:00")


    def add_story(self, user, story_type, duration, timestamp):
        """
        Insert a new story at the tail of the feed.
        Time Complexity: O(1)
        """
        new_node = Node(user, story_type, duration, timestamp)

        if self.head is None:
            self.head      = new_node
            self.tail      = new_node
            new_node.next  = new_node
            new_node.prev  = new_node
        else:
            new_node.prev      = self.tail
            new_node.next      = self.head
            self.tail.next     = new_node
            self.head.prev     = new_node
            self.tail          = new_node

        self.size += 1
        print(f"[ADDED]   {user} | {story_type} | {duration}s | {timestamp}")


    def delete_by_index(self, index):
        """
        Remove the story at a given index (0-based).
        Time Complexity: O(n) to traverse, O(1) to delete.
        """
        if not self.head:
            print("[ERROR]   No stories to delete.")
            return

        if index < 0 or index >= self.size:
            print(f"[ERROR]   Invalid index. Valid range: 0 to {self.size - 1}.")
            return

        current = self.head
        for i in range(index):
            current = current.next

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
            if current == self.tail:
                self.tail = current.prev

        self.size -= 1
        print(f"[DELETED] Index {index}: {current.user} | {current.story_type}")


    def update_story(self, index, user=None, story_type=None,
                     duration=None, timestamp=None):
        """
        Update one or more attributes of the story at a given index.
        Only the provided arguments are updated.
        Time Complexity: O(n)
        """
        if not self.head:
            print("[ERROR]   No stories to update.")
            return

        if index < 0 or index >= self.size:
            print(f"[ERROR]   Invalid index. Valid range: 0 to {self.size - 1}.")
            return

        current = self.head
        for i in range(index):
            current = current.next

        if user:        current.user       = user
        if story_type:  current.story_type = story_type
        if duration:    current.duration   = duration
        if timestamp:   current.timestamp  = timestamp

        print(f"[UPDATED] Index {index}: {current.user} | "
              f"{current.story_type} | {current.duration}s | {current.timestamp}")


    def filter_by_type(self, story_type):
        """
        Return all stories matching a given story type.
        Traverses the full list exactly once.
        Algorithm       : Linear Search
        Time Complexity : O(n)
        """
        if not self.head:
            print("[ERROR]   No stories available.")
            return

        print(f"[FILTER]  Showing all '{story_type}' stories:")
        current = self.head
        found   = False

        for _ in range(self.size):
            if current.story_type == story_type:
                print(f"          {current.user} | {current.story_type} | "
                      f"{current.duration}s | {current.timestamp}")
                found = True
            current = current.next

        if not found:
            print(f"          No '{story_type}' stories found.")