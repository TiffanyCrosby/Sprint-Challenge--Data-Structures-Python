class RingBuffer:
    def __init__(self, capacity, data=[]):
        self.list_index = 0 #makes it so i can replace new item with old item starting at first item
        self.capacity = capacity
        self.data = list(data)[capacity:] #using list to store items

    def append(self, item):
        if len(self.data) == self.capacity: #check to see if list is full
            self.data[self.list_index] = item #if list is full then replace OLDEST item with item passed in
        else:
            self.data.append(item) #adding item to list 

        self.list_index = (self.list_index + 1) % self.capacity #increments index in order to replace oldest item NOT first item,
        # also checks to make sure not going past capacity

    def get(self):
        return self.data #returns list