#push elements directly to inStack making it O(1)
# when pop function arrives we will push all instack elements to outstack 
# and pop elements from outstack making it amortised O(1).
# We check if outstack is empty or not at every pop function 
# and if its empty then we empty out instack into outstack
#better than everytime pushing all elements to outstack
# so that pop will be O(1) but push will be O(n)  


class MyQueue:

    def __init__(self):
        # Initialize two stacks, one for incoming elements and one for outgoing elements.
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        # Append the element directly to inStack, making this operation O(1).
        self.inStack.append(x)

    def pop(self) -> int:
        # Ensure outStack has elements to pop. If outStack is empty, transfer all elements from inStack to outStack.
        self.peek()  # This transfers elements if needed.
        # Pop the top element from outStack, which corresponds to the front of the queue.
        return self.outStack.pop()

    def peek(self) -> int:
        # If outStack is empty, we need to transfer elements from inStack to outStack.
        # This reverses the order, so the first element added to inStack ends up on the top of outStack.
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        # Return the top element of outStack, which corresponds to the front of the queue.
        return self.outStack[-1]

    def empty(self) -> bool:
        # The queue is empty if both inStack and outStack are empty.
        return not self.inStack and not self.outStack
