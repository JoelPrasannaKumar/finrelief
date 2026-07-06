# Team Involvement in Demonstration
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
| **Document Type** | Team Involvement & Contribution Report |
| **Date** | July 2026 |

---

## Table of Contents

1. [Team Member Profiles & Contributions](#1-team-member-profiles--contributions)
2. [Individual Contribution Percentage Table](#2-individual-contribution-percentage-table)
3. [Skills Demonstrated by Each Member](#3-skills-demonstrated-by-each-member)
4. [Learning Outcomes](#4-learning-outcomes)
5. [Team Dynamics & Collaboration](#5-team-dynamics--collaboration)
6. [Acknowledgements](#6-acknowledgements)

---

## 1. Team Member Profiles & Contributions

---

### 👨‍💻 Yeleti Joel Prasanna Kumar — Team Lead & Backend Developer

**Roll Number:** 23PA1A45D0  
**Email:** 23pa1a45d0@vishnu.edu.in  
**Role:** Team Lead, Backend Architect, AI Integration Engineer, DevOps  
**GitHub:** Primary repository owner and administrator

#### Technical Contributions

**Architecture Design:**
Joel designed the complete system architecture for FinRelief AI — the three-tier decoupled structure with React frontend, FastAPI backend, and SQLite/PostgreSQL data layer. He made all key technology choices: FastAPI over Django/Flask (for auto-documentation and async support), SQLAlchemy ORM (for security and flexibility), JWT HS256 authentication (for stateless scalability), and Google Gemini 2.0 Flash (for speed-accuracy balance). The architectural decisions proved correct — the application scales cleanly and the tech stack choices were praised by the SmartBridge mentor.

**Backend Development — All 7 API Modules:**

| API Module | File | Endpoints | Description |
|---|---|---|---|
| Authentication | `app/api/auth.py` | `/register`, `/login` | User registration with bcrypt hashing, JWT token issuance |
| Users | `app/api/users.py` | `GET /me`, `PUT /me` | Profile retrieval and update |
| Loans | `app/api/loans.py` | Full CRUD (5 endpoints) | Loan portfolio management with ownership authorization |
| Analysis | `app/api/analysis.py` | `GET /analysis/` | Financial metrics computation via Financial Engine |
| Settlement | `app/api/settlement.py` | `POST /generate`, `GET /history` | AI settlement plan generation with Gemini |
| Letters | `app/api/letters.py` | `POST /generate`, `GET /` | AI letter generation for lender correspondence |
| History | `app/api/history.py` | `GET /` | Action log retrieval |

**Financial Engine (`app/financial/engine.py`):**
Joel authored the entire financial calculation engine, implementing:
- Standard EMI formula: `P × r × (1+r)^n / ((1+r)^n - 1)`
- Debt-to-Income ratio computation with divide-by-zero guard.
- **Recovery Score algorithm** — a proprietary metric designed collaboratively with the team, implemented by Joel.
- Total interest calculation, estimated payoff date computation.

**AI Integration (`app/api/settlement.py`, `app/api/letters.py`):**
Joel designed and implemented the prompt engineering strategy for both the Settlement Engine and Letter Generator. Key innovations:
- **Pre-computation before AI:** Financial Engine calculates all numerical metrics first; Gemini receives verified numbers, not raw data.
- **Structured prompt templates** with role definition, data injection, output format specification, and constraint clauses.
- **Safety settings** configuration to prevent over-blocking of financial content.

**Settlement Engine (`app/settlement/engine.py`):**
Implemented the Debt Snowball (ascending balance sort) and Debt Avalanche (descending interest rate sort) algorithms, plus the auto-recommendation logic based on Recovery Score threshold.

**Authentication Security:**
- bcrypt password hashing with cost factor 12.
- JWT token creation and validation utilities.
- FastAPI dependency `get_current_user` protecting all secured routes.
- Ownership authorization checks on loan and letter endpoints.

**Deployment:**
- **Backend:** Deployed to Render.com using Docker container. Configured environment variables, CORS settings, and root_path for reverse proxy compatibility.
- **Frontend:** Deployed to Vercel with automatic CI/CD from GitHub main branch.
- **Docker:** Created `Dockerfile` for both backend and frontend, and `docker-compose.yml` for local orchestration.

**Testing:**
- Architected the Pytest test suite structure.
- Wrote 12 of the 20 unit tests (auth, financial engine, settlement engine, API behavior).
- Fixed BUG-001 (critical auth bug), BUG-002 (authorization bypass), BUG-005 (NaN in DTI), BUG-009 (Swagger root_path).

**Demo Role:**
- **Scene 1:** Project introduction, problem statement, live URL demonstration.
- **Scene 6:** Conclusion, architecture overview, scalability roadmap.
- **Q&A:** Primary technical respondent for architecture, AI, and security questions.

---

### 👩‍💻 Kambala Kusuma Saisri — Frontend Developer (Auth & Design)

**Roll Number:** 23PA1A4553  
**Email:** 23pa1a4553@vishnu.edu.in  
**Role:** Frontend Developer, UI/UX Designer, CSS Design System Architect

#### Technical Contributions

**Login Page (`src/pages/Login.jsx`):**
Kusuma Saisri built the complete login page, including:
- Controlled React form with email and password fields.
- Real-time form validation: empty field detection, email format validation.
- Error state handling with descriptive error messages displayed below each field.
- "Show/Hide password" toggle functionality.
- JWT token storage in `localStorage` on successful login.
- Redirect to `/dashboard` after successful authentication.
- Loading state on the submit button during API call.

**Register Page (`src/pages/Register.jsx`):**
- Registration form with: Full Name, Email, Password, Confirm Password.
- Password strength indicator (Weak / Moderate / Strong) with visual bar.
- Password match validation.
- Password complexity requirements displayed dynamically.
- Auto-focus management for form accessibility.
- Error display for API errors (e.g., "Email already in use").

**Profile Page (`src/pages/Profile.jsx`):**
- Displays current user information fetched from `GET /api/users/me`.
- Editable fields: Full Name, Monthly Income.
- Email displayed as read-only (non-editable for security).
- Save Changes button with loading state and success toast notification.
- Updates propagate to Dashboard metrics in real-time via Context refresh.

**CSS Design System:**
Perhaps Kusuma Saisri's most impactful contribution — she designed the entire CSS custom property system that gives FinRelief AI its consistent visual identity:

```css
:root {
  --bg-primary: #0f172a;      /* Deep navy — main background */
  --bg-secondary: #1e293b;    /* Slightly lighter — card backgrounds */
  --bg-tertiary: #334155;     /* Lightest — hover states, borders */
  --accent-blue: #3b82f6;     /* Primary action color */
  --accent-green: #10b981;    /* Positive metrics, success */
  --accent-red: #ef4444;      /* Warnings, high debt indicators */
  --accent-orange: #f59e0b;   /* Moderate concern indicators */
  --text-primary: #f8fafc;    /* Main body text */
  --text-secondary: #94a3b8;  /* Subdued labels, hints */
  --border-color: #334155;    /* Subtle borders */
  --shadow-card: 0 4px 24px rgba(0,0,0,0.3); /* Depth for cards */
}
```

This system ensured visual consistency across all 8 pages built by different team members.

**Toast Notification System:**
Kusuma Saisri built the reusable `<Toast>` component used across the application for:
- "Profile updated successfully" (success)
- "Copied!" (when letter is copied to clipboard)
- "Loan added" / "Loan deleted" (feedback)
- Error toasts for API failures.

The component uses CSS animations for slide-in/slide-out effects.

**Mobile Responsiveness Audit:**
During Week 6, conducted a systematic mobile responsiveness review across all 8 pages, identifying and fixing 5 layout issues (sidebar overflow, card wrapping on 375px viewport, font size on metric cards).

**Demo Role:**
- **Scene 2:** Dashboard overview presentation.
- **Timekeeper:** Manages time signals for all scenes.
- **Moderator:** Facilitates Q&A session management.

---

### 👨‍💻 Kusume Raju — Frontend Developer (Dashboard & Charts)

**Roll Number:** 23PA1A4579  
**Email:** 23pa1a4579@vishnu.edu.in  
**Role:** Frontend Developer, Data Visualization Engineer

#### Technical Contributions

**Dashboard Page (`src/pages/Dashboard.jsx`):**
Built the primary user landing experience after login:
- **Metric Cards Component:** Four cards displaying Total Debt, Monthly EMI, DTI Ratio, Recovery Score. Each card uses color-coded theming based on metric severity (green/orange/red thresholds).
- **Recovery Score Progress Bar:** Custom CSS-animated progress bar from 0–100 with dynamic fill color based on score range.
- **Loan Table:** Tabular display of all user loans with columns for lender, type, outstanding balance, interest rate, and action buttons (Edit, Delete, Letter).
- **Empty State:** Illustration and CTA "Add Your First Loan" displayed when user has no loans.
- **Add Loan Modal:** Inline modal form triggered by the "Add Loan" button. Full form with all loan fields, validation, and API submission.
- **Edit Loan Modal:** Pre-populated with existing loan data, allows update.
- **Delete Confirmation Dialog:** Confirmation before irreversible deletion.

**Analysis Page (`src/pages/Analysis.jsx`):**
The most visually complex page in the application:

**Recharts Integration:**
```jsx
// Donut Pie Chart — Debt by Type
<ResponsiveContainer width="100%" height={300}>
  <PieChart>
    <Pie data={debtByType} cx="50%" cy="50%" innerRadius={60} outerRadius={110}
         dataKey="value" label={({name, percent}) => `${name}: ${(percent*100).toFixed(0)}%`}>
      {debtByType.map((entry, index) => (
        <Cell key={index} fill={COLORS[index % COLORS.length]} />
      ))}
    </Pie>
    <Tooltip formatter={(value) => `₹${value.toLocaleString('en-IN')}`} />
    <Legend />
  </PieChart>
</ResponsiveContainer>

// Bar Chart — EMI vs Income
<ResponsiveContainer width="100%" height={300}>
  <BarChart data={emiData}>
    <XAxis dataKey="lender" />
    <YAxis tickFormatter={(v) => `₹${(v/1000).toFixed(0)}k`} />
    <Tooltip formatter={(v) => `₹${v.toLocaleString('en-IN')}`} />
    <Bar dataKey="emi" fill="#3b82f6" name="Monthly EMI" />
    <ReferenceLine y={monthlyIncome} stroke="#10b981" strokeDasharray="3 3" label="Income" />
  </BarChart>
</ResponsiveContainer>
```

**Loan Breakdown Table:** Detailed per-loan analysis table showing outstanding balance, interest rate, total interest remaining (calculated from backend), estimated payoff date, and burden percentage.

**Sidebar Navigation Component:** Kusume Raju also built the sidebar navigation component (`src/components/Sidebar.jsx`) that is shared across all pages — collapsible on mobile, with active route highlighting using React Router's `useLocation`.

**Axios API Client:**
Co-built the API client module (`src/api/client.js`) with Siva Manikanta — specifically handled the Axios interceptor that automatically attaches JWT token to every request:
```javascript
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem('finrelief_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

**Demo Role:**
- **Scene 3:** Add Loan demonstration and Analysis page walkthrough.
- **Backup technical support:** Has local full-stack running as contingency.

---

### 👨‍💻 Siva Manikanta Akula — Frontend Developer (AI Features)

**Email:** akulasivamanikanta14@gmail.com  
**Role:** Frontend Developer, API Client Architect, AI Feature UI Developer

#### Technical Contributions

**Settlement Page (`src/pages/Settlement.jsx`):**
The most AI-intensive page in the frontend:

- **Strategy Toggle:** Custom toggle component switching between Snowball and Avalanche modes with explanatory tooltips for each ("Pay off smallest balance first" vs. "Pay off highest interest rate first").
- **Auto-Recommendation Banner:** Displays the system-recommended strategy based on Recovery Score, with explanation (e.g., "Based on your Recovery Score of 72, we recommend Avalanche — the mathematical optimum for your profile").
- **Generate Plan Button:** Disabled when no loans exist; shows loading spinner and text "FinRelief AI is analyzing your portfolio..." during API call (typically 3–4 seconds).
- **Plan Display Component:** Renders the AI-generated plan as formatted monthly milestone cards. Each card shows: Month number, target loan, payment breakdown (minimum + extra), projected balance after payment, and a milestone badge.
- **Plan History:** Shows previously generated plans in a collapsible history section.

**Letters Page (`src/pages/Letters.jsx`):**

- **Letter Type Selector:** Dropdown with three options: Hardship Letter, Settlement Offer Letter, Payment Plan Request Letter. Each has a brief description of when to use it.
- **Loan Selector:** Dropdown populated with user's active loans.
- **Generate Letter Button:** Loading state with spinner during API call.
- **Letter Display:** AI-generated letter displayed in a styled card with formal document aesthetic (monospace-leaning font, proper spacing, letterhead area).
- **Copy to Clipboard:** Button that copies full letter text. On success, shows toast "Copied! Ready to paste into email."
- **Letter History:** Optional toggle to show previously generated letters.

**Axios API Client (`src/api/client.js`):**
Siva Manikanta was primarily responsible for designing and implementing the complete API client module:

```javascript
// Full API client with all 7 endpoint groups
export const authAPI = {
  register: (data) => axiosInstance.post('/auth/register', data),
  login: (data) => axiosInstance.post('/auth/login', data),
};

export const loansAPI = {
  getAll: () => axiosInstance.get('/loans/'),
  create: (data) => axiosInstance.post('/loans/', data),
  update: (id, data) => axiosInstance.put(`/loans/${id}`, data),
  delete: (id) => axiosInstance.delete(`/loans/${id}`),
};

export const settlementAPI = {
  generate: (strategy) => axiosInstance.post('/settlement/generate', { strategy }),
  getHistory: () => axiosInstance.get('/settlement/history'),
};

export const lettersAPI = {
  generate: (data) => axiosInstance.post('/letters/generate', data),
  getAll: () => axiosInstance.get('/letters/'),
};
// ... analysisAPI, usersAPI, historyAPI
```

This centralized API client was used by all team members' components — a key infrastructure contribution.

**Error Handling & Loading States:**
Siva Manikanta implemented consistent loading state and error state patterns used across all AI feature pages:
- Spinner component during API calls.
- Error message cards for API failures.
- Empty state components when no data exists.

**Demo Role:**
- **Scene 4:** AI Settlement Engine demonstration — the highest-impact demo scene.
- **Technical support:** Manages screen sharing, browser tabs during full demo.

---

### 👨‍💻 Harsha Vardhan Gorle — Frontend Developer & QA Engineer

**Email:** harshavardhanngorle@gmail.com  
**Role:** Frontend Developer, Quality Assurance Lead, Testing Engineer

#### Technical Contributions

**History Page (`src/pages/History.jsx`):**

- **Timeline Component:** Chronological action log displayed as a vertical timeline with colored dot indicators.
- **Action Type Icons:** Different icons for LOAN_ADDED (➕), PLAN_GENERATED (🤖), LETTER_CREATED (✉️), LOAN_UPDATED (✏️), LOAN_DELETED (🗑️).
- **Relative Timestamps:** "2 minutes ago," "3 hours ago," "Yesterday" format using date-fns library.
- **Empty State:** "No actions recorded yet — start by adding a loan!" with illustrated empty state.
- **BUG-007 Fix:** Identified and fixed the React StrictMode double-invoke bug causing duplicate history entries.

**Borrower Rights Page (`src/pages/BorrowerRights.jsx`):**

- **Accordion Component:** Custom accordion (expand/collapse) for each rights category.
- **Rights Categories:**
  - Rights During Loan Collection (RBI Fair Practices Code)
  - SARFAESI Act Protections (secured loan holders)
  - DRT/NCLT Recourse (legal remedies)
  - What Lenders CANNOT Do (prohibited practices)
  - Useful Contacts (Banking Ombudsman, RBI helpline)
- **Search Functionality:** Basic text search through rights content.

**Quality Assurance — Testing:**

Harsha Vardhan was the team's primary QA engineer and authored the comprehensive testing documentation.

**Unit Tests Authored (8 of 20):**
- UT-001, UT-002, UT-003: Password hashing and verification tests.
- UT-008, UT-009: EMI and interest calculation accuracy tests.
- UT-013, UT-014: Snowball and Avalanche sort order verification.
- UT-020: Login with non-existent user test.

**Bug Discovery Record:**
Harsha Vardhan discovered or first reported 5 of the 9 bugs fixed during development:
- BUG-001 (auth failure — discovered during Week 3 integration testing)
- BUG-003 (avalanche sort reversed — discovered during unit testing)
- BUG-006 (clipboard in Firefox — discovered during browser compatibility testing)
- BUG-007 (duplicate history — discovered during UI testing)
- BUG-008 (dark mode text — discovered during visual audit)

**Browser Compatibility Testing:**
Conducted systematic testing across Chrome, Firefox, Edge, and Safari, documenting results in the testing report.

**API Testing:**
Ran the complete Postman collection against the live API, verifying all 19 endpoints.

**Demo Role:**
- **Scene 5:** Letter Generator and Borrower Rights page demonstration.
- **Backup presenter** for any absent team member.

---

## 2. Individual Contribution Percentage Table

### 2.1 Overall Project Contribution

| Member | Backend | Frontend | AI/Prompts | Testing | Deployment | Documentation | Overall % |
|---|---|---|---|---|---|---|---|
| Yeleti Joel | 95% | 5% | 70% | 20% | 95% | 25% | **38%** |
| Kusuma Saisri | 0% | 22% | 5% | 10% | 0% | 15% | **13%** |
| Kusume Raju | 0% | 28% | 5% | 10% | 0% | 15% | **14%** |
| Siva Manikanta | 5% | 25% | 15% | 10% | 5% | 20% | **14%** |
| Harsha Vardhan | 0% | 20% | 5% | 50% | 0% | 25% | **16%** |

> Note: Percentages reflect domain-specific contribution; "Overall %" weights each domain by project complexity and time investment.

### 2.2 GitHub Commit Distribution

```
Total Commits: 199

Joel:          ████████████████████████████████████  87 (44%)
Kusuma Saisri: ████████████████                      34 (17%)
Kusume Raju:   █████████████                         28 (14%)
Siva Manikanta: ████████████████                     31 (16%)
Harsha Vardhan: █████████                            19 (10%)
```

### 2.3 Lines of Code by Member (Approximate)

| Member | Backend LOC | Frontend LOC | Test LOC | Total |
|---|---|---|---|---|
| Joel | ~1,800 | ~200 | ~350 | **~2,350** |
| Kusuma Saisri | 0 | ~850 | ~50 | **~900** |
| Kusume Raju | 0 | ~950 | ~30 | **~980** |
| Siva Manikanta | ~150 | ~820 | ~40 | **~1,010** |
| Harsha Vardhan | 0 | ~550 | ~280 | **~830** |
| **Total** | **~1,950** | **~3,370** | **~750** | **~6,070** |

---

## 3. Skills Demonstrated by Each Member

### Joel — Skills Demonstrated

| Skill | Evidence |
|---|---|
| Python / FastAPI | Complete backend with 7 API modules, middleware, dependency injection |
| SQLAlchemy ORM | Model definitions, relationships, CRUD operations, migration with Alembic |
| JWT Authentication | Token creation, validation, expiry, refresh mechanism |
| bcrypt Security | Password hashing, verification, cost factor configuration |
| Google Gemini API | SDK integration, prompt engineering, safety settings, structured output |
| Docker / Docker Compose | Backend Dockerfile, frontend Dockerfile, docker-compose.yml |
| Cloud Deployment | Render.com backend, Vercel frontend, environment variable management |
| API Design | RESTful principles, HTTP status codes, Swagger auto-documentation |
| Pytest | Unit and integration test suite, coverage reporting |

### Kusuma Saisri — Skills Demonstrated

| Skill | Evidence |
|---|---|
| React 18 (Hooks) | Login, Register, Profile pages with useState, useEffect, useContext |
| CSS Custom Properties | Design system with 12+ CSS variables used across all pages |
| Form Validation | Real-time validation, error state management, accessibility |
| CSS Animation | Toast slide-in/out, password strength bar animation |
| UX Design | Figma wireframes, design-implementation fidelity |
| Mobile Responsiveness | CSS Grid/Flexbox responsive layouts, viewport-based breakpoints |
| Git Collaboration | PR reviews, branch management, conflict resolution |

### Kusume Raju — Skills Demonstrated

| Skill | Evidence |
|---|---|
| Recharts | Pie chart, bar chart, reference lines, tooltips, responsive containers |
| React Data Fetching | useEffect, Axios, loading/error/success state management |
| Data Visualization | Chart selection, color encoding, accessible labels |
| React Router v6 | Navigation, active route detection, protected routes |
| Axios Interceptors | JWT auto-attachment in request interceptor |
| Component Architecture | Reusable Sidebar, Metric Card, Loan Table components |

### Siva Manikanta — Skills Demonstrated

| Skill | Evidence |
|---|---|
| API Client Design | Centralized Axios client with all 7 API endpoint groups |
| React Async Patterns | Loading states, error boundaries, optimistic UI updates |
| AI Feature UI | Settlement toggle, loading animation, plan display, letter display |
| JavaScript ES6+ | Async/await, destructuring, template literals, optional chaining |
| Error Handling | Try/catch patterns, error message propagation to UI |
| Docker (Basic) | Docker Compose setup assistance |

### Harsha Vardhan — Skills Demonstrated

| Skill | Evidence |
|---|---|
| Pytest | Unit test case design, fixtures, assertions, coverage reporting |
| API Testing | Postman collection, curl commands, status code validation |
| Bug Reporting | Structured bug reports with reproduction steps and root cause analysis |
| Browser Compatibility Testing | Cross-browser testing methodology |
| React (Intermediate) | History timeline, accordion, search functionality |
| QA Methodology | Test case design, regression testing, severity classification |

---

## 4. Learning Outcomes

### 4.1 Technical Learnings

| Member | Key Technical Learning |
|---|---|
| **Joel** | Prompt engineering is as much a technical skill as coding — the quality difference between a naive prompt and an engineered prompt is dramatic. Google Gemini's structured output feature enables reliable UI rendering of AI-generated content. |
| **Kusuma Saisri** | CSS custom properties (design tokens) are the most maintainable way to implement a design system — updating the primary color across 8 pages takes 1 line of code. |
| **Kusume Raju** | Recharts' `ResponsiveContainer` is essential for mobile-compatible charts. Data visualization is an art — the same data presented differently can be intuitive or confusing. |
| **Siva Manikanta** | A centralized Axios client with interceptors eliminates repetitive auth header code across 50+ API calls. Loading and error states are as important as the success state. |
| **Harsha Vardhan** | Testing is not a phase — it's a continuous activity. Bugs found during development are 10× cheaper to fix than bugs found during demo. React StrictMode's double-invoke behavior is a common source of subtle bugs. |

### 4.2 Soft Skill Learnings

| Member | Key Soft Skill Learning |
|---|---|
| **Joel** | Leading a team means unblocking others — the most important thing I did wasn't writing code, it was responding to questions quickly so my teammates could keep moving. |
| **Kusuma Saisri** | Design decisions need justification — when I proposed the dark theme, I prepared a rationale about eye strain for evening users. Having reasons matters. |
| **Kusume Raju** | "Done is better than perfect" — shipping a working chart that looked 80% of my vision was more valuable than spending 3 more days perfecting the 100% vision. |
| **Siva Manikanta** | Communication > code — when I was blocked, asking in the WhatsApp group immediately got me help. Staying silent on a blocker wastes everyone's time. |
| **Harsha Vardhan** | Reporting bugs constructively (with reproduction steps, screenshots, severity) makes fixing them much faster than just saying "it doesn't work." |

### 4.3 Industry Knowledge Gained

- **Gemini AI Studio:** All team members gained practical experience with Google AI Studio for prompt experimentation.
- **Cloud Deployment:** Joel's deployment walkthroughs gave the team real understanding of Vercel, Render.com, and Docker.
- **API Documentation:** The team understands how Swagger/OpenAPI documentation works and why it matters.
- **Agile-ish Development:** Weekly sprints, GitHub Issues for task tracking, and PR reviews gave the team experience with modern software development workflows.
- **Financial Domain Knowledge:** All members gained understanding of DTI ratios, EMI formulas, debt settlement strategies, and Indian banking regulations.

---

## 5. Team Dynamics & Collaboration

### 5.1 Team Composition Assessment

The team composition worked extremely well — Joel's deep technical leadership on the backend freed the four frontend members to focus on their respective UI modules without backend concerns. The clear module ownership (each member owns specific pages) prevented conflicts while the shared design system (Kusuma Saisri) and shared API client (Siva Manikanta) ensured cohesion.

### 5.2 Communication Quality

**Strengths:**
- Rapid response on WhatsApp (typically within 30 minutes during waking hours).
- All team members attended 7 of 8 weekly meetings fully; attendance was 96% overall.
- Code review culture was established early and maintained throughout.
- No significant interpersonal conflicts reported.

**Areas for Growth:**
- Kusume Raju's one late attendance (Week 6) highlighted the need for earlier notification when scheduling conflicts arise.
- Documentation writing was consistently the least preferred task — better incentivization and clearer ownership earlier in the project would have helped.

### 5.3 Peer Evaluations (Anonymous Ratings, 1–5 Scale)

| Member | Technical Contribution | Communication | Reliability | Team Spirit | Avg |
|---|---|---|---|---|---|
| Joel | 5.0 | 4.8 | 5.0 | 4.8 | **4.9** |
| Kusuma Saisri | 4.5 | 5.0 | 4.8 | 5.0 | **4.8** |
| Kusume Raju | 4.5 | 4.3 | 4.5 | 4.8 | **4.5** |
| Siva Manikanta | 4.8 | 4.5 | 4.8 | 4.8 | **4.7** |
| Harsha Vardhan | 4.3 | 4.5 | 4.8 | 5.0 | **4.7** |

> *Ratings submitted by the four other team members for each person (average of 4 ratings).*

### 5.4 Most Memorable Team Moments

1. **The First Gemini Response** (Week 5): When the settlement plan API first returned a real, coherent, data-specific plan from Gemini, the team collectively celebrated in the WhatsApp group with a flood of emoji. This was the moment the project felt "real."

2. **The Live Deployment Moment** (Week 7): When https://finrelief.vercel.app loaded for the first time on all team members' devices simultaneously, and the dashboard displayed Rahul Sharma's correct financial data pulled from the live Render backend — the team's reaction was genuine excitement.

3. **The Recovery Score Design Session** (Week 4): A 20-minute debate about the exact formula for the Recovery Score — which ended with everyone contributing a component — was the most collaborative intellectual moment of the project.

---

## 6. Acknowledgements

The team extends heartfelt acknowledgements to:

### 6.1 Academic & Institutional Support

**Vishnu Institute of Technology, Bhimavaram**  
For providing the academic environment, computing infrastructure, and encouragement for students to participate in industry internship programs. The institution's progressive approach to allowing students to pursue external learning opportunities is commendable.

**Department of CSE (AI & DS)**  
For the strong foundation in Artificial Intelligence, Data Structures, and Software Engineering that enabled the team to conceptualize and execute a project of this technical depth within an 8-week internship period.

**Faculty Advisors and Evaluators**  
For providing honest feedback during the internal review session, particularly the suggestion to add a more detailed explanation of the Recovery Score metric (addressed with a tooltip in v1.1).

### 6.2 Program Support

**SmartBridge Educational Services**  
For organizing the Google Cloud Generative AI Internship program, providing access to expert mentors, and curating a curriculum that gave the team the knowledge foundation to integrate Gemini 2.0 Flash effectively.

**SmartBridge Mentors**  
For the guidance on Gemini API best practices (particularly the recommendation to use structured output format and to clearly separate role definition from task specification in prompts), and for the candid feedback on deployment documentation completeness.

### 6.3 Technology Acknowledgements

**Google DeepMind — Gemini 2.0 Flash**  
The quality and speed of Gemini 2.0 Flash made the core AI features of FinRelief AI possible. The model's ability to generate professionally formatted financial correspondence and detailed debt recovery plans, with context-specificity based on injected loan data, is remarkable.

**Open Source Community**  
FastAPI (Sebastián Ramírez), React (Meta Open Source), Recharts, SQLAlchemy, Pydantic, Python-Jose, Passlib — these open-source projects represent countless hours of expert engineering freely shared with the world. FinRelief AI stands on the shoulders of giants.

### 6.4 Personal Acknowledgements

**Families of all team members**  
For supporting late-night coding sessions, understanding the time commitment, and — in the case of the family members who participated in user testing — providing invaluable real-world feedback from people who actually face debt challenges.

**The 18 testers and evaluators** who reviewed the application during the testing phase — your feedback shaped the product materially, particularly the decision to add the Recovery Score tooltip and to add the "Hardship Type" dropdown for the letter generator (Phase 1 roadmap).

---

*Team Involvement & Contribution Report prepared by Team FinRelief AI | Vishnu Institute of Technology, Bhimavaram | SmartBridge Google Cloud Generative AI Internship | July 2026*

---

| Member | Signature Placeholder | Date |
|---|---|---|
| Yeleti Joel Prasanna Kumar (Team Lead) | ___________________ | July 2026 |
| Kambala Kusuma Saisri | ___________________ | July 2026 |
| Kusume Raju | ___________________ | July 2026 |
| Siva Manikanta Akula | ___________________ | July 2026 |
| Harsha Vardhan Gorle | ___________________ | July 2026 |
