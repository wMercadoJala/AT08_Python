class SmsStore:
    """
    This Class simulate the messages of a Cell-Phone
    """

    def __init__(self):
        """
        Constructor
        """
        self.message_list = []

    def add_new_arrival_(self, from_number, time_arrived, text_of_SMS):
        """
        This method add new message
        :param from_number: Number message
        :param time_arrived: Time of inbox
        :param text_of_SMS: Body message
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
        unread_list = list(
            filter(lambda x: x is not None,
                   map(lambda x: self.message_list.index(x) if x[0] is False else None, self.message_list)))
        return unread_list

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
sms.add_new_arrival_(12345678, "23/01", "Hi men, how are u")
sms.add_new_arrival_(74859612, "21/02", "Did u see the new movie?")
print(sms.get_unread_indexes(), "Indexes")
print(sms.get_message(0), "Message")
print(sms.message_list, "Message List")
print(sms.get_unread_indexes(), "Unread Indexed")
print(sms.inbox_clear(), "Clear all")
print(sms.message_list, "Message List")
