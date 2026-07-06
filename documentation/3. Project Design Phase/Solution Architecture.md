# Solution Architecture
## FinRelief AI — AI-Powered Debt Relief & Financial Recovery Platform

---

## 📋 Team Header

| Field | Details |
|---|---|
| **Institution** | Vishnu Institute of Technology, Bhimavaram |
| **Department** | CSE (AI & DS) |
| **Academic Year** | 2026–2027 |
| **Program** | SmartBridge Google Cloud Generative AI Internship |
| **Project Title** | FinRelief AI — AI-Powered Debt Relief & Financial Recovery Platform |
| **GitHub** | https://github.com/JoelPrasannaKumar/finrelief |
| **Live URL** | https://finrelief.vercel.app |

### Team Members

| Role | Name | Email |
|---|---|---|
| **Team Lead** | Yeleti Joel Prasanna Kumar | 23pa1a45d0@vishnu.edu.in |
| Member | Kambala Kusuma Saisri | 23pa1a4553@vishnu.edu.in |
| Member | Kusume Raju | 23pa1a4579@vishnu.edu.in |
| Member | Siva Manikanta Akula | akulasivamanikanta14@gmail.com |
| Member | Harsha Vardhan Gorle | harshavardhanngorle@gmail.com |

---

## 1. High-Level Architecture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         FINRELIEF AI ARCHITECTURE                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   ┌──────────────────────────────────────────────────────────────┐          ║
║   │                     CLIENT LAYER                             │          ║
║   │    React + Vite  │  Vercel CDN  │  HTTPS  │  JWT Storage    │          ║
║   │                                                              │          ║
║   │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │          ║
║   │  │ Landing  │ │Dashboard │ │Settlement│ │ Recovery │  ...  │          ║
║   │  │   Page   │ │   Page   │ │  Advisor │ │ Planner  │       │          ║
║   │  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │          ║
║   └──────────────────────────┬───────────────────────────────────┘          ║
║                              │ HTTPS REST API                               ║
║   ┌──────────────────────────▼───────────────────────────────────┐          ║
║   │                     API GATEWAY LAYER                        │          ║
║   │              FastAPI + Uvicorn + CORS Middleware              │          ║
║   │                    Render.com Hosting                        │          ║
║   │  ┌────────────┐  ┌────────────┐  ┌────────────┐             │          ║
║   │  │ /api/auth  │  │ /api/loans │  │  /api/ai   │             │          ║
║   │  │  Router    │  │  Router    │  │  Router    │             │          ║
║   │  └────────────┘  └────────────┘  └────────────┘             │          ║
║   └────────────────┬──────────────────┬────────────────────────-─┘          ║
║                    │                  │                                      ║
║   ┌────────────────▼──┐  ┌────────────▼────────────────────────────┐       ║
║   │   DATA LAYER      │  │              AI LAYER                   │       ║
║   │                   │  │                                         │       ║
║   │  SQLite Database  │  │  ┌───────────────┐  ┌───────────────┐  │       ║
║   │  SQLAlchemy ORM   │  │  │ Google Gemini │  │ Python        │  │       ║
║   │                   │  │  │ 2.0 Flash API │  │ Fallback      │  │       ║
║   │  ┌─────────────┐  │  │  │               │  │ Engine        │  │       ║
║   │  │   users     │  │  │  │ Settlement    │  │               │  │       ║
║   │  │   loans     │  │  │  │ Advice        │  │ Template      │  │       ║
║   │  │   analysis  │  │  │  │ Letter Gen    │  │ Letters       │  │       ║
║   │  │   letters   │  │  │  │ Recovery Plan │  │ Rule-based    │  │       ║
║   │  │   recovery  │  │  │  │               │  │ Advice        │  │       ║
║   │  │   ai_hist   │  │  │  └───────────────┘  └───────────────┘  │       ║
║   │  │   rights    │  │  │         ↑ primary        ↑ fallback    │       ║
║   │  └─────────────┘  │  └─────────────────────────────────────────┘       ║
║   └───────────────────┘                                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Component Breakdown

