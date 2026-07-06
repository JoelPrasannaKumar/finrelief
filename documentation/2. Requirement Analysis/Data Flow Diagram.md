# Data Flow Diagram (DFD)
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

## 1. Introduction to DFD

A **Data Flow Diagram (DFD)** is a structured representation of how data moves through a system. It shows:
- **External Entities** (users, third-party systems) — represented as rectangles
- **Processes** (transformations applied to data) — represented as circles/rounded rectangles
- **Data Stores** (databases, file systems) — represented as open rectangles
- **Data Flows** (movement of data) — represented as arrows

### DFD Notation Used

| Symbol | Notation in ASCII | Description |
|---|---|---|
| External Entity | `[  ENTITY  ]` | Users or external systems |
| Process | `(  PROCESS  )` | Computation or transformation |
| Data Store | `=== STORE ===` | Persistent data storage |
| Data Flow | `──────────→` | Direction of data movement |

### DFD Levels Covered
1. **Level 0 (Context Diagram)** — System as a single process, all external entities
2. **Level 1 DFD** — System decomposed into 7 major processes
3. **Data Store Details** — All 6 data stores with schemas
4. **Security Considerations** — How data is protected at each flow

---

## 2. Level 0 DFD — Context Diagram

The Context Diagram shows FinRelief AI as a single system ("black box") with all external entities that interact with it.

### External Entities

| Entity ID | Name | Role |
|---|---|---|
| E1 | Borrower (User) | Primary user who registers, adds loans, and requests AI analysis |
| E2 | Google Gemini 2.0 Flash API | AI model provider for analysis, letter generation, and chat |
| E3 | Email Service (SMTP/SendGrid) | Sends verification emails and notifications to users |
| E4 | System Administrator | Manages system configuration and monitors health |

### Level 0 ASCII Diagram

```
                      ┌─────────────────────────────────────┐
                      │                                     │
   Registration Data  │                                     │  Verification Email
   Loan Information   │                                     │──────────────────────→  [E3: Email Service]
   Analysis Requests  │                                     │
   ─────────────────→ │                                     │
                      │                                     │  AI Prompts (Structured)
   [E1: BORROWER]     │     FinRelief AI System             │──────────────────────→  [E2: Gemini API]
                      │         (Central System)            │
   ←─────────────── │                                     │  ←────────────────────
   Analysis Reports   │                                     │  AI Responses (JSON)
   OTS Letters        │                                     │
   Recovery Plans     │                                     │
   Financial Insights │                                     │  Admin Commands
                      │                                     │  ←────────────────────  [E4: Admin]
                      │                                     │
                      │                                     │──────────────────────→
                      │                                     │  System Logs / Reports
                      └─────────────────────────────────────┘
```

---

## 3. Level 1 DFD — Process Decomposition

The Level 1 DFD decomposes the FinRelief AI system into **7 major processes**, each handling a distinct functional area.

### Process List

| Process ID | Process Name | Description |
|---|---|---|
| P1 | User Authentication & Authorization | Handles registration, login, JWT issuance |
| P2 | User Profile Management | Manages financial profile data (income, expenses) |
| P3 | Loan Management | CRUD operations for user loan records |
| P4 | AI Debt Analysis Engine | Sends loan data to Gemini API, processes response |
| P5 | OTS Settlement Advisor | Determines OTS eligibility and generates advice |
| P6 | Letter Generation System | Generates professional OTS/debt negotiation letters |
| P7 | Recovery Dashboard & Tracking | Tracks progress, updates scores, displays roadmap |

### Data Stores

| Store ID | Store Name | Description | Technology |
|---|---|---|---|
| DS1 | User Store | User accounts, credentials, and profile data | SQLite (via SQLAlchemy) |
| DS2 | Loan Store | All user loan records with full details | SQLite (via SQLAlchemy) |
| DS3 | Analysis Store | AI-generated analysis results (cached) | SQLite (via SQLAlchemy) |
| DS4 | Letter Store | Generated OTS letters (stored for history) | SQLite (via SQLAlchemy) |
| DS5 | Session Store | Active JWT tokens and session data | In-memory (FastAPI) |
| DS6 | System Logs | Application logs, error logs, audit trails | File system / logging |

---

## 4. Full Level 1 DFD — ASCII Art

