# Code Layout, Readability and Reusability
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

## 1. Code Quality Philosophy

FinRelief AI's codebase is engineered with three core principles:

1. **Readability**: Code is written for the next developer (or reviewer), not just for the machine. Every non-obvious function has a docstring. Every magic number has a named constant. Every complex formula has an inline comment explaining the rationale.

2. **Reusability**: Common patterns are extracted into reusable components (frontend) and service modules (backend). No business logic is duplicated. UI elements used in more than two places become dedicated components.

3. **Maintainability**: The folder structure mirrors the domain model. Files are small and focused. Side effects are isolated to service layers. The codebase can be extended by any new developer with minimal onboarding time.

---

## 2. Full Project Structure with Explanations

```
finrelief/
│
├── 📁 backend/
│   │
│   ├── 📄 Dockerfile
│   │   # Containerizes the FastAPI backend for consistent deployment.
│   │   # Uses python:3.11-slim for minimal image size.
│   │
│   ├── 📄 requirements.txt
│   │   # All Python dependencies with pinned versions for reproducibility.
│   │   # Organized in groups: web framework, database, auth, AI, utilities.
│   │
│   ├── 📄 .env.example
│   │   # Documents all required environment variables without exposing values.
│   │   # Developers copy this to .env and fill in real values.
│   │
│   └── 📁 app/
│       │
│       ├── 📄 main.py
│       │   # Entry point. Creates FastAPI app, registers all routers,
│       │   # configures CORS middleware, and initializes the database.
│       │   # Kept minimal — no business logic here.
│       │
│       ├── 📄 database.py
│       │   # Single responsibility: DB connection setup.
│       │   # Creates SQLAlchemy engine and session factory.
│       │   # Exports get_db() dependency for injection into endpoints.
│       │
│       ├── 📄 models.py
│       │   # All 7 SQLAlchemy ORM models in one file.
│       │   # Each model maps 1:1 to a database table.
│       │   # Relationships defined via SQLAlchemy relationship().
│       │
│       ├── 📄 schemas.py
│       │   # All Pydantic v2 schemas for request/response validation.
│       │   # Organized in pairs: RequestCreate + ResponseModel.
│       │   # Validators embedded in schema classes (field validators).
│       │
│       ├── 📄 auth.py
│       │   # JWT utilities only: create_access_token, create_refresh_token,
│       │   # verify_token, hash_password, verify_password.
│       │   # No FastAPI dependency here — pure utility module.
│       │
│       ├── 📄 dependencies.py
│       │   # FastAPI dependency injection functions.
│       │   # get_current_user() — validates JWT and returns user from DB.
│       │   # Injected into all protected endpoints via Depends().
│       │
│       ├── 📁 routers/
│       │   │   # Each router file handles one domain area.
│       │   │   # Routers are registered in main.py with a prefix.
│       │   │
│       │   ├── 📄 auth.py        # prefix="/api/auth"
│       │   │   # Endpoints: /register, /login, /me, /refresh, /logout
│       │   │   # Only auth logic — delegates to auth.py utilities.
│       │   │
│       │   ├── 📄 loans.py       # prefix="/api/loans"
│       │   │   # Full CRUD for loan management.
│       │   │   # Validates that user owns the loan before any operation.
│       │   │
│       │   ├── 📄 analysis.py    # prefix="/api/analysis"
│       │   │   # Delegates to financial_engine.py service.
│       │   │   # Returns health score, DTI, settlement %, summary.
│       │   │
│       │   ├── 📄 ai.py          # prefix="/api/ai"
│       │   │   # Orchestrates: financial_engine → gemini_service → fallback.
│       │   │   # Logs all interactions to ai_history table.
│       │   │
│       │   └── 📄 rights.py      # prefix="/api/rights"
│       │       # Serves static borrower rights content.
│       │       # No auth required — public endpoint.
│       │
│       └── 📁 services/
│           │   # Business logic layer — completely decoupled from HTTP.
│           │   # Can be unit-tested independently of FastAPI.
│           │
│           ├── 📄 financial_engine.py
│           │   # Core financial calculations: DTI, health score, surplus.
│           │   # Pure functions — no DB access, no side effects.
│           │   # Fully type-hinted and documented.
│           │
│           ├── 📄 settlement_engine.py
│           │   # Settlement percentage calculator.
│           │   # Pure function — no external dependencies.
│           │   # Extensible: add more adjustment factors easily.
│           │
│           ├── 📄 gemini_service.py
│           │   # Gemini API integration only.
│           │   # Returns None on failure — callers handle fallback.
│           │   # All prompts centralized here for easy tuning.
│           │
│           └── 📄 fallback_service.py
│               # Rule-based AI engine — no external API dependency.
│               # Mirrors gemini_service's function signatures exactly.
│               # Drop-in replacement when Gemini is unavailable.
│
└── 📁 frontend/
    │
    ├── 📄 index.html
    │   # Minimal HTML shell. Sets meta tags, font imports, root div.
    │   # All content is rendered by React.
    │
    ├── 📄 vite.config.js
    │   # Vite configuration: React plugin, proxy for local dev.
    │   # Proxy: /api → http://localhost:8000 (avoids CORS in dev).
    │
    ├── 📄 package.json
    │   # Dependencies organized: dependencies (prod) + devDependencies.
    │   # Scripts: dev, build, lint, preview.
    │
    └── 📁 src/
        │
        ├── 📄 main.jsx
        │   # React DOM root. Wraps App with AuthProvider + BrowserRouter.
        │
        ├── 📄 App.jsx
        │   # Route definitions only. Maps URLs to page components.
        │   # Protected routes wrapped in <ProtectedRoute>.
        │
        ├── 📄 index.css
        │   # Global design system:
        │   #   - CSS custom properties (--color-*, --spacing-*, --radius-*)
        │   #   - Typography (Outfit font from Google Fonts)
        │   #   - Reset styles
        │   #   - Utility classes (used sparingly)
        │   #   - Component base styles (buttons, inputs, cards)
        │
        ├── 📁 components/        # Reusable UI components (see Section 4)
        ├── 📁 pages/             # Route-level components (one per route)
        ├── 📁 context/           # React Context providers (global state)
        ├── 📁 services/          # API service layer (all Axios calls)
        └── 📁 utils/             # Pure utility functions (no React)
```

