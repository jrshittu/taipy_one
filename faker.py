from faker import Faker
from taipy.gui import Gui, notify

name = ""
phone = ""
address = ""

fake = Faker()

def generate_name(state):
    state.name = fake.name()
    state.phone = fake.phone_number()
    state.address = fake.address()
    notify(state, 'info', f'Here is your new details: {state.name}')

page = """
# Click to generate random details

Generated name is: <|{name}|> <br />
Generated Phone Number: <|{phone}|> <br />
Generated Address: <|{address}|>

<|Generate|button|class_name=plain mt1 p1|on_action=generate_name|>
"""

Gui(page).run(debug=True, title="personal_details_generator")