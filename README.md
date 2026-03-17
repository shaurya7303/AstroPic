AstroPic — Data Pipeline with Apache Airflow

AstroPic is a data pipeline orchestration project built using Apache Airflow, designed to automate workflows using DAGs (Directed Acyclic Graphs). The project demonstrates containerized workflow management, scheduling, and testing of pipelines using modern data engineering practices.

🧠 What This Project Shows

This project is not just about code—it demonstrates:

Workflow orchestration using Apache Airflow

DAG creation and scheduling

Containerized environments using Docker

Structured testing of pipelines

Reproducible data workflows

⚙️ Tech Stack

Orchestration: Apache Airflow

Environment: Astronomer (Astro CLI)

Containerization: Docker & Docker Compose

Language: Python

Testing: Pytest (for DAG validation)

📁 Project Structure
AstroPic/
│── .astro/              # Astronomer project configuration
│── dags/               # Airflow DAGs (core workflows)
│── tests/dags/         # DAG testing modules
│── Dockerfile          # Custom Airflow container
│── docker-compose.yaml # Multi-service setup
│── requirements.txt    # Python dependencies
│── packages.txt        # System-level dependencies
│── README.md
🔄 How It Works

DAGs define workflows in the dags/ directory

Airflow scheduler executes tasks based on defined dependencies

Docker ensures consistent environment setup

Tests validate DAG integrity and execution logic

Think of it like this:

Airflow = “Operating system for your data pipelines”

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/shaurya7303/AstroPic.git
cd AstroPic
2. Start Airflow (via Docker)
docker-compose up --build
3. Access Airflow UI

Open in browser:

http://localhost:8080

(Default credentials if unchanged:)

username: admin
password: admin

Key Highlights

Modular DAG structure

Fully containerized setup

Testable workflows (big plus for production systems)

Clean separation of orchestration and logic

🚀 Future Improvements

Add real data sources (APIs / databases)

Integrate ML pipelines (model training + inference DAGs)

Add monitoring & alerting

Deploy on cloud (AWS / GCP Airflow)