```
══════════════════════════════════════════════════════════════════════════════════
                        FinRelief AI — Level 1 DFD
══════════════════════════════════════════════════════════════════════════════════

[E1: BORROWER]
      │
      │  Registration Data (name, email, password)
      ▼
┌─────────────────────────────┐
│  P1: USER AUTHENTICATION    │
│  & AUTHORIZATION            │
│  • Validate credentials     │
│  • Hash passwords (bcrypt)  │
│  • Generate JWT token       │
│  • Verify email             │
└─────────────────────────────┘
      │                    │                    │
      │  User Record       │  JWT Token         │  Verification Email
      ▼                    ▼                    ▼
=== DS1: USER STORE ===  === DS5: SESSION ===  [E3: EMAIL SERVICE]
      │
      │  User Data Read
      ▼
┌─────────────────────────────┐
│  P2: USER PROFILE           │
│  MANAGEMENT                 │
│  • Store income/expenses    │
│  • Calculate savings rate   │
│  • Compute DTI ratio        │
│  • Generate health snapshot │
└─────────────────────────────┘
      │                         │
      │  Profile Data Saved     │  Updated Profile
      ▼                         ▼
=== DS1: USER STORE ===      [E1: BORROWER] ← Financial Health Snapshot
      │
      │
[E1: BORROWER]
      │
      │  Loan Data (lender, amount, rate, tenure, EMI)
      ▼
┌─────────────────────────────┐
│  P3: LOAN MANAGEMENT        │
│  • Add/Edit/Delete loans    │
│  • Calculate outstanding    │
│  • Compute total EMI burden │
│  • Validate loan data       │
└─────────────────────────────┘
      │                    │
      │  Loan Records      │  Loan Summary
      ▼                    ▼
=== DS2: LOAN STORE ===  [E1: BORROWER] ← Loan Dashboard


═══════════ AI-POWERED PROCESSES ═══════════

[E1: BORROWER] → "Generate Analysis" Request
      │
      ▼
┌─────────────────────────────┐
│  P4: AI DEBT ANALYSIS       │
│  ENGINE                     │
│  • Retrieve all user loans  │
│  • Retrieve user profile    │
│  • Build analysis prompt    │
│  • Call Gemini 2.0 Flash    │
│  • Parse AI response        │
│  • Calculate Debt Severity  │
│    Score (proprietary)      │
│  • Cache results in DS3     │
└─────────────────────────────┘
      │              │              │
      │ Read Loans   │ Read Profile │ Store Analysis
      ▼              ▼              ▼
=== DS2 ===    === DS1 ===    === DS3: ANALYSIS STORE ===
      │
      │  Structured Prompt (JSON)
      ▼
[E2: GOOGLE GEMINI 2.0 FLASH API]
      │
      │  AI Analysis Response (JSON)
      ▼
┌─────────────────────────────┐
│  (Back to P4 for parsing)   │
└─────────────────────────────┘
      │
      │  Analysis Report
      ▼
[E1: BORROWER] ← Debt Severity Score, Recovery Plan, Recommendations


[E1: BORROWER] → "Check OTS Options" Request for specific loan
      │
      ▼
┌─────────────────────────────┐
│  P5: OTS SETTLEMENT         │
│  ADVISOR                    │
│  • Retrieve loan details    │
│  • Assess OTS eligibility   │
│    (loan type, outstanding, │
│     loan age, payment hist) │
│  • Call Gemini for OTS      │
│    negotiation range        │
│  • Generate prerequisites   │
│  • Store OTS advice         │
└─────────────────────────────┘
      │                    │
      │  Loan Data         │  OTS Advice Prompt
      ▼                    ▼
=== DS2: LOAN STORE ===  [E2: GEMINI API]
                              │
                              │  OTS Range + Strategy
                              ▼
                   ┌─────────────────────────────┐
                   │  (Back to P5 for processing)│
                   └─────────────────────────────┘
                              │
                              │  Settlement Advice
                              ▼
                   [E1: BORROWER] ← OTS Range, Prerequisites, Strategy


[E1: BORROWER] → "Generate OTS Letter" Request
      │  (with loan details + hardship context)
      ▼
┌─────────────────────────────┐
│  P6: LETTER GENERATION      │
│  SYSTEM                     │
│  • Collect letter params    │
│  • Build letter prompt with │
│    legal/regulatory context │
│  • Call Gemini 2.0 Flash    │
│  • Post-process response    │
│  • Format as professional   │
│    letter                   │
│  • Store in DS4             │
│  • Offer PDF/DOCX export    │
└─────────────────────────────┘
      │                    │
      │  Store Letter      │  Letter Generation Prompt
      ▼                    ▼
=== DS4: LETTER STORE === [E2: GEMINI API]
                              │
                              │  Generated Letter Text
                              ▼
                   ┌─────────────────────────────┐
                   │  (Back to P6 for formatting)│
                   └─────────────────────────────┘
                              │
                              │  Formatted OTS Letter (editable)
                              ▼
                   [E1: BORROWER] ← Professional OTS Letter (PDF/DOCX/Copy)


[E1: BORROWER] → Dashboard View / Loan Updates
      │
      ▼
┌─────────────────────────────┐
│  P7: RECOVERY DASHBOARD     │
│  & TRACKING                 │
│  • Retrieve all loans       │
│  • Load latest analysis     │
│  • Calculate progress       │
│  • Update loan statuses     │
│  • Compute recovery %       │
│  • Display roadmap timeline │
│  • Trigger celebration on   │
│    loan payoff              │
└─────────────────────────────┘
      │          │          │
      │ Loans    │ Analysis │ Store Log
      ▼          ▼          ▼
=== DS2 === === DS3 === === DS6: SYSTEM LOGS ===
      │
      │  Complete Dashboard Data
      ▼
[E1: BORROWER] ← Recovery Progress, Roadmap, Updated Severity Score


[E4: ADMINISTRATOR]
      │  Admin Commands (config updates, monitoring)
      ▼
┌──────────────────┐
│  Admin Interface │
└──────────────────┘
      │
      ▼
=== DS6: SYSTEM LOGS === ← All processes write logs here

══════════════════════════════════════════════════════════════════════════════════
```