### 2.1 Frontend Layer (React + Vite)

| Component | Technology | Purpose |
|---|---|---|
| Framework | React 18 + Vite 5 | SPA with fast HMR and build |
| Routing | React Router v6 | Client-side navigation |
| State Management | React Context API + useState/useEffect | Auth state, loan data |
| HTTP Client | Axios | API calls with interceptors |
| Styling | Vanilla CSS + CSS Variables | Custom design system |
| Icons | Lucide React | Consistent icon library |
| Charts | Recharts | Financial data visualizations |
| Hosting | Vercel | Global CDN, auto-deploy from GitHub |

**Key Frontend Directories:**
```
src/
├── components/         # Reusable UI components
│   ├── LoanCard.jsx
│   ├── MetricCard.jsx
│   ├── HealthScoreRing.jsx
│   ├── LoadingSkeleton.jsx
│   ├── EmptyState.jsx
│   └── Modal.jsx
├── pages/              # Route-level page components
│   ├── Landing.jsx
│   ├── Dashboard.jsx
│   ├── Settlement.jsx
│   ├── LetterGenerator.jsx
│   ├── RecoveryPlanner.jsx
│   ├── BorrowerRights.jsx
│   └── AIHistory.jsx
├── services/           # API service functions
│   └── api.js
├── context/            # React Context providers
│   └── AuthContext.jsx
└── utils/              # Utility functions
    └── formatters.js
```

---

### 2.2 Backend Layer (FastAPI)

| Component | Technology | Purpose |
|---|---|---|
| Framework | FastAPI 0.111+ | High-performance async API |
| Server | Uvicorn | ASGI server |
| ORM | SQLAlchemy 2.0 | Database abstraction |
| Auth | python-jose + passlib | JWT + bcrypt |
| AI Client | google-generativeai | Gemini API SDK |
| Validation | Pydantic v2 | Request/response schemas |
| Hosting | Render.com | Auto-deploy, free tier |

**Key Backend Directories:**
```
backend/
├── app/
│   ├── main.py             # FastAPI app entry point
│   ├── database.py         # DB connection + session
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── auth.py             # JWT utilities
│   ├── routers/
│   │   ├── auth.py         # Auth endpoints
│   │   ├── loans.py        # Loan CRUD endpoints
│   │   ├── analysis.py     # Financial analysis endpoints
│   │   └── ai.py           # AI advice endpoints
│   └── services/
│       ├── financial_engine.py  # DTI/Health Score calculations
│       ├── settlement_engine.py # Settlement % calculator
│       ├── gemini_service.py    # Gemini API integration
│       └── fallback_service.py  # Fallback AI engine
└── requirements.txt
```

---

### 2.3 AI Layer (Gemini + Fallback)

```
AI Request Flow:
─────────────────────────────────────────────────
User Request
    │
    ▼
Financial Engine (Calculate Health Score, DTI, Settlement %)
    │
    ▼
Try: Gemini 2.0 Flash API
    ├── Success → Return Gemini Response (labeled "AI-Powered")
    └── Failure (timeout/quota/error)
           │
           ▼
        Fallback Engine
        ├── Settlement: Rule-based calculation with template advice
        ├── Letter: Template-based with dynamic variables
        └── Recovery: Algorithmic plan generation
        Return Response (labeled "Standard Analysis")
─────────────────────────────────────────────────
```

---

### 2.4 Database Layer (SQLite + SQLAlchemy)

SQLite was chosen for simplicity in the internship context. The SQLAlchemy ORM abstraction means migration to PostgreSQL (production) requires only a connection string change.

---

## 3. Full API Endpoints Table

### Authentication Endpoints

