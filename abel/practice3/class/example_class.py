class SMS_store:
    message_list = []

    def new_arrival(self, from_number, time_arrived, test_SMS):
        message = (False, from_number, time_arrived, test_SMS)
        self.message_list.append(message)

    def mesage_cont(self):
        return len(self.message_list)

    def get_unread_indexes(self):
        index_list = []
        for index in range(len(self.message_list)):
            if self.message_list[index][0] is False:
                index_list.append(index)
        return index_list

    def get_message(self, index):
        if index < len(self.message_list):
            message = self.message_list[index]
            self.message_list[index] = (True, message[1], message[2], message[3])
            return message[1], message[2], message[3]
        else:
            return "none"

    def delete(self, index):
        self.message_list.__delitem__(index)

    def inbox_clear(self):
        self.message_list.clear()


sms_instance = SMS_store()
sms_instance.new_arrival(7565656, "2019-01-24 22:12:41", "Hi, ")
sms_instance.new_arrival(7878789, "2019-01-24 22:12:45", "how are you? ")
sms_instance.new_arrival(7565656, "2019-01-24 22:12:41", "fain and you ")
sms_instance.new_arrival(7878789, "2019-01-24 22:12:45", "do you like played football?")
print("Indexes:")
print(sms_instance.get_unread_indexes())
print("Message index 1")
print(sms_instance.get_message(1))
print("Message List :")
print(sms_instance.message_list)
print("Unread Indexed:")
print(sms_instance.get_unread_indexes())
print("Clear all List :")
print(sms_instance.inbox_clear())
print("Message List")
print(sms_instance.message_list)