---

## 3. Naming Conventions

### 3.1 Python (Backend)

| Element | Convention | Example |
|---|---|---|
| Files/Modules | `snake_case` | `financial_engine.py` |
| Functions | `snake_case` + verb prefix | `calculate_health_score()`, `get_current_user()` |
| Variables | `snake_case` | `monthly_income`, `health_score` |
| Constants | `UPPER_SNAKE_CASE` | `SECRET_KEY`, `ACCESS_TOKEN_EXPIRE_MINUTES` |
| Classes | `PascalCase` | `UserCreate`, `LoanResponse`, `AIHistory` |
| DB Models | `PascalCase` noun | `User`, `Loan`, `AIHistory` |
| Pydantic Schemas | `PascalCase` + suffix | `UserCreate`, `LoanUpdate`, `HealthScoreResponse` |
| API Functions | `snake_case` + verb | `create_loan()`, `get_health_score()` |
| Boolean Variables | `is_` / `has_` prefix | `is_active`, `has_overdue_loans` |

### 3.2 JavaScript/React (Frontend)

| Element | Convention | Example |
|---|---|---|
| Files (Components) | `PascalCase` | `HealthScoreRing.jsx` |
| Files (Utilities) | `camelCase` | `formatters.js`, `api.js` |
| React Components | `PascalCase` | `LoanCard`, `MetricCard` |
| Functions | `camelCase` + verb prefix | `fetchLoans()`, `calculateDTI()` |
| Variables | `camelCase` | `healthScore`, `totalDebt` |
| Constants | `UPPER_SNAKE_CASE` | `API_BASE_URL`, `LOAN_TYPES` |
| CSS Classes | `kebab-case` | `.loan-card`, `.metric-card`, `.health-score-ring` |
| CSS Variables | `--category-property` | `--color-primary`, `--spacing-md` |
| Event Handlers | `handle` prefix | `handleSubmit()`, `handleLoanDelete()` |
| State Variables | descriptive noun | `isLoading`, `loans`, `healthData` |

---

## 4. Reusable Components (Frontend)

### 4.1 LoanCard

