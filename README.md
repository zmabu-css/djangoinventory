# Inventory Management System

## Overview

The Inventory Management System is a Django-based web application designed to help users manage products and categories efficiently. This system allows for user authentication, product image uploads, and easy navigation through a modern and responsive interface.

## Features

- **Modular Design:** Utilizing Django's MVT architecture for scalability and easy maintenance.
- **Dynamic Image Handling:** Integrates image uploads and real-time display functionality with Django and Pillow.
- **Responsive UI:** A clean interface ensuring a seamless user experience across devices.
- **Admin Interface:** Provides easy management of products and categories via Django’s admin interface.

## Installation

### Prerequisites

- **Python 3.6+**
- **Pip (Python package installer)**
- **Virtual environment tool** (`virtualenv` or built-in `venv`)

### Setup Instructions

1. **Clone the Repository:**
shell git clone https://github.com/yourusername/inventorymanagementsystem.git cd inventorymanagementsystem

2. **Create and Activate a Virtual Environment:**
   - **Windows:**
     ```shell
     python -m venv myenv
     myenv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```shell
     python -m venv myenv
     source myenv/bin/activate
     ```

3. **Install Required Packages:**
shell pip install -r requirements.txt

4. **Configure Database:**
shell python manage.py makemigrations python manage.py migrate

5. **Create a Superuser:**
shell python manage.py createsuperuser

6. **Run the Development Server:**
shell python manage.py runserver

7. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:8000`
   - **Admin Interface:** `http://127.0.0.1:8000/admin/` (use superuser credentials to log in)

## Usage

1. **Admin Interface:**
   - Add categories and products using the admin panel.
   - Upload images for products to enhance the visual presentation.

2. **Category and Product Viewing:**
   - View the list of categories and click on any category to see associated products.
   - View detailed information and images for each product.

## Packages Used

- **Django:** The web framework used for developing the application.
- **Pillow:** Python Imaging Library used for handling image uploads.

## Background

This project was developed to provide a simple solution for managing inventory with dynamic image handling and a responsive design. The use of Django’s MVT architecture ensures scalability and easy maintenance, while the integration of Pillow allows for rich product displays. The admin interface simplifies management tasks, making the system accessible for non-technical users.

---

By following these instructions, you should be able to set up and run the Inventory Management System locally, enabling efficient management of products and categories with a modern interface.

