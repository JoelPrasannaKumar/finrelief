# Technology Stack
## SmartBridge Google Cloud Generative AI Internship

---

## 📋 Team Information

| Field | Details |
|---|---|
| **Institution** | Vishnu Institute of Technology, Bhimavaram |
| **Department** | CSE (AI & DS) |
| **Academic Year** | 2026–2027 |
| **Program** | SmartBridge Google Cloud Generative AI Internship |
| **Project Title** | FinRelief AI – AI-Powered Debt Relief & Financial Recovery Platform |
| **GitHub** | https://github.com/JoelPrasannaKumar/finrelief |
| **Live URL** | https://finrelief.vercel.app |

### 👥 Team Members

| Role | Name | Email |
|---|---|---|
| **Team Lead** | Yeleti Joel Prasanna Kumar | 23pa1a45d0@vishnu.edu.in |
| **Member** | Kambala Kusuma Saisri | 23pa1a4553@vishnu.edu.in |
| **Member** | Kusume Raju | 23pa1a4579@vishnu.edu.in |
| **Member** | Siva Manikanta Akula | akulasivamanikanta14@gmail.com |
| **Member** | Harsha Vardhan Gorle | harshavardhanngorle@gmail.com |

---

## 1. Architecture Overview

FinRelief AI follows a **3-tier client-server architecture** with a dedicated AI integration layer:

```
┌─────────────────────────────────────────────────────────┐
│                   PRESENTATION TIER                      │
│         React 18 + Vite (Deployed on Vercel)            │
│    Components │ Routing │ State │ API Client (Axios)     │
└────────────────────────┬────────────────────────────────┘
                         │ HTTPS REST API
┌────────────────────────▼────────────────────────────────┐
│                    BUSINESS LOGIC TIER                   │
│         FastAPI (Python 3.11) - Deployed on Render      │
│    Auth │ Loan Mgmt │ AI Orchestration │ Letter Gen      │
│                    SQLAlchemy ORM                        │
└───────────────────┬──────────────┬──────────────────────┘
                    │              │ HTTPS API Call
┌───────────────────▼────┐  ┌──────▼───────────────────────┐
│      DATA TIER          │  │       AI INTEGRATION TIER    │
│  SQLite (Development)   │  │  Google Gemini 2.0 Flash API │
│  PostgreSQL (Prod-ready)│  │  (google-generativeai SDK)   │
│  via SQLAlchemy         │  │  Structured Prompt Pipeline  │
└─────────────────────────┘  └──────────────────────────────┘
```

---

## 2. Complete Technology Stack Table

| Layer | Technology | Version | Purpose | Why Chosen |
|---|---|---|---|---|
| **Frontend Framework** | React | 18.2.0 | UI component library | Industry standard, component reusability, vast ecosystem |
| **Frontend Build Tool** | Vite | 5.0.0 | Dev server & bundler | 10–100x faster than Create React App; native ESM support |
| **Frontend Routing** | React Router | 6.22.0 | Client-side navigation | De-facto standard for React SPAs |
| **HTTP Client** | Axios | 1.6.0 | API communication | Interceptors for JWT token injection; better than fetch |
| **Charts & Visualization** | Recharts | 2.10.0 | Debt composition charts | React-native charts; minimal bundle size |
| **Backend Framework** | FastAPI | 0.104.1 | REST API server | Async support; auto OpenAPI docs; Python type hints |
| **Backend Language** | Python | 3.11.0 | Server-side logic | FastAPI requires Python 3.7+; 3.11 for performance gains |
| **ASGI Server** | Uvicorn | 0.24.0 | FastAPI runtime server | Recommended ASGI server for FastAPI; async-capable |
| **ORM** | SQLAlchemy | 2.0.23 | Database abstraction | Supports SQLite and PostgreSQL; clean async ORM |
| **DB Migrations** | Alembic | 1.12.0 | Schema versioning | Native SQLAlchemy migrations; version-controlled schemas |
| **Database (Dev)** | SQLite | 3.42+ | Local data persistence | Zero config; perfect for development and small deployments |
| **Authentication** | python-jose | 3.3.0 | JWT token creation/validation | Battle-tested JWT library for Python |
| **Password Hashing** | passlib[bcrypt] | 1.7.4 | Secure credential storage | bcrypt is the gold standard for password hashing |
| **AI Model** | Google Gemini 2.0 Flash | 2.0-flash | Debt analysis, letter generation | Fast, affordable, Google Cloud integration, multimodal |
| **AI SDK** | google-generativeai | 0.7.0 | Python SDK for Gemini API | Official Google SDK; clean API; streaming support |
| **Environment Config** | python-dotenv | 1.0.0 | Environment variable management | Separates config from code; 12-factor app compliance |
| **PDF Generation** | ReportLab / fpdf2 | 2.7.0 | OTS letter PDF export | Pure Python PDF generation; no external dependencies |
| **CORS Middleware** | FastAPI CORSMiddleware | Built-in | Cross-origin request handling | Required for React (port 5173) → FastAPI (port 8000) |
| **Data Validation** | Pydantic | 2.5.0 | Request/response validation | Integrated with FastAPI; auto-generates JSON schemas |
| **Containerization** | Docker | 24.0+ | Application packaging | Environment-agnostic deployment; reproducible builds |
| **Orchestration** | Docker Compose | 2.21+ | Multi-service local dev | Start all services with single command |
| **Frontend Hosting** | Vercel | Latest | React app deployment | Zero-config deployment; free tier; global CDN |
| **Backend Hosting** | Render.com | Latest | FastAPI deployment | Free tier; Docker support; easy environment variables |
| **Version Control** | Git + GitHub | Latest | Source code management | Industry standard; GitHub Actions for CI/CD |
| **CI/CD** | GitHub Actions | Latest | Automated deployment | On push to main: test → build → deploy |
| **Code Style (Python)** | flake8 + black | Latest | Linting and formatting | PEP 8 compliance; consistent code style |
| **Testing (Python)** | pytest + httpx | 7.4.0 | Backend unit and API tests | FastAPI's recommended testing approach |
| **Testing (Frontend)** | Vitest | 1.0.0 | Frontend unit tests | Vite-native; same config as Vite build |

