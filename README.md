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


---

### **6. Remove the Secret API Key**

1. **Move API Key to `.env`:**
   - Create a `.env` file (if you haven’t already) and add:
     ```
     SECRET_API_KEY=your_api_key_here
     ```

2. **Update `docker-compose.yml`:**
   - Link the `.env` file:
     ```yaml
     services:
       app:
         environment:
           - SECRET_API_KEY=${SECRET_API_KEY}
     ```

3. **Update `.gitignore`:**
   - Add `.env` so it won’t get uploaded to the repository:
     ```
     .env
     ```

---

### **7. Fix the `app.py` File**

1. Open the `app.py` file.

2. Remove anything that doesn’t belong in the code, like:
   - Debug lines (`print("Debugging...")`)
   - Random pasted terminal text.

3. Clean it up:
   - Keep only the actual logic needed for the app to run.
   - Check for sensitive data and remove it.

---

### **8. Simplify the Dockerfile**

1. Open the Dockerfile.

2. Decide between **CMD** or **ENTRYPOINT**:
   - If you just want the app to run, use CMD:
     ```dockerfile
     CMD ["python", "app.py"]
     ```
   - If you always want Python as the entry point, use ENTRYPOINT:
     ```dockerfile
     ENTRYPOINT ["python", "app.py"]
     ```

3. Don’t use both at the same time! Pick one.

---

Let me know if you need a step-by-step for any of these parts in more detail!