---

## 5. Data Flow Descriptions

### Flow Table — All Data Flows

| Flow ID | From | To | Data Carried | Format |
|---|---|---|---|---|
| F01 | Borrower (E1) | P1: Authentication | Email, Password, Name | JSON POST |
| F02 | P1 | DS1: User Store | Hashed password, user record | SQL INSERT |
| F03 | P1 | DS5: Session Store | JWT access token + refresh token | In-memory |
| F04 | P1 | E3: Email Service | Email address, verification link | SMTP |
| F05 | E3 | Borrower (E1) | Verification email | Email |
| F06 | Borrower (E1) | P2: Profile Mgmt | Monthly income, expenses, city, occupation | JSON PUT |
| F07 | P2 | DS1: User Store | Updated financial profile | SQL UPDATE |
| F08 | DS1 | P2 | Existing profile data | SQL SELECT |
| F09 | P2 | Borrower (E1) | Financial Health Snapshot | JSON response |
| F10 | Borrower (E1) | P3: Loan Mgmt | Loan details (all fields) | JSON POST |
| F11 | P3 | DS2: Loan Store | Validated loan record | SQL INSERT |
| F12 | DS2 | P3 | All user loan records | SQL SELECT |
| F13 | P3 | Borrower (E1) | Loan dashboard summary | JSON response |
| F14 | Borrower (E1) | P4: AI Analysis | Analysis request (user_id) | JSON POST |
| F15 | DS2 | P4 | All user loans | SQL SELECT |
| F16 | DS1 | P4 | User profile (income/expenses) | SQL SELECT |
| F17 | P4 | E2: Gemini API | Structured analysis prompt | HTTPS POST |
| F18 | E2: Gemini API | P4 | AI analysis response | JSON |
| F19 | P4 | DS3: Analysis Store | Parsed analysis results | SQL INSERT |
| F20 | P4 | Borrower (E1) | Analysis report, Debt Severity Score | JSON response |
| F21 | Borrower (E1) | P5: OTS Advisor | Loan ID for OTS assessment | JSON POST |
| F22 | DS2 | P5 | Specific loan details | SQL SELECT |
| F23 | P5 | E2: Gemini API | OTS eligibility prompt | HTTPS POST |
| F24 | E2: Gemini API | P5 | OTS range and negotiation strategy | JSON |
| F25 | P5 | Borrower (E1) | Settlement advice and prerequisites | JSON response |
| F26 | Borrower (E1) | P6: Letter Gen | Letter params (loan ID, amount, context) | JSON POST |
| F27 | DS2 | P6 | Loan details for letter | SQL SELECT |
| F28 | P6 | E2: Gemini API | Letter generation prompt | HTTPS POST |
| F29 | E2: Gemini API | P6 | Generated letter text | JSON |
| F30 | P6 | DS4: Letter Store | Formatted letter record | SQL INSERT |
| F31 | P6 | Borrower (E1) | Professional OTS letter (multiple formats) | JSON/PDF/DOCX |
| F32 | Borrower (E1) | P7: Recovery Dashboard | Dashboard view request / loan update | JSON GET/PUT |
| F33 | DS2 | P7 | All loans with statuses | SQL SELECT |
| F34 | DS3 | P7 | Latest analysis results | SQL SELECT |
| F35 | P7 | DS2 | Updated loan status | SQL UPDATE |
| F36 | P7 | Borrower (E1) | Recovery dashboard data | JSON response |
| F37 | All Processes | DS6: Logs | Audit logs, error logs | Log files |
| F38 | Admin (E4) | DS6 | Admin queries | Direct DB/Log access |

---

## 6. Data Store Schemas

### DS1: User Store (users table)

```sql
CREATE TABLE users (
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(150) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL,  -- bcrypt hashed
    city        VARCHAR(100),
    occupation  VARCHAR(100),
    income      FLOAT,                  -- monthly take-home
    expenses    FLOAT,                  -- monthly non-EMI expenses
    is_verified BOOLEAN     DEFAULT FALSE,
    created_at  DATETIME    DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME    DEFAULT CURRENT_TIMESTAMP
);
```

