def bubble_sort_2d(arr):
    n = len(arr)
    m = len(arr(0))
    total_elements = n * m

    for i in range(total_elements -1):

        for j in range(total_elements -1 -i):

            
            row1 = j // m
            cil1 = j % m


            row2 = j // m
            col2 = j % m


            if arr[row1][col1] > arr[row2][col2]:

            arr[row1][col2], arr[row2][col2] =  arr[row2][col2], arr[row1][col1]

            def search_element(arr, element):
                found = False
                for i in range(len(arr)):
                    for j in range(len(arr(i))):
                        if arr[i][j] == element:
                            print(f"element found in position: row = {i}, column = {j}")
                            found = True
                            return
                if not found:
                    print("element not found in the given array.")        


            arr = [[9, 2, 3],
                   [4, 5, 6],
                   [7, 8, 1]
                           ]
                    
                print(arr)
                bubble_sort_2d(arr)
                print(arr)

                    search = int(input("enter the element to search: "))
                    search_element(arr, search)


                 
