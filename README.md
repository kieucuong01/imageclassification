# Imageclassification
This is an image classification app built using **Django 4**, **Django REST Framework 3**, **Next.js 12**. The app uses built model to classify images selected by the user.


## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the application](#run-the-application)


## Prerequisites

Install the following prerequisites:

1. [Python 3.7-3.10](https://www.python.org/downloads/)
<br>This project uses **TensorFlow v2.9.1**. For TensorFlow to work, you must have a correct Python version installed on your machine. More information [here](https://www.tensorflow.org/install/source#tested_build_configurations).
2. [Visual Studio Code](https://code.visualstudio.com/download)

## Installation

### 1. Create a virtual environment

From the **root** directory run:


```bash
python -m venv venv
```

### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required backend dependencies

From the **backend** directory run:

```bash
pip install -r requirements.txt
```

### 4. Run migrations

From the **root** directory run:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## 5.Run the application

From the **root** directory run:

```bash
python manage.py runserver
```
