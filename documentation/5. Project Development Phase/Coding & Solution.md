# Coding & Solution
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

## 1. Development Methodology — Agile (Scrum-Lite)

FinRelief AI was developed using an **Agile Scrum-Lite** methodology adapted for a 5-member student team working part-time. Rather than strict Scrum ceremonies, the team adopted a lightweight version preserving the core principles:

- **Iterative delivery** in 2-week sprints
- **Daily async standups** via WhatsApp (What I did / What I'm doing / Blockers)
- **Sprint planning** at the start of each sprint (Google Meet, 1 hour)
- **Sprint review** at end of each sprint (demo + retrospective, 30 min)
- **Continuous integration** via GitHub with protected `main` branch
- **Backlog management** via GitHub Issues with labels (feature, bug, docs, enhancement)

### Agile Principles Applied

| Principle | How Applied in FinRelief AI |
|---|---|
| Working software over documentation | Each sprint delivered deployable features |
| Individuals over processes | Team self-organized; Joel arbitrated conflicts |
| Customer collaboration | Real user scenarios drove feature design |
| Responding to change | Settlement engine formula revised mid-Sprint 2 based on research |

---

## 2. Sprint Plan (4 Sprints × 2 Weeks)

### Sprint 1 (Weeks 1–2): Foundation
**Goal:** Project foundation — architecture, auth, and base setup

| Task | Owner | Status |
|---|---|---|
| GitHub repo + branch strategy | Joel | ✅ Done |
| FastAPI project scaffolding + Docker | Joel | ✅ Done |
| SQLAlchemy models (all 7 tables) | Joel | ✅ Done |
| JWT authentication endpoints | Joel + Saisri | ✅ Done |
| React + Vite project setup | Raju | ✅ Done |
| Design system (CSS variables, fonts) | Saisri | ✅ Done |
| Login + Register pages | Saisri | ✅ Done |
| Auth context + Axios interceptors | Saisri | ✅ Done |
| Architecture documentation | Joel | ✅ Done |

**Sprint 1 Demo:** Working login/register flow with JWT stored in localStorage; protected route redirects.

---

### Sprint 2 (Weeks 3–4): Core Business Logic
**Goal:** Loan management, financial engine, and dashboard

| Task | Owner | Status |
|---|---|---|
| Loan CRUD endpoints (backend) | Joel | ✅ Done |
| Financial Engine (DTI/Health Score) | Joel | ✅ Done |
| Settlement Engine (percentage calculation) | Siva | ✅ Done |
| Dashboard UI + Health Score Ring | Raju | ✅ Done |
| Metric Cards component | Raju | ✅ Done |
| Add/Edit/Delete Loan pages | Raju | ✅ Done |
| Recharts integration (loan distribution) | Raju | ✅ Done |
| Profile edit page | Saisri | ✅ Done |

**Sprint 2 Demo:** Full loan management workflow; dashboard with health score, DTI, and charts.

---

### Sprint 3 (Weeks 5–6): AI Integration
**Goal:** All AI features — Gemini integration, settlement, letter generation, recovery

| Task | Owner | Status |
|---|---|---|
| Google Gemini 2.0 Flash integration | Joel | ✅ Done |
| Fallback AI engine (all 3 types) | Joel | ✅ Done |
| Settlement Advisor page | Siva | ✅ Done |
| Letter Generator page | Siva | ✅ Done |
| Recovery Planner backend | Joel | ✅ Done |
| Recovery Planner page | Harsha | ✅ Done |
| Borrower Rights module | Harsha | ✅ Done |
| AI History backend + page | Harsha | ✅ Done |
| Backend deployment on Render | Joel | ✅ Done |

**Sprint 3 Demo:** Full AI features working — settlement advice, letter generation, recovery planning.

---

### Sprint 4 (Weeks 7–8): Polish, Testing & Documentation
**Goal:** Bug fixes, UI polish, testing, deployment, documentation

| Task | Owner | Status |
|---|---|---|
| Frontend deployment on Vercel | Joel | ✅ Done |
| CORS configuration and testing | Joel | ✅ Done |
| End-to-end testing all flows | Harsha | ✅ Done |
| Cross-browser testing | Harsha | ✅ Done |
| Mobile responsiveness fixes | All | ✅ Done |
| Landing page design | Raju | ✅ Done |
| README.md and GitHub documentation | Joel | ✅ Done |
| All phase documentation | All | ✅ Done |
| Performance optimization | Joel | ✅ Done |
| Final review and submission | All | ✅ Done |

**Sprint 4 Demo:** Live at https://finrelief.vercel.app — all 18 features working.

---

## 3. Full Project Folder Structure

```
finrelief/
│
├── 📁 backend/                          # FastAPI Backend
│   ├── 📄 Dockerfile                    # Docker containerization
│   ├── 📄 requirements.txt             # Python dependencies
│   ├── 📄 .env.example                 # Environment variable template
│   └── 📁 app/
│       ├── 📄 main.py                  # FastAPI application entry point
│       ├── 📄 database.py              # SQLAlchemy engine + session
│       ├── 📄 models.py                # All 7 SQLAlchemy models
│       ├── 📄 schemas.py               # Pydantic request/response schemas
│       ├── 📄 auth.py                  # JWT token utilities
│       ├── 📄 dependencies.py          # FastAPI dependency injection
│       ├── 📁 routers/
│       │   ├── 📄 auth.py              # /api/auth/* endpoints
│       │   ├── 📄 loans.py             # /api/loans/* endpoints
│       │   ├── 📄 analysis.py          # /api/analysis/* endpoints
│       │   ├── 📄 ai.py                # /api/ai/* endpoints
│       │   └── 📄 rights.py            # /api/rights/* endpoints
│       └── 📁 services/
│           ├── 📄 financial_engine.py  # DTI, Health Score, projections
│           ├── 📄 settlement_engine.py # Settlement % calculator
│           ├── 📄 gemini_service.py    # Google Gemini API integration
│           └── 📄 fallback_service.py  # Rule-based fallback AI
│
├── 📁 frontend/                         # React + Vite Frontend
│   ├── 📄 index.html                   # HTML entry point
│   ├── 📄 package.json                 # Node dependencies
│   ├── 📄 vite.config.js               # Vite configuration
│   ├── 📄 .env.example                 # VITE_API_BASE_URL template
│   └── 📁 src/
│       ├── 📄 main.jsx                 # React DOM entry point
│       ├── 📄 App.jsx                  # Routes + auth wrapper
│       ├── 📄 index.css                # Global styles + CSS variables
│       ├── 📁 components/              # Reusable UI components
│       │   ├── 📄 LoanCard.jsx         # Loan display card
│       │   ├── 📄 MetricCard.jsx       # Financial metric display
│       │   ├── 📄 HealthScoreRing.jsx  # Circular health score
│       │   ├── 📄 LoadingSkeleton.jsx  # Loading placeholder
│       │   ├── 📄 EmptyState.jsx       # Empty state with CTA
│       │   ├── 📄 Modal.jsx            # Reusable modal dialog
│       │   ├── 📄 Navbar.jsx           # Navigation bar
│       │   └── 📄 ProtectedRoute.jsx   # Auth-gated route wrapper
│       ├── 📁 pages/                   # Route-level page components
│       │   ├── 📄 Landing.jsx          # Homepage /
│       │   ├── 📄 Login.jsx            # Login page /login
│       │   ├── 📄 Register.jsx         # Register page /register
│       │   ├── 📄 Dashboard.jsx        # Main dashboard /dashboard
│       │   ├── 📄 AddLoan.jsx          # Add loan /loans/new
│       │   ├── 📄 EditLoan.jsx         # Edit loan /loans/:id/edit
│       │   ├── 📄 Settlement.jsx       # Settlement advisor /settlement/:id
│       │   ├── 📄 LetterGenerator.jsx  # Letter gen /letters/:id
│       │   ├── 📄 RecoveryPlanner.jsx  # Recovery /recovery
│       │   ├── 📄 BorrowerRights.jsx   # Rights /rights
│       │   ├── 📄 AIHistory.jsx        # History /history
│       │   └── 📄 Profile.jsx          # Profile /profile
│       ├── 📁 context/
│       │   └── 📄 AuthContext.jsx      # Global auth state
│       ├── 📁 services/
│       │   └── 📄 api.js               # Axios instance + all API functions
│       └── 📁 utils/
│           └── 📄 formatters.js        # Currency, date, percentage formatters
│
├── 📁 documentation/                    # All project documentation
│   ├── 📁 1. Problem Identification/
│   ├── 📁 2. Feasibility Study/
│   ├── 📁 3. Project Design Phase/
│   ├── 📁 4. Project Planning Phase/
│   └── 📁 5. Project Development Phase/
│
├── 📄 README.md                         # Project overview + setup guide
├── 📄 docker-compose.yml               # Local development orchestration
└── 📄 .gitignore                        # Git ignore rules
```

---

## 4. Key Implementation Snippets

### 4.1 Financial Engine — Health Score Calculator

```python
# backend/app/services/financial_engine.py

"""
FinRelief AI — Financial Engine
Calculates DTI ratio, financial health score, and monthly surplus.
"""

from typing import List, Dict, Any


def calculate_dti_ratio(monthly_income: float, total_monthly_emi: float) -> float:
    """
    Calculate Debt-to-Income (DTI) ratio.
    
    Args:
        monthly_income: Gross monthly income in INR
        total_monthly_emi: Sum of all monthly EMI obligations in INR
    
    Returns:
        DTI ratio as a percentage (0-100+)
    
    Formula:
        DTI = (Total Monthly EMIs / Gross Monthly Income) × 100
    """
    if monthly_income <= 0:
        return 100.0  # Edge case: no income = maximum DTI
    return round((total_monthly_emi / monthly_income) * 100, 2)


def calculate_health_score(
    monthly_income: float,
    loans: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Calculate the overall financial health score (0-100).
    
    Score components (penalty-based system):
        - DTI Penalty:         0-40 points
        - Delinquency Penalty: 0-30 points (15 per overdue loan)
        - Loan Density Penalty: 0-20 points (5 per loan above 3)
        - LTI Penalty:         0-20 points (Loan-to-Income ratio)
    
    Args:
        monthly_income: Gross monthly income in INR
        loans: List of loan objects (dicts with 'monthly_emi',
               'overdue_months', 'outstanding_balance', 'status')
    
    Returns:
        Dict with 'health_score', 'dti_ratio', 'risk_level',
        'penalty_breakdown', 'total_debt', 'total_emi'
    """
    # Aggregate loan data
    total_emi = sum(loan.get("monthly_emi", 0) or 0 for loan in loans)
    total_debt = sum(
        loan.get("outstanding_balance", 0) or 0 for loan in loans
    )
    overdue_count = sum(
        1 for loan in loans
        if (loan.get("overdue_months", 0) or 0) > 0
    )
    loan_count = len(loans)
    annual_income = monthly_income * 12

    # Calculate DTI ratio
    dti_ratio = calculate_dti_ratio(monthly_income, total_emi)

    # Calculate penalties
    penalty_dti = min(dti_ratio * 0.5, 40)  # Max 40 points
    penalty_delinquency = min(overdue_count * 15, 30)  # Max 30 points
    penalty_density = max(0, (loan_count - 3) * 5)  # 5 per loan above 3
    lti_ratio = total_debt / annual_income if annual_income > 0 else 10
    penalty_lti = max(0, (lti_ratio - 1) * 10)  # Penalize if debt > 1yr income

    total_penalty = (
        penalty_dti + penalty_delinquency + penalty_density + penalty_lti
    )

    # Compute final score (clamped 0-100)
    health_score = max(0, min(100, 100 - total_penalty))

    # Determine risk level
    if health_score >= 80:
        risk_level = "Excellent"
    elif health_score >= 60:
        risk_level = "Good"
    elif health_score >= 40:
        risk_level = "Fair"
    else:
        risk_level = "Critical"

    # Monthly surplus estimate
    living_expenses = monthly_income * 0.40
    monthly_surplus = monthly_income - total_emi - living_expenses

    return {
        "health_score": round(health_score, 1),
        "dti_ratio": dti_ratio,
        "risk_level": risk_level,
        "total_debt": total_debt,
        "total_emi": total_emi,
        "monthly_surplus": round(monthly_surplus, 2),
        "penalty_breakdown": {
            "dti": round(penalty_dti, 2),
            "delinquency": round(penalty_delinquency, 2),
            "density": round(penalty_density, 2),
            "lti": round(penalty_lti, 2),
            "total": round(total_penalty, 2),
        },
    }
```

---

### 4.2 Settlement Engine

```python
# backend/app/services/settlement_engine.py

"""
FinRelief AI — Settlement Engine
Calculates data-driven settlement percentage recommendations.
"""


def calculate_settlement_percentage(
    loan: Dict[str, Any],
    financial_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Calculate recommended settlement percentage range for a loan.
    
    Args:
        loan: Loan dict with type, outstanding_balance, overdue_months, lender_type
        financial_data: Dict from financial_engine with health_score
    
    Returns:
        Dict with recommended_pct, min_pct, max_pct, 
        offer_min, offer_max, factors_applied
    """
    health_score = financial_data.get("health_score", 50)
    overdue_months = loan.get("overdue_months", 0) or 0
    loan_type = loan.get("loan_type", "Personal").lower()
    lender_type = loan.get("lender_type", "Private Bank").lower()
    outstanding = loan.get("outstanding_balance", 0) or 0

    # Base settlement percentage (industry midpoint)
    base_pct = 50
    factors = []

    # Adjust for financial health (more distress = bigger discount)
    if health_score < 30:
        base_pct += 10
        factors.append("Severe financial distress (+10%)")
    elif health_score < 50:
        base_pct += 5
        factors.append("Moderate financial stress (+5%)")

    # Adjust for overdue duration
    if overdue_months > 12:
        base_pct += 5
        factors.append("Long-standing NPA (>12 months) (+5%)")
    elif overdue_months > 6:
        base_pct += 3
        factors.append("Significant overdue period (>6 months) (+3%)")

    # Adjust for loan type (unsecured = more settlement room)
    if loan_type in ["personal loan", "credit card", "bnpl", "medical"]:
        base_pct += 5
        factors.append("Unsecured loan — no collateral (+5%)")
    elif loan_type in ["home loan", "vehicle loan"]:
        base_pct -= 10
        factors.append("Secured loan — collateral reduces discount (-10%)")

    # Adjust for lender type (PSU banks vs private)
    if "psu" in lender_type or "public" in lender_type:
        base_pct -= 3
        factors.append("PSU bank — stricter settlement norms (-3%)")

    # Adjust for loan amount
    if outstanding > 2500000:  # > 25 Lakhs
        base_pct -= 5
        factors.append("High loan amount — harder to settle (-5%)")

    # Clamp between 30% and 80%
    recommended_pct = max(30, min(80, base_pct))
    min_pct = max(25, recommended_pct - 5)
    max_pct = min(85, recommended_pct + 5)

    return {
        "recommended_pct": recommended_pct,
        "min_pct": min_pct,
        "max_pct": max_pct,
        "offer_min": round(outstanding * min_pct / 100, 2),
        "offer_max": round(outstanding * max_pct / 100, 2),
        "offer_recommended": round(outstanding * recommended_pct / 100, 2),
        "factors_applied": factors,
    }
```

---

### 4.3 Gemini API Integration

```python
# backend/app/services/gemini_service.py

"""
FinRelief AI — Gemini Service
Integrates Google Gemini 2.0 Flash for AI-powered financial advice.
"""

import google.generativeai as genai
import os
import time
from typing import Dict, Any, Optional


# Configure Gemini SDK
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
_model = genai.GenerativeModel("gemini-2.0-flash")


def generate_settlement_advice(
    loan: Dict[str, Any],
    financial_data: Dict[str, Any],
    settlement_data: Dict[str, Any],
    user: Dict[str, Any],
) -> Optional[str]:
    """
    Generate personalized settlement advice using Google Gemini 2.0 Flash.
    
    Args:
        loan: Loan details dict
        financial_data: Financial health data from financial_engine
        settlement_data: Settlement percentage data from settlement_engine
        user: User profile dict
    
    Returns:
        Generated advice string, or None if Gemini unavailable
    """
    prompt = f"""You are FinRelief AI, an expert Indian debt counselor with 20 years of experience
helping borrowers negotiate debt settlements with banks and NBFCs.

BORROWER PROFILE:
- Monthly Income: ₹{user.get('monthly_income', 0):,.0f}
- Employment Type: {user.get('employment_type', 'Salaried')}
- Financial Health Score: {financial_data.get('health_score', 50)}/100 ({financial_data.get('risk_level', 'Fair')})
- Debt-to-Income Ratio: {financial_data.get('dti_ratio', 50):.1f}%

LOAN TO SETTLE:
- Lender: {loan.get('lender_name', 'Bank')} ({loan.get('lender_type', 'Private Bank')})
- Loan Type: {loan.get('loan_type', 'Personal Loan')}
- Outstanding Balance: ₹{loan.get('outstanding_balance', 0):,.0f}
- Overdue Period: {loan.get('overdue_months', 0)} months

CALCULATED SETTLEMENT RANGE: {settlement_data.get('min_pct')}% – {settlement_data.get('max_pct')}%
(Recommended: {settlement_data.get('recommended_pct')}% = ₹{settlement_data.get('offer_recommended', 0):,.0f})

Please provide:
1. Why this settlement range is justified (2-3 sentences)
2. How to approach the lender (step-by-step, 3 steps)
3. Best timing for negotiation (1-2 sentences)
4. Key mistakes to avoid (3 bullet points)
5. Documents to prepare (4 bullet points)

Be specific to Indian banking practices. Use ₹ for amounts. 
Keep response under 450 words. Use a professional, empathetic tone."""

    try:
        start_time = time.time()
        response = _model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                max_output_tokens=600,
                temperature=0.7,
            ),
        )
        elapsed_ms = int((time.time() - start_time) * 1000)
        
        if response.text:
            return {
                "advice": response.text,
                "source": "gemini",
                "model": "gemini-2.0-flash",
                "response_time_ms": elapsed_ms,
            }
        return None
        
    except Exception as e:
        # Log error; caller will use fallback
        print(f"[Gemini] Error generating settlement advice: {e}")
        return None
```

---

### 4.4 JWT Authentication

```python
# backend/app/auth.py

"""
FinRelief AI — JWT Authentication Utilities
Handles token creation, verification, and user extraction.
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a short-lived JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict) -> str:
    """Create a long-lived JWT refresh token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, token_type: str = "access") -> Optional[dict]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT string
        token_type: "access" or "refresh"
    
    Returns:
        Decoded payload dict, or None if invalid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != token_type:
            return None
        return payload
    except JWTError:
        return None


def hash_password(password: str) -> str:
    """Hash a plain-text password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against its bcrypt hash."""
    return pwd_context.verify(plain_password, hashed_password)
```

---

### 4.5 React Component — HealthScoreRing

```jsx
// frontend/src/components/HealthScoreRing.jsx

/**
 * HealthScoreRing — Circular health score visualization
 * 
 * @param {number} score - Financial health score (0-100)
 * @param {string} riskLevel - "Excellent" | "Good" | "Fair" | "Critical"
 * @param {number} size - SVG size in pixels (default: 160)
 */
const HealthScoreRing = ({ score, riskLevel, size = 160 }) => {
  const radius = (size - 20) / 2;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (score / 100) * circumference;

  const colorMap = {
    Excellent: '#22c55e',   // Green
    Good: '#eab308',        // Yellow
    Fair: '#f97316',        // Orange
    Critical: '#ef4444',    // Red
  };

  const color = colorMap[riskLevel] || '#6b7280';

  return (
    <div className="health-score-ring" aria-label={`Health Score: ${score}/100`}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        {/* Background circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="var(--color-border)"
          strokeWidth="12"
        />
        {/* Score arc */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={color}
          strokeWidth="12"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          transform={`rotate(-90 ${size / 2} ${size / 2})`}
          style={{ transition: 'stroke-dashoffset 1s ease-in-out' }}
        />
        {/* Score text */}
        <text
          x="50%"
          y="45%"
          textAnchor="middle"
          dominantBaseline="middle"
          fill={color}
          fontSize={size * 0.2}
          fontWeight="700"
          fontFamily="'Outfit', sans-serif"
        >
          {score}
        </text>
        <text
          x="50%"
          y="65%"
          textAnchor="middle"
          fill="var(--color-text-muted)"
          fontSize={size * 0.08}
          fontFamily="'Outfit', sans-serif"
        >
          {riskLevel}
        </text>
      </svg>
    </div>
  );
};

export default HealthScoreRing;
```

---

## 5. Coding Standards

### 5.1 Python — PEP 8 Compliance

| Standard | Rule | Example |
|---|---|---|
| Indentation | 4 spaces (no tabs) | `def func():` `    pass` |
| Line length | Max 88 characters (Black formatter) | — |
| Naming | snake_case for functions/variables | `health_score`, `calculate_dti` |
| Classes | PascalCase | `UserCreate`, `LoanResponse` |
| Constants | UPPER_SNAKE_CASE | `SECRET_KEY`, `ALGORITHM` |
| Docstrings | Google style | `"""Summary.\n\nArgs:\n    ..."""` |
| Imports | stdlib → third-party → local | `os` → `fastapi` → `app.models` |
| Type hints | Required on all function signatures | `def f(x: int) -> str:` |

**Tools:** `flake8` for linting, `black` for formatting, `mypy` for type checking.

### 5.2 JavaScript/React — ESLint

| Standard | Rule | Example |
|---|---|---|
| Indentation | 2 spaces | — |
| Naming | camelCase for variables/functions | `healthScore`, `fetchLoans` |
| Components | PascalCase | `HealthScoreRing`, `MetricCard` |
| Constants | UPPER_SNAKE_CASE | `API_BASE_URL` |
| Imports | Third-party → local → styles | `react` → `./components` → `./styles.css` |
| Props | Destructure in parameters | `const Card = ({ title, value }) =>` |
| Async | async/await over .then chains | — |

**Tools:** ESLint with `eslint-plugin-react`, `eslint-plugin-react-hooks`.

---

## 6. Git Workflow

```
main branch (protected — production)
    │
    ├── develop branch (integration)
    │       │
    │       ├── feature/joel/financial-engine
    │       ├── feature/saisri/auth-pages
    │       ├── feature/raju/dashboard-ui
    │       ├── feature/siva/settlement-advisor
    │       └── feature/harsha/borrower-rights
    │
    └── hotfix/* (critical fixes to main)

Commit Convention:
  feat: add settlement percentage engine
  fix: correct DTI calculation for zero-income edge case
  docs: update API documentation
  test: add integration test for login flow
  style: format financial_engine.py with black
  refactor: extract health score logic to separate function
```

---

## 7. Sample API Request/Responses

### 7.1 POST /api/auth/login

**Request:**
```json
{
  "email": "joel@example.com",
  "password": "SecurePass@2024"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "name": "Joel Prasanna Kumar",
    "email": "joel@example.com",
    "monthly_income": 75000,
    "employment_type": "Salaried",
    "created_at": "2026-06-01T10:30:00Z"
  }
}
```

### 7.2 GET /api/analysis/health

**Response (200 OK):**
```json
{
  "health_score": 52.3,
  "dti_ratio": 41.67,
  "risk_level": "Fair",
  "total_debt": 1250000,
  "total_emi": 31250,
  "monthly_surplus": 13750,
  "penalty_breakdown": {
    "dti": 20.83,
    "delinquency": 15.0,
    "density": 0.0,
    "lti": 11.83,
    "total": 47.67
  }
}
```

### 7.3 POST /api/ai/settlement-advice

**Request:**
```json
{ "loan_id": 3 }
```

**Response (200 OK):**
```json
{
  "advice": "Based on your financial health score of 52/100 and 8 months of overdue...",
  "settlement_data": {
    "recommended_pct": 58,
    "min_pct": 53,
    "max_pct": 63,
    "offer_min": 212000,
    "offer_max": 252000,
    "offer_recommended": 232000
  },
  "source": "gemini",
  "model": "gemini-2.0-flash",
  "response_time_ms": 1842
}
```

---

## 8. Challenges & Solutions

| # | Challenge | Solution |
|---|---|---|
| 1 | Gemini API quota limits (15 RPM free tier) | Built fallback engine; added response caching for same loan within 1 hour |
| 2 | Render free tier cold starts (50s delay) | Added keep-alive ping endpoint; frontend shows loading state with explanation |
| 3 | SQLite data loss on Render redeploy | Added seed script; documented limitation; planned PostgreSQL migration |
| 4 | JWT token expiry causing silent failures | Implemented Axios interceptor for automatic token refresh |
| 5 | Complex settlement formula calibration | Cross-referenced NARCL/IBC data; iteratively tested against real settlement ranges |
| 6 | CORS blocking frontend-backend | Configured exact origin whitelist; used proxy in Vite dev config |
| 7 | Health Score Ring animation on first load | Added CSS transition with `will-change: stroke-dashoffset` |
| 8 | Letter text formatting from Gemini | Post-processed response to preserve paragraphs; added monospace display option |

---

*Document Version: 1.0 | Created: July 2026 | FinRelief AI Team — Vishnu Institute of Technology, Bhimavaram*