---

## 3. Backend Stack — Detailed

### FastAPI

**What it is:** FastAPI is a modern, high-performance Python web framework for building APIs. It is built on top of Starlette (ASGI) and Pydantic.

**Why FastAPI over Django/Flask:**

| Feature | FastAPI | Django REST | Flask |
|---|---|---|---|
| Performance | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Auto API Docs | ✅ Built-in | ❌ Requires drf-yasg | ❌ Manual |
| Async Support | ✅ Native | 🟡 Limited | ❌ Add-on needed |
| Type Safety | ✅ Pydantic | 🟡 Partial | ❌ None |
| Learning Curve | Medium | High | Low |
| Boilerplate | Minimal | Heavy | Minimal |

**Key FastAPI Features Used:**
- `Depends()` for dependency injection (auth middleware, DB sessions)
- `APIRouter` for modular routing (auth, loans, AI, letters)
- `HTTPException` for standardized error responses
- `BackgroundTasks` for async operations (email sending)
- Auto-generated Swagger UI at `/docs` for API documentation

### SQLAlchemy 2.0

**Architecture Pattern Used:** Repository Pattern with SQLAlchemy ORM

```python
# Example: Loan Repository Pattern
class LoanRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_loans(self, user_id: int) -> List[Loan]:
        return self.db.query(Loan).filter(Loan.user_id == user_id).all()
    
    def create_loan(self, loan_data: LoanCreate, user_id: int) -> Loan:
        loan = Loan(**loan_data.dict(), user_id=user_id)
        self.db.add(loan)
        self.db.commit()
        self.db.refresh(loan)
        return loan
```

**Why SQLAlchemy 2.0 specifically:**
- New `select()` style queries are more readable and type-safe
- Better async support with `AsyncSession`
- Compatible with both SQLite (dev) and PostgreSQL (production) without code changes

### JWT Authentication Flow

```
Client                    FastAPI                    SQLAlchemy
  │                          │                           │
  │  POST /auth/login        │                           │
  │  {email, password}       │                           │
  │─────────────────────────►│                           │
  │                          │  Query user by email      │
  │                          │──────────────────────────►│
  │                          │  Return user record       │
  │                          │◄──────────────────────────│
  │                          │  Verify bcrypt hash       │
  │                          │  Generate JWT (24h exp)   │
  │  200 OK {access_token}   │                           │
  │◄─────────────────────────│                           │
  │                          │                           │
  │  GET /loans              │                           │
  │  Authorization: Bearer   │                           │
  │─────────────────────────►│                           │
  │                          │  Decode JWT               │
  │                          │  Extract user_id          │
  │                          │  Query loans              │
  │                          │──────────────────────────►│
  │  200 OK {loans}          │                           │
  │◄─────────────────────────│                           │
```

---

## 4. Frontend Stack — Detailed

### React 18 + Vite

