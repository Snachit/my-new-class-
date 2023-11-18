class Mobile : 
    def __init__(self, company_name, storage, serial_num, name, dual_sim, support_4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support_4k = support_4k

    def call(self, number):
        print(f"Calling {number} from  {self.name}.")

    def send_message(self, number, message ):
        print(f"Sending a message to {number} : '{message}'")

    def play_media(self, media_name):
        print(f"Playing '{media_name}' on '{self.name}'.")

# Exemple of usage 
mob1 = Mobile("iPhone", 1000, "339421235cb", "iPhone 15 pro max", True, True)
mob1.call("911")
mob1.send_message("9918240982", "Hi i am Mr Soap, i hope you're doing great")
mob1.play_media("UNKNOW T , AVEN9ERS")

