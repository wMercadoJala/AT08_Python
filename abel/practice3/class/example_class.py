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

    def get_message(self, i):
        if i > len(self.message_list):
            self.message_list[i][0] = True
            return self.message_list[i][1] + self.message_list[i][2] + self.message_list[i][3]
        else:
            return "none"

