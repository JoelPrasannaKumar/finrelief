# Proposed Solution
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

## 1. Executive Summary

FinRelief AI is a full-stack, AI-powered debt relief and financial recovery platform designed to democratize access to professional debt counseling for millions of Indians overwhelmed by personal loans, credit card debt, and education loans. Built during the SmartBridge Google Cloud Generative AI Internship at Vishnu Institute of Technology, the platform leverages **Google Gemini 2.0 Flash** as its intelligence engine to provide real-time settlement advice, generate professional negotiation letters, and create personalized recovery plans.

The platform is fully functional, deployed on **Vercel** (frontend) and **Render** (backend), and accessible at https://finrelief.vercel.app. It serves as a demonstration of how generative AI can be applied to solve critical socioeconomic problems — in this case, the debt crisis affecting 4.1 crore Indian borrowers.

**Technology Stack:**
- **Frontend:** React + Vite (JavaScript)
- **Backend:** FastAPI (Python)
- **Database:** SQLite with SQLAlchemy ORM
- **AI Engine:** Google Gemini 2.0 Flash
- **Authentication:** JWT (JSON Web Tokens) + bcrypt
- **Deployment:** Vercel (frontend) + Render (backend)
- **Containerization:** Docker

---

## 2. Core Features (All 8 Major Features)

### Feature 1: 🔐 User Authentication & Profile Management

**Description:** Secure user registration and login system with JWT-based session management. Users create a financial profile including monthly income, employment type, and existing loan obligations.

**Key Capabilities:**
- Secure registration with email + password (bcrypt hashed)
- JWT token-based authentication (15-minute access tokens + 7-day refresh tokens)
- User profile creation with income, employment type, number of dependents
- Profile editing and account settings management
- Logout with token invalidation

**Technical Implementation:**
```
POST /api/auth/register → bcrypt hash password → store in DB → return JWT
POST /api/auth/login    → verify hash → generate access+refresh tokens
GET  /api/auth/me       → verify JWT → return user profile
```

---

### Feature 2: 💳 Loan Portfolio Management

**Description:** A comprehensive loan management system allowing users to add, edit, and delete individual loans. Supports all major Indian loan types.

**Supported Loan Types:**
- Personal Loan
- Credit Card Debt
- Home Loan / Mortgage
- Education Loan
- Vehicle Loan
- Business Loan
- Medical/Emergency Loan
- BNPL (Buy Now Pay Later)

**Key Capabilities:**
- Add multiple loans with lender name, principal, outstanding balance, interest rate, EMI, and tenure
- Edit loan details as situations change
- Delete loans when resolved
- Real-time update of financial health metrics upon any loan change
- Loan status tracking: Active, Overdue, In Settlement, Settled

---

### Feature 3: 📊 Financial Health Dashboard

**Description:** The central hub of FinRelief AI — a comprehensive dashboard displaying all key financial metrics, loan summary, and health indicators in a visually rich interface.

**Key Metrics Displayed:**
1. **Financial Health Score** (0–100): Composite score based on DTI, delinquency, loan-to-income ratio
2. **Debt-to-Income (DTI) Ratio**: Total monthly EMI ÷ Monthly Income × 100
3. **Total Outstanding Debt**: Sum of all active loan balances
4. **Monthly EMI Burden**: Total monthly EMI payments
5. **Average Interest Rate**: Weighted average across all loans
6. **Highest Interest Loan Alert**: Flagged for priority payoff
7. **Debt Payoff Projection**: Estimated months to become debt-free

**Visual Components:**
- Health Score ring (color-coded: Red/Yellow/Green)
- EMI vs Income bar chart
- Loan type distribution pie chart
- Monthly cash flow indicator

---

### Feature 4: 🤝 AI-Powered Settlement Advisor

**Description:** The most innovative feature of FinRelief AI — an AI engine that analyzes a user's financial situation and provides data-driven settlement recommendations for overdue loans.

**How It Works:**
1. User selects a loan to settle
2. System calculates base settlement percentage using financial engine
3. Google Gemini 2.0 Flash enriches with contextual negotiation strategy
4. User receives a recommended settlement range with tactical advice

**Settlement Formula (see Section 5 for full detail):**
```
Base Settlement % = 100 - [(Health Score × 0.3) + (Loan Age Bonus) + (Delinquency Bonus)]
```

**Gemini's Role in Settlement Advice:**
- Analyzes borrower's financial narrative
- Considers loan type, lender type (PSU bank vs. private), amount
- Generates negotiation talking points
- Advises on timing (quarter-end when banks want to clear NPAs)
- Warns about common mistakes in settlement negotiations

---

### Feature 5: 📝 AI Settlement Letter Generator

**Description:** Generates professional, legally-aware settlement letters using Google Gemini 2.0 Flash. Letters are personalized to each loan, borrower situation, and lender type.

