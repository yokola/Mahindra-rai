from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# Visite function
NoOfvisits = 
print("eneter URLs to visit:")
for i in range(NoOfvisists):
    url = input("URL: ")
    print(f"visiting {url}")
    backward_history.put(current_page)
    current_page = url

    # display current page
    print(f"current page: {current_page}")

# Go back
while input("Do you want to go back? (yes\no):  ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"going back to {current_page}")
    else:
        print("no previous page aviable")    

# Go forward
while input("Do you want to go forward? (yes\no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page) 
        current_page = forward_history.grt() 
        print   

     