Django Blog Website
A dynamic blog website built using Django, featuring post management, category filtering, pagination, and an interactive admin panel.

📌 Features
Django Apps & Project Structure for scalable development
Dynamic URLs & Views for seamless navigation
Template Rendering & Static Files for UI customization
MySQL Database Integration with CRUD operations
Slug-Based Routing for SEO-friendly URLs
Error Handling & Custom 404 Page
Category & Post Relationships (Many-to-One)
Pagination for structured content display
Contact Form with Validation
Django Admin Customization for efficient management
⚙️ Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/your-repository.git
cd your-repository
2️⃣ Create & Activate a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate      # For Windows
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure the Database (MySQL)
Update settings.py with your MySQL credentials. Then, run:

sh
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a Superuser for Admin Panel
sh
Copy
Edit
python manage.py createsuperuser
6️⃣ Run the Development Server
sh
Copy
Edit
python manage.py runserver
Now, open http://127.0.0.1:8000/ in your browser! 🚀
