# Project Executable Files & Deployment Guide
## FinRelief AI - AI-Powered Debt Relief & Financial Recovery Platform

---

| Field | Details |
|---|---|
| **Institution** | Vishnu Institute of Technology, Bhimavaram |
| **Department** | CSE (AI & DS) |
| **Academic Year** | 2026–2027 |
| **Program** | SmartBridge Google Cloud Generative AI Internship |
| **Project Title** | FinRelief AI – AI-Powered Debt Relief & Financial Recovery Platform |
| **Team Lead** | Yeleti Joel Prasanna Kumar (23pa1a45d0@vishnu.edu.in) |
| **Team Members** | Kambala Kusuma Saisri, Kusume Raju, Siva Manikanta Akula, Harsha Vardhan Gorle |
| **Document Type** | Executable Files & Deployment Guide |
| **Date** | July 2026 |

---

## Table of Contents

1. [Live Application URLs](#1-live-application-urls)
2. [GitHub Repository](#2-github-repository)
3. [System Requirements](#3-system-requirements)
4. [Local Setup — Backend (FastAPI)](#4-local-setup--backend-fastapi)
5. [Local Setup — Frontend (React + Vite)](#5-local-setup--frontend-react--vite)
6. [Environment Variables](#6-environment-variables)
7. [Docker Setup](#7-docker-setup)
8. [Demo Account Credentials](#8-demo-account-credentials)
9. [Feature Access Guide](#9-feature-access-guide)
10. [Known Limitations](#10-known-limitations)
11. [Support Contact](#11-support-contact)

---

## 1. Live Application URLs

> [!IMPORTANT]
> The backend is hosted on Render.com's free tier. It may take **5–10 seconds to wake up** after a period of inactivity. Please wait for the first request to complete before using the application.

| Service | URL | Status |
|---|---|---|
| **Frontend (React App)** | https://finrelief.vercel.app | 🟢 Live |
| **Backend REST API** | https://finrelief-ai-backend.onrender.com | 🟢 Live |
| **Swagger API Documentation** | https://finrelief-ai-backend.onrender.com/api/docs | 🟢 Live |
| **ReDoc API Documentation** | https://finrelief-ai-backend.onrender.com/api/redoc | 🟢 Live |

### Accessing the Application

1. Open your browser and navigate to **https://finrelief.vercel.app**
2. You will be directed to the **Login** page.
3. Use the [demo credentials](#8-demo-account-credentials) or register a new account.
4. Upon login, the **Dashboard** appears showing your financial overview.

---

## 2. GitHub Repository

| Field | Detail |
|---|---|
| **Repository URL** | https://github.com/JoelPrasannaKumar/finrelief |
| **Visibility** | Public |
| **Default Branch** | `main` |
| **Backend Directory** | `/backend/` |
| **Frontend Directory** | `/frontend/` |
| **Documentation Directory** | `/documentation/` |

### Cloning the Repository

```bash
git clone https://github.com/JoelPrasannaKumar/finrelief.git
cd finrelief
```

### Repository Structure

```
finrelief/
├── backend/
│   ├── app/
│   │   ├── api/            # FastAPI route handlers
│   │   ├── models/         # SQLAlchemy ORM models
│   │   ├── schemas/        # Pydantic request/response schemas
│   │   ├── auth/           # JWT & password utilities
│   │   ├── financial/      # Financial calculation engine
│   │   └── settlement/     # Debt settlement engine
│   ├── tests/              # Pytest test suite
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend Docker configuration
│   └── main.py             # Application entry point
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable React components
│   │   ├── pages/          # Page-level components
│   │   ├── api/            # Axios API client
│   │   ├── context/        # Auth context (React Context API)
│   │   └── assets/         # Images, icons
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile          # Frontend Docker configuration
├── docker-compose.yml      # Full-stack Docker orchestration
└── documentation/          # All project documentation
```

---

## 3. System Requirements

### 3.1 Backend Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| **Python** | 3.10+ | 3.11+ |
| **RAM** | 512 MB | 2 GB |
| **Disk Space** | 200 MB | 1 GB |
| **OS** | Windows 10 / Ubuntu 20.04 / macOS 12 | Ubuntu 22.04 LTS |
| **Network** | Internet access for Gemini API | Stable broadband |

### 3.2 Frontend Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| **Node.js** | 18.x | 20.x LTS |
| **npm** | 9.x | 10.x |
| **RAM** | 1 GB | 4 GB |
| **Browser** | Chrome 110+ / Firefox 110+ | Latest Chrome |

### 3.3 Optional (Docker)

| Requirement | Version |
|---|---|
| Docker Engine | 24.x+ |
| Docker Compose | v2.x+ |

---

## 4. Local Setup — Backend (FastAPI)

Follow these steps precisely to set up the FinRelief AI backend on your local machine.

### Step 1: Navigate to the Backend Directory

```bash
cd finrelief/backend
```

### Step 2: Create and Activate a Python Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:

```
fastapi==0.111.0
uvicorn[standard]==0.30.0
sqlalchemy==2.0.30
pydantic==2.7.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.9
google-generativeai==0.7.2
python-dotenv==1.0.1
alembic==1.13.1
httpx==0.27.0
pytest==8.2.2
pytest-asyncio==0.23.7
```

### Step 4: Configure Environment Variables

Create a `.env` file in the `backend/` directory (see [Section 6](#6-environment-variables) for full variable list):

```bash
# backend/.env
SECRET_KEY=your-super-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
GOOGLE_API_KEY=your-google-gemini-api-key-here
DATABASE_URL=sqlite:///./finrelief.db
CORS_ORIGINS=http://localhost:5173,https://finrelief.vercel.app
```

### Step 5: Initialize the Database

```bash
# Run database migrations with Alembic
alembic upgrade head

# OR if Alembic is not configured, the app auto-creates tables on first run
```

### Step 6: Start the Backend Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will now be available at:
- **API Base:** `http://localhost:8000/api/`
- **Swagger Docs:** `http://localhost:8000/api/docs`
- **ReDoc:** `http://localhost:8000/api/redoc`

### Step 7: Verify the Backend is Running

```bash
curl http://localhost:8000/api/health
# Expected: {"status": "ok", "message": "FinRelief AI Backend is running"}
```

---

## 5. Local Setup — Frontend (React + Vite)

### Step 1: Navigate to the Frontend Directory

```bash
cd finrelief/frontend
```

### Step 2: Install Node.js Dependencies

```bash
npm install
```

### Step 3: Configure Environment Variables

Create a `.env` file in the `frontend/` directory:

```bash
# frontend/.env
VITE_API_BASE_URL=http://localhost:8000/api
```

> For production builds pointing to the live backend, set:
> ```
> VITE_API_BASE_URL=https://finrelief-ai-backend.onrender.com/api
> ```

### Step 4: Start the Development Server

```bash
npm run dev
```

The frontend will be available at **http://localhost:5173**

### Step 5: Build for Production

```bash
npm run build
# Output will be in the dist/ directory
```

### Step 6: Preview Production Build Locally

```bash
npm run preview
# Available at http://localhost:4173
```

---

## 6. Environment Variables

### 6.1 Backend Environment Variables

| Variable | Required | Description | Example Value |
|---|---|---|---|
| `SECRET_KEY` | ✅ Yes | JWT signing secret (use a long random string in production) | `a3f8k9...` (64+ chars) |
| `ALGORITHM` | ✅ Yes | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | ✅ Yes | JWT token validity duration | `1440` (24 hours) |
| `GOOGLE_API_KEY` | ✅ Yes | Google Gemini API key from Google AI Studio | `AIzaSy...` |
| `DATABASE_URL` | ✅ Yes | SQLAlchemy database connection string | `sqlite:///./finrelief.db` |
| `CORS_ORIGINS` | ✅ Yes | Comma-separated list of allowed CORS origins | `http://localhost:5173` |

### 6.2 Frontend Environment Variables

| Variable | Required | Description | Example Value |
|---|---|---|---|
| `VITE_API_BASE_URL` | ✅ Yes | Full URL to the backend API | `http://localhost:8000/api` |

### 6.3 Getting a Google Gemini API Key

1. Visit **https://aistudio.google.com/app/apikey**
2. Sign in with a Google account.
3. Click **"Create API Key"**.
4. Copy the key and paste it as `GOOGLE_API_KEY` in your `.env` file.

> [!CAUTION]
> Never commit your `.env` file to version control. Ensure `.env` is listed in `.gitignore`.

---

## 7. Docker Setup

### 7.1 Running with Docker Compose (Recommended)

Docker Compose will start both the backend and frontend containers simultaneously.

```bash
# From the project root (where docker-compose.yml lives)
docker-compose up --build
```

Services will be available at:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000/api`
- Swagger: `http://localhost:8000/api/docs`

### 7.2 `docker-compose.yml`

```yaml
version: '3.9'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - DATABASE_URL=sqlite:///./finrelief.db
      - CORS_ORIGINS=http://localhost:3000
    volumes:
      - ./backend/finrelief.db:/app/finrelief.db

  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    environment:
      - VITE_API_BASE_URL=http://localhost:8000/api
    depends_on:
      - backend
```

### 7.3 Backend Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 7.4 Frontend Dockerfile

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### 7.5 Running Individual Docker Containers

```bash
# Backend only
cd backend
docker build -t finrelief-backend .
docker run -p 8000:8000 --env-file .env finrelief-backend

# Frontend only
cd frontend
docker build -t finrelief-frontend .
docker run -p 3000:80 finrelief-frontend
```

---

## 8. Demo Account Credentials

A pre-seeded demo account is available for evaluators to test the application without registering.

> [!NOTE]
> This demo account has pre-loaded loan data (2 loans) so evaluators can immediately see the Dashboard, Analysis, and Settlement features in action.

| Field | Value |
|---|---|
| **Email** | `demo@finrelief.ai` |
| **Password** | `Demo@1234` |
| **Account Name** | Rahul Sharma |
| **Pre-loaded Loans** | HDFC Bank Personal Loan (₹1,50,000), Bajaj Finserv EMI (₹45,000) |

> [!WARNING]
> Data associated with the demo account may be reset periodically. Do not use this account to store real financial information.

---

## 9. Feature Access Guide

| Feature | How to Access | Notes |
|---|---|---|
| **Register** | Home page → "Get Started" | Creates a new account |
| **Login** | `/login` route | JWT token stored in localStorage |
| **Dashboard** | `/dashboard` (post-login home) | Shows financial summary cards |
| **Add Loan** | Dashboard → "Add Loan" button | Opens loan entry modal/form |
| **View Analysis** | Sidebar → "Analysis" | Recharts pie + bar charts |
| **Settlement AI** | Sidebar → "Settlement" | Calls Gemini 2.0 Flash |
| **Letter Generator** | Sidebar → "Letters" | AI-generated negotiation letter |
| **Action History** | Sidebar → "History" | Timeline of past actions |
| **Borrower Rights** | Sidebar → "Rights" | Static AI-curated content |
| **Profile** | Top right avatar → "Profile" | Edit name, income details |
| **Logout** | Top right avatar → "Logout" | Clears JWT, redirects to login |
| **API Docs** | https://finrelief-ai-backend.onrender.com/api/docs | Interactive Swagger UI |

---

## 10. Known Limitations

> [!WARNING]
> Please review the following known limitations before evaluating the application.

| # | Limitation | Impact | Workaround / Future Fix |
|---|---|---|---|
| 1 | **SQLite data wipe on Render free tier** | Database resets when the backend container restarts (Render free tier does not persist disk) | Use demo account; production deployment will use PostgreSQL |
| 2 | **Render cold start delay** | Backend takes 5–10 seconds to respond after inactivity | Wait for the first request; subsequent calls are fast |
| 3 | **No email verification** | Users can register with any email without verification | Email OTP planned in Phase 1 roadmap |
| 4 | **Gemini API rate limits** | Google Gemini 2.0 Flash free tier has per-minute request limits | Rate limiting and retry logic planned |
| 5 | **No real bank data integration** | All loan data is manually entered by the user | Bank API integration planned in Phase 3 |
| 6 | **Single-currency support** | Only Indian Rupee (₹) supported | Multi-currency support in Phase 2 |
| 7 | **No mobile app** | Web-only, though mobile-responsive | React Native app planned in Phase 2 |
| 8 | **No 2FA authentication** | Password-only login | TOTP/2FA planned in Phase 1 |

---

## 11. Support Contact

For technical issues, questions about setup, or access problems:

| Contact | Details |
|---|---|
| **Primary Contact** | Yeleti Joel Prasanna Kumar |
| **Email** | 23pa1a45d0@vishnu.edu.in |
| **GitHub Issues** | https://github.com/JoelPrasannaKumar/finrelief/issues |
| **Institution** | Vishnu Institute of Technology, Bhimavaram |

For team member contacts:
- Kambala Kusuma Saisri: 23pa1a4553@vishnu.edu.in
- Kusume Raju: 23pa1a4579@vishnu.edu.in
- Siva Manikanta Akula: akulasivamanikanta14@gmail.com
- Harsha Vardhan Gorle: harshavardhanngorle@gmail.com

---

*Document prepared by Team FinRelief AI | Vishnu Institute of Technology, Bhimavaram | July 2026*
