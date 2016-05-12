import zmq
import cPickle as pickle

class BqSubscriber:
    """
    The Subscriber class, responsible for adding/deleting/viewing/initiating 
    the current subscribers. It is also responsible for receiving data in
    these subscribers.
    """

    def __init__(self, subscriber_name, port, topic):
        """Initializing the subscriber class with name, port and topic."""
        self.subscriber_name = subscriber_name
        self.port = str(port)
        self.topic = str(topic)
        context = zmq.Context()
        self.subscriber_socket = context.socket(zmq.SUB)
        self.subscriber_socket.connect("tcp://localhost:%s" % self.port)
        self.subscriber_socket.setsockopt(zmq.SUBSCRIBE, self.topic)

    def start_listening(self):
        """Starting to listen to data"""
        print("Starting to listen to the port")
        while True:
	        received_data = self.subscriber_socket.recv()
	        received_message = received_data[len(self.topic)+1:]
	        actual_message = pickle.loads(received_message)
	        print "The recieved message data is: " + str(actual_message)