### DS2: Loan Store (loans table)

```sql
CREATE TABLE loans (
    id              INTEGER     PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER     NOT NULL REFERENCES users(id),
    loan_type       VARCHAR(50) NOT NULL,   -- home, personal, education, vehicle, credit_card
    lender_name     VARCHAR(150) NOT NULL,
    original_amount FLOAT       NOT NULL,
    outstanding     FLOAT       NOT NULL,
    emi_amount      FLOAT       NOT NULL,
    interest_rate   FLOAT       NOT NULL,   -- annual %
    tenure_months   INTEGER,
    start_date      DATE,
    status          VARCHAR(20) DEFAULT 'active',  -- active, settled, closed, restructured
    account_number  VARCHAR(50),            -- optional
    created_at      DATETIME    DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME    DEFAULT CURRENT_TIMESTAMP
);
```

### DS3: Analysis Store (analyses table)

```sql
CREATE TABLE analyses (
    id                  INTEGER     PRIMARY KEY AUTOINCREMENT,
    user_id             INTEGER     NOT NULL REFERENCES users(id),
    severity_score      FLOAT       NOT NULL,   -- 1-10 scale
    summary             TEXT        NOT NULL,   -- AI summary
    recommendations     TEXT        NOT NULL,   -- JSON array
    recovery_plan       TEXT        NOT NULL,   -- JSON array of monthly steps
    raw_ai_response     TEXT,                   -- full Gemini response
    generated_at        DATETIME    DEFAULT CURRENT_TIMESTAMP
);
```

### DS4: Letter Store (letters table)

```sql
CREATE TABLE letters (
    id              INTEGER     PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER     NOT NULL REFERENCES users(id),
    loan_id         INTEGER     REFERENCES loans(id),
    letter_type     VARCHAR(50) NOT NULL,   -- ots_request, hardship, restructuring
    offer_amount    FLOAT,
    hardship_reason TEXT,
    letter_content  TEXT        NOT NULL,   -- full generated letter
    generated_at    DATETIME    DEFAULT CURRENT_TIMESTAMP
);
```

---

## 7. Security Considerations

Security is a critical non-functional requirement for FinRelief AI given the sensitive financial nature of user data.

### Data Flow Security Matrix

| Flow | Security Measure | Implementation |
|---|---|---|
| F01 (Registration) | Password never stored in plaintext | bcrypt with salt rounds=12 |
| F03 (JWT issuance) | Tokens signed and time-limited | HS256 signing, 24hr expiry |
| F17, F23, F28 (Gemini calls) | API key not exposed to client | Server-side only; env variable |
| All DB reads | SQL injection prevention | SQLAlchemy ORM parameterized queries |
| F31 (Letter download) | User can only access own letters | User ID validation on every request |
| All HTTPS flows | Transport encryption | TLS 1.3 enforced |
| DS1 (User data) | PII protection | No PII sent to Gemini without anonymization |

### Threat Model

| Threat | Risk Level | Mitigation |
|---|---|---|
| SQL Injection | High | SQLAlchemy ORM; no raw SQL with user input |
| JWT Forgery | High | Strong secret key; RS256 in production |
| Unauthorized Data Access | Critical | Row-level security: user_id check on all queries |
| Gemini API Key Exposure | Critical | Server-side only; Docker secrets in production |
| Brute Force Login | Medium | Rate limiting (10 attempts/hour per IP) |
| Data Breach (DB) | High | SQLite encrypted at rest; no PII in logs |
| MITM Attack | Medium | HTTPS enforced; HSTS headers |
| Prompt Injection (Gemini) | Medium | Sanitize user input before sending to AI |

### GDPR / Data Privacy Compliance

| Principle | Implementation |
|---|---|
| **Data Minimization** | Only collect data necessary for debt analysis |
| **Purpose Limitation** | User data only used for financial analysis; never sold |
| **Right to Erasure** | DELETE /api/users/me endpoint available |
| **Transparency** | Clear privacy policy; data usage explained in plain language |
| **Security** | bcrypt, JWT, HTTPS, parameterized queries |

---

## 8. DFD Validation

### Completeness Check

| Requirement | Verified |
|---|---|
| All external entities identified | ✅ Yes (Borrower, Gemini API, Email Service, Admin) |
| All processes have at least one input and one output | ✅ Yes |
| All data stores connected to at least one process | ✅ Yes (DS1–DS6) |
| No direct entity-to-entity flows (must go through process) | ✅ Yes |
| All data flows labeled | ✅ Yes (F01–F38) |
| Security review completed | ✅ Yes |

---

*Document prepared by: Team FinRelief AI | SmartBridge Google Cloud Generative AI Internship | Vishnu Institute of Technology, Bhimavaram*
