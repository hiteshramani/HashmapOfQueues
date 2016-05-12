from bq_subscriber import BqSubscriber


#Creating an instance of BqHashmap with sub name sub1, port no. 5000 and 
#topic 1000
bq_subscriber_instance = BqSubscriber("sub1",5000,1000)

def start_listening():
	bq_subscriber_instance.start_listening()

if __name__ == '__main__':
	start_listening()