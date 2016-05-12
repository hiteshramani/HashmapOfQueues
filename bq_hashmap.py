from queue import Queue
import zmq
import cPickle as pickle
import time

class BqHashmap:
    """
    The primary data structure being used to store the data in key-value
    pairs.
    """

    def __init__(self, port, topic):
        """Constructs/Initiates a hashmap/dictionary"""
        
        self.hashmap = {}
        self.port = str(port)
        self.topic = topic
        self.context = zmq.Context()

        #creating the hashmap_socket to transfer data to the subscribers
        self.hashmap_socket = self.context.socket(zmq.PUB)
        
        #assigning it the given port for communication
        self.hashmap_socket.bind("tcp://*:%s" % self.port)
        
        #Sleep to make sure the connection is made before communication starts
        time.sleep(.2)
        print "Hashmap successfully initiated."


    def create_queue(self, Qi, Bi):
        """Creates a empty buffered queue with key Qi"""
        self.hashmap[Qi] = Queue(Bi)


    def put_data(self, Qi, data):
        """Enqueues data into the queue with key Qi"""
        try:
            self.hashmap[Qi].enqueue(data)
        except KeyError:
            print("Error: queue with key " +str(Qi)+" does not exist or has \
been popped, please create it before accessing")
            raise

        if self.hashmap[Qi].is_queue_full():
            #the queue will only be popped when it has reached its buffer size
            self.send_zipped_pickle(self.hashmap[Qi].dequeue())
            self.hashmap.pop(Qi)


    def display_queue(self, Qi):
        """Displays the current data in the queue with key Qi"""
        try:
            print "Current data in queue: " + str(self.hashmap[Qi].dequeue())
        except KeyError:
            print("Error: queue with key " +str(Qi)+" does not exist or has \
been popped, please create it before accessing")
            raise


    def send_zipped_pickle(self, obj):
        """
        pickle an object before sending it to make sure we are able to deal
        with complicated data as well.
        """
        pickled_data = pickle.dumps(obj)
        return self.hashmap_socket.send("%d %s" % (self.topic, pickled_data))