**Why React 18:**
- Industry-standard library with massive component ecosystem
- Concurrent Mode for better performance with AI streaming responses
- React Hooks (useState, useContext, useEffect, useCallback) for clean state management
- JSX for readable, component-based UI architecture

**Why Vite over Create React App:**

| Feature | Vite | Create React App |
|---|---|---|
| Dev Server Start Time | < 500ms | 5–15 seconds |
| Hot Module Replacement | Instant | 2–10 seconds |
| Build Tool | Rollup (optimized) | Webpack |
| Bundle Size | Smaller (tree-shaking) | Larger |
| Config Flexibility | High | Limited |
| Community Trend | Growing rapidly | Deprecated by React team |

**Project Structure:**

```
finrelief-frontend/
├── src/
│   ├── components/         # Reusable UI components
│   │   ├── LoanCard.jsx
│   │   ├── DebtSeverityGauge.jsx
│   │   ├── RecoveryRoadmap.jsx
│   │   └── ...
│   ├── pages/              # Route-level page components
│   │   ├── Dashboard.jsx
│   │   ├── AddLoan.jsx
│   │   ├── Analysis.jsx
│   │   ├── OTSAdvisor.jsx
│   │   ├── LetterGenerator.jsx
│   │   └── ...
│   ├── context/            # React Context for global state
│   │   ├── AuthContext.jsx
│   │   └── LoanContext.jsx
│   ├── api/                # Axios API client and endpoints
│   │   ├── client.js       # Axios instance with JWT interceptor
│   │   ├── auth.js
│   │   ├── loans.js
│   │   └── ai.js
│   ├── hooks/              # Custom React Hooks
│   │   ├── useLoans.js
│   │   └── useAnalysis.js
│   └── utils/              # Utility functions
│       ├── formatCurrency.js
│       └── calculateDTI.js
└── public/
```

### Axios JWT Interceptor

```javascript
// src/api/client.js — Automatic JWT injection
import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: { 'Content-Type': 'application/json' }
});

// Request interceptor: Inject JWT token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor: Handle 401 (token expiry)
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Attempt token refresh
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default apiClient;
```

---

## 5. AI/ML Stack — Detailed

### Google Gemini 2.0 Flash

**Model Details:**

| Property | Value |
|---|---|
| **Model ID** | `gemini-2.0-flash-exp` |
| **Provider** | Google DeepMind |
| **Context Window** | 1 million tokens |
| **Output Tokens** | Up to 8,192 tokens |
| **Latency** | < 3 seconds (average) |
| **Cost (Free Tier)** | 15 RPM, 1M TPD |
| **Safety Filters** | Built-in (harassment, hate speech, dangerous content) |
| **Multimodal** | Text, Image (vision), Code |

**Why Gemini 2.0 Flash over Alternatives:**

| Criterion | Gemini 2.0 Flash | GPT-4o | Claude 3.5 Sonnet | Llama 3.1 70B |
|---|---|---|---|---|
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Cost (free tier) | ✅ Generous | ❌ Paid only | ❌ Limited free | ✅ Free (self-host) |
| Google Cloud Integration | ✅ Native | ❌ None | ❌ None | ⚠️ Via Vertex AI |
| Financial Domain Knowledge | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Indian Context | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Internship Program Fit | ✅ Required | ❌ N/A | ❌ N/A | ❌ N/A |
| Infrastructure Required | None (API) | None (API) | None (API) | GPU cluster |

**Prompt Engineering Architecture:**

```python
# Example: Debt Analysis Prompt Structure
def build_analysis_prompt(user_profile: dict, loans: list) -> str:
    return f"""
You are FinRelief AI, an expert financial counselor specializing in 
Indian personal debt management and OTS settlement strategies.

USER FINANCIAL PROFILE:
- Monthly Income: ₹{user_profile['income']:,.0f}
- Monthly Non-EMI Expenses: ₹{user_profile['expenses']:,.0f}
- Disposable Income (before EMIs): ₹{user_profile['income'] - user_profile['expenses']:,.0f}
- City: {user_profile['city']}
- Occupation: {user_profile['occupation']}

ACTIVE LOANS ({len(loans)} total):
{format_loans_for_prompt(loans)}

TASK: Provide a comprehensive debt analysis report with:
1. Overall Financial Health Assessment (2-3 sentences)
2. Debt Severity Score (1-10) with detailed breakdown
3. Prioritized Loan Payoff Strategy (avalanche or snowball with justification)
4. Month-by-month 12-month recovery roadmap
5. Three specific, actionable recommendations
6. OTS settlement opportunity identification

Format your response as structured JSON matching this schema:
{ANALYSIS_RESPONSE_SCHEMA}

IMPORTANT: This is informational guidance only. Always include appropriate 
disclaimers. Base recommendations on the user's actual financial data provided.
Reference RBI guidelines where relevant.
"""
```