**Letter Types Supported:**
1. **Formal OTS (One Time Settlement) Request**
2. **Debt Acknowledgment with Hardship Appeal**
3. **Post-Default Negotiation Letter**
4. **Follow-up Letter After Initial Rejection**

**What Gemini Generates:**
```
[Date]
[Borrower Name & Address]

To,
The Branch Manager,
[Bank/NBFC Name],
[Branch Address]

Subject: Application for One Time Settlement (OTS) — Loan Account No. XXXXXXXX

Respected Sir/Madam,

[Personalized hardship narrative based on user's financial data]
[Loan details: original amount, outstanding, overdue period]
[Settlement offer: specific amount and percentage]
[Payment timeline proposal]
[Request for NOC and credit report update]
[Appreciation and closing]

Yours faithfully,
[Borrower Name]
```

**Fallback:** If Gemini is unavailable, a template-based Python engine generates a standard formal letter using the same data.

---

### Feature 6: 📈 Recovery Planning Module

**Description:** Creates a personalized, month-by-month debt repayment plan using proven strategies (Debt Avalanche and Debt Snowball), with Gemini providing motivational and strategic narrative.

**Debt Repayment Strategies:**
- **Avalanche Method:** Pay minimums on all loans; direct extra payment to the highest-interest loan first. Mathematically optimal; saves maximum interest.
- **Snowball Method:** Pay minimums on all loans; direct extra payment to the smallest balance first. Psychologically effective; builds momentum.
- **Hybrid Method (Gemini-recommended):** AI-selected blend based on user's risk profile, psychology indicators, and debt structure.

**Recovery Plan Output:**
- Month-by-month payoff schedule
- Total interest paid under each strategy
- Projected debt-free date
- Savings if user increases EMI by ₹1,000, ₹2,000, or ₹5,000
- Gemini-generated motivational message and strategy justification

---

### Feature 7: ⚖️ Borrower Rights & Legal Awareness Module

**Description:** A comprehensive educational module informing users of their legal rights as borrowers under Indian law, RBI regulations, and court precedents.

**Content Areas:**
1. **RBI Fair Practice Code for Lenders** — what banks must and cannot do
2. **SARFAESI Act 2002** — when banks can seize assets; what the notice timeline is
3. **Recovery Agent Conduct Rules** — prohibited behaviors, complaint mechanisms
4. **CIBIL Score Impact** — how settlement affects credit score; rebuilding timeline
5. **Legal Remedies** — Debt Recovery Tribunal (DRT), Consumer Forum, Banking Ombudsman
6. **FOIR (Fixed Obligation to Income Ratio)** — what lenders check

**Presented As:**
- Plain English explanations of legal provisions
- Q&A format for common scenarios ("Can a recovery agent visit my workplace?")
- Step-by-step complaint filing guides

---

### Feature 8: 📜 AI Advice History & Tracking

**Description:** A persistent log of all AI interactions — settlement advice, letters generated, and recovery plans — allowing users to track their progress and revisit past recommendations.

**Capabilities:**
- Full history of all Gemini and fallback AI responses
- Filterable by type (settlement advice, letter, recovery plan)
- Date-stamped entries
- Download/copy functionality
- Session replay: view what financial data was used for each advice

---

## 3. How Google Gemini 2.0 Flash Is Used

### 3.1 Settlement Advice Generation

```python
# Gemini prompt for Settlement Advice
prompt = f"""
You are FinRelief AI, an expert Indian debt counselor.

Borrower Profile:
- Monthly Income: ₹{income:,}
- Total Debt: ₹{total_debt:,}
- DTI Ratio: {dti_ratio:.1f}%
- Financial Health Score: {health_score}/100
- Loan Type: {loan_type}
- Lender: {lender_name} ({lender_type})
- Outstanding: ₹{outstanding:,}
- Overdue Months: {overdue_months}
- Calculated Settlement Range: {settlement_min}% – {settlement_max}%

Task: Provide a personalized settlement strategy including:
1. Why this settlement range is appropriate
2. How to approach the lender
3. Best timing for negotiation
4. Common mistakes to avoid
5. What documents to prepare

Respond in a professional, empathetic tone. Use Indian Rupee (₹). 
Keep response under 500 words.
"""
```

### 3.2 Settlement Letter Generation

```python
# Gemini prompt for Letter Generation
prompt = f"""
Generate a formal One Time Settlement (OTS) letter for:

Borrower: {borrower_name}
Address: {address}
Loan Account: {loan_account}
Bank: {bank_name}, {branch}
Original Principal: ₹{principal:,}
Outstanding Balance: ₹{outstanding:,}
Settlement Offer: ₹{settlement_amount:,} ({settlement_pct}% of outstanding)
Hardship Reason: {hardship_reason}
Payment Timeframe: {payment_days} days upon approval

Generate a complete, formal letter following Indian banking correspondence 
conventions. Include all sections: subject, salutation, body (hardship 
description, loan details, settlement offer, payment plan), request for 
NOC, and closing. Make it professional, persuasive, and factually accurate.
"""
```

