# Project Planning
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

### Team Members & Roles

| Role | Name | Email | Responsibilities |
|---|---|---|---|
| **Team Lead + Backend** | Yeleti Joel Prasanna Kumar | 23pa1a45d0@vishnu.edu.in | Architecture, FastAPI, Financial Engine, Gemini Integration, Deployment |
| Auth + Profile | Kambala Kusuma Saisri | 23pa1a4553@vishnu.edu.in | Registration, Login, JWT, Profile pages, Auth Context |
| Dashboard + Analysis | Kusume Raju | 23pa1a4579@vishnu.edu.in | Dashboard UI, Health Score, DTI visualization, Analysis APIs |
| Settlement + Letters | Siva Manikanta Akula | akulasivamanikanta14@gmail.com | Settlement Advisor, Letter Generator, Settlement Engine |
| History + Rights + Testing | Harsha Vardhan Gorle | harshavardhanngorle@gmail.com | AI History page, Borrower Rights, QA Testing, Documentation |

---

## 1. Scope Statement

### 1.1 Project Overview

FinRelief AI is a full-stack web application that provides AI-powered debt relief and financial recovery guidance to Indian borrowers. The project will be developed over **8 weeks** as part of the SmartBridge Google Cloud Generative AI Internship.

### 1.2 In Scope

- ✅ User authentication system (register, login, JWT, profile)
- ✅ Loan portfolio management (CRUD for all loan types)
- ✅ Financial health dashboard with real-time metrics
- ✅ AI-powered settlement advisor (Gemini + fallback)
- ✅ Settlement letter generator (Gemini + fallback)
- ✅ Recovery planning module (Avalanche/Snowball/Hybrid)
- ✅ Borrower rights educational module
- ✅ AI interaction history tracking
- ✅ Responsive web design (desktop + mobile)
- ✅ Deployment on Vercel (frontend) + Render (backend)
- ✅ Docker containerization
- ✅ Complete project documentation (all phases)

### 1.3 Out of Scope

- ❌ Native mobile applications (iOS/Android)
- ❌ Real-time bank account integration (requires RBI sandbox approval)
- ❌ Payment gateway integration
- ❌ Multi-language support (Hindi, Telugu) — planned future enhancement
- ❌ SMS/Email notifications
- ❌ Credit score fetch from CIBIL (requires official API partnership)

### 1.4 Assumptions

- Team members have basic familiarity with Python and JavaScript
- Google Gemini API key will be provided via SmartBridge program
- All members have access to GitHub and development tools
- Render and Vercel free tiers will be sufficient for deployment
- SQLite is acceptable for internship-scale demo

### 1.5 Constraints

- **Time:** 8 weeks total project duration
- **Budget:** Zero monetary budget (all free tiers)
- **Team Size:** 5 members (part-time, alongside coursework)
- **API Quota:** Gemini free tier — 15 requests per minute

---

## 2. Work Breakdown Structure (WBS)

```
FinRelief AI Project
│
├── 1. Project Initiation
│   ├── 1.1 Team formation & role assignment
│   ├── 1.2 Requirement gathering
│   ├── 1.3 Technology stack finalization
│   └── 1.4 GitHub repository setup
│
├── 2. Project Design
│   ├── 2.1 Problem-Solution Fit Analysis
│   ├── 2.2 Architecture design
│   ├── 2.3 Database schema design
│   ├── 2.4 API contract definition
│   ├── 2.5 UI/UX wireframes
│   └── 2.6 Design documentation
│
├── 3. Backend Development
│   ├── 3.1 FastAPI project setup + Docker
│   ├── 3.2 Database models (SQLAlchemy)
│   ├── 3.3 Authentication system (JWT + bcrypt)
│   ├── 3.4 Loan management APIs
│   ├── 3.5 Financial Engine (DTI/Health Score)
│   ├── 3.6 Settlement Engine
│   ├── 3.7 Gemini API integration
│   ├── 3.8 Fallback AI engine
│   ├── 3.9 AI history logging
│   └── 3.10 Backend deployment (Render)
│
├── 4. Frontend Development
│   ├── 4.1 React + Vite project setup
│   ├── 4.2 Design system (CSS variables, fonts)
│   ├── 4.3 Auth components (Login, Register)
│   ├── 4.4 Auth context + Axios interceptors
│   ├── 4.5 Dashboard + Health Score visualization
│   ├── 4.6 Loan management pages
│   ├── 4.7 Settlement Advisor page
│   ├── 4.8 Letter Generator page
│   ├── 4.9 Recovery Planner page
│   ├── 4.10 Borrower Rights page
│   ├── 4.11 AI History page
│   └── 4.12 Frontend deployment (Vercel)
│
├── 5. Integration & Testing
│   ├── 5.1 Frontend-Backend API integration
│   ├── 5.2 Auth flow end-to-end testing
│   ├── 5.3 Loan CRUD testing
│   ├── 5.4 AI features testing (Gemini + fallback)
│   ├── 5.5 Cross-browser testing
│   ├── 5.6 Mobile responsiveness testing
│   └── 5.7 Performance testing
│
└── 6. Documentation & Submission
    ├── 6.1 Phase 1: Problem & Ideation docs
    ├── 6.2 Phase 2: Feasibility docs
    ├── 6.3 Phase 3: Design docs
    ├── 6.4 Phase 4: Planning docs
    ├── 6.5 Phase 5: Development docs
    └── 6.6 Final review & submission
```

