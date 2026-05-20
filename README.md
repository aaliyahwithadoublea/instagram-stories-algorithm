# Instagram Stories Algorithm

A Data Structures and Algorithms project implementing an Instagram Stories feed manager using a Circular Doubly Linked List in Python.

---

## Overview

| Component | Choice |
|---|---|
| Real-World Example | Instagram Stories Manager |
| Data Structure | Circular Doubly Linked List |
| Filter Algorithm | Linear Search |
| Sort Algorithm | Merge Sort |
| Primary Sort Key | Duration (ascending) |
| Secondary Sort Key | Timestamp (ascending) |
| Filter Attribute | Story Type (caption, feedback, promotion) |
| Language | Python 3 |
| Interface | Command Line |

---

## Project Structure

```
instagram-stories-algorithm/
|
|-- instagram_stories.py    # all classes and operations
|-- README.md               # project documentation
```

---

## Data Structure

### Circular Doubly Linked List

Each story is stored as a node. Every node holds the story data and two pointers — one to the next story and one to the previous story. The last node points back to the first, forming a circle.

```
head                                              tail
 |                                                 |
[Alice] <-> [Bob] <-> [Carol] <-> [Dave] <-> [Eve]
  ^                                               |
  |_______________________________________________|
              loops back to head
```

This structure was chosen because Instagram Stories naturally loop — when the last story ends, the feed returns to the first. A Circular Doubly Linked List mirrors this behavior directly.

### Node Attributes

| Attribute | Type | Description |
|---|---|---|
| user | string | Who posted the story |
| story_type | string | caption, feedback, or promotion |
| duration | int | Length of the story in seconds |
| timestamp | string | Time the story was posted |
| next | Node | Pointer to the next story |
| prev | Node | Pointer to the previous story |

---

## Operations

### Add
Inserts a new story at the tail and reconnects the circle.

```python
feed.add_story("Alice", "promotion", 15, "09:00")
```

Time Complexity: O(1)

---

### Delete by Index
Removes the story at a given position (0-based index). Relinks the surrounding nodes to maintain the circular structure.

```python
feed.delete_by_index(2)
```

Time Complexity: O(n) to traverse, O(1) to delete

---

### Update
Updates one or more attributes of the story at a given index. Only the arguments provided are changed.

```python
feed.update_story(1, story_type="promotion", duration=25)
```

Time Complexity: O(n)

---

### Filter
Returns all stories that match a given story type. Traverses the full list exactly once using Linear Search.

```python
feed.filter_by_type("promotion")
```

Algorithm: Linear Search  
Time Complexity: O(n)

Note: Filter differs from Search. Search finds one item and stops. Filter traverses the entire list and returns every match.

---

### Sort
Sorts stories by duration (shortest first). If two stories share the same duration, they are sorted by timestamp (earliest first).

The circle is temporarily broken before sorting because Merge Sort requires a defined start and end. It is restored once sorting is complete.

```python
feed.sort_stories()
```

Algorithm: Merge Sort  
Time Complexity: O(n log n)  
Primary sort key: duration  
Secondary sort key: timestamp  

Merge Sort was chosen because it only requires forward traversal, which suits linked lists. Bubble Sort is O(n^2) and too slow for large datasets. Quick Sort requires random access, which linked lists do not support.

---

### Reverse
Swaps the next and prev pointers on every node, then swaps head and tail.

```python
feed.reverse()
```

Time Complexity: O(n)

---

## Complexity Summary

| Operation | Time Complexity |
|---|---|
| Add | O(1) |
| Delete by Index | O(n) |
| Update | O(n) |
| Filter | O(n) |
| Sort | O(n log n) |
| Reverse | O(n) |

---

## How to Run

Requires Python 3. No external dependencies.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/instagram-stories-algorithm.git

# Navigate into the project folder
cd instagram-stories-algorithm

# Run the program
python instagram_stories.py
```

---

## Sample Output

```
INSTAGRAM STORIES MANAGER
=============================================

-- PREFILL: 5 stories
[ADDED]   Alice | promotion | 15s | 09:00
[ADDED]   Bob | caption | 8s | 09:30
[ADDED]   Carol | feedback | 12s | 10:00
[ADDED]   Dave | promotion | 5s | 10:30
[ADDED]   Eve | caption | 20s | 11:00

  Index  User       Type         Duration Posted
  ----- --------- ----------- --------- ------
  [0]   Alice      promotion       15s   09:00
  [1]   Bob        caption          8s   09:30
  [2]   Carol      feedback        12s   10:00
  [3]   Dave       promotion        5s   10:30
  [4]   Eve        caption         20s   11:00

-- SORT: by duration then timestamp
[SORTED]  Stories sorted by duration, then timestamp.

  Index  User       Type         Duration Posted
  ----- --------- ----------- --------- ------
  [0]   Dave       promotion        5s   10:30
  [1]   Bob        caption          8s   09:30
  [2]   Carol      feedback        12s   10:00
  [3]   Alice      promotion       15s   09:00
  [4]   Eve        caption         20s   11:00
```

---

## Authors

Aaliyah Momodu