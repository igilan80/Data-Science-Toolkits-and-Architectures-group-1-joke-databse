# Data-Science-Toolkits-and-Architectures-group-1-joke-databse
# Python App with Docker and PostgreSQL

## How to Set It Up
1. **Install Prerequisites**: Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

2. **Create a `.env` File**:
   - In the project folder, create a file called `.env` with the following content:
     ```
     SECRET_API_KEY= {your-API-Key}
     DATABASE_URL=postgresql://username:password@postgres:5432/dbname
     ```

3. **Run the Containers**:
   - Open your terminal in the project folder and run:
     ```bash
     docker-compose up --build
     ```

---

## How to Use the App
1. Go to `http://localhost:<port>` in your browser (replace `<port>` with the port set in `docker-compose.yml`).
2. API Endpoints:
   - `GET /example`: Does XYZ.
   - `POST /data`: Does ABC.

---

## Troubleshooting Tips
- If the **database doesn't connect**: Double-check the `DATABASE_URL` in `.env` matches `docker-compose.yml`.
- If the app doesn't start: Check logs with:
  ```bash
  docker-compose logs