---

## 3. Gantt Chart (8 Weeks)

```
WEEK  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ Owner
──────┼────┼────┼────┼────┼────┼────┼────┼────┼──────────────────────
      │ Project Initiation & Design                │
1.1 Team & Roles       │████│    │    │    │    │    │    │    │ Joel
1.2 Requirements       │████│████│    │    │    │    │    │    │ All
1.3 Architecture       │    │████│████│    │    │    │    │    │ Joel
1.4 GitHub Setup       │████│    │    │    │    │    │    │    │ Joel
1.5 DB Schema Design   │    │████│    │    │    │    │    │    │ Joel
1.6 API Contract       │    │████│    │    │    │    │    │    │ Joel
1.7 UI Wireframes      │    │████│████│    │    │    │    │    │ Raju
──────┼────┼────┼────┼────┼────┼────┼────┼────┼──────────────────────
      │ Backend Development                        │
2.1 FastAPI Setup      │    │    │████│    │    │    │    │    │ Joel
2.2 SQLAlchemy Models  │    │    │████│    │    │    │    │    │ Joel
2.3 JWT Auth APIs      │    │    │████│████│    │    │    │    │ Joel+Saisri
2.4 Loan CRUD APIs     │    │    │    │████│    │    │    │    │ Joel
2.5 Financial Engine   │    │    │    │████│    │    │    │    │ Joel
2.6 Settlement Engine  │    │    │    │████│████│    │    │    │ Siva
2.7 Gemini Integration │    │    │    │    │████│    │    │    │ Joel
2.8 Fallback Engine    │    │    │    │    │████│    │    │    │ Joel
2.9 Backend Deploy     │    │    │    │    │    │████│    │    │ Joel
──────┼────┼────┼────┼────┼────┼────┼────┼────┼──────────────────────
      │ Frontend Development                       │
3.1 React+Vite Setup   │    │    │████│    │    │    │    │    │ Raju
3.2 Design System CSS  │    │    │████│████│    │    │    │    │ Saisri
3.3 Auth Pages         │    │    │    │████│    │    │    │    │ Saisri
3.4 Auth Context       │    │    │    │████│    │    │    │    │ Saisri
3.5 Dashboard UI       │    │    │    │    │████│    │    │    │ Raju
3.6 Loan Pages         │    │    │    │████│████│    │    │    │ Raju
3.7 Settlement Page    │    │    │    │    │████│████│    │    │ Siva
3.8 Letter Page        │    │    │    │    │    │████│    │    │ Siva
3.9 Recovery Planner   │    │    │    │    │    │████│████│    │ Harsha
3.10 Rights Module     │    │    │    │    │    │    │████│    │ Harsha
3.11 AI History Page   │    │    │    │    │    │    │████│    │ Harsha
3.12 Frontend Deploy   │    │    │    │    │    │    │████│    │ Joel
──────┼────┼────┼────┼────┼────┼────┼────┼────┼──────────────────────
      │ Testing & Documentation                    │
4.1 Integration Testing│    │    │    │    │    │████│████│    │ All
4.2 Bug Fixes          │    │    │    │    │    │    │████│    │ All
4.3 Documentation      │    │████│████│████│████│████│████│████│ All
4.4 Final Review       │    │    │    │    │    │    │    │████│ All
4.5 Submission         │    │    │    │    │    │    │    │████│ Joel
──────┴────┴────┴────┴────┴────┴────┴────┴────┴──────────────────────
WEEK:   1    2    3    4    5    6    7    8
```

---

## 4. Team Roles & Responsibility Matrix (RACI)

### 4.1 Detailed Role Descriptions

