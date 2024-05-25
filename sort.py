# sort_search.py

def bubble_sort_2d(arr):
    # Convert 2D array to 1D list for sorting
    flat_arr = [item for sublist in arr for item in sublist]
    n = len(flat_arr)
    
    # Bubble sort algorithm
    for i in range(n):
        for j in range(0, n-i-1):
            if flat_arr[j] > flat_arr[j+1]:
                # Swap elements
                flat_arr[j], flat_arr[j+1] = flat_arr[j+1], flat_arr[j]
    
    # Map the sorted 1D list back to 2D array
    sorted_arr = [flat_arr[i:i+len(arr[0])] for i in range(0, len(flat_arr), len(arr[0]))]
    return sorted_arr

def search_element(arr, element):
    found = False
    # Iterate through each element of the 2D array
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == element:
                # If element is found, print its position and exit
                print(f"Element {element} found at position: ({i}, {j})")
                found = True
                break
        if found:
            break
    else:
        # If element is not found after checking entire array
        print(f"Element {element} is not in the array.")

if __name__ == "__main__":
    # Sample array
    arr = [
        [3, 5, 1],
        [9, 2, 7],
        [4, 6, 8]
    ]

    # Print original array
    print("Original Array:")
    for row in arr:
        print(row)

    # Sort array using bubble sort
    sorted_arr = bubble_sort_2d(arr)
    print("\nSorted Array:")
    for row in sorted_arr:
        print(row)

    # Ask user to enter element for search
    search_element_input = int(input("\nEnter the element you want to search for: "))

    # Search for the element in sorted array
    search_element(sorted_arr, search_element_input)
