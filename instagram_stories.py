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


    # --- Merge Sort helpers ---

    def _get_middle(self, head, size):
        """Return the middle node of a list segment."""
        current = head
        for _ in range(size // 2 - 1):
            current = current.next
        return current

    def _merge(self, left, right, left_size, right_size):
        """
        Merge two sorted halves.
        Primary sort key  : duration (ascending)
        Secondary sort key: timestamp (ascending, used when durations are equal)
        """
        if not left:  return right
        if not right: return left

        left_wins = (
            left.duration < right.duration or
            (left.duration == right.duration and
             left.timestamp <= right.timestamp)
        )

        if left_wins:
            result      = left
            result.next = self._merge(left.next, right, left_size - 1, right_size)
        else:
            result      = right
            result.next = self._merge(left, right.next, left_size, right_size - 1)

        if result.next:
            result.next.prev = result

        return result

    def _merge_sort(self, head, size):
        """Recursively split the list and sort each half."""
        if size <= 1:
            return head

        middle     = self._get_middle(head, size)
        right_head = middle.next
        middle.next = None
        if right_head:
            right_head.prev = None

        left  = self._merge_sort(head, size // 2)
        right = self._merge_sort(right_head, size - size // 2)
        return self._merge(left, right, size // 2, size - size // 2)

    def sort_stories(self):
        """
        Sort stories by duration (primary) then timestamp (secondary).
        The circle is broken before sorting and restored after,
        because Merge Sort requires a clear start and end point.
        Algorithm       : Merge Sort
        Time Complexity : O(n log n)
        """
        if not self.head:
            return

        # break the circle
        self.tail.next = None
        self.head.prev = None

        # sort
        self.head = self._merge_sort(self.head, self.size)

        # restore the circle
        current = self.head
        while current.next:
            current = current.next
        self.tail          = current
        self.tail.next     = self.head
        self.head.prev     = self.tail

        print("[SORTED]  Stories sorted by duration, then timestamp.")


    def reverse(self):
        """
        Reverse the order of the feed by swapping all next and prev pointers,
        then swapping head and tail.
        Time Complexity: O(n)
        """
        if not self.head:
            return

        current = self.head
        for _ in range(self.size):
            current.next, current.prev = current.prev, current.next
            current = current.prev

        self.head, self.tail = self.tail, self.head
        print("[REVERSED] Feed order reversed.")


    def display(self):
        """Print all stories in the current feed order."""
        if not self.head:
            print("Feed is empty.")
            return

        current = self.head
        print(f"  {'Index':<6} {'User':<10} {'Type':<12} {'Duration':>9} {'Posted'}")
        print(f"  {'-'*5} {'-'*9} {'-'*11} {'-'*9} {'-'*6}")
        for i in range(self.size):
            print(f"  [{i}]   {current.user:<10} {current.story_type:<12} "
                  f"{current.duration:>6}s   {current.timestamp}")
            current = current.next
        print()