#### Joel Prasanna Kumar — Team Lead + Backend Architecture
- **Primary Responsibilities:**
  - Overall project architecture and technical decisions
  - FastAPI backend development and all API endpoints
  - SQLAlchemy database models and migrations
  - Financial Engine (DTI, Health Score, calculations)
  - Google Gemini 2.0 Flash integration
  - Fallback AI engine
  - Docker containerization
  - Render backend deployment
  - Vercel frontend deployment
  - Code reviews and merge management
  - Final submission coordination

#### Kambala Kusuma Saisri — Authentication & Profile Pages
- **Primary Responsibilities:**
  - Registration and Login page UI (React)
  - Form validation and error handling
  - React AuthContext (global auth state)
  - Axios request interceptors for JWT
  - User profile page (view + edit)
  - Protected route implementation
  - Password strength indicator component
  - Account settings page

#### Kusume Raju — Dashboard & Analysis
- **Primary Responsibilities:**
  - Financial Health Dashboard page
  - Health Score Ring visualization (CSS + SVG)
  - Metric Cards (DTI, Total Debt, EMI Burden, Surplus)
  - Loan list display with status badges
  - Recharts integration (bar charts, pie charts)
  - React + Vite project setup and configuration
  - Responsive layout design
  - Loading skeleton components

#### Siva Manikanta Akula — Settlement & Letters
- **Primary Responsibilities:**
  - Settlement Advisor page (loan selection, advice display)
  - Settlement Engine (Python — percentage calculation logic)
  - Letter Generator page (type selector, generated letter display)
  - Copy and download functionality for letters
  - Letter type explanation components
  - Settlement factor visualization
  - API integration for settlement and letter endpoints

#### Harsha Vardhan Gorle — History, Rights & Testing
- **Primary Responsibilities:**
  - AI History page (list, filter, replay)
  - Borrower Rights module (accordion, content sections)
  - End-to-end testing (all user flows)
  - Cross-browser testing (Chrome, Firefox, Edge)
  - Mobile responsiveness testing
  - Bug documentation and reporting
  - Documentation compilation and review

### 4.2 RACI Matrix

| Task | Joel | Saisri | Raju | Siva | Harsha |
|---|---|---|---|---|---|
| Architecture Design | **R/A** | C | C | C | C |
| Backend APIs | **R/A** | I | I | C | I |
| JWT Auth | **A** | **R** | I | I | I |
| Login/Register UI | C | **R/A** | I | I | I |
| Dashboard UI | C | C | **R/A** | I | I |
| Settlement Engine | **A** | I | I | **R** | I |
| Settlement Page | C | I | I | **R/A** | I |
| Letter Generator | C | I | I | **R/A** | I |
| Recovery Planner | **A** | I | C | I | **R** |
| Rights Module | C | I | I | I | **R/A** |
| AI History | **A** | I | I | I | **R** |
| Gemini Integration | **R/A** | I | I | C | I |
| Testing | A | C | C | C | **R** |
| Documentation | A | C | C | C | **R** |
| Deployment | **R/A** | I | I | I | I |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

---

## 5. Milestones

| # | Milestone | Target Date | Success Criteria | Owner |
|---|---|---|---|---|
| M1 | **Project Kickoff** | End of Week 1 | All roles assigned, repo created, tech stack confirmed | Joel |
| M2 | **Architecture Finalized** | End of Week 2 | DB schema, API contracts, wireframes approved by team | Joel |
| M3 | **Backend Core Done** | End of Week 4 | Auth APIs + Loan CRUD working + DB seeded | Joel + Saisri |
| M4 | **AI Engine Integrated** | End of Week 5 | Gemini + Fallback returning valid responses | Joel |
| M5 | **Frontend Alpha** | End of Week 6 | All pages built, basic API integration | All |
| M6 | **Full Integration** | End of Week 7 | All features working end-to-end on deployed URLs | All |
| M7 | **Project Submission** | End of Week 8 | All docs complete, GitHub README done, live demo working | All |

---

## 6. Risk Register

| # | Risk | Probability | Impact | Severity | Mitigation | Contingency |
|---|---|---|---|---|---|---|
| R1 | **Gemini API quota exceeded** | High | High | 🔴 Critical | Build fallback engine from Week 5 | Deploy fallback; label responses transparently |
| R2 | **Render backend cold starts** | High | Medium | 🟠 High | Implement keep-alive ping; optimize startup | Use Render paid tier if demo critical |
| R3 | **Team member unavailability** | Medium | High | 🟠 High | Cross-train on each other's modules; document all code | Redistribute tasks to available members |
| R4 | **Scope creep (new features)** | Medium | Medium | 🟡 Medium | Strict WBS adherence; change control via GitHub Issues | Defer to Phase 2 roadmap |
| R5 | **Frontend-Backend CORS issues** | Low | Medium | 🟡 Medium | Configure CORS in Week 3; test early | Use proxy in development; fix origin list |
| R6 | **SQLite data loss on Render redeploy** | High | Low | 🟡 Medium | Document that DB resets on redeploy; use seeding script | Migrate to persistent volume or PostgreSQL |