```jsx
/**
 * LoanCard — Displays a single loan's key information in a card format.
 * 
 * Used on: Dashboard (loan list), Settlement page (loan selector)
 * 
 * @param {Object} loan - Loan data object from API
 * @param {string} loan.lender_name - Name of the lender
 * @param {string} loan.loan_type - Type of loan
 * @param {number} loan.outstanding_balance - Current outstanding in INR
 * @param {number} loan.monthly_emi - Monthly EMI in INR
 * @param {string} loan.status - Loan status (Active/Overdue/etc.)
 * @param {number} loan.overdue_months - Months overdue (0 if current)
 * @param {Function} onEdit - Callback when Edit is clicked
 * @param {Function} onDelete - Callback when Delete is clicked
 * @param {Function} onSettle - Callback when Settle is clicked
 */
const LoanCard = ({ loan, onEdit, onDelete, onSettle }) => {
  const statusColors = {
    Active: 'var(--color-success)',
    Overdue: 'var(--color-danger)',
    'In Settlement': 'var(--color-warning)',
    Settled: 'var(--color-text-muted)',
  };

  return (
    <div className="loan-card" data-status={loan.status}>
      <div className="loan-card__header">
        <div>
          <h3 className="loan-card__lender">{loan.lender_name}</h3>
          <span className="loan-card__type">{loan.loan_type}</span>
        </div>
        <span
          className="loan-card__status-badge"
          style={{ color: statusColors[loan.status] }}
        >
          {loan.status}
          {loan.overdue_months > 0 && ` (${loan.overdue_months}mo)`}
        </span>
      </div>

      <div className="loan-card__metrics">
        <div className="loan-card__metric">
          <span className="label">Outstanding</span>
          <span className="value">{formatCurrency(loan.outstanding_balance)}</span>
        </div>
        <div className="loan-card__metric">
          <span className="label">Monthly EMI</span>
          <span className="value">{formatCurrency(loan.monthly_emi)}</span>
        </div>
        <div className="loan-card__metric">
          <span className="label">Rate</span>
          <span className="value">{loan.interest_rate}% p.a.</span>
        </div>
      </div>

      <div className="loan-card__actions">
        <button onClick={() => onEdit(loan.id)} className="btn btn-ghost btn-sm">
          Edit
        </button>
        {loan.status === 'Overdue' && (
          <button onClick={() => onSettle(loan.id)} className="btn btn-primary btn-sm">
            Get Settlement Advice
          </button>
        )}
        <button onClick={() => onDelete(loan.id)} className="btn btn-danger-ghost btn-sm">
          Delete
        </button>
      </div>
    </div>
  );
};
```

**Reuse count:** Used in `Dashboard.jsx`, `Settlement.jsx` — 2 pages.

---

### 4.2 MetricCard

```jsx
/**
 * MetricCard — Displays a single financial metric with label, value, and trend.
 * 
 * Used on: Dashboard (4 instances), Settlement page, Recovery page
 * 
 * @param {string} label - Metric name (e.g., "Financial Health Score")
 * @param {string|number} value - Display value (formatted)
 * @param {string} unit - Optional unit suffix (e.g., "%", "months")
 * @param {string} color - CSS color for value text
 * @param {string} icon - Emoji or icon identifier
 * @param {string} description - Tooltip/subtitle text
 * @param {boolean} isLoading - Show skeleton when true
 */
const MetricCard = ({ label, value, unit = '', color, icon, description, isLoading }) => {
  if (isLoading) return <LoadingSkeleton type="metric-card" />;

  return (
    <div className="metric-card">
      <div className="metric-card__header">
        <span className="metric-card__icon">{icon}</span>
        <span className="metric-card__label">{label}</span>
      </div>
      <div className="metric-card__value" style={{ color }}>
        {value}
        {unit && <span className="metric-card__unit">{unit}</span>}
      </div>
      {description && (
        <p className="metric-card__description">{description}</p>
      )}
    </div>
  );
};
```

**Reuse count:** Used in `Dashboard.jsx` (4×), `Settlement.jsx` (2×), `RecoveryPlanner.jsx` (2×) — 3 pages, 8 instances.

---

### 4.3 Modal

```jsx
/**
 * Modal — Accessible, animated modal dialog component.
 * 
 * Used on: Loan deletion confirmation, letter preview, 
 *          settlement confirmation, rights detail overlays.
 * 
 * @param {boolean} isOpen - Controls visibility
 * @param {Function} onClose - Called when overlay or X clicked
 * @param {string} title - Modal header title
 * @param {React.ReactNode} children - Modal body content
 * @param {string} size - "sm" | "md" | "lg" (default: "md")
 * @param {React.ReactNode} footer - Optional footer content (action buttons)
 */
const Modal = ({ isOpen, onClose, title, children, size = 'md', footer }) => {
  // Close on Escape key
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) onClose();
    };
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  // Prevent body scroll when open
  useEffect(() => {
    document.body.style.overflow = isOpen ? 'hidden' : 'unset';
    return () => { document.body.style.overflow = 'unset'; };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose} role="dialog" aria-modal="true">
      <div
        className={`modal modal--${size}`}
        onClick={(e) => e.stopPropagation()}
        aria-labelledby="modal-title"
      >
        <div className="modal__header">
          <h2 id="modal-title" className="modal__title">{title}</h2>
          <button className="modal__close" onClick={onClose} aria-label="Close modal">
            ✕
          </button>
        </div>
        <div className="modal__body">{children}</div>
        {footer && <div className="modal__footer">{footer}</div>}
      </div>
    </div>
  );
};
```

