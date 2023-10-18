
import requests, json
from behave import *

from features.steps.Todo import Todo




@step('Le contenu de la réponse doit être égal à cet objet')
def step_then_response_contains(context):
    parameters = context.table[0]
    user_id = int(parameters['user_id'])
    id = int(parameters['id'])
    title = parameters['title']
    completed = parameters['completed'] == 'true'  # Convert 'true' to a boolean

    # Deserialize the JSON response into a Todo object
    todo_dict = json.loads(context.response.text)
    todo_object = Todo(
        user_id=user_id,
        id=id,
        title=title,
        completed=completed
    )

    # Compare the deserialized Todo object with the expected parameters
    assert todo_object.user_id == user_id
    assert todo_object.id == id
    assert todo_object.title == title
    assert todo_object.completed == completed
