def before_scenario(context, scenario):
    if 'before' in scenario.tags:
        print("********************************Scenario tags*************************************\n")
    if 'Test' in scenario.name:
        print("Scenario test")
    if 'post_membership_account' in scenario.tags:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        context.execute_steps('''
        Given I set up a "POST" request to "/accounts/1080889/memberships" endpoint
        And I set up the data
        """
        {
            "person_id": 3143926
        }
        """
        And I send the request
        ''')


def after_scenario(context, scenario):
    if 'delete_data' in scenario.tags:
        print("**************************************************************\n")
        context.execute_steps('''
        Given I set up a "DELETE" request to "/accounts/1080889/memberships/3143926" endpoint
        And I send the request
        ''')