**Reuse count:** Used in 5 pages for 7 different dialog types.

---

### 4.4 HealthScoreRing

*(Full implementation in Coding & Solution document)*

**Reuse count:** `Dashboard.jsx` (primary display), `Settlement.jsx` (context sidebar).

---

### 4.5 LoadingSkeleton

```jsx
/**
 * LoadingSkeleton — Animated placeholder for async content.
 * Prevents layout shift and provides visual feedback during API calls.
 * 
 * @param {string} type - "metric-card" | "loan-card" | "text" | "chart"
 * @param {number} count - Number of skeleton items to render (default: 1)
 */
const LoadingSkeleton = ({ type = 'text', count = 1 }) => {
  const skeletons = Array.from({ length: count }, (_, i) => (
    <div key={i} className={`skeleton skeleton--${type}`} aria-hidden="true">
      {type === 'metric-card' && (
        <>
          <div className="skeleton__line skeleton__line--short" />
          <div className="skeleton__line skeleton__line--full skeleton__line--tall" />
          <div className="skeleton__line skeleton__line--medium" />
        </>
      )}
      {type === 'loan-card' && (
        <>
          <div className="skeleton__line skeleton__line--full" />
          <div className="skeleton__line skeleton__line--medium" />
          <div className="skeleton__row">
            <div className="skeleton__line skeleton__line--third" />
            <div className="skeleton__line skeleton__line--third" />
            <div className="skeleton__line skeleton__line--third" />
          </div>
        </>
      )}
      {type === 'text' && (
        <div className="skeleton__line skeleton__line--full" />
      )}
    </div>
  ));

  return <>{skeletons}</>;
};
```

**CSS Animation (in index.css):**
```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-surface) 25%,
    var(--color-surface-hover) 50%,
    var(--color-surface) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-md);
}
```

**Reuse count:** Used in all 7 data-fetching pages.

---

### 4.6 EmptyState

```jsx
/**
 * EmptyState — Friendly empty state display with action prompt.
 * Prevents blank screens when no data exists.
 * 
 * @param {string} icon - Emoji icon for visual identity
 * @param {string} title - Primary empty state message
 * @param {string} description - Explanatory text
 * @param {string} actionLabel - CTA button text
 * @param {Function} onAction - CTA click handler
 */
const EmptyState = ({ icon, title, description, actionLabel, onAction }) => (
  <div className="empty-state">
    <div className="empty-state__icon">{icon}</div>
    <h3 className="empty-state__title">{title}</h3>
    <p className="empty-state__description">{description}</p>
    {actionLabel && onAction && (
      <button onClick={onAction} className="btn btn-primary">
        {actionLabel}
      </button>
    )}
  </div>
);
```

**Reuse count:** `Dashboard.jsx` (no loans), `AIHistory.jsx` (no history), `Settlement.jsx` (no overdue loans) — 3 pages.

---

## 5. Reusable Services (Backend)

### 5.1 FinancialEngine (`financial_engine.py`)

**Reused by:** `analysis.py` router, `ai.py` router (as context for Gemini/fallback)

```python
# Public API of financial_engine.py:

def calculate_dti_ratio(monthly_income: float, total_monthly_emi: float) -> float: ...
def calculate_health_score(monthly_income: float, loans: List[Dict]) -> Dict: ...
def calculate_debt_projection(loans: List[Dict], extra_payment: float = 0) -> Dict: ...
def get_priority_loans(loans: List[Dict]) -> List[Dict]: ...
```

---

### 5.2 SettlementEngine (`settlement_engine.py`)

**Reused by:** `analysis.py` router (GET /analysis/settlement/{id}), `ai.py` router (as input to Gemini prompt)