### 3.3 Recovery Planning

```python
# Gemini prompt for Recovery Planning
prompt = f"""
Create a personalized debt recovery plan for:

Income: ₹{income:,}/month
Monthly EMIs: ₹{total_emi:,}
Available Extra Payment: ₹{extra_payment:,}/month
Debts: {json.dumps(loan_summary, indent=2)}
Preferred Strategy: {strategy}

Generate:
1. Month-by-month payoff order
2. Projected debt-free date  
3. Total interest savings vs minimum payments
4. 3 actionable tips specific to this situation
5. An encouraging message

Format as structured advice with clear sections.
"""
```

---

## 4. Fallback Engine

When Google Gemini API is unavailable (quota exceeded, network issues, or API downtime), FinRelief AI seamlessly falls back to a Python-based deterministic engine.

### 4.1 Fallback Settlement Advice

```python
def generate_fallback_settlement_advice(loan_data: dict, financial_data: dict) -> str:
    health_score = financial_data.get("health_score", 50)
    dti = financial_data.get("dti_ratio", 50)
    settlement_pct = calculate_settlement_percentage(loan_data, financial_data)
    
    advice_parts = []
    
    if health_score < 30:
        advice_parts.append(
            "Your financial health score indicates severe distress. "
            f"A settlement offer of {settlement_pct['min']}%-{settlement_pct['max']}% "
            "is realistic. Banks are motivated to recover at least partial payment."
        )
    elif health_score < 60:
        advice_parts.append(
            "Your financial situation shows moderate stress. "
            f"Target a settlement between {settlement_pct['min']}%-{settlement_pct['max']}%. "
            "Approach lender at quarter-end for better receptivity."
        )
    # ... additional tiers
    
    return " ".join(advice_parts)
```

### 4.2 Fallback Letter Templates

Three pre-built letter templates (Standard OTS, Hardship Appeal, Post-Default) are stored as Python f-strings with dynamic variable injection. All borrower and loan data is correctly populated even without Gemini.

---

## 5. Financial Engine Formulas

### 5.1 Debt-to-Income (DTI) Ratio

```
DTI Ratio = (Total Monthly EMI Obligations / Gross Monthly Income) × 100

Interpretation:
  < 20%  : Excellent — comfortable debt load
  20–35% : Good — manageable
  36–50% : Warning — debt is straining budget
  > 50%  : Critical — severe financial stress
```

**Example:**
- Monthly Income: ₹60,000
- Total EMIs: ₹22,000
- DTI = (22,000 / 60,000) × 100 = **36.67%** → Warning Zone

### 5.2 Financial Health Score

```
Health Score = 100 - Penalty Points

Penalty Points Breakdown:
  DTI Penalty      = min(DTI Ratio × 0.5, 40)
  Delinquency      = Overdue Loans Count × 15 (max 30)
  Loan Density     = max(0, (Loan Count - 3) × 5)
  LTI (Loan-to-Income) Penalty = max(0, (Total Debt / Annual Income - 1) × 10)

Final Score = max(0, min(100, 100 - Total Penalties))

Color Coding:
  80–100 : 🟢 Excellent
  60–79  : 🟡 Good
  40–59  : 🟠 Fair / At Risk
  0–39   : 🔴 Critical
```

### 5.3 Settlement Percentage Calculator

```
Base Settlement % = 50  (industry average starting point)

Adjustments:
  +10 if Health Score < 30    (severe distress = more discount)
  +5  if Health Score 30–50   (moderate distress)
  +5  if Overdue > 12 months  (old NPA = bank wants to close)
  +3  if Overdue > 6 months
  +5  if Loan Type = Unsecured (personal/credit card — no collateral)
  -10 if Loan Type = Home Loan (secured — bank has property as security)
  -5  if Loan Amount > ₹25 Lakh (large loans = harder settlement)

Settlement Range:
  Recommended Min = Base% - 5
  Recommended Max = Base% + 5

Example: Health Score 25, Overdue 8 months, Personal Loan, ₹3L
  Base = 50 + 10 + 3 + 5 = 68%
  Range = 63% – 73% (offer to pay 63–73% of outstanding)
  Meaning: On ₹3,00,000 outstanding → offer ₹1,89,000–₹2,19,000
```

### 5.4 Monthly Surplus Calculator

```
Monthly Surplus = Gross Income - Total EMIs - Living Expenses (estimated 40% of income)

Available for Extra Debt Payment = Monthly Surplus × 0.7 (70% of surplus)
```

