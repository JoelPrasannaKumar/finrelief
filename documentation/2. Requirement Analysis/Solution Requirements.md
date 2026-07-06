# Solution Requirements
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

## 1. Requirements Overview

This document captures the complete set of requirements for FinRelief AI, structured as:
- **Functional Requirements (FR):** What the system must do
- **Non-Functional Requirements (NFR):** How well the system must do it
- **System Requirements:** Infrastructure and environment needs
- **API Requirements:** REST API specifications
- **Constraints:** Limitations and boundaries
- **Acceptance Criteria:** Definition of done

Requirements are prioritized using **MoSCoW** method:
- **M** = Must Have (MVP critical)
- **S** = Should Have (important but not MVP-blocking)
- **C** = Could Have (desirable if time permits)
- **W** = Won't Have (out of scope for this version)

---

## 2. Functional Requirements

### FR-001: User Registration

| Field | Details |
|---|---|
| **ID** | FR-001 |
| **Title** | User Registration |
| **Priority** | Must Have (M) |
| **Category** | Authentication |
| **Description** | The system shall allow new users to create an account using their full name, email address, and password. The system shall send an email verification link to the registered email. Users cannot access core features until their email is verified. |
| **Inputs** | Full name (string, max 100 chars), Email (valid email format), Password (min 8 chars, 1 uppercase, 1 number) |
| **Outputs** | User account created, verification email sent, success message displayed |
| **Business Rule** | Duplicate email addresses shall be rejected with a clear error message |
| **Acceptance Criteria** | New user can register, receives verification email within 60 seconds, and can log in after verifying |

---

### FR-002: User Authentication (Login/Logout)

| Field | Details |
|---|---|
| **ID** | FR-002 |
| **Title** | User Authentication |
| **Priority** | Must Have (M) |
| **Category** | Authentication |
| **Description** | The system shall authenticate users with email and password, issuing a JWT access token valid for 24 hours. The system shall also issue a refresh token valid for 7 days. Logout shall invalidate the current session. |
| **Inputs** | Email, Password |
| **Outputs** | JWT access token, refresh token, user profile data |
| **Business Rule** | After 5 failed login attempts, account shall be locked for 15 minutes |
| **Acceptance Criteria** | Valid credentials produce a JWT; invalid credentials produce a 401 error; logout clears session |

---

### FR-003: Financial Profile Management

| Field | Details |
|---|---|
| **ID** | FR-003 |
| **Title** | Financial Profile Setup & Management |
| **Priority** | Must Have (M) |
| **Category** | User Profile |
| **Description** | The system shall allow authenticated users to create and update their financial profile including: monthly income, monthly non-EMI expenses, city of residence, occupation type. The system shall compute and display: savings ratio, debt-to-income ratio, disposable income. |
| **Inputs** | Monthly income (float), Monthly expenses (float), City (string), Occupation (string) |
| **Outputs** | Saved financial profile, computed financial health indicators |
| **Business Rule** | Monthly expenses cannot exceed monthly income |
| **Acceptance Criteria** | User can save and update profile; financial indicators are accurately computed; DTI ratio is highlighted if > 50% |

---

### FR-004: Loan Management — Add Loan

| Field | Details |
|---|---|
| **ID** | FR-004 |
| **Title** | Add Loan Record |
| **Priority** | Must Have (M) |
| **Category** | Loan Management |
| **Description** | The system shall allow users to add loan records with full details: loan type (home/personal/education/vehicle/credit card/other), lender name, original loan amount, current outstanding balance, monthly EMI, annual interest rate, loan start date, remaining tenure, and optional loan account number. |
| **Inputs** | Loan type, lender name, original amount, outstanding amount, EMI, interest rate, start date, tenure, account number (optional) |
| **Outputs** | Loan record saved, dashboard updated with new loan card |
| **Business Rule** | Outstanding balance cannot exceed original loan amount; interest rate must be between 1% and 100% |
| **Acceptance Criteria** | Loan is saved and immediately appears on dashboard; total EMI and total outstanding are updated |

---

### FR-005: Loan Management — View, Edit, Delete

| Field | Details |
|---|---|
| **ID** | FR-005 |
| **Title** | Loan CRUD Operations |
| **Priority** | Must Have (M) |
| **Category** | Loan Management |
| **Description** | The system shall allow users to view the complete list of their loans, edit any loan's details, and delete a loan record. Deleting a loan shall prompt for confirmation and shall cascade-delete related analyses. |
| **Inputs** | Loan ID, updated field values |
| **Outputs** | Updated loan list, confirmation message |
| **Business Rule** | Users can only view/edit/delete their own loans (user_id validation enforced server-side) |
| **Acceptance Criteria** | All CRUD operations work correctly; unauthorized access attempts return 403 |

