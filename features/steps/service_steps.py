import requests
from behave import *

@given('J\'ai accès au service web à l\'URL "{url}"')
def step_given_access_to_web_service(context, url):
    context.url = url

@when('Je fais une requête GET à l\'operation "{url}"')
def step_when_make_get_request(context, url):
    context.response = requests.get(context.url + url)

@then('La réponse HTTP doit avoir le code de statut {status_code:d}')
def step_then_response_status_code(context, status_code):
    assert context.response.status_code == status_code

@step('Le contenu de la réponse doit contenir "{expected_content}"')
def step_then_response_contains(context, expected_content):
    assert expected_content in context.response.text