| Method | Endpoint | Auth Required | Request Body | Response | Description |
|---|---|---|---|---|---|
| POST | `/api/auth/register` | No | `{name, email, password, income, employment_type}` | `{user, access_token, refresh_token}` | Register new user |
| POST | `/api/auth/login` | No | `{email, password}` | `{access_token, refresh_token, user}` | Login user |
| GET | `/api/auth/me` | Yes | — | `{user profile}` | Get current user |
| PUT | `/api/auth/me` | Yes | `{name, income, employment_type, dependents}` | `{updated user}` | Update profile |
| POST | `/api/auth/refresh` | No | `{refresh_token}` | `{new access_token}` | Refresh JWT |
| POST | `/api/auth/logout` | Yes | — | `{message}` | Logout user |

### Loan Management Endpoints

| Method | Endpoint | Auth Required | Request Body | Response | Description |
|---|---|---|---|---|---|
| GET | `/api/loans` | Yes | — | `[loan list]` | Get all user loans |
| POST | `/api/loans` | Yes | Loan schema | `{created loan}` | Add new loan |
| GET | `/api/loans/{id}` | Yes | — | `{loan detail}` | Get specific loan |
| PUT | `/api/loans/{id}` | Yes | Loan schema | `{updated loan}` | Update loan |
| DELETE | `/api/loans/{id}` | Yes | — | `{message}` | Delete loan |

### Financial Analysis Endpoints

| Method | Endpoint | Auth Required | Request Body | Response | Description |
|---|---|---|---|---|---|
| GET | `/api/analysis/health` | Yes | — | `{health_score, dti, breakdown}` | Get financial health |
| GET | `/api/analysis/summary` | Yes | — | `{totals, averages, projection}` | Get portfolio summary |
| GET | `/api/analysis/settlement/{loan_id}` | Yes | — | `{settlement_pct, range, factors}` | Get settlement % for loan |

### AI Endpoints

| Method | Endpoint | Auth Required | Request Body | Response | Description |
|---|---|---|---|---|---|
| POST | `/api/ai/settlement-advice` | Yes | `{loan_id}` | `{advice, source, model}` | Get settlement advice |
| POST | `/api/ai/generate-letter` | Yes | `{loan_id, letter_type, hardship_reason}` | `{letter_text, source}` | Generate letter |
| POST | `/api/ai/recovery-plan` | Yes | `{strategy, extra_payment}` | `{plan, timeline, source}` | Generate recovery plan |
| GET | `/api/ai/history` | Yes | — | `[history entries]` | Get AI history |
| GET | `/api/ai/history/{id}` | Yes | — | `{history entry}` | Get specific entry |

### Rights Endpoints

| Method | Endpoint | Auth Required | Request Body | Response | Description |
|---|---|---|---|---|---|
| GET | `/api/rights` | No | — | `[rights categories]` | Get all borrower rights |
| GET | `/api/rights/{category}` | No | — | `{category content}` | Get specific category |

---

## 4. Full Database Schema (All 7 Tables)

### Table 1: `users`

```sql
CREATE TABLE users (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            VARCHAR(100) NOT NULL,
    email           VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    monthly_income  DECIMAL(15, 2) NOT NULL DEFAULT 0.0,
    employment_type VARCHAR(50),        -- Salaried/Self-Employed/Business/Gig
    dependents      INTEGER DEFAULT 0,
    city            VARCHAR(100),
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_users_email (UNIQUE)
```

### Table 2: `loans`

```sql
CREATE TABLE loans (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    lender_name         VARCHAR(150) NOT NULL,
    lender_type         VARCHAR(50),    -- PSU Bank/Private Bank/NBFC/Cooperative/Other
    loan_type           VARCHAR(50) NOT NULL, -- Personal/Home/Vehicle/Education/CreditCard/Business/Medical/BNPL
    principal_amount    DECIMAL(15, 2) NOT NULL,
    outstanding_balance DECIMAL(15, 2) NOT NULL,
    interest_rate       DECIMAL(5, 2),  -- Annual percentage
    monthly_emi         DECIMAL(15, 2),
    tenure_months       INTEGER,
    remaining_months    INTEGER,
    start_date          DATE,
    overdue_months      INTEGER DEFAULT 0,
    status              VARCHAR(30) DEFAULT 'Active', -- Active/Overdue/In Settlement/Settled/Written Off
    loan_account_number VARCHAR(100),
    branch              VARCHAR(200),
    notes               TEXT,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_loans_user_id, idx_loans_status
```

