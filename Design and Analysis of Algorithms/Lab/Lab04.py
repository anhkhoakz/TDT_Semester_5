def find_element(arr: list, element: int, start: int, end: int) -> int:
    """Find an element in an ascending sorted array using recursion

    Args:
        arr (list): the array to search
        element (int): the element to find
        start (int): the start index of the array
        end (int): the end index of the array

    Returns:
        int: the index of the element in the array
    """
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == element:
        return mid
    if arr[mid] < element:
        return find_element(arr, element, mid + 1, end)
    return find_element(arr, element, start, mid - 1)


def partition(arr: list, start: int, end: int) -> int:
    """Partition the array for quick sort

    Args:
        arr (list): the array to partition
        start (int): the start index of the array
        end (int): the end index of the array

    Returns:
        int: the pivot index
    """
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def sort_array_quick_sort(arr: list, start: int, end: int) -> list:
    """Sort an array using quick sort algorithm

    Args:
        arr (list): the array to sort
        start (int): the start index of the array
        end (int): the end index of the array

    Returns:
        list: the sorted array
    """
    if start < end:
        pivot = partition(arr, start, end)
        sort_array_quick_sort(arr, start, pivot - 1)
        sort_array_quick_sort(arr, pivot + 1, end)
    return arr

class Node:
    def __init__(self: int, value: int) -> None:
        """Initialize a new Node.

        Args:
            value (int): The value to be stored in the Node.
        """
        self.value = value
        self.left = None
        self.right = None

def height_of_binary_tree(root: Node) -> int:
    """Identify the height of a binary tree

    Args:
        root (Node): the root of the binary tree

    Returns:
        int: the height of the binary tree
    """
    if root is None:
        return -1
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)
    return max(left_height, right_height) + 1


# Traverse a binary tree in Pre-order, Post-order, In-order

def pre_order_traversal(root: Node) -> None:
    """Perform pre-order traversal on a binary tree.

    Args:
        root (Node): The root node of the binary tree.
    """
    if root is None:
        return
    print(root.value)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
    


def main() -> None:
    # Ex01
    arr = [1, 2, 3, 4, 5]
    element = 3
    start = 0
    end = len(arr) - 1
    print("\nEx01: Find element in array")
    print(find_element(arr, element, start, end))

    # Ex02
    arr = [5, 4, 3, 2, 1]
    start = 0
    end = len(arr) - 1
    print("\nEx02: Sort array using quick sort")
    print(sort_array_quick_sort(arr, start, end))
    
    # Ex03
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    print("\nEx03: Height of binary tree")
    print(height_of_binary_tree(root))
    print(height_of_binary_tree(root.left.left.left))
    
    # Ex04
    print("\nEx04: Pre-order traversal of binary tree")
    pre_order_traversal(root)
    

if __name__ == "__main__":
    main()
