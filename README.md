# Student Project

This is a Django project for managing student information. It includes functionalities for creating, updating, listing, and deleting student records.


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/raghu295/student_entry_system.git
    cd student_project
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv myenv
    myenv\Scripts\activate  # On Windows
    source myenv/bin/activate  # On Unix or MacOS
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Endpoints

- `GET /students/` - List all students
- `POST /students/` - Create a new student
- `GET /students/<id>/` - Retrieve a student by ID
- `PUT /students/<id>/` - Update a student by ID
- `DELETE /students/<id>/` - Delete a student by ID

## Usage

### Creating a Student

To create a student, navigate to the student creation form and fill in the required details. Submit the form to save the student record.

### Listing Students

To list all students, navigate to the student list page. You will see a table with all student records.

### Updating a Student

To update a student, navigate to the student update form for the specific student, make the necessary changes, and submit the form.

### Deleting a Student

To delete a student, navigate to the student list page, and click the delete button for the specific student.

