def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]  #swap
    return arr

# Take array input from the user
input_str = input("Enter the elements of the array separated by space: \n")
arr =list(map(int, input_str.split()))
# Sort the array using selection sort
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)