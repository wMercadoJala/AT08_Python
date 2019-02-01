def before_scenario(context, scenario):
    if 'before' in scenario.tags:
        print("********************************Scenario tags*************************************\n")
    if 'Test' in scenario.name:
        print("Scenario test")