**Gemini Integration Flow:**

```python
# src/services/gemini_service.py
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

class GeminiService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        self.generation_config = genai.types.GenerationConfig(
            temperature=0.4,        # Lower temp for more consistent financial advice
            top_p=0.95,
            top_k=40,
            max_output_tokens=4096,
        )
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
    
    async def analyze_debt(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )
        return response.text
    
    async def generate_letter(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.6,    # Slightly higher for natural letter writing
                max_output_tokens=2048,
            )
        )
        return response.text
```

---

## 6. DevOps Stack — Detailed

### Docker

**Dockerfile (Backend):**

```dockerfile
# Production Dockerfile for FinRelief AI Backend
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Expose port
EXPOSE 8000

# Run with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=sqlite:///./finrelief.db
    volumes:
      - ./backend:/app
      - db_data:/app/data
    restart: unless-stopped

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:8000
    depends_on:
      - backend

volumes:
  db_data:
```

### GitHub Actions CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy FinRelief AI

on:
  push:
    branches: [main]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r backend/requirements.txt
      - name: Run tests
        run: pytest backend/tests/ -v --cov=backend

  deploy-backend:
    needs: test-backend
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Render
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}

  deploy-frontend:
    needs: test-backend
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Vercel
        run: npx vercel --prod --token ${{ secrets.VERCEL_TOKEN }}
```

---

## 7. Architecture Decision Records (ADRs)

Architecture Decision Records document the **why** behind major technical decisions. This ensures future developers (and reviewers) understand the reasoning.

---

### ADR-001: Choosing FastAPI Over Django REST Framework

**Date:** Week 1 of Internship  
**Status:** Accepted  
**Deciders:** Yeleti Joel Prasanna Kumar, Siva Manikanta Akula

#### Context
The team needed a Python backend framework for the FinRelief AI REST API. The two primary options considered were Django REST Framework (DRF) and FastAPI.

#### Decision
**FastAPI was selected as the backend framework.**

#### Rationale

**Arguments FOR FastAPI:**
1. **Async-native:** FastAPI is built on Starlette, which is fully async. This is critical because Gemini API calls are I/O-bound — async allows the server to handle multiple AI requests concurrently without blocking.
2. **Auto-generated documentation:** FastAPI automatically generates Swagger UI at `/docs` and ReDoc at `/redoc`. This is invaluable for team collaboration and project presentation.
3. **Pydantic integration:** Pydantic v2 (bundled with FastAPI) provides automatic request validation, type checking, and serialization — reducing boilerplate significantly.
4. **Performance:** FastAPI benchmarks show 2–3x better requests/second than Django REST Framework under concurrent load.
5. **Learning curve:** For a 6-week internship, FastAPI's minimal boilerplate means faster time-to-MVP compared to Django's "batteries included" setup.
6. **Modern Python:** FastAPI uses Python type hints throughout, which improves code readability and IDE support.

**Arguments AGAINST FastAPI:**
1. Django has a mature admin interface (not needed for this project)
2. Django has more built-in features (ORM, templating) — but we're using SQLAlchemy separately and React for templates

#### Consequences
- All API endpoints will use FastAPI's router pattern
- Pydantic models define all request/response schemas
- Uvicorn serves as the ASGI server
- No Django admin; admin operations done directly via DB

---

### ADR-002: SQLite for Development, SQLAlchemy for DB Abstraction

**Date:** Week 1 of Internship  
**Status:** Accepted  
**Deciders:** Full Team

#### Context
The team needed to choose a database for the FinRelief AI backend. Options considered: SQLite, PostgreSQL, MongoDB, and Firebase.

#### Decision
**SQLite for development with SQLAlchemy ORM for database abstraction (enabling future migration to PostgreSQL).**

#### Rationale

**Why SQLite for development:**
1. **Zero setup:** No separate database server to install and manage. Perfect for a 5-person team with varying environment setups.
2. **File-based:** The database is a single `.db` file — easy to back up, share, and inspect.
3. **SQLAlchemy compatibility:** SQLite is fully supported by SQLAlchemy, and switching to PostgreSQL requires only changing the `DATABASE_URL` environment variable.
4. **Project scale:** For an internship project with hundreds (not millions) of users, SQLite performance is entirely adequate.
5. **Docker simplicity:** No need for a `db` service in docker-compose.yml during development.

**Why NOT MongoDB:**
1. FinRelief AI's data model is highly relational (users → loans → analyses → letters)
2. ORM tools like SQLAlchemy make relational data significantly easier to manage
3. SQL is more appropriate for financial data integrity (ACID compliance)

**SQLAlchemy's role:** By using SQLAlchemy as the ORM abstraction layer, we can switch from SQLite to PostgreSQL by changing ONE line:
```
# Development
DATABASE_URL = "sqlite:///./finrelief.db"