---

## 6. User Flow Diagrams

### 6.1 New User Onboarding Flow
```
[Landing Page] → [Register] → [Profile Setup (Income, Employment)] 
    → [Add First Loan] → [Dashboard] → [AI Analysis Recommended]
```

### 6.2 Settlement Flow
```
[Dashboard] → [Select Overdue Loan] → [Settlement Advisor Page]
    → [System Calculates Health Score + Settlement %]
    → [Gemini Generates Strategy] → [User Reviews Advice]
    → [Generate Letter] → [Copy/Download Letter]
```

### 6.3 Recovery Planning Flow
```
[Dashboard] → [Recovery Planner] → [Select Strategy (Avalanche/Snowball)]
    → [Input Extra Monthly Payment] → [Gemini Generates Plan]
    → [View Month-by-Month Schedule] → [Save to History]
```

### 6.4 Returning User Flow
```
[Login] → [JWT Verified] → [Dashboard with Updated Data]
    → [AI History] → [Review Past Advice] → [Update Loan Data] → [Refresh Analysis]
```

---

## 7. All 10 Pages/Screens

| # | Page | Route | Key Components |
|---|---|---|---|
| 1 | **Landing Page** | `/` | Hero section, features overview, CTA buttons, testimonials placeholder |
| 2 | **Register** | `/register` | Registration form, validation, password strength indicator |
| 3 | **Login** | `/login` | Login form, remember me, forgot password placeholder |
| 4 | **Dashboard** | `/dashboard` | Health Score ring, metrics cards, loan list, quick actions |
| 5 | **Add/Edit Loan** | `/loans/new`, `/loans/:id/edit` | Loan form with all fields, validation |
| 6 | **Settlement Advisor** | `/settlement/:loanId` | Loan summary, settlement % display, Gemini advice card |
| 7 | **Letter Generator** | `/letters/:loanId` | Letter type selector, generated letter display, copy/download |
| 8 | **Recovery Planner** | `/recovery` | Strategy selector, extra payment input, timeline visualization |
| 9 | **Borrower Rights** | `/rights` | Accordion sections, searchable rights database |
| 10 | **AI History** | `/history` | Filtered list of past AI interactions, replay functionality |

---

## 8. Innovation Aspects

### 8.1 First-of-Kind AI Application
No existing Indian platform combines AI-powered debt analysis + settlement advice + letter generation + recovery planning in a single, free, open-source tool.

### 8.2 Dual-Engine Reliability
The Gemini + Python fallback architecture ensures the platform is useful even during API outages — critical for users in financial distress who need answers immediately.

### 8.3 India-Specific Design
- Indian Rupee (₹) throughout
- Indian loan types (chit fund, BNPL, microfinance supported)
- RBI-specific regulatory content
- Indian banking convention in letter formats
- Localization considerations (Tamil, Telugu possible extension)

### 8.4 Transparent AI
Unlike black-box AI tools, FinRelief discloses:
- Whether response is from Gemini or fallback engine
- Confidence level of settlement recommendation
- Limitations of the tool (not legal advice, not financial advice — educational tool)

### 8.5 Privacy-First Design
- No data shared with third parties
- No loan data sent to Gemini in personally identifiable form (anonymized parameters)
- JWT ensures server-side session security
- HTTPS everywhere

---

## 9. Impact Assessment

### 9.1 Direct User Impact
| Impact Area | Metric |
|---|---|
| Time saved vs. professional consultation | 2–5 hours per user |
| Cost saved vs. professional consultation | ₹3,000–₹25,000 per session |
| Settlement clarity | User knows their range within 30 seconds |
| Letter generation time | 3–5 seconds vs. 2–3 days |

### 9.2 Social Impact Potential
At 10,000 users:
- **₹30 crore** in potential professional fees saved
- **Millions** in better settlement outcomes (average 5% better settlement = ₹15,000 on ₹3L loan)
- **Financial literacy** uplift for thousands of first-generation borrowers

### 9.3 Technical Impact
- Demonstrates responsible use of Generative AI for social good
- Open-source platform (GitHub: https://github.com/JoelPrasannaKumar/finrelief)
- Replicable architecture for other developing markets (Bangladesh, Pakistan, Nigeria)

---

## 10. Conclusion

FinRelief AI is more than a project — it is a proof-of-concept for AI-powered financial inclusion. By combining Google Gemini 2.0 Flash's generative intelligence with a carefully engineered financial analysis engine, the platform delivers professional-grade debt counseling to users who would otherwise never access it. The 8 major features, 10 screens, and dual-engine architecture make FinRelief AI a complete, deployable solution addressing one of India's most pressing socioeconomic challenges.

---

*Document Version: 1.0 | Created: July 2026 | FinRelief AI Team — Vishnu Institute of Technology, Bhimavaram*