```python
# Public API of settlement_engine.py:

def calculate_settlement_percentage(loan: Dict, financial_data: Dict) -> Dict: ...
def get_settlement_factors(loan: Dict, financial_data: Dict) -> List[str]: ...
def format_settlement_summary(settlement_data: Dict) -> str: ...
```

---

### 5.3 GeminiService (`gemini_service.py`)

**Reused by:** `ai.py` router for all 3 AI endpoint types

```python
# Public API of gemini_service.py:

def generate_settlement_advice(loan, financial_data, settlement_data, user) -> Optional[Dict]: ...
def generate_settlement_letter(loan, user, letter_type, hardship_reason) -> Optional[Dict]: ...
def generate_recovery_plan(loans, user, strategy, extra_payment) -> Optional[Dict]: ...
```

All functions return `None` on failure — the caller in `ai.py` then calls the corresponding fallback function.

---

### 5.4 FallbackService (`fallback_service.py`)

**Design pattern:** Mirrors `gemini_service.py` function signatures exactly. This ensures `ai.py` can swap between services with one-line changes.

```python
# Public API mirrors gemini_service.py exactly:

def generate_settlement_advice(loan, financial_data, settlement_data, user) -> Dict: ...
def generate_settlement_letter(loan, user, letter_type, hardship_reason) -> Dict: ...
def generate_recovery_plan(loans, user, strategy, extra_payment) -> Dict: ...
```

**Key Difference:** Fallback functions never return `None` — they always return a result (rule-based).

---

## 6. Docstring Standards

### 6.1 Python — Google Style Docstrings

```python
def calculate_health_score(
    monthly_income: float,
    loans: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Calculate the overall financial health score for a user.

    Applies a penalty-based scoring system that deducts points based on
    DTI ratio, delinquency status, loan density, and loan-to-income ratio.
    Score ranges from 0 (worst) to 100 (best).

    Args:
        monthly_income: User's gross monthly income in INR. Must be > 0.
        loans: List of loan dictionaries. Each loan should contain:
            - monthly_emi (float): Monthly EMI amount
            - overdue_months (int): Months overdue (0 if current)
            - outstanding_balance (float): Current outstanding amount
            - status (str): Loan status string

    Returns:
        Dictionary containing:
            - health_score (float): Score 0-100
            - dti_ratio (float): Debt-to-income ratio percentage
            - risk_level (str): "Excellent" | "Good" | "Fair" | "Critical"
            - total_debt (float): Sum of all outstanding balances
            - total_emi (float): Sum of all monthly EMIs
            - monthly_surplus (float): Estimated monthly surplus after EMIs
            - penalty_breakdown (dict): Component-wise penalty scores

    Raises:
        No exceptions raised. Edge cases (zero income, no loans) are 
        handled gracefully.

    Example:
        >>> score_data = calculate_health_score(
        ...     monthly_income=60000,
        ...     loans=[{"monthly_emi": 22000, "overdue_months": 0, 
        ...             "outstanding_balance": 500000, "status": "Active"}]
        ... )
        >>> print(score_data["health_score"])  # e.g., 61.7
    """
```

### 6.2 JavaScript — JSDoc

```javascript
/**
 * Formats a number as Indian Rupee currency string.
 * 
 * @param {number} amount - Amount to format (in INR)
 * @param {boolean} [compact=false] - If true, use compact notation (1L, 10L, 1Cr)
 * @returns {string} Formatted currency string (e.g., "₹1,25,000" or "₹1.25L")
 * 
 * @example
 * formatCurrency(125000)         // "₹1,25,000"
 * formatCurrency(125000, true)   // "₹1.25L"
 * formatCurrency(1250000, true)  // "₹12.5L"
 * formatCurrency(12500000, true) // "₹1.25Cr"
 */
export const formatCurrency = (amount, compact = false) => {
  if (amount === null || amount === undefined) return '—';
  
  if (compact) {
    if (amount >= 10000000) return `₹${(amount / 10000000).toFixed(2)}Cr`;
    if (amount >= 100000)   return `₹${(amount / 100000).toFixed(2)}L`;
    if (amount >= 1000)     return `₹${(amount / 1000).toFixed(1)}K`;
  }
  
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(amount);
};
```

---

## 7. DRY (Don't Repeat Yourself) Practices

### 7.1 Centralized API Service (`api.js`)

All Axios calls are centralized in a single file. No component makes raw `axios.get()` calls — they all call named service functions:

