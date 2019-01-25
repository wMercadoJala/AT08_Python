from behave import *


@given(u'I am a student')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given I am a student')
    pass

@when(u'I learn "{amount}" test')
def step_impl(context, amount):
    # raise NotImplementedError(u'STEP: When i learn API test')
    print(amount)

@then(u'I can work in jala')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then I can work in jala')
    pass
