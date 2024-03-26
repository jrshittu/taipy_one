# Taipy: Building Interactive Web Apps without HTML/CSS and JavaScript

| Table of Contents |
| --- |
| [Introduction](#intro) |
| [Meet Taipy](#meet)
| [Why Taipy?](#why)  |
| [Building Web Apps with Taipy](#build) |
| [Live Demo Tutorials](#example) |
| [Conclusion](#conc)|

## Introduction <a name="intro"></a>
Over the past few years, HTML, CSS & JavaScript has been the go to technologies for building web applications. However, the learning curve has been a tedious and time consuming especially for python developers and data scientists. This is where Taipy comes into play. 

## Meet Taipy! <a name="meet"></a>
Taipy is an open-source Python library that enables data scientists and developers to build robust end-to-end data pipelines.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k24u6ko4tkjffice6thz.gif)

Source: [Taipy Docs](https://docs.taipy.io/en/latest/)

Taipy GUI enables developers to create interactive web interfaces for their data pipelines without requiring HTML/CSS & JavaScript skills. It provides access to interactive widgets, controls and presentative elements to design user interfaces using Python and connect them to your data pipeline functions.

## Why Taipy? <a name="why"></a>
Taipy provides a simple and intuitive way to build web apps with minimal coding. It offers several advantages over traditional methods. Here are some reasons why Taipy is worth considering for your next web development project:

1. Simplicity: Taipy simplifies web development by providing an intuitive GUI and a Python API that enable developers to build web applications without the need for extensive coding skills. This makes it an ideal choice for python developers, data scientists and citizen developers who want to build web applications that meet their needs.

2. Flexibility: Taipy's data-centric approach offers flexibility in building web applications that are optimized for performance, scalability, and adaptability. With Taipy, developers can build web applications that handle large and complex data sets with ease, making it an ideal choice for building data-driven web applications.

3. Efficiency: Taipy's data-centric approach enables developers to focus on what really matters: the data. By prioritizing data management and analysis, Taipy streamlines the development process, making it more efficient and less time-consuming. This means that developers can build web applications faster and with fewer resources.

4. Powerful data processing capabilities: Taipy offers powerful data processing capabilities that enable developers to perform complex data analysis and visualization tasks with ease. This makes it an ideal choice for building web applications in fields such as finance, healthcare, and science, where data analysis and visualization are critical.

5. Easy deployment: Taipy makes it easy to deploy web applications, with support for popular cloud platforms such as AWS, Azure, and Google Cloud. This means that developers can easily deploy their web applications to the cloud, without the need for extensive configuration or setup.

## Building Web Apps with Taipy <a name="build"></a>
**Requirement:** Python 3.8 or later on Linux, Windows, and Mac. 

**Installing Taipy:** Open up a terminal and run the following command, which will install Taipy with all its dependencies.

```bash
pip install taipy
```
Hence, let say hello to Taipy...

![hi_py](https://github.com/jrshittu/build_with_taipy/assets/110542235/3667c954-c4e6-4224-b76c-0cb59bb00450)

```python
# import the library
from taipy import Gui

page = "# Hello Taipy!" 

# run the gui
Gui(page).run()
```

Save the code as a Python file: e.g., `app.py`. 
Run the code and wait for the client link `http://127.0.0.1:5000` to display and pop up in your browser. 

You can change the port if you want to run multiple servers at the same time with `Gui(...).run(port=xxxx)`.

### Project One: Personal Details Generator
![fake](https://github.com/jrshittu/taipy_one/assets/110542235/9c4e6803-eec4-4a4d-86ab-45ef98d3b357)

A simple GUI application that generates random user details, including a name, phone number, and address, using the `Faker` library.

**Full code**
```python
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
# Generate Fake Data {: .color-primary}

<|personal.png|image|> <br />
Generated name is: <|{name}|> <br />
Generated Phone Number: <|{phone}|> <br />
Generated Address: <|{address}|>

<|Generate|button|class_name=plain mt1 p1|on_action=generate_name|>
"""

Gui(page).run(debug=True, title="Fake Details")
```
**Q:** What do you think will happen when you run the program?

Now, let's break it down and create the program step by step

**Step 1: Import the required libraries**

* Import the `Faker` library to generate fake data.
* Import the `Gui` and `notify` classes from `taipy.gui` to create the GUI and display notifications.
```python
from faker import Faker
from taipy.gui import Gui, notify
```
**Step 2: Initialize global variables**

Initialize three global variables `name`, `phone`, and `address` as empty strings. These variables will store the generated fake data.
```python
name = ""
phone = ""
address = ""
```
**Step 3: Create an instance of the `Faker` class**

Create an instance of the `Faker` class to generate fake data.
```python
fake = Faker()
```
**Step 4: Define the `generate_name` function**

Define a function `generate_detail` that takes a `state` parameter. This function generates fake data using the `Faker` instance and updates the global variables `name`, `phone`, and `address` with the generated data. The `notify` function is used to display a notification to the user with the generated name.
```python
def generate_detail(state):
    state.name = fake.name()
    state.phone = fake.phone_number()
    state.address = fake.address()
    notify(state, 'info', f'Here is your new details: {state.name}')
```
**Step 5: Define the Taipy GUI page layout**

Define the Taipy GUI page layout using Markdown syntax. The layout includes a header, an image, three text fields to display the generated fake data, and a button to generate new data. The `on_action` attribute of the button is set to the `generate_name` function.
```python
page = """
# Generate Fake Data {: .color-primary}

<|personal.png|image|> <br />
Generated name is: <|{name}|> <br />
Generated Phone Number: <|{phone}|> <br />
Generated Address: <|{address}|>

<|Generate|button|class_name=plain mt1 p1|on_action=generate_detail|>
"""
```
**Step 6: Run the Taipy GUI application**

Finally, run the Taipy GUI application using the `Gui` class. The `page` variable is passed to the `Gui` constructor to set the page layout. The `debug` parameter is set to `True` to enable debug mode, and the `title` parameter is set to `"Fake Details"` to set the application title.
```python
Gui(page).run(debug=True, title="Fake Details")
```

When you run this code, the "Generate" button triggers the `generate_detail` function, which updates the displayed data and shows a notification with the generated name.

### Project 2: Image Background Remover 🤖
![bg_remover](https://github.com/jrshittu/build_with_taipy/assets/110542235/9c9d321c-90ca-4faf-876d-c8ae7a88c0fd)

Now let's create a Taipy GUI app to remove backgrounds from images

**Full Code: `main.py`**
```python
from PIL import Image
from rembg import remove
from taipy.gui import Gui, notify
from io import BytesIO

image_upload = ""
image_download = "removebg_img.png"
old_image = None
new_image = None
bg_removed = False

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def rm_bg(state):
    notify(state, 'info', 'Uploading image...')
    image = Image.open(state.image_upload)
    
    notify(state, 'info', 'Removing bg...')
    new_image = remove(image)
    new_image.save("removebg_img.png")

    notify(state, 'success', 'bg removed successfully!')
    state.old_image = convert_image(image)
    state.new_image = convert_image(new_image)
    state.bg_removed = True

page = """
# Image Background Remover {: .color-primary}
Upload an Image: <|{image_upload}|file_selector|extensions=.png,.jpg|on_action=rm_bg|> <br />
<|{old_image}|image|>
<|{new_image}|image|><br/>
<|{image_download}|file_download|label=Download Image|active={bg_removed}|>
"""

Gui(page).run(debug=True)
```

Now, let's break it down and create the program step by step

**Step 1: Import necessary libraries**

In this step, we import the necessary libraries for working with images, removing backgrounds, creating a GUI, and working with binary data.
```python
from PIL import Image
from rembg import remove
from taipy.gui import Gui, notify
from io import BytesIO
```
**Step 2: Initialize variables**

In this step, we initialize variables for storing the uploaded image file, the name of the downloaded image file, the original and processed images, and a boolean variable for indicating whether the background has been removed.
```python
image_upload = ""
image_download = "removebg_img.png"
old_image = None
new_image = None
bg_removed = False
```
**Step 3: Define the `convert_image` function**

In this step, we define a function for converting an image to binary data. This function takes an image as input and returns its binary data.
```python
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im
```
**Step 4: Define the `rm_bg` function**

In this step, we define a function for removing the background from an image and displaying notifications to the user. This function takes a state object as input and performs the following operations:

* Displays a notification indicating that the image is being uploaded.
* Opens the uploaded image using the `Image.open` method from the `PIL` library.
* Displays a notification indicating that the background is being removed.
* Removes the background from the image using the `remove` function from the `rembg` library.
* Saves the processed image to a file using the `save` method from the `PIL` library.
* Displays a notification indicating that the background has been removed successfully.
* Converts the original and processed images to binary data using the `convert_image` function.
* Sets the `old_image`, `new_image`, and `bg_removed` attributes of the state object to the original image data, processed image data, and `True` respectively.
```python
def rm_bg(state):
    notify(state, 'info', 'Uploading image...')
    image = Image.open(state.image_upload)

    notify(state, 'info', 'Removing bg...')
    new_image = remove(image)
    new_image.save("removebg_img.png")

    notify(state, 'success', 'bg removed successfully!')
    state.old_image = convert_image(image)
    state.new_image = convert_image(new_image)
    state.bg_removed = True
```
**Step 5: Define the GUI layout**

In this step, we define the layout of the GUI using a string. The layout consists of a file upload widget, two image display widgets, and a file download widget.
```python
page = """
# Image Background Remover {: .color-primary}
Upload an Image: <|{image_upload}|file_selector|extensions=.png,.jpg|on_action=rm_bg|> <br />
<|{old_image}|image|>
<|{new_image}|image|><br/>
<|{image_download}|file_download|label=Download Image|active={bg_removed}|>
"""
```
**Step 6: Run the GUI**

In this step, we create a `Gui` object using the `page` string and run it in debug mode.
```python
Gui(page).run(debug=True)
```

## Live Demo Tutorials <a name="example"></a>

## Conclusions <a name="conc"></a>