### Table 3: `financial_analysis`

```sql
CREATE TABLE financial_analysis (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    health_score    DECIMAL(5, 2) NOT NULL,
    dti_ratio       DECIMAL(5, 2) NOT NULL,
    total_debt      DECIMAL(15, 2) NOT NULL,
    total_emi       DECIMAL(15, 2) NOT NULL,
    monthly_surplus DECIMAL(15, 2),
    risk_level      VARCHAR(20),     -- Excellent/Good/Fair/Critical
    penalty_dti     DECIMAL(5, 2),
    penalty_delinquency DECIMAL(5, 2),
    penalty_density DECIMAL(5, 2),
    penalty_lti     DECIMAL(5, 2),
    calculated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_analysis_user_id, idx_analysis_calculated_at
```

### Table 4: `settlement_analyses`

```sql
CREATE TABLE settlement_analyses (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_id             INTEGER NOT NULL REFERENCES loans(id) ON DELETE CASCADE,
    user_id             INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    settlement_pct_min  DECIMAL(5, 2) NOT NULL,
    settlement_pct_max  DECIMAL(5, 2) NOT NULL,
    settlement_pct_rec  DECIMAL(5, 2) NOT NULL,
    offer_amount_min    DECIMAL(15, 2) NOT NULL,
    offer_amount_max    DECIMAL(15, 2) NOT NULL,
    factors_applied     TEXT,          -- JSON string of factors used
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_settlement_loan_id, idx_settlement_user_id
```

### Table 5: `generated_letters`

```sql
CREATE TABLE generated_letters (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    loan_id         INTEGER NOT NULL REFERENCES loans(id) ON DELETE CASCADE,
    letter_type     VARCHAR(50) NOT NULL,  -- OTS/Hardship/PostDefault/FollowUp
    hardship_reason TEXT,
    letter_content  TEXT NOT NULL,
    generated_by    VARCHAR(20) DEFAULT 'gemini',  -- gemini/fallback
    model_version   VARCHAR(50),
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_letters_user_id, idx_letters_loan_id
```

### Table 6: `recovery_plans`

```sql
CREATE TABLE recovery_plans (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id             INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    strategy            VARCHAR(30) NOT NULL,   -- Avalanche/Snowball/Hybrid
    extra_payment       DECIMAL(15, 2) DEFAULT 0,
    plan_content        TEXT NOT NULL,           -- Full plan text/JSON
    debt_free_date      DATE,
    total_interest_saved DECIMAL(15, 2),
    months_to_freedom   INTEGER,
    generated_by        VARCHAR(20) DEFAULT 'gemini',
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_recovery_user_id
```

### Table 7: `ai_history`

```sql
CREATE TABLE ai_history (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    interaction_type VARCHAR(50) NOT NULL,  -- settlement_advice/letter/recovery_plan
    loan_id         INTEGER REFERENCES loans(id),
    input_data      TEXT NOT NULL,    -- JSON: financial data used as input
    ai_response     TEXT NOT NULL,    -- Full AI response text
    generated_by    VARCHAR(20) DEFAULT 'gemini',
    model_version   VARCHAR(50),
    tokens_used     INTEGER,
    response_time_ms INTEGER,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Indexes: idx_ai_history_user_id, idx_ai_history_type, idx_ai_history_created
```

---

## 5. Security Architecture

### 5.1 Authentication — JWT (JSON Web Tokens)

