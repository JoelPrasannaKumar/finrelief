# Team Communication Log
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
| **Document Type** | Team Communication & Collaboration Log |
| **Period Covered** | Week 1 – Week 8 (May–July 2026) |

---

## Table of Contents

1. [Team Communication Structure](#1-team-communication-structure)
2. [Communication Tools](#2-communication-tools)
3. [Weekly Meeting Logs](#3-weekly-meeting-logs)
4. [Task Delegation & Tracking](#4-task-delegation--tracking)
5. [Mentor Communication Log](#5-mentor-communication-log)
6. [Challenges & Resolutions](#6-challenges--resolutions)
7. [Team Collaboration Highlights](#7-team-collaboration-highlights)

---

## 1. Team Communication Structure

### 1.1 Team Hierarchy

```
Team Lead
└── Yeleti Joel Prasanna Kumar
    ├── Backend & Architecture (Joel — Lead)
    ├── Frontend Auth & Design (Kusuma Saisri)
    ├── Frontend Dashboard & Charts (Kusume Raju)
    ├── Frontend Settlement & Letters (Siva Manikanta)
    └── Frontend History & Testing (Harsha Vardhan)
```

### 1.2 Roles & Responsibilities

| Member | Role | Primary Responsibility | Secondary |
|---|---|---|---|
| Yeleti Joel Prasanna Kumar | Team Lead & Backend Dev | FastAPI architecture, all 7 API modules, AI integration, deployment | Code review, documentation |
| Kambala Kusuma Saisri | Frontend Dev (UI/Auth) | Login/Register pages, Profile page, CSS design system | Meeting moderator, timekeeper |
| Kusume Raju | Frontend Dev (Dashboard) | Dashboard page, Analysis page, Recharts integration | Backend API liaison |
| Siva Manikanta Akula | Frontend Dev (AI Features) | Settlement page, Letters page, Axios API client setup | Demo technical support |
| Harsha Vardhan Gorle | Frontend Dev & QA | History page, BorrowerRights page, testing, bug reporting | Documentation support |

### 1.3 Decision-Making Protocol

- **Day-to-day decisions:** Made independently by the responsible member.
- **Architecture decisions:** Discussed in weekly meetings, Joel has final call.
- **Disputes:** Discussed via WhatsApp group poll; majority vote for non-technical issues.
- **Emergency decisions (blocking issues):** Immediate WhatsApp message to Joel + affected member, resolved within 2 hours.

### 1.4 Code Review Protocol

- All code merged to `main` branch via **Pull Requests** on GitHub.
- Minimum 1 reviewer approval required before merge.
- Joel reviews all backend PRs; Kusuma Saisri reviews frontend PRs.
- PR template includes: description of changes, testing steps, screenshots for UI changes.

---

## 2. Communication Tools

| Tool | Purpose | Usage Frequency | Notes |
|---|---|---|---|
| **WhatsApp Group** ("FinRelief Team 🚀") | Day-to-day coordination, quick updates, file sharing | Multiple times daily | Primary async communication channel |
| **GitHub Issues** | Bug tracking, feature requests, task assignment | As needed (avg 3-4 per week) | Each issue labeled: `bug`, `feature`, `question`, `documentation` |
| **GitHub Projects** | Kanban board for sprint tracking | Reviewed weekly | Columns: Backlog, In Progress, Review, Done |
| **VS Code Live Share** | Real-time pair programming sessions | 2-3 sessions per week | Used for debugging complex issues together |
| **Google Meet** | Weekly team meetings | Once per week (Sunday evenings) | Sessions recorded for members who can't attend |
| **Google Docs** | Shared planning documents, meeting notes drafts | During planning phases | Later transferred to markdown files |
| **Google AI Studio** | Gemini prompt experimentation | Daily during AI development weeks | Joel shared prompt experiments with team |

---

## 3. Weekly Meeting Logs

### Week 1 — Project Kickoff (May 5–11, 2026)

**Meeting Date:** Sunday, May 10, 2026 | **Duration:** 2 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅

**Agenda:**
1. SmartBridge program overview and expectations.
2. Brainstorm project ideas.
3. Finalize project choice and name.
4. Assign roles and responsibilities.

**Discussion Points:**
- Joel presented 3 project ideas: (1) AI Recipe Generator, (2) AI Customer Support Bot, (3) AI Debt Relief Platform.
- Team unanimously voted for the Debt Relief Platform — noted as the most socially impactful and technically challenging.
- Project name brainstormed: "DebtFree AI," "ClearDebt," "FinRelief AI" — **FinRelief AI** selected.
- Tech stack decided: FastAPI + React + Gemini 2.0 Flash.
- GitHub repository created: `JoelPrasannaKumar/finrelief`.

**Action Items:**
- [ ] Joel: Set up GitHub repo, backend structure, initial FastAPI skeleton. *(Due: May 12)*
- [ ] Kusuma Saisri: Create Figma wireframes for Login and Register pages. *(Due: May 12)*
- [ ] Kusume Raju: Create Vite + React project, set up routing. *(Due: May 12)*
- [ ] Siva Manikanta: Research Gemini API documentation and Python SDK. *(Due: May 13)*
- [ ] Harsha Vardhan: Draft initial feature list and testing plan skeleton. *(Due: May 14)*

**Outcome:** ✅ Project direction finalized. Team energized and aligned.

---

### Week 2 — Foundation Setup (May 12–18, 2026)

**Meeting Date:** Sunday, May 17, 2026 | **Duration:** 1.5 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅

**Agenda:**
1. Review Week 1 action items.
2. Demo backend skeleton and frontend setup.
3. Plan Week 2 deliverables.

**Discussion Points:**
- Joel demoed the FastAPI skeleton with health check endpoint working.
- Kusume Raju demoed the React project with React Router setup and placeholder pages.
- Kusuma Saisri shared Figma wireframes — team appreciated the dark theme design direction.
- Siva Manikanta reported that Gemini API setup is straightforward with Python SDK.
- **Decision made:** Use SQLite for development, plan for PostgreSQL in production.
- **Issue raised:** CORS would need configuration — Joel to handle in backend setup.

**Action Items:**
- Joel: Implement User model, auth routes (register/login), JWT utility functions.
- Kusuma Saisri: Build Login and Register React components matching wireframes.
- Kusume Raju: Set up Axios API client in frontend, auth context with React Context API.
- Siva Manikanta: Experiment with Gemini prompts for financial advice in AI Studio.
- Harsha Vardhan: Set up pytest structure, write first 3 unit tests for password hashing.

**Outcome:** ✅ Strong foundation established on both frontend and backend.

---

### Week 3 — Authentication & Core Features (May 19–25, 2026)

**Meeting Date:** Sunday, May 24, 2026 | **Duration:** 2 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅

**Agenda:**
1. Review auth implementation.
2. Discuss loan CRUD API design.
3. Define API response schemas.

**Discussion Points:**
- Joel demonstrated working register and login APIs via Swagger UI.
- Kusuma Saisri demonstrated Login and Register pages with form validation.
- Integration test: Frontend login form → Backend API → JWT returned → Stored in localStorage. **SUCCESS.**
- Loan API schema discussed — decided to include `outstanding_balance` as separate field from `principal` to track repayment progress.
- Harsha Vardhan reported a bug: `verify_password` was failing — identified incorrect bcrypt call (`checkpw` with wrong encoding). **BUG-001 logged and fixed live during meeting.**

**Action Items:**
- Joel: Implement Loan CRUD API (GET all, POST, PUT, DELETE), User profile endpoint.
- Kusuma Saisri: Build Profile page.
- Kusume Raju: Build Dashboard page skeleton with metric cards (static data first).
- Siva Manikanta: Build Settlement page UI skeleton.
- Harsha Vardhan: Write 5 more unit tests covering JWT token creation and verification.

**Outcome:** ✅ Auth flow fully working end-to-end. BUG-001 fixed.

---

### Week 4 — Financial Engine & Dashboard (May 26 – June 1, 2026)

**Meeting Date:** Sunday, June 1, 2026 | **Duration:** 2.5 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅

**Agenda:**
1. Financial engine logic review.
2. Dashboard integration.
3. Charts discussion.

**Discussion Points:**
- Joel presented the Financial Engine — DTI, EMI calculation (standard formula), Recovery Score algorithm.
- Team reviewed the Recovery Score formula collaboratively — Kusume Raju suggested adding the "total loans count" penalty, which Joel agreed was a good addition.
- Kusume Raju selected **Recharts** over Chart.js for the Analysis charts (better React integration, TypeScript support).
- **Critical discussion:** The Recovery Score formula — after debate, team settled on: Start 100, deduct up to 50 for DTI, deduct 5 per missed payment, deduct 5 per extra loan beyond 3.
- Siva Manikanta raised concern about Gemini API key security — Joel clarified env variable approach and `.gitignore` setup.
- **BUG-005 identified:** DTI returns `NaN` when income is 0. Joel fixed it with income > 0 guard immediately.

**Action Items:**
- Joel: Wire financial engine to Analysis API endpoint. Implement Settlement Engine (Snowball/Avalanche sorting logic).
- Kusume Raju: Connect dashboard metric cards to real API data. Begin Recharts integration on Analysis page.
- Kusuma Saisri: Polish Login/Register pages, add password strength indicator.
- Siva Manikanta: Build Axios API client module (all 7 API endpoint functions).
- Harsha Vardhan: Test financial engine calculations against manual calculator results.

**Outcome:** ✅ Financial engine validated. Recovery Score formula finalized.

---

### Week 5 — AI Integration (June 2–8, 2026)

**Meeting Date:** Sunday, June 7, 2026 | **Duration:** 3 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅ (longest meeting — AI integration is the project core)

**Agenda:**
1. Gemini API integration demo.
2. Prompt engineering review.
3. Settlement plan UI design.

**Discussion Points:**
- Joel demoed the settlement plan generation live — team was visibly impressed by Gemini's output quality.
- **Key insight shared by Joel:** Pre-calculating metrics in the Financial Engine before sending to Gemini dramatically improves response quality — AI does reasoning, Python does math.
- Team collaboratively refined the Gemini prompt over 45 minutes — 6 iterations tested in AI Studio before settling on the final version.
- Siva Manikanta asked about error handling if Gemini API fails — Joel implemented try/except with fallback message.
- Letter generator discussed — Harsha Vardhan suggested adding letter type selection dropdown with three options.
- Kusuma Saisri flagged that the loading state (spinner) was implemented but needed better copy — team settled on "FinRelief AI is analyzing your portfolio..." text.

**Action Items:**
- Joel: Implement letter generation API. Wire settlement history storage.
- Siva Manikanta: Build Settlement page with strategy toggle, generate button, loading state, result display.
- Siva Manikanta: Build Letters page with type selector, loan selector, generation display.
- Kusuma Saisri: Add toast notification system for copy-to-clipboard, form success/error messages.
- Harsha Vardhan: Begin end-to-end testing — register → add loan → generate plan → generate letter.
- Kusume Raju: Complete Analysis page charts, add detailed loan breakdown table.

**Outcome:** ✅ AI features working. Prompt engineering finalized. Team at peak energy.

---

### Week 6 — UI Polish & History Feature (June 9–15, 2026)

**Meeting Date:** Sunday, June 14, 2026 | **Duration:** 1.5 hours | **Platform:** Google Meet
**Attendees:** Joel, Kusuma Saisri, Siva Manikanta, Harsha Vardhan ✅ | Kusume Raju ⚠️ (joined late, 30 min)

**Agenda:**
1. UI polish review.
2. History and Borrower Rights pages.
3. Bug review.

**Discussion Points:**
- Harsha Vardhan demonstrated History page timeline — team appreciated the visual design.
- **BUG-007 identified by Harsha:** Duplicate history entries appearing on page refresh. Root cause: React StrictMode double-invoking useEffect. Fixed with useRef to prevent double-fetch.
- Kusuma Saisri demonstrated CSS dark mode improvements — updated color palette for better contrast.
- **BUG-008 identified:** Dark mode text invisible on Settlement page nested component. Fixed with CSS variable correction.
- Team reviewed Borrower Rights page content — Harsha Vardhan presented accordion-style FAQ format, approved unanimously.
- Kusume Raju (when joined) shared completed Analysis page — team requested minor chart padding improvement.

**Action Items:**
- Joel: Final API testing, Swagger docs cleanup, deployment preparation.
- Kusuma Saisri: Mobile responsiveness audit across all pages.
- Kusume Raju: Chart padding fix, final Analysis page polishing.
- Siva Manikanta: Error state handling on Settlement and Letters pages.
- Harsha Vardhan: Complete full bug regression test cycle, update bug tracker.

**Outcome:** ✅ Most bugs resolved. UI quality dramatically improved. 80% feature complete.

---

### Week 7 — Deployment & Testing (June 16–22, 2026)

**Meeting Date:** Sunday, June 21, 2026 | **Duration:** 2 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅

**Agenda:**
1. Deployment walkthrough.
2. Full testing session.
3. Documentation plan.

**Discussion Points:**
- Joel demonstrated deploying the backend to Render.com — first deployment took 18 minutes due to dependency resolution.
- **Critical discovery:** Render.com free tier does not persist SQLite files — data resets on each deploy. Team discussed this openly.
- **Resolution:** Will clearly document this limitation. Phase 1 roadmap will address with PostgreSQL migration.
- Joel demonstrated Vercel deployment of frontend — took 4 minutes, seamless.
- Live URL tested by all team members simultaneously — application stable.
- **BUG-009 discovered:** Swagger docs not loading in production — root_path configuration issue. Fixed.
- Full regression test cycle conducted with all team members — no P1 bugs found.
- Documentation task assignments distributed.

**Action Items:**
- All members: Complete their respective documentation sections.
- Joel: Set up demo account with pre-seeded loan data.
- Harsha Vardhan: Complete full testing report.
- Siva Manikanta: Create Docker Compose setup.
- Kusuma Saisri: Create demo environment checklist.
- Kusume Raju: Record backup demo video.

**Outcome:** ✅ Application fully deployed and live. Major milestone achieved.

---

### Week 8 — Documentation & Demo Preparation (June 23 – July 6, 2026)

**Meeting Date:** Sunday, June 29, 2026 | **Duration:** 2.5 hours | **Platform:** Google Meet
**Attendees:** All 5 members ✅

**Agenda:**
1. Documentation review.
2. Demo rehearsal.
3. Q&A preparation.

**Discussion Points:**
- First full demo rehearsal conducted — total time: 38 minutes (over target of 30).
- **Scene 3 (Kusume Raju) was too detailed** — cut the form validation demo from 6 minutes to 4 minutes.
- Q&A practice: Joel asked Siva Manikanta the Gemini accuracy question — Siva's answer refined collaboratively.
- Kusuma Saisri's timer role practiced — hand signal system agreed upon.
- Documentation reviewed — all members submitted their sections.
- **Final meeting morale:** Very high. Team confident in the product quality.

**Additional Rehearsal Date:** July 4, 2026 (45-minute final rehearsal — all timings hit)

**Action Items (Final):**
- All: Final documentation proof-reading.
- Joel: Consolidate all docs into submission package.
- All: Confirm internet and hardware for demo day.

**Outcome:** ✅ Demo rehearsal successful. Team fully prepared.

---

## 4. Task Delegation & Tracking

### 4.1 GitHub Issues Statistics (8-week period)

| Category | Issues Created | Issues Closed | Open |
|---|---|---|---|
| Bug | 9 | 9 | 0 |
| Feature | 18 | 18 | 0 |
| Documentation | 8 | 8 | 0 |
| Question / Discussion | 6 | 6 | 0 |
| **Total** | **41** | **41** | **0** |

### 4.2 GitHub Contribution Summary

| Member | Commits | PRs Opened | PRs Reviewed | Issues Closed |
|---|---|---|---|---|
| Yeleti Joel | 87 | 12 | 8 | 18 |
| Kusuma Saisri | 34 | 6 | 4 | 7 |
| Kusume Raju | 28 | 5 | 3 | 6 |
| Siva Manikanta | 31 | 5 | 3 | 7 |
| Harsha Vardhan | 19 | 3 | 6 | 9 |
| **Total** | **199** | **31** | **24** | **47** |

---

## 5. Mentor Communication Log

| Date | Platform | Mentor Topic | Key Guidance Received | Action Taken |
|---|---|---|---|---|
| May 15, 2026 | SmartBridge Portal | Project idea validation | "Debt relief is a strong, socially relevant use case. Make sure AI adds real value, not just cosmetic." | Refined AI integration to use pre-calculated data in prompts |
| May 28, 2026 | Google Meet | Tech stack review | "FastAPI is an excellent choice. Ensure Pydantic validation is thorough." | Added comprehensive Pydantic schemas for all request bodies |
| June 12, 2026 | SmartBridge Portal | Midpoint check-in | "Gemini integration looks promising. Document your prompt engineering choices." | Created prompt engineering documentation section |
| June 25, 2026 | Google Meet | Pre-final review | "Deployment is good. Document the SQLite limitation clearly — evaluators will ask about it." | Added Known Limitations section to executable files guide |
| July 3, 2026 | SmartBridge Portal | Final submission guidance | "Include user feedback in demonstration documentation." | Added User Feedback Collected section to Demo documentation |

---

## 6. Challenges & Resolutions

| # | Challenge | Week Encountered | Impact | Resolution | Team Member(s) Involved |
|---|---|---|---|---|---|
| 1 | bcrypt `verify_password` always returning `False` | Week 3 | Blocker — auth completely broken | Fixed encoding issue in `checkpw` call | Joel + Harsha Vardhan |
| 2 | CORS errors blocking frontend-backend communication | Week 3 | Blocker — API calls failing | Configured CORSMiddleware correctly in FastAPI | Joel + Kusume Raju |
| 3 | Gemini API key accidentally committed to GitHub | Week 5 | Critical security risk | Revoked old key, generated new key, updated `.gitignore`, reviewed git history | Joel (immediate action) |
| 4 | Recharts charts not rendering on mobile | Week 6 | Medium — mobile UX broken | Added `ResponsiveContainer` wrapper with proper height constraints | Kusume Raju |
| 5 | Render.com SQLite data persistence issue | Week 7 | High — demo data resets | Created demo account seeding script run pre-demo; documented limitation | Joel + team |
| 6 | React StrictMode causing double API calls | Week 6 | Medium — duplicate history entries | Added `useRef` flag to prevent double-invocation of `useEffect` | Harsha Vardhan + Joel |
| 7 | Letter copy function failing in Firefox | Week 6 | Low — minor UX issue | Implemented fallback `execCommand('copy')` for non-HTTPS contexts | Harsha Vardhan |
| 8 | Demo account data wiped the day before rehearsal | Week 8 | High — demo setup broken | Created automated seeder script; added pre-demo checklist step | Joel + Kusuma Saisri |

---

## 7. Team Collaboration Highlights

### 7.1 Most Effective Collaboration Moments

**Moment 1 — The Prompt Engineering Session (Week 5 Meeting)**
The 45-minute collaborative prompt engineering session on June 7 was the most intellectually productive team moment of the internship. All five members contributed ideas — Harsha Vardhan suggested adding "don't give generic advice" as an explicit constraint; Kusuma Saisri suggested including the recovery score context; Kusume Raju proposed using structured JSON output format for easy rendering. The resulting prompt produced Gemini responses that were qualitatively far superior to the initial version.

**Moment 2 — Bug-Resolution During Meeting (Week 3)**
When BUG-001 (authentication failure) was identified by Harsha Vardhan during the Week 3 meeting, Joel screen-shared VS Code and fixed the bug live with the whole team watching. This 12-minute live debugging session was educational for the entire team — everyone understood the bcrypt API better afterward.

**Moment 3 — Recovery Score Formula Design (Week 4)**
The collaborative design of the Recovery Score formula was a genuine team effort. Joel proposed the base structure; Kusume Raju added the loan count penalty; Harsha Vardhan validated it against manual calculations. The formula became one of the most distinctive features of the platform.

### 7.2 Team Atmosphere & Culture

- **Psychological safety:** All team members felt comfortable raising bugs and concerns without fear of blame. Issues were treated as "problems to solve together," not individual failures.
- **Celebration of milestones:** Each major milestone (auth working, first Gemini response, live deployment) was celebrated with a shared message in the WhatsApp group. The live deployment message received 🎉🔥💯 reactions from all members.
- **Mutual support:** When Kusume Raju joined the Week 6 meeting late due to a personal commitment, no judgment was expressed — notes were shared, and his contribution was accepted without comment.
- **Shared ownership:** Despite distinct module ownership, team members frequently helped each other. Kusuma Saisri designed the CSS toast notification system that everyone used; Siva Manikanta set up the Axios API client that all frontend developers benefited from.

### 7.3 Acknowledgements

The team would like to acknowledge:

- **SmartBridge** for organizing the Google Cloud Generative AI Internship program and providing access to expert mentorship and Google Cloud resources.
- **Google DeepMind** for making Gemini 2.0 Flash available through a developer-accessible API, enabling student teams to build genuine AI-powered applications.
- **The faculty of Vishnu Institute of Technology, Bhimavaram** for supporting and encouraging student participation in industry internship programs.
- **Family members and peers** who provided honest feedback during the testing phase — their insights significantly improved the product.

---

*Communication log compiled by Team FinRelief AI | Vishnu Institute of Technology, Bhimavaram | July 2026*
