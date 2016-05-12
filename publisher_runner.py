from bq_hashmap import BqHashmap
from bq_publisher import BqPublisher

#Creating an instance of BqHashmap with port no. 5000 and topic 1000
bq_hashmap_instance = BqHashmap(port=5000, topic=1000)

#Creating an instance of BqPublisher with publisher id pub1 and above
#created hashmap instance
bq_publisher_instance = BqPublisher(publisher_id="pub1",
									hashmap=bq_hashmap_instance)

def pub_runner_numbers():

	#Defining the key
    Q1 = "key1"

    #Creating an entry in the hashmap with key key1 and buffer size 5
    bq_publisher_instance.create_entry(Qi=Q1,Bi=5)
    
    print "\nSending numbered data"
    #Publishing numbered data via the send data method
    bq_publisher_instance.send_data(Q1,4)
    bq_publisher_instance.send_data(Q1,5)
    bq_publisher_instance.send_data(Q1,6)

    #Displaying the current data in the queue
    bq_hashmap_instance.display_queue(Q1)

    bq_publisher_instance.send_data(Q1,4)
    bq_publisher_instance.send_data(Q1,655)
    print "Numbered data sent"

def pub_runner_characters():

	#Defining the key
    Q2 = "key2"

    #Creating an entry in the hashmap with key key2 and buffer size 3
    bq_publisher_instance.create_entry(Qi=Q2,Bi=3)
    
    print "\nSending character data"    
    #Publishing character data via the send data method
    bq_publisher_instance.send_data(Q2,"hello")
    bq_publisher_instance.send_data(Q2,"squadrun")
    bq_publisher_instance.send_data(Q2,"let's do some missions!")
    print "Character data sent"


def pub_runner_list():

	#Defining the key
    Q3 = "key3"

    #Creating an entry in the hashmap with key key1 and buffer size 5
    bq_publisher_instance.create_entry(Qi=Q3,Bi=4)
    
    print "\nSending list data"

    #Publishing numbered data via the send data method
    bq_publisher_instance.send_data(Q3,[1,2,3,4])
    bq_publisher_instance.send_data(Q3,['a','bq_publisher_instance','c','d'])
    bq_publisher_instance.send_data(Q3,['hello'])
    bq_publisher_instance.send_data(Q3,[''])
    print "List data sent"

def pub_runner_no_queue_error_1():
    
    #Defining the key
    Q4 = "key4"

    #Trying to access queue of this key without creating it
    bq_hashmap_instance.display_queue(Q4)

def pub_runner_no_queue_error_2():
    
    #Defining the key
    Q5 = "key5"

    #Trying to access queue of this key without creating it
    bq_publisher_instance.send_data(Q5,"gonna be an error!")


if __name__ == "__main__":

    print "Time for some results!"
    #To run the method, simple remove the comment.

    pub_runner_numbers()
    # pub_runner_characters()
    # pub_runner_list()
    # pub_runner_no_queue_error_1()
    # pub_runner_no_queue_error_2()	