```
┌────────────────────────────────────────────────┐
│           JWT Token Architecture                │
├────────────────────────────────────────────────┤
│                                                │
│  Access Token:                                 │
│  ├── Algorithm: HS256                          │
│  ├── Expiry: 15 minutes                        │
│  ├── Payload: {sub: user_id, exp, iat}         │
│  └── Storage: localStorage (frontend)          │
│                                                │
│  Refresh Token:                                │
│  ├── Algorithm: HS256                          │
│  ├── Expiry: 7 days                            │
│  ├── Payload: {sub: user_id, type: "refresh"}  │
│  └── Storage: localStorage (frontend)          │
│                                                │
│  Token Refresh Flow:                           │
│  ├── Axios interceptor catches 401             │
│  ├── POST /api/auth/refresh with refresh_token │
│  ├── Get new access_token                      │
│  └── Retry original request                    │
└────────────────────────────────────────────────┘
```

### 5.2 Password Security — bcrypt

```python
# Password hashing configuration
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# bcrypt work factor: 12 rounds (default)
# Each hash is unique (random salt embedded)
# Resistant to rainbow table and brute-force attacks

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

### 5.3 CORS Configuration

```python
# CORS Middleware — FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://finrelief.vercel.app",  # Production frontend
        "http://localhost:5173",          # Development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
```

### 5.4 Additional Security Measures

| Security Measure | Implementation |
|---|---|
| SQL Injection | SQLAlchemy ORM (parameterized queries — no raw SQL) |
| XSS | React's automatic JSX escaping; no dangerouslySetInnerHTML |
| HTTPS | Enforced by Vercel (frontend) and Render (backend) |
| Sensitive Data | `.env` for secrets; never committed to GitHub |
| Gemini Data Privacy | Only anonymized financial parameters sent to API |
| Rate Limiting | Planned: SlowAPI middleware for production |
| Input Validation | Pydantic v2 schemas on all endpoints |

---

## 6. Deployment Architecture

### 6.1 Frontend — Vercel

```
GitHub Push to main branch
    │
    ▼
Vercel GitHub Integration (Auto-deploy)
    │
    ▼
npm run build (Vite)
    │
    ▼
Static files deployed to Vercel CDN (Edge Network)
    │
    ▼
https://finrelief.vercel.app (Live)

Environment Variables (Vercel Dashboard):
  VITE_API_BASE_URL=https://finrelief-api.onrender.com
```

### 6.2 Backend — Render

```
GitHub Push to main branch
    │
    ▼
Render GitHub Integration (Auto-deploy)
    │
    ▼
Docker Build (if Dockerfile present) OR
pip install -r requirements.txt
    │
    ▼
uvicorn app.main:app --host 0.0.0.0 --port $PORT
    │
    ▼
https://finrelief-api.onrender.com (Live)

Environment Variables (Render Dashboard):
  GEMINI_API_KEY=<secret>
  SECRET_KEY=<jwt_secret>
  DATABASE_URL=sqlite:///./finrelief.db
```

### 6.3 Docker Configuration

```dockerfile
# Dockerfile (Backend)
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 7. Sequence Diagrams

### 7.1 Login Flow

```
User          React Frontend        FastAPI Backend          SQLite DB
 │                  │                      │                     │
 │  Enter creds     │                      │                     │
 │─────────────────►│                      │                     │
 │                  │  POST /api/auth/login│                     │
 │                  │─────────────────────►│                     │
 │                  │                      │  SELECT user WHERE  │
 │                  │                      │  email=?            │
 │                  │                      │────────────────────►│
 │                  │                      │◄────────────────────│
 │                  │                      │  bcrypt.verify()    │
 │                  │                      │  Generate JWT       │
 │                  │◄─────────────────────│                     │
 │                  │  {access, refresh}   │                     │
 │                  │  Store in localStorage                      │
 │◄─────────────────│                      │                     │
 │  Redirect to     │                      │                     │
 │  Dashboard       │                      │                     │
```