---

## 7. Resources

### 7.1 Human Resources

| Resource | Availability | Skills Applied |
|---|---|---|
| Yeleti Joel Prasanna Kumar | ~20 hrs/week | Python, FastAPI, React, Gemini API, Docker |
| Kambala Kusuma Saisri | ~15 hrs/week | React, JavaScript, CSS |
| Kusume Raju | ~15 hrs/week | React, JavaScript, Data visualization |
| Siva Manikanta Akula | ~15 hrs/week | Python, React, API integration |
| Harsha Vardhan Gorle | ~15 hrs/week | Testing, Documentation, React |

### 7.2 Technology Resources (All Free Tier)

| Resource | Tool | Cost |
|---|---|---|
| Frontend Hosting | Vercel Free Tier | ₹0 |
| Backend Hosting | Render Free Tier | ₹0 |
| AI Engine | Google Gemini API (Free Tier) | ₹0 |
| Version Control | GitHub (Public Repo) | ₹0 |
| Database | SQLite (file-based) | ₹0 |
| IDE | VS Code | ₹0 |
| Design Reference | Figma (Free) | ₹0 |

### 7.3 Knowledge Resources

- Google AI for Developers documentation
- FastAPI official documentation
- React + Vite documentation
- SQLAlchemy 2.0 documentation
- RBI publications (Fair Practice Code, SARFAESI guidelines)

---

## 8. Communication Plan

### 8.1 Meeting Schedule

| Meeting Type | Frequency | Platform | Participants | Duration |
|---|---|---|---|---|
| Sprint Planning | Every 2 weeks (start) | Google Meet | All 5 | 1 hour |
| Daily Standup | Daily (async) | WhatsApp Group | All 5 | 5 min |
| Sprint Review | Every 2 weeks (end) | Google Meet | All 5 | 30 min |
| Pair Programming | As needed | Google Meet + VS Code Live Share | 2 members | Variable |
| Mentor Check-in | Weekly | SmartBridge platform | All 5 + Mentor | 30 min |

### 8.2 Communication Channels

| Channel | Purpose | Response Time |
|---|---|---|
| WhatsApp Group "FinRelief Dev" | Daily coordination, quick questions | Within 2 hours |
| GitHub Issues | Bug reports, feature requests, task tracking | Within 24 hours |
| GitHub Pull Requests | Code reviews, merge requests | Within 48 hours |
| Google Meet | Scheduled meetings, pair programming | Per schedule |
| Email | Formal communications, mentor updates | Within 24 hours |

### 8.3 Escalation Path

```
Team Member Issue
    │
    ▼ (1st: WhatsApp Group)
Team Discussion
    │
    ▼ (2nd: If unresolved — 24 hours)
Team Lead (Joel) Decision
    │
    ▼ (3rd: If unresolved — 48 hours)
SmartBridge Mentor
    │
    ▼ (4th: Critical issues)
Program Coordinator
```

### 8.4 Documentation Standards

- All code to be documented with docstrings (Python) / JSDoc (JavaScript)
- README.md updated with every major feature addition
- GitHub commits: Conventional commit format (`feat:`, `fix:`, `docs:`, `test:`)
- All design decisions documented in GitHub Wiki

---

## 9. Quality Assurance Plan

### 9.1 Code Quality

- Backend: PEP 8 compliance (enforced via `flake8`)
- Frontend: ESLint with React recommended rules
- All functions documented with docstrings/JSDoc
- Code review required for all PRs (minimum 1 reviewer)

### 9.2 Testing Strategy

| Test Type | Tool | Coverage Target |
|---|---|---|
| Manual Testing | Browser + Postman | All 18 features |
| API Testing | Postman collection | All 25 endpoints |
| Cross-browser | Chrome, Firefox, Edge | 3 browsers |
| Mobile Testing | DevTools responsive mode | 320px – 1440px |
| AI Testing | Mock responses + real Gemini calls | Settlement, Letter, Recovery |

---

*Document Version: 1.0 | Created: July 2026 | FinRelief AI Team — Vishnu Institute of Technology, Bhimavaram*
