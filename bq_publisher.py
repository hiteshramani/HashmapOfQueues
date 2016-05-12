class BqPublisher:
    """
    The publisher class, responsible for creating publishers which send data 
    to a particular port. Each publisher has it's own publisher.
    """

    def __init__(self, publisher_id, hashmap):
        """Initializing the publisher"""
        self.publisher_id = publisher_id
        self.hashmap = hashmap
        print("Publisher " + str(publisher_id) + " has been initiated.")

    def create_entry(self, Qi, Bi):
        """Creates a queue in the hashmap with key Qi and buffer size Bi"""
        self.hashmap.create_queue(Qi,Bi)

    def send_data(self, Qi, data):
        """
        Sending data to the hashmap, to be enqueued to the queue of the key 
        Qi. If they queue has reached it's buffer, it'll be sent to the 
        subscribers.
        """
        self.hashmap.put_data(Qi, data)

    def get_id(self):
        """Publisher's id for identification, if needed"""
        return self.publisher_id

