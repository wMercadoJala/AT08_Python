class SmsStore:
    """
    This Class simulate the messages of a Cell Phone
    """

    def __init__(self):
        """
        Constructor
        """
        self.message_list = []

    def add_new_arrival_(self, from_number, time_arrived, text_of_SMS):
        """
        This method add a new message
        :param from_number: Number message
        :param time_arrived: Date
        :param text_of_SMS: Message
        """
        message = (False, from_number, time_arrived, text_of_SMS)
        self.message_list.append(message)

    def message_count(self):
        """
        Count the number of messages
        :return: Number of messages
        """
        return len(self.message_list)

    def get_unread_indexes(self):
        """
        This method create a list of unread messages by index
        :return: List of Unread messages
        """
        unread_list = []
        for index in range(len(self.message_list)):
            if not self.message_list[index][0]:
                unread_list.append(index)
        return unread_list

    def get_read_indexes(self):
        """
        This method create a list of unread messages by index
        :return: List of Unread messages
        """
        read_list = []
        for index in range(len(self.message_list)):
            if self.message_list[index][0]:
                read_list.append(index)
        return read_list

    def get_message(self, index):
        """
        This method get the message by index
        :param index: Input index
        :return: The message
        """
        if index > len(self.message_list):
            return None
        message = self.message_list[index]
        self.message_list[index] = (True, message[1], message[2], message[3])
        return message[1], message[2], message[3]

    def delete(self, index):
        """
        This method delete a message by index
        :param index: Input index
        """
        self.message_list.__delitem__(index)

    def inbox_clear(self):
        """
        This method clear all the inbox
        """
        self.message_list.clear()


sms = SmsStore()
sms.add_new_arrival_(12345678, "23/01", "Hi men, how are you")
sms.add_new_arrival_(72726016, "21/02", "Did you see the new movie?")
sms.add_new_arrival_(72726016, "21/02", "The movie is Deadpool")
print("  Message List -> ", sms.message_list)
print("       Indexes -> ", sms.get_unread_indexes())
print("     Message 1 -> ", sms.get_message(1))
print("  Message List -> ", sms.message_list)
print("Unread Indexed -> ", sms.get_unread_indexes())
print("  Read Indexed -> ", sms.get_read_indexes())
print("     Clear all -> ", sms.inbox_clear())
print("  Message List -> ", sms.message_list)
