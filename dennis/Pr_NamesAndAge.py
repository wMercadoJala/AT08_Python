from dennis import Pr_ConvertAge, Pr_AgeMessage

users_dic = {}


def read_amount_users_from_kb():
    amount = input("How many users do you want to in?")
    while not amount.isdigit():
        amount = input(amount + " is not a number. How many users do you want to in?")
    return int(amount)


def read_user_from_kb(user):
    name = input("Enter name %s: " % user)
    age = input("Enter age: ")
    while not age.isdigit():
        age = input(age + " is not a number. Enter age: ")
    users_dic.update({name: int(age)})


def main():
    amount_users = read_amount_users_from_kb()
    for number in range(1, amount_users + 1):
        read_user_from_kb(number)
    for key in users_dic:
        print(key + " age: " + str(users_dic[key])
              + ". In days: " + str(Pr_ConvertAge.convert_age_to_days(users_dic[key]))
              + ". In hours: " + str(Pr_ConvertAge.convert_age_to_hours(users_dic[key]))
              + ". In minutes: " + str(Pr_ConvertAge.convert_age_to_minutes(users_dic[key])))
        Pr_AgeMessage.print_age_message(users_dic[key])
        print("")


if __name__ == "__main__":
    main()
