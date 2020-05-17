import glob 
import random

class Init_Messages:

    '''
        Docstring:
            This is used to read all the messages from the messages folder into a list for it to be randomized. 
            All the messages in the folder must be in .txt format for this portion of the script to work. 
    '''

    def __init__(self):
        self.message_list = glob.glob("messages/*.txt")
        self.messages =[]
        self.messages = self.setup()

   
        
    def setup(self):
        tmp = []
        for msg in self.message_list:
            with open(msg, 'r') as file:
                text = file.read().replace('\n', '')
            tmp.append(text)
        return tmp

   


class randomize_messages(Init_Messages):

    '''
        DocString:
            Child class of Init_Messages. Given the list of messages, it randomizes messages and sends them, along with an ID to the CSV
            This way, the same person doesn't get the messages repeated
    '''

    def __init__(self, already_sent):
        Init_Messages.__init__(self)
        self.already_sent = already_sent
        self.return_value = self.randomize()
        
    
    def randomize(self):
        while True:
            self.chosen_index = random.choice(range(len(self.messages)))
            if self.chosen_index not in self.already_sent:
                break
        self.chosen_message = self.messages[self.chosen_index]
        return [self.chosen_index, self.chosen_message]
    
    def __call__(self):
        return self.return_value


        



