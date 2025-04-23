# Streamlit MySQL Data Viewer

This project sets up a simple Streamlit application that connects to a MySQL database and displays data from a `users` table in a web interface.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using Git:
```bash
git clone <your-repository-url>
cd <your-project-directory>
2. Create Docker Network
Run the following command to create a custom Docker network:

bash
Copy code
docker network create my-bridge-net
3. Set Up Project Directories
Ensure the required directories for the Streamlit app and MySQL initialization are created:

bash
Copy code
mkdir -p streamlit_app mysql_init
4. Set Up MySQL Database
In the mysql_init/ directory, create the SQL file to initialize the MySQL database and insert sample data:

mysql_init/init.sql:

sql
Copy code
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');
5. Create Streamlit Application
Inside the streamlit_app/ directory, create the following files:

streamlit_app/requirements.txt:

txt
Copy code
streamlit
mysql-connector-python
streamlit_app/app.py:

python
Copy code
import streamlit as st
import mysql.connector

st.title("📊 MySQL Data Viewer")

conn = mysql.connector.connect(
    host="mysql-db",
    user="user",
    password="pass",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

st.write("Data from 'users' table:")
st.table(rows)

cursor.close()
conn.close()
streamlit_app/Dockerfile:

Dockerfile
Copy code
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
6. Build and Run Docker Containers
Build the MySQL Container
Run the following command to initialize the MySQL database container:

bash
Copy code
docker run --name mysql-db \
  --network my-bridge-net \
  -v $(pwd)/mysql_init:/docker-entrypoint-initdb.d \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=pass \
  -d mysql:8.0
Build the Streamlit Container
Navigate to the streamlit_app/ directory and build the Streamlit Docker image:

bash
Copy code
docker build -t my-streamlit-app ./streamlit_app
Run the Streamlit Container
Run the Streamlit app container:

bash
Copy code
docker run --name streamlit-frontend \
  --network my-bridge-net \
  -p 8501:8501 \
  my-streamlit-app
7. Access the Streamlit App
Once the containers are up and running, open your browser and go to:

arduino
Copy code
http://localhost:8501
You should now see the Streamlit application displaying data from the users table in the MySQL database.

Project Structure
csharp
Copy code
postgresql_test/
├── streamlit_app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── mysql_init/
│   ├── init.sql
Troubleshooting
Error: Docker image not found: Make sure the mysql:8.0 image is correctly pulled and available locally.

Error: Container not starting: Verify that the required ports are not being used by other applications.

License
This project is licensed under the MIT License.

sql
Copy code

You can copy and paste this into your `README.md` file in the root of your project. Let me know if you need any further adjustments!





You said:
gimme in 1 i dont hace time i will jyst upload it


ChatGPT said:
Here’s the README.md in one block:

markdown
Copy code
# Streamlit MySQL Data Viewer

This project sets up a simple Streamlit application that connects to a MySQL database and displays data from a `users` table in a web interface.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using Git:
```bash
git clone <your-repository-url>
cd <your-project-directory>
2. Create Docker Network
Run the following command to create a custom Docker network:

bash
Copy code
docker network create my-bridge-net
3. Set Up Project Directories
Ensure the required directories for the Streamlit app and MySQL initialization are created:

bash
Copy code
mkdir -p streamlit_app mysql_init
4. Set Up MySQL Database
In the mysql_init/ directory, create the SQL file to initialize the MySQL database and insert sample data:

mysql_init/init.sql:

sql
Copy code
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');
5. Create Streamlit Application
Inside the streamlit_app/ directory, create the following files:

streamlit_app/requirements.txt:

txt
Copy code
streamlit
mysql-connector-python
streamlit_app/app.py:

python
Copy code
import streamlit as st
import mysql.connector

st.title("📊 MySQL Data Viewer")

conn = mysql.connector.connect(
    host="mysql-db",
    user="user",
    password="pass",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

st.write("Data from 'users' table:")
st.table(rows)

cursor.close()
conn.close()
streamlit_app/Dockerfile:

Dockerfile
Copy code
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
6. Build and Run Docker Containers
Build the MySQL Container
Run the following command to initialize the MySQL database container:

bash
Copy code
docker run --name mysql-db \
  --network my-bridge-net \
  -v $(pwd)/mysql_init:/docker-entrypoint-initdb.d \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=pass \
  -d mysql:8.0
Build the Streamlit Container
Navigate to the streamlit_app/ directory and build the Streamlit Docker image:

bash
Copy code
docker build -t my-streamlit-app ./streamlit_app
Run the Streamlit Container
Run the Streamlit app container:

bash
Copy code
docker run --name streamlit-frontend \
  --network my-bridge-net \
  -p 8501:8501 \
  my-streamlit-app
7. Access the Streamlit App
Once the containers are up and running, open your browser and go to:

arduino
Copy code
http://localhost:8501
You should now see the Streamlit application displaying data from the users table in the MySQL database.

Project Structure
csharp
Copy code
postgresql_test/
├── streamlit_app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── mysql_init/
│   ├── init.sql
