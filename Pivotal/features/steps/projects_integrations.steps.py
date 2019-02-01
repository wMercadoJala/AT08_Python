from behave import *
from compare import expect


# @given(u'I setup a "{method}" request to "/projects/{projectId}/integrations" endpoint')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I setup a "GET" request to "/projects/{projectId}/integrations" endpoint')


@then(u'I get status code "200"')
def step_impl(context):
    expect(200).to_equal(context.response.status_code)