### 7.2 Settlement Advice Flow

```
User    Frontend   FastAPI   Financial Engine   Gemini API   Fallback Engine
 │         │          │             │               │              │
 │  Click  │          │             │               │              │
 │ "Get    │          │             │               │              │
 │ Advice" │          │             │               │              │
 │────────►│          │             │               │              │
 │         │ POST     │             │               │              │
 │         │ /api/ai/ │             │               │              │
 │         │ settlement-advice      │               │              │
 │         │─────────►│             │               │              │
 │         │          │ calculate() │               │              │
 │         │          │────────────►│               │              │
 │         │          │◄────────────│               │              │
 │         │          │ {score,dti,settlement%}      │              │
 │         │          │ Try Gemini  │               │              │
 │         │          │─────────────────────────────►│              │
 │         │          │             │   Success?    │              │
 │         │          │ ┌─────────────────────────────►            │
 │         │          │ │  Return advice             │              │
 │         │          │ │  labeled "gemini"          │              │
 │         │          │ │                            │              │
 │         │          │ └─ On Failure ────────────────────────────►│
 │         │          │             │               │  Rule-based  │
 │         │          │             │               │  advice      │
 │         │          │◄────────────────────────────────────────── │
 │         │          │  Save to ai_history         │              │
 │         │◄─────────│             │               │              │
 │◄────────│           {advice, source, settlement%}│              │
```

### 7.3 Letter Generation Flow

```
User          Frontend          FastAPI          Gemini API
 │               │                 │                 │
 │ Select letter │                 │                 │
 │ type + reason │                 │                 │
 │──────────────►│                 │                 │
 │               │ POST            │                 │
 │               │ /api/ai/        │                 │
 │               │ generate-letter │                 │
 │               │────────────────►│                 │
 │               │                 │ Fetch loan data │
 │               │                 │ Fetch user data │
 │               │                 │ Build prompt    │
 │               │                 │────────────────►│
 │               │                 │ Generate letter │
 │               │                 │◄────────────────│
 │               │                 │ Save to         │
 │               │                 │ generated_letters
 │               │                 │ Save to         │
 │               │                 │ ai_history      │
 │               │◄────────────────│                 │
 │◄──────────────│ {letter_text}   │                 │
 │               │                 │                 │
 │ Copy/Download │                 │                 │
 │ Letter        │                 │                 │
```

---

## 8. Scalability Considerations

### 8.1 Current Architecture (Internship/MVP Scale)
- SQLite sufficient for thousands of users
- Single Render instance handles hundreds of concurrent users
- Gemini API quota: 15 RPM (free tier) — sufficient for demo

### 8.2 Production Scaling Path

| Component | Current | Production Scale |
|---|---|---|
| Database | SQLite | PostgreSQL (Supabase/RDS) — change only `DATABASE_URL` |
| Backend | Single Render instance | Multiple instances + Load Balancer |
| AI | Gemini API (free tier) | Gemini API (paid tier, higher RPM) |
| Frontend | Vercel (free tier) | Vercel Pro (custom domain, analytics) |
| Caching | None | Redis for frequent analysis queries |
| Queue | None | Celery + Redis for async letter generation |

### 8.3 Horizontal Scalability
FastAPI's async/await design enables high concurrency. The stateless JWT authentication allows any number of backend instances to serve requests without shared session state.

---

## 9. Monitoring & Observability (Planned)

| Area | Tool | Metric |
|---|---|---|
| API Health | Render built-in monitoring | Uptime, response time |
| Frontend | Vercel Analytics | Page views, TTFB |
| Error Tracking | Sentry (planned) | Exception rates |
| AI Usage | Custom logging in ai_history | Gemini vs. fallback ratio |
| DB Performance | SQLAlchemy query logging | Slow query detection |

---

*Document Version: 1.0 | Created: July 2026 | FinRelief AI Team — Vishnu Institute of Technology, Bhimavaram*