# Production (when needed)
DATABASE_URL = "postgresql://user:pass@host:5432/finrelief"
```

#### Consequences
- All database interactions go through SQLAlchemy models
- No raw SQL queries anywhere in the codebase
- Alembic manages schema migrations
- Production deployment can upgrade to PostgreSQL without refactoring

---

### ADR-003: React + Vite Over Next.js

**Date:** Week 1 of Internship  
**Status:** Accepted  
**Deciders:** Yeleti Joel Prasanna Kumar, Kusume Raju

#### Context
The team needed a frontend framework. Options: React + Vite (SPA), Next.js (SSR/SSG), Vue.js + Vite, or vanilla JavaScript.

#### Decision
**React 18 with Vite as the frontend framework and build tool.**

#### Rationale

**Why React + Vite over Next.js:**
1. **SPA is sufficient:** FinRelief AI is a web application requiring authentication. All pages require login, so Server-Side Rendering (Next.js's primary advantage) provides minimal SEO benefit.
2. **Simpler deployment:** A React SPA can be deployed to Vercel as static files. Next.js requires a Node.js server runtime, which complicates the Render.com free tier deployment.
3. **Team familiarity:** The team has more experience with plain React patterns vs. Next.js's App Router and server components — important for a time-constrained internship.
4. **Vite speed:** Vite's dev server starts in < 500ms vs. Next.js's 5–10 seconds, significantly improving development velocity.
5. **Bundle optimization:** Vite uses Rollup for production builds with automatic code splitting, tree shaking, and asset optimization.

**Why React over Vue.js:**
1. React has a significantly larger ecosystem (more third-party component libraries, more Stack Overflow answers)
2. Better TypeScript support (TypeScript migration is easier if needed)
3. Team has more existing React knowledge

**Why NOT vanilla JavaScript:**
1. Component reusability is critical for FinRelief AI (loan cards, analysis components reused across pages)
2. State management across pages (auth state, loan data) requires a proper framework
3. React Router provides clean SPA navigation without page reloads

#### Consequences
- Frontend is deployed as static files on Vercel (free tier)
- Client-side routing via React Router v6
- All data fetching via Axios to the FastAPI backend
- No server-side rendering; SEO for public pages (landing, login) handled with react-helmet

---

## 8. Technology Risks and Mitigations

| Technology | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| Gemini 2.0 Flash | API rate limits (15 RPM free tier) | Medium | High | Response caching; rate limiting middleware; user-facing message |
| Gemini 2.0 Flash | Model unavailability / service outage | Low | High | Graceful error handling; retry with exponential backoff |
| SQLite | Concurrent write conflicts | Low | Medium | SQLAlchemy connection pooling; WAL mode enabled |
| Vercel | Free tier function timeout (12s) | Medium | Medium | AI endpoints optimized for < 10s; Gemini Flash chosen for speed |
| React | Large bundle size degrading performance | Low | Medium | Vite code splitting; lazy loading of heavy components |
| JWT | Token expiry causing UX disruption | Medium | Low | Refresh token flow; auto-renewal 5 minutes before expiry |
| Docker | Environment inconsistencies | Low | Low | docker-compose ensures consistent environments |

---

## 9. Technology License Summary

| Technology | License | Commercial Use Allowed |
|---|---|---|
| React | MIT | ✅ Yes |
| Vite | MIT | ✅ Yes |
| FastAPI | MIT | ✅ Yes |
| SQLAlchemy | MIT | ✅ Yes |
| google-generativeai | Apache 2.0 | ✅ Yes (subject to Google's Terms of Service) |
| SQLite | Public Domain | ✅ Yes |
| Docker | Apache 2.0 | ✅ Yes |
| Pydantic | MIT | ✅ Yes |
| python-jose | MIT | ✅ Yes |
| passlib | BSD | ✅ Yes |

---

*Document prepared by: Team FinRelief AI | SmartBridge Google Cloud Generative AI Internship | Vishnu Institute of Technology, Bhimavaram*
