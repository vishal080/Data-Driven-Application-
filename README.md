# Data-Driven Web Application

This is a Django-based web application designed to efficiently handle CSV file uploads, display data with pagination, and calculate subscription pricing based on the uploaded data. The application ensures smooth handling of large datasets and provides real-time feedback during uploads.

## Features

1. **CSV Upload Service**
   - Users can upload CSV files.
   - Efficient handling of large datasets.
   - Real-time progress indicators during uploads.
   - Error handling for invalid file types and data formats.

2. **Data Display and Pagination**
   - Displays uploaded data on the UI after upload completion.
   - Implements pagination for smooth navigation through large datasets.
   - Responsive UI for a seamless user experience.

3. **Subscription Pricing Calculator**
   - Utilizes the uploaded CSV data to calculate and display subscription pricing.

## Installation

### Prerequisites

- Python 3.6 or higher
- Django 3.0 or higher
- Ensure you have pip installed for managing Python packages.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Uploading a CSV File

1. Navigate to the upload page.
2. Select a valid CSV file.
3. Click the 'Upload' button.
4. Monitor the real-time progress indicator.
5. After a successful upload, you will be redirected to the data display page.

### Viewing Uploaded Data

1. The data display page shows the uploaded data in a paginated table.
2. Use the pagination controls to navigate through the dataset.

### Subscription Pricing Calculator

1. Navigate to the subscription pricing calculator page.
2. The total subscription price is calculated and displayed based on the uploaded data.


## Troubleshooting

- **Invalid CSV File Error**: Ensure the file is a valid CSV and properly formatted.
- **Upload Issues**: Check file size and ensure it does not exceed the upload limit configured in Django settings.
- **Data Display Issues**: Verify that the data is correctly uploaded and formatted.

 

 

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [DataTables](https://datatables.net/)