---

### FR-006: Loan Dashboard Summary

| Field | Details |
|---|---|
| **ID** | FR-006 |
| **Title** | Loan Portfolio Dashboard |
| **Priority** | Must Have (M) |
| **Category** | Dashboard |
| **Description** | The system shall display a comprehensive dashboard showing: total outstanding debt, total monthly EMI, debt composition by loan type (chart), debt-to-income ratio, number of active loans, and individual loan cards. |
| **Inputs** | User ID (from JWT) |
| **Outputs** | Dashboard with aggregated financial data and visualizations |
| **Business Rule** | Dashboard must reflect real-time data from the database |
| **Acceptance Criteria** | Dashboard loads within 2 seconds; all aggregations are mathematically accurate |

---

### FR-007: AI-Powered Debt Analysis

| Field | Details |
|---|---|
| **ID** | FR-007 |
| **Title** | Gemini AI Debt Analysis |
| **Priority** | Must Have (M) |
| **Category** | AI Features |
| **Description** | The system shall send the user's complete financial profile (income, expenses, all loans) to Google Gemini 2.0 Flash API and generate a comprehensive debt analysis report including: Debt Severity Score (1–10), overall financial assessment, prioritized loan payoff order with rationale, month-by-month recovery roadmap, and actionable recommendations. |
| **Inputs** | User's complete financial profile and all loan records |
| **Outputs** | Structured analysis report with severity score, roadmap, and recommendations |
| **Business Rule** | Analysis is rate-limited to 3 requests per day per user; results are cached for 24 hours |
| **Acceptance Criteria** | Analysis is generated within 10 seconds; Debt Severity Score is between 1–10; recommendations are specific to the user's situation |

---

### FR-008: Debt Severity Score

| Field | Details |
|---|---|
| **ID** | FR-008 |
| **Title** | Proprietary Debt Severity Score |
| **Priority** | Must Have (M) |
| **Category** | AI Features |
| **Description** | The system shall compute a proprietary Debt Severity Score (DSS) on a scale of 1–10 (1=low stress, 10=critical) based on: DTI ratio (40%), interest rate exposure (20%), loan diversification (15%), EMI-to-savings ratio (15%), and loan tenure exposure (10%). Score shall be displayed prominently with color coding. |
| **Inputs** | User financial profile, all loan records |
| **Outputs** | DSS score (float, 1 decimal), risk category (Low/Medium/High/Critical), score breakdown by factor |
| **Business Rule** | Score < 4 = Low (green), 4–6 = Medium (amber), 6–8 = High (red), 8–10 = Critical (dark red) |
| **Acceptance Criteria** | Score correctly reflects financial stress; color coding is immediately visible; breakdown is available on click |

---

### FR-009: OTS Eligibility Assessment

| Field | Details |
|---|---|
| **ID** | FR-009 |
| **Title** | One-Time Settlement Eligibility Advisor |
| **Priority** | Must Have (M) |
| **Category** | AI Features |
| **Description** | The system shall assess OTS settlement eligibility for any specific loan using Gemini AI, providing: eligibility likelihood (High/Medium/Low), estimated settlement range (percentage of outstanding), key eligibility factors, documentation checklist, and negotiation strategy. |
| **Inputs** | Loan ID, user's financial profile |
| **Outputs** | OTS eligibility report with range, documentation list, and strategy |
| **Business Rule** | Always include disclaimer: "This is AI-generated guidance; consult a financial advisor for formal advice" |
| **Acceptance Criteria** | OTS report includes estimated range, prerequisites checklist, and strategy; disclaimer is always present |

---

### FR-010: OTS Letter Generation

| Field | Details |
|---|---|
| **ID** | FR-010 |
| **Title** | AI-Powered OTS Letter Generator |
| **Priority** | Must Have (M) |
| **Category** | AI Features |
| **Description** | The system shall generate professional OTS negotiation letters using Gemini 2.0 Flash. Users provide: loan details, settlement offer amount, hardship reason. The system generates a formal letter including: borrower details, loan reference, hardship narrative, specific settlement offer, request for written response, and references to RBI Fair Practices Code. |
| **Inputs** | Loan ID, settlement amount, hardship reason (free text), optional additional context |
| **Outputs** | Formatted OTS letter (display preview + downloadable PDF/DOCX) |
| **Business Rule** | Letter must include RBI Fair Practices Code reference and request written acknowledgment from lender |
| **Acceptance Criteria** | Letter is professional, properly formatted, includes all required sections, downloadable as PDF |

