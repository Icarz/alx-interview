#!/usr/bin/python3
"""
0-lockboxes.py
Determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    if not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False

    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            # Add keys only if they point to a valid box index
            for key in boxes[current_box]:
                if isinstance(key, int) and 0 <= key < n:
                    stack.append(key)

    return len(visited) == n
