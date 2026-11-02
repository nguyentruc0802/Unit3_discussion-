"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Just using the built-in insert method here
    lst.insert(index, value)

    # [Performance]
    # - Index 0 (Start): Worst case O(n). We have to move absolutely everything.
    # - Middle: Average case O(n). We shift about half the items.
    # - End: Best case O(1). No shifting needed, it just goes right at the back.
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Need to check if the index is actually valid first.
    # If we don't, Python will throw an IndexError and crash the script.
    if index < 0 or index >= len(lst):
        # Safe exit if the index is out of bounds
        return None

    # pop() grabs the item out and closes the gap.
    # Everything to the right of this index has to shift one slot to the left.
    # Speed is O(n) for start/middle because of shifting, but O(1) at the very end.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # We are looping through the list item by item from start to finish.
    # Since the list isn't sorted, we can't skip anything.
    # Worst case is O(n) if the item is at the end or completely missing.
    for i in range(len(lst)):
        if lst[i] == value:
            return i  # Found it, return the index

    return -1  # Checked everywhere and didn't find it


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.
    # Simple starting list with games

    inventory = ["Minecraft", "Elden Ring", "Cyberpunk"]
    print(f"Original list: {inventory}")

    # Test 1: Front of the list (shifts everything)
    insert_at(inventory, 0, "Zelda")
    print(f"After insertion at the BEGINNING (Index 0): {inventory}")

    # Test 2: Middle of the list (shifts everything after index 2)
    insert_at(inventory, 2, "Terraria")
    print(f"After insertion in the MIDDLE (Index 2): {inventory}")

    # Test 3: Back of the list (fast, no shifting)
    insert_at(inventory, len(inventory), "Doom")
    print(f"After insertion at the END: {inventory}")

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Test 1: Pop the first item (everything shifts left)
    removed_start = delete_at(inventory, 0)
    print(f"Removed element (BEGINNING): {removed_start}")
    print(f"List after deletion at the beginning: {inventory}")

    # Test 2: Pop a middle item
    removed_mid = delete_at(inventory, 2)
    print(f"Removed element (MIDDLE): {removed_mid}")
    print(f"List after deletion in the middle: {inventory}")

    # Test 3: Pop the last item (no shifting needed)
    removed_end = delete_at(inventory, len(inventory) - 1)
    print(f"Removed element (END): {removed_end}")
    print(f"List after deletion at the end: {inventory}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    # Test 1: Look for something we know is there
    search_target1 = "Terraria"
    result1 = search_value(inventory, search_target1)
    print(f"Searching for '{search_target1}': Found at index {result1}")

    # Test 2: Look for something that isn't there
    search_target2 = "Pacman"
    result2 = search_value(inventory, search_target2)
    print(f"Searching for '{search_target2}': Result {result2} (Not Found)")

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Case 1: Trying to delete a crazy high index (checks our validation)
    invalid_index = 99
    edge_delete = delete_at(inventory, invalid_index)
    print(f"Edge Case 1 - Deleting at invalid index ({invalid_index}): Return value = {edge_delete}")

    # Case 2: Dealing with empty lists
    empty_list = []
    print(f"Empty list created: {empty_list}")

    # Adding to a fresh empty list works fine at index 0
    insert_at(empty_list, 0, "First Item")
    print(f"Edge Case 2a - Inserting into empty list: {empty_list}")

    # Making sure deleting from an empty list doesn't crash the script
    empty_list.clear()
    edge_delete_empty = delete_at(empty_list, 0)
    print(f"Edge Case 2b - Deleting from empty list: Return value = {edge_delete_empty}")

    # ===============================
    # REAL-WORLD SCENARIO: E-Commerce Shopping Cart
    # ===============================
    print("\n=== REAL-WORLD SCENARIO: SHOPPING CART ===")

    # Starting a fresh cart list
    cart = []

    # 1. Simulating a user clicking "Add to Cart" (Appends to the end)
    print("--- 1. Items added to cart ---")
    insert_at(cart, len(cart), "Gaming Headset")
    insert_at(cart, len(cart), "Mechanical Keyboard")
    insert_at(cart, len(cart), "USB-C Cable")
    print(f"Current Cart: {cart}")

    # User adds a priority service charge, system forces it to index 0
    insert_at(cart, 0, "Express Shipping")
    print(f"Cart after forcing Express Shipping to the top: {cart}")

    # 2. Looking up an item to see if it's already in the cart
    print("\n--- 2. Checking if an item is in the cart ---")
    item_to_find = "Mechanical Keyboard"
    position = search_value(cart, item_to_find)

    if position != -1:
        print(f"Success: '{item_to_find}' is in the cart at index {position}.")
    else:
        print(f"Notice: '{item_to_find}' not found.")

    # 3. User drops the USB-C cable before checking out
    print("\n--- 3. Removing an item from the cart ---")
    cable_index = search_value(cart, "USB-C Cable")
    if cable_index != -1:
        removed_item = delete_at(cart, cable_index)
        print(f"Removed '{removed_item}' from the cart.")

    print(f"Final Cart Status before checkout: {cart}")


if __name__ == "__main__":
    main()