---

### FR-011: Letter History & Management

| Field | Details |
|---|---|
| **ID** | FR-011 |
| **Title** | Letter History |
| **Priority** | Should Have (S) |
| **Category** | Letter Management |
| **Description** | The system shall maintain a history of all letters generated by a user, allowing them to view, download, and delete previous letters. |
| **Inputs** | User ID |
| **Outputs** | List of previously generated letters with generation date and loan reference |
| **Business Rule** | Users can only access their own letters |
| **Acceptance Criteria** | Letter history page loads with all previous letters; each letter can be re-downloaded |

---

### FR-012: Recovery Roadmap Visualization

| Field | Details |
|---|---|
| **ID** | FR-012 |
| **Title** | Debt Recovery Roadmap |
| **Priority** | Should Have (S) |
| **Category** | Dashboard |
| **Description** | The system shall display a visual timeline-based recovery roadmap generated by AI, showing month-by-month milestones: loan payoff dates, expected savings increases, Debt Severity Score improvement trajectory, and total debt-free date. |
| **Inputs** | AI analysis results, user profile, loan data |
| **Outputs** | Visual roadmap timeline with milestones |
| **Business Rule** | Roadmap must be updated whenever loan data or profile changes |
| **Acceptance Criteria** | Roadmap is visually clear; milestones are date-specific; debt-free date is prominently displayed |

---

### FR-013: Loan Status Updates

| Field | Details |
|---|---|
| **ID** | FR-013 |
| **Title** | Loan Status Management |
| **Priority** | Should Have (S) |
| **Category** | Loan Management |
| **Description** | The system shall allow users to update a loan's status to: Active, Settled (OTS), Closed (fully paid), Under Restructuring, or In Dispute. When a loan is marked as Closed or Settled, a celebration animation shall trigger, and the dashboard shall update accordingly. |
| **Inputs** | Loan ID, new status |
| **Outputs** | Updated loan status, celebration animation (on payoff), updated dashboard totals |
| **Business Rule** | When all loans are Closed or Settled, display "Debt-Free" celebration |
| **Acceptance Criteria** | Status updates persist; celebration animation triggers on payoff; dashboard reflects new totals |

---

### FR-014: AI Financial Q&A Chat

| Field | Details |
|---|---|
| **ID** | FR-014 |
| **Title** | AI Financial Advisor Chat |
| **Priority** | Could Have (C) |
| **Category** | AI Features |
| **Description** | The system shall provide a conversational AI chat interface where users can ask financial questions. Gemini 2.0 Flash shall respond with personalized answers based on the user's financial profile and loans. Chat history shall be preserved for the current session. |
| **Inputs** | User message (free text) |
| **Outputs** | AI response, chat history |
| **Business Rule** | All responses include disclaimer that advice is not professional financial advice |
| **Acceptance Criteria** | Chat responds within 8 seconds; responses are contextually relevant to user's financial situation |

---

### FR-015: Data Export

| Field | Details |
|---|---|
| **ID** | FR-015 |
| **Title** | Data Export |
| **Priority** | Could Have (C) |
| **Category** | User Features |
| **Description** | The system shall allow users to export their complete loan data and analysis history as a PDF report or CSV file for offline reference. |
| **Inputs** | User ID, export format selection |
| **Outputs** | Downloadable PDF or CSV file |
| **Business Rule** | Export includes only the requesting user's data |
| **Acceptance Criteria** | Export generates within 10 seconds; all loan data and analyses are included |

---

## 3. Functional Requirements Summary Table

| ID | Title | Priority | Category | Status |
|---|---|---|---|---|
| FR-001 | User Registration | Must Have | Auth | ✅ Implemented |
| FR-002 | User Authentication | Must Have | Auth | ✅ Implemented |
| FR-003 | Financial Profile Management | Must Have | Profile | ✅ Implemented |
| FR-004 | Add Loan Record | Must Have | Loans | ✅ Implemented |
| FR-005 | Loan CRUD Operations | Must Have | Loans | ✅ Implemented |
| FR-006 | Loan Portfolio Dashboard | Must Have | Dashboard | ✅ Implemented |
| FR-007 | Gemini AI Debt Analysis | Must Have | AI | ✅ Implemented |
| FR-008 | Debt Severity Score | Must Have | AI | ✅ Implemented |
| FR-009 | OTS Eligibility Assessment | Must Have | AI | ✅ Implemented |
| FR-010 | OTS Letter Generator | Must Have | AI | ✅ Implemented |
| FR-011 | Letter History | Should Have | Letters | ✅ Implemented |
| FR-012 | Recovery Roadmap | Should Have | Dashboard | ✅ Implemented |
| FR-013 | Loan Status Updates | Should Have | Loans | ✅ Implemented |
| FR-014 | AI Q&A Chat | Could Have | AI | 🚧 Planned v2 |
| FR-015 | Data Export | Could Have | Export | 🚧 Planned v2 |

---

## 4. Non-Functional Requirements

### NFR-001: Performance

| Field | Details |
|---|---|
| **ID** | NFR-001 |
| **Category** | Performance |
| **Requirement** | API endpoints (non-AI) must respond within 500ms for P95 requests under normal load. AI-powered endpoints must respond within 10 seconds for P95 requests. Dashboard must load completely within 2 seconds on a 4G connection. |
| **Measurement** | Load testing with k6; API monitoring with response time tracking |
| **Acceptance** | P95 < 500ms for standard APIs; P95 < 10s for AI APIs |

### NFR-002: Availability & Reliability

| Field | Details |
|---|---|
| **ID** | NFR-002 |
| **Category** | Reliability |
| **Requirement** | System uptime must be ≥ 99% (excluding planned maintenance). Planned maintenance windows must be announced 24 hours in advance. The system must gracefully handle Gemini API unavailability with a clear user message. |
| **Measurement** | Uptime monitoring via external service (UptimeRobot) |
| **Acceptance** | ≥ 99% uptime measured over 30-day periods |

### NFR-003: Security

| Field | Details |
|---|---|
| **ID** | NFR-003 |
| **Category** | Security |
| **Requirement** | All user passwords must be hashed using bcrypt (minimum 12 salt rounds). All API communication must be over HTTPS (TLS 1.2+). JWT tokens must expire after 24 hours. All database queries must use parameterized statements. API keys must never be exposed in client-side code. |
| **Measurement** | Security audit, penetration testing, OWASP Top 10 compliance check |
| **Acceptance** | Zero critical security vulnerabilities; OWASP Top 10 addressed |

### NFR-004: Scalability

| Field | Details |
|---|---|
| **ID** | NFR-004 |
| **Category** | Scalability |
| **Requirement** | The system architecture must support horizontal scaling of the FastAPI backend. The database should be migratable from SQLite to PostgreSQL without code changes (SQLAlchemy abstraction). The system should handle 500 concurrent users without performance degradation. |
| **Measurement** | Load testing; architecture review |
| **Acceptance** | 500 concurrent users with < 20% response time increase |

### NFR-005: Usability

| Field | Details |
|---|---|
| **ID** | NFR-005 |
| **Category** | Usability |
| **Requirement** | New users must be able to complete the full onboarding flow (register → profile → add first loan → generate analysis) within 10 minutes without external help. The UI must achieve a Lighthouse usability score ≥ 85. All interactive elements must have descriptive ARIA labels. |
| **Measurement** | User testing, Lighthouse audit |
| **Acceptance** | ≥ 85 Lighthouse score; 90% of test users complete onboarding in < 10 minutes |

### NFR-006: Accessibility

| Field | Details |
|---|---|
| **ID** | NFR-006 |
| **Category** | Accessibility |
| **Requirement** | The application must meet WCAG 2.1 Level AA standards. This includes: keyboard navigation support, sufficient color contrast ratios (≥ 4.5:1), screen reader compatibility, and no reliance on color alone to convey information. |
| **Measurement** | axe DevTools accessibility audit, manual keyboard navigation testing |
| **Acceptance** | Zero WCAG 2.1 Level AA violations in automated audit |

### NFR-007: Maintainability

| Field | Details |
|---|---|
| **ID** | NFR-007 |
| **Category** | Maintainability |
| **Requirement** | All backend code must follow PEP 8 style guidelines. All API endpoints must be documented via FastAPI's auto-generated OpenAPI/Swagger UI. Code coverage for backend unit tests must be ≥ 70%. All environment-specific configuration must use environment variables. |
| **Measurement** | Code linting (flake8), test coverage reports (pytest-cov), Swagger UI validation |
| **Acceptance** | ≥ 70% test coverage; all endpoints visible in Swagger UI; PEP 8 compliance |

### NFR-008: Data Privacy

| Field | Details |
|---|---|
| **ID** | NFR-008 |
| **Category** | Privacy |
| **Requirement** | User PII (name, email) must never be sent to the Gemini API in identifiable form. Financial data sent to Gemini must be anonymized (amounts only, no account numbers). Users must have the ability to delete their account and all associated data. Privacy policy must be clearly accessible. |
| **Measurement** | Code review of Gemini prompt construction; privacy policy publication |
| **Acceptance** | No PII in Gemini API calls; account deletion endpoint functional |

### NFR-009: Portability

| Field | Details |
|---|---|
| **ID** | NFR-009 |
| **Category** | Portability |
| **Requirement** | The backend must be containerized using Docker for environment-agnostic deployment. A docker-compose.yml must be provided for local development. The application must run consistently across Windows, Linux, and macOS development environments. |
| **Measurement** | Docker build test across platforms |
| **Acceptance** | Docker build succeeds; docker-compose up starts all services correctly |

### NFR-010: Compliance

| Field | Details |
|---|---|
| **ID** | NFR-010 |
| **Category** | Compliance |
| **Requirement** | All AI-generated financial content must include a mandatory disclaimer: "This is AI-generated guidance for informational purposes only. It does not constitute professional financial, legal, or investment advice. Please consult a qualified financial advisor for decisions." The system must not claim to provide regulated financial advice. |
| **Measurement** | UI review; automated disclaimer presence test |
| **Acceptance** | Disclaimer present on all AI-generated content; no regulated advice claims |

---

## 5. Non-Functional Requirements Summary Table

| ID | Category | Requirement | Priority | Acceptance Metric |
|---|---|---|---|---|
| NFR-001 | Performance | API response < 500ms (std), < 10s (AI) | Must Have | P95 latency |
| NFR-002 | Reliability | ≥ 99% uptime | Must Have | Monthly uptime % |
| NFR-003 | Security | bcrypt + JWT + HTTPS | Must Have | Security audit pass |
| NFR-004 | Scalability | 500 concurrent users | Should Have | Load test results |
| NFR-005 | Usability | Lighthouse ≥ 85, onboarding < 10 min | Must Have | Lighthouse score |
| NFR-006 | Accessibility | WCAG 2.1 AA | Should Have | axe audit |
| NFR-007 | Maintainability | PEP 8 + 70% test coverage | Must Have | pytest-cov report |
| NFR-008 | Privacy | No PII to Gemini | Must Have | Code review |
| NFR-009 | Portability | Docker containerized | Should Have | Docker build test |
| NFR-010 | Compliance | AI disclaimer present | Must Have | UI review |

---

## 6. System Requirements

### Backend System Requirements

| Requirement | Specification |
|---|---|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI 0.104+ |
| **ORM** | SQLAlchemy 2.0+ with Alembic for migrations |
| **Database** | SQLite (development), PostgreSQL-ready via SQLAlchemy |
| **Authentication** | python-jose for JWT, passlib[bcrypt] for password hashing |
| **AI Client** | google-generativeai SDK (Gemini 2.0 Flash) |
| **Server** | Uvicorn ASGI server |
| **Environment** | Docker + python-dotenv |

### Frontend System Requirements

| Requirement | Specification |
|---|---|
| **Framework** | React 18+ with Vite build tool |
| **Language** | JavaScript (ES2022+) |
| **Routing** | React Router v6 |
| **HTTP Client** | Axios |
| **Charts** | Recharts or Chart.js |
| **State Management** | React Context API + useState/useReducer |
| **Styling** | CSS Modules + CSS custom properties |
| **Build** | Vite with tree-shaking and code splitting |

### Infrastructure Requirements

| Component | Specification |
|---|---|
| **Backend Hosting** | Render.com / Railway (free tier) or Docker-deployed VPS |
| **Frontend Hosting** | Vercel (free tier) — vercel.app |
| **Database** | SQLite file (development), Supabase PostgreSQL (production option) |
| **Email** | SendGrid free tier or SMTP |
| **CI/CD** | GitHub Actions (on push to main) |
| **Monitoring** | UptimeRobot for uptime, Sentry for error tracking |

---

## 7. API Requirements