```javascript
// WRONG (anti-pattern — never done in FinRelief):
// In Dashboard.jsx:
const response = await axios.get('/api/analysis/health', {
  headers: { Authorization: `Bearer ${token}` }
});

// RIGHT (how it's done):
// In api.js:
export const getHealthAnalysis = () => api.get('/analysis/health');

// In Dashboard.jsx:
const { data } = await getHealthAnalysis();
```

**Benefits:** Change the endpoint once in `api.js` — all pages pick it up automatically.

### 7.2 CSS Custom Properties (Zero Magic Numbers)

```css
/* index.css — All design tokens defined once */
:root {
  /* Colors */
  --color-primary: hsl(230, 85%, 60%);
  --color-primary-hover: hsl(230, 85%, 55%);
  --color-success: hsl(142, 71%, 45%);
  --color-warning: hsl(38, 92%, 50%);
  --color-danger: hsl(0, 84%, 60%);
  --color-background: hsl(222, 47%, 8%);
  --color-surface: hsl(222, 35%, 12%);
  --color-surface-hover: hsl(222, 35%, 16%);
  --color-text: hsl(220, 20%, 95%);
  --color-text-muted: hsl(220, 15%, 55%);
  --color-border: hsl(222, 30%, 20%);

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 3rem;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;

  /* Shadows */
  --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.3);
  --shadow-modal: 0 20px 60px rgba(0, 0, 0, 0.5);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-normal: 250ms ease;
}
```

### 7.3 Python — Shared Response Patterns

```python
# dependencies.py — Reusable dependency for all protected routes
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """Single definition, used in every protected endpoint via Depends()."""
    ...

# Every protected endpoint uses:
@router.get("/me")
def get_profile(current_user: User = Depends(get_current_user)):
    ...
```

---

## 8. SOLID Principles Applied

| Principle | Application in FinRelief AI |
|---|---|
| **S**ingle Responsibility | Each service module does one thing: `financial_engine.py` calculates, `gemini_service.py` calls Gemini, `fallback_service.py` provides fallback. No file mixes responsibilities. |
| **O**pen/Closed | Settlement engine's adjustment factors are additive — adding a new factor doesn't modify existing logic, only extends it. |
| **L**iskov Substitution | `FallbackService` and `GeminiService` are interchangeable — same signatures, both return compatible response dicts. |
| **I**nterface Segregation | Pydantic schemas are split: `LoanCreate` (for creation), `LoanUpdate` (for updates), `LoanResponse` (for API output). No one schema does everything. |
| **D**ependency Inversion | FastAPI routers depend on service modules (abstractions), not on concrete implementations like `sqlite3`. Database access is abstracted by SQLAlchemy. |

---

## 9. Code Review Process

### 9.1 Pull Request Requirements

Before merging to `develop`:
- [ ] Feature branch created from latest `develop`
- [ ] Code runs locally without errors
- [ ] Docstrings added to all new functions
- [ ] PEP 8 / ESLint checks passing
- [ ] At least 1 team member has reviewed
- [ ] No secrets or API keys in code
- [ ] README updated if new setup step required

### 9.2 Review Checklist

```
Code Review Checklist (reviewer fills before approving):

□ Logic is correct and handles edge cases
□ No duplicated logic — DRY principle followed
□ Variable and function names are descriptive
□ Error cases are handled gracefully (try/except, null checks)
□ No console.log() or print() debugging statements left in
□ Components are properly typed (PropTypes or TypeScript-style JSDoc)
□ API calls use service functions (not raw axios)
□ All user-facing text is clear and professional
□ No hardcoded values that should be constants/env vars
```

---

## 10. Linting Tools & Configuration

### 10.1 Backend — Python

```ini
# .flake8
[flake8]
max-line-length = 88
exclude = .git,__pycache__,.venv,migrations
per-file-ignores =
    __init__.py: F401  # allow unused imports in __init__
```

```toml
# pyproject.toml (Black formatter)
[tool.black]
line-length = 88
target-version = ['py311']
```

### 10.2 Frontend — ESLint

```json
// .eslintrc.json
{
  "env": { "browser": true, "es2021": true },
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended"
  ],
  "rules": {
    "no-console": "warn",
    "no-unused-vars": "error",
    "react/prop-types": "warn",
    "react-hooks/exhaustive-deps": "warn",
    "prefer-const": "error",
    "no-var": "error"
  }
}
```

---

*Document Version: 1.0 | Created: July 2026 | FinRelief AI Team — Vishnu Institute of Technology, Bhimavaram*
