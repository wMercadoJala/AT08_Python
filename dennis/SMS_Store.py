class SMS_Store:
    #pass
    @staticmethod
    def return_tuple():
        return "test", "hello", "bye"

    def __init__(self):
        self.message_list = []

    def new_arrival(self, from_number, time_arrived, text_of_SMS):
        message = (False, from_number, time_arrived, text_of_SMS)
        self.message_list.append(message)

    def message_count(self):
        return self.message_list.count

    def get_unread_indexes(self):
        list_unread = []
        for index in range(len(self.message_list)):
            if self.message_list[index][0] is False:
                list_unread.append(index)
        return list_unread

    def get_unread_indexes_new(self):
        list_unread = []
        for x in self.message_list:
            if x[0] is False:
                list_unread.append(self.message_list.index(x))
        return list_unread

    def get_message(self, index):
        return self.return_message(index) if index < len(self.message_list) else None

    def return_message(self, index):
        self.message_list[index][0] = True
        return self.message_list[index]

    def delete(self, index):
        self.message_list.remove(index) if index < len(self.message_list) else None

    def clear(self):
        self.message_list.clear()


tuple, hello, bye = SMS_Store.return_tuple()
print(tuple)
print(bye)