### API Design Principles
1. RESTful architecture following HTTP standards
2. All endpoints prefixed with `/api/v1/`
3. JSON request and response bodies
4. Standard HTTP status codes (200, 201, 400, 401, 403, 404, 422, 500)
5. All authenticated endpoints require `Authorization: Bearer <token>` header
6. Auto-documentation via FastAPI Swagger UI at `/docs`

### Core API Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/api/v1/auth/register` | No | Register new user |
| POST | `/api/v1/auth/login` | No | Login and get JWT |
| POST | `/api/v1/auth/refresh` | No | Refresh JWT token |
| GET | `/api/v1/auth/verify/{token}` | No | Email verification |
| GET | `/api/v1/users/me` | Yes | Get current user profile |
| PUT | `/api/v1/users/me` | Yes | Update user profile |
| DELETE | `/api/v1/users/me` | Yes | Delete account |
| GET | `/api/v1/loans` | Yes | List all user loans |
| POST | `/api/v1/loans` | Yes | Add new loan |
| GET | `/api/v1/loans/{id}` | Yes | Get specific loan |
| PUT | `/api/v1/loans/{id}` | Yes | Update loan |
| DELETE | `/api/v1/loans/{id}` | Yes | Delete loan |
| POST | `/api/v1/ai/analyze` | Yes | Generate AI debt analysis |
| GET | `/api/v1/ai/analysis/latest` | Yes | Get latest analysis |
| POST | `/api/v1/ai/ots/{loan_id}` | Yes | Get OTS eligibility for loan |
| POST | `/api/v1/ai/letter` | Yes | Generate OTS letter |
| GET | `/api/v1/letters` | Yes | List all generated letters |
| GET | `/api/v1/letters/{id}` | Yes | Get specific letter |
| DELETE | `/api/v1/letters/{id}` | Yes | Delete letter |
| GET | `/api/v1/dashboard` | Yes | Get dashboard summary data |

---

## 8. Constraints

### Technical Constraints

| Constraint | Description | Impact |
|---|---|---|
| Gemini API Rate Limits | Free tier: 15 requests/minute, 1M tokens/day | Rate limiting required; cached responses used |
| SQLite Concurrency | SQLite handles limited concurrent writes | Acceptable for internship project; PostgreSQL for production |
| Vercel Serverless Limits | 12-second function timeout on free tier | AI endpoints must respond within 10 seconds |
| Docker Size | Container image should be < 500MB | Optimize dependencies |

### Business Constraints

| Constraint | Description |
|---|---|
| No Regulated Financial Advice | System cannot claim to provide regulated financial advisory; AI disclaimer mandatory |
| No Banking API Integration | Cannot directly connect to banks (no SEBI license); users must manually enter loan data |
| Data Residency | User data stored within India for DPDP Act compliance (v2 goal) |
| No Minor Users | Must be 18+ to register (financial platform) |

### Project Constraints

| Constraint | Description |
|---|---|
| Timeline | 6-week internship; MVP must be completed in 4 weeks |
| Team Size | 5 developers sharing responsibilities |
| Budget | Zero cost (all free tiers: Gemini API, Vercel, Render, GitHub) |
| Technology Lock | Must use Google Cloud Generative AI (program requirement) |

---

## 9. Acceptance Criteria

### MVP Acceptance Criteria (Must pass before project submission)

| ID | Criterion | How Verified |
|---|---|---|
| AC-001 | User can register, verify email, and log in | Manual testing + automated test |
| AC-002 | User can add 3+ loans of different types | Manual testing |
| AC-003 | Dashboard correctly shows total EMI, total outstanding, DTI ratio | Manual calculation comparison |
| AC-004 | AI analysis generates within 10 seconds with all required sections | Timed testing |
| AC-005 | Debt Severity Score is between 1–10 for all test profiles | Multiple user profile tests |
| AC-006 | OTS assessment provides settlement range and prerequisites | Manual review of output quality |
| AC-007 | Generated OTS letter is professionally formatted and downloadable as PDF | Manual quality review |
| AC-008 | JWT authentication correctly protects all authenticated endpoints | 401 test for unauthenticated requests |
| AC-009 | AI disclaimer is present on all AI-generated content | UI audit |
| AC-010 | Application achieves Lighthouse score ≥ 85 | Lighthouse automated audit |
| AC-011 | Application is deployed and accessible at finrelief.vercel.app | Live URL verification |
| AC-012 | Docker build completes successfully | CI/CD pipeline |

---

*Document prepared by: Team FinRelief AI | SmartBridge Google Cloud Generative AI Internship | Vishnu Institute of Technology, Bhimavaram*
