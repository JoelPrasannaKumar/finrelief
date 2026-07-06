# Project Demo Planning
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
| **Document Type** | Demo Planning Guide |
| **Demo Date** | July 2026 |

---

## Table of Contents

1. [Demo Objectives](#1-demo-objectives)
2. [Team Presentation Assignments](#2-team-presentation-assignments)
3. [Demo Environment Setup Checklist](#3-demo-environment-setup-checklist)
4. [Sample Data for Demo](#4-sample-data-for-demo)
5. [Scene-by-Scene Demo Script](#5-scene-by-scene-demo-script)
6. [Time Allocation](#6-time-allocation)
7. [Backup Plan (Offline Contingency)](#7-backup-plan-offline-contingency)
8. [Q&A Preparation](#8-qa-preparation)

---

## 1. Demo Objectives

The FinRelief AI project demonstration aims to achieve the following goals with the SmartBridge evaluators and mentors:

| # | Objective | Success Indicator |
|---|---|---|
| 1 | Demonstrate a fully functional, deployed web application | Live URL loads without errors within the demo |
| 2 | Show seamless AI integration with Google Gemini 2.0 Flash | Live AI-generated settlement plan and letter appear on screen |
| 3 | Highlight the real-world social impact of the platform | Evaluators acknowledge the problem-solution fit |
| 4 | Present each team member's individual contribution | Every member speaks on their own module |
| 5 | Demonstrate technical depth: auth, APIs, DB, AI, deployment | Technical questions answered confidently |
| 6 | Show a polished UI/UX with responsive design | No UI glitches visible during demo |

---

## 2. Team Presentation Assignments

| Scene | Topic | Presenter | Email |
|---|---|---|---|
| **Scene 1** | Introduction, Problem Statement, Live URL | Yeleti Joel Prasanna Kumar | 23pa1a45d0@vishnu.edu.in |
| **Scene 2** | Dashboard – Financial Overview & Metrics | Kambala Kusuma Saisri | 23pa1a4553@vishnu.edu.in |
| **Scene 3** | Add Loan, Financial Analysis Charts | Kusume Raju | 23pa1a4579@vishnu.edu.in |
| **Scene 4** | AI Settlement Engine – Generate Plan | Siva Manikanta Akula | akulasivamanikanta14@gmail.com |
| **Scene 5** | AI Letter Generator – Hardship Letter | Harsha Vardhan Gorle | harshavardhanngorle@gmail.com |
| **Scene 6** | Conclusion, Scalability, Q&A | Yeleti Joel Prasanna Kumar | 23pa1a45d0@vishnu.edu.in |

**Moderator / Timekeeper:** Kambala Kusuma Saisri  
**Technical Support (screen sharing, backup):** Siva Manikanta Akula

---

## 3. Demo Environment Setup Checklist

Complete this checklist **30 minutes before** the scheduled demonstration time.

### 3.1 Hardware & Network

- [ ] Laptop charged to 100% or plugged in.
- [ ] Backup laptop with project cloned and running locally (Kusume Raju's machine).
- [ ] Internet connection tested — check speed ≥ 10 Mbps download/upload.
- [ ] Mobile hotspot (Jio/Airtel) ready as backup internet source.
- [ ] External monitor or projector connected and display mirrored/extended.
- [ ] Cursor pointer (if available) for highlighting UI elements during presentation.

### 3.2 Browser Setup

- [ ] Open **Google Chrome** (latest version) as primary browser.
- [ ] Pre-open the following tabs (in order):
  - Tab 1: https://finrelief.vercel.app (landing/login page)
  - Tab 2: https://finrelief-ai-backend.onrender.com/api/docs (Swagger UI)
  - Tab 3: https://github.com/JoelPrasannaKumar/finrelief (GitHub repo)
  - Tab 4: Google Slides presentation (title slide shown by default)
- [ ] Log in to demo account (`demo@finrelief.ai` / `Demo@1234`) **5 minutes before** to warm up Render backend.
- [ ] Zoom browser to 110% for better visibility on projector.
- [ ] Close all non-essential browser tabs and applications.
- [ ] Disable browser notifications (Chrome Settings → Notifications → Blocked).
- [ ] Turn off desktop notifications (Windows Focus Assist → Priority Only).

### 3.3 Application State Setup

- [ ] Confirm demo account is logged in and dashboard loads correctly.
- [ ] Verify **Rahul Sharma** profile shows name correctly in top-right avatar.
- [ ] Confirm both demo loans are visible on Dashboard:
  - HDFC Bank Personal Loan (₹1,50,000)
  - Bajaj Finserv EMI (₹45,000)
- [ ] Confirm Analysis page charts load and render correctly.
- [ ] Test one AI call (Settlement) before demo to ensure Gemini API is responding.
- [ ] Navigate back to Login page so demo begins from the beginning.

### 3.4 Presentation Materials

- [ ] PowerPoint/Slides open on second screen (not the main demo screen).
- [ ] Slide deck includes: Title slide, Architecture diagram, Team photo, GitHub QR code.
- [ ] Screen recording software running as backup capture of entire demo.
- [ ] Team members positioned with microphone access (if online demo via Meet/Zoom).

---

## 4. Sample Data for Demo

Use the following data consistently throughout the demonstration to maintain a coherent narrative about the fictional demo user.

### 4.1 Demo User Profile

| Field | Value |
|---|---|
| **Full Name** | Rahul Sharma |
| **Email** | demo@finrelief.ai |
| **Password** | Demo@1234 |
| **Monthly Income** | ₹45,000 |
| **City** | Hyderabad, Telangana |

### 4.2 Demo Loan 1

| Field | Value |
|---|---|
| **Lender Name** | HDFC Bank |
| **Loan Type** | Personal Loan |
| **Original Principal** | ₹2,00,000 |
| **Outstanding Balance** | ₹1,50,000 |
| **Annual Interest Rate** | 14.5% |
| **Tenure** | 36 months |
| **Monthly EMI** | ₹5,124 |
| **Missed Payments** | 2 |
| **Start Date** | January 2024 |

### 4.3 Demo Loan 2

| Field | Value |
|---|---|
| **Lender Name** | Bajaj Finserv |
| **Loan Type** | Consumer Durable EMI |
| **Original Principal** | ₹60,000 |
| **Outstanding Balance** | ₹45,000 |
| **Annual Interest Rate** | 22% |
| **Tenure** | 24 months |
| **Monthly EMI** | ₹2,100 |
| **Missed Payments** | 1 |
| **Start Date** | June 2024 |

### 4.4 Expected Computed Metrics (for reference)

| Metric | Expected Value |
|---|---|
| Total Outstanding Debt | ₹1,95,000 |
| Total Monthly EMI | ₹7,224 |
| Debt-to-Income Ratio | 0.16 (16%) |
| Recovery Score | ~72/100 |
| Recommended Strategy | AVALANCHE (Bajaj Finserv first due to 22% rate) |

---

## 5. Scene-by-Scene Demo Script

### Scene 1 — Introduction & Live URL Reveal
**Presenter:** Yeleti Joel Prasanna Kumar | **Duration:** 3 minutes

**[Joel speaks]**

> "Good [morning/afternoon], mentors and evaluators. My name is Yeleti Joel Prasanna Kumar, team lead of FinRelief AI, and I'm joined by my teammates — Kusuma Saisri, Kusume Raju, Siva Manikanta, and Harsha Vardhan — all from the CSE AI & DS department at Vishnu Institute of Technology, Bhimavaram.
>
> Today we are presenting FinRelief AI — an AI-powered Debt Relief and Financial Recovery Platform built using FastAPI, React, and Google Gemini 2.0 Flash, developed as part of the SmartBridge Google Cloud Generative AI Internship.
>
> The problem we solve: Over 8 million Indian households are in debt distress today. When someone gets overwhelmed by loans, they have no affordable, accessible tool to help them plan their way out. FinRelief AI changes that.
>
> Let me open our live application now. Here is our frontend, deployed on Vercel: [open https://finrelief.vercel.app]. The backend API runs on Render.com, and the full Swagger documentation is live at this URL [show Tab 2 briefly]. Our complete source code is on GitHub [show Tab 3 briefly].
>
> I'll now log in with our demo account to walk you through the platform."

**[Action: Navigate to login page, type demo@finrelief.ai and Demo@1234, click Login]**

---

### Scene 2 — Dashboard Overview
**Presenter:** Kambala Kusuma Saisri | **Duration:** 3 minutes

**[Kusuma Saisri speaks]**

> "Welcome to the FinRelief AI Dashboard. I'm Kusuma Saisri, and I built the authentication pages, the profile page, and the entire CSS design system you see here.
>
> When a user logs in, they land here. The dashboard immediately presents four key financial metrics for Rahul's portfolio:
>
> — Total Outstanding Debt: ₹1,95,000 — shown in red because it represents urgency.
> — Total Monthly EMI: ₹7,224 — the amount Rahul must pay every month combined.
> — Debt-to-Income Ratio: 0.16 — meaning 16% of Rahul's income goes to EMIs. This is actually manageable — our system color-codes this green.
> — Recovery Score: 72 out of 100 — a proprietary metric our engine computes based on DTI, missed payments, and loan count.
>
> Below the metrics you can see Rahul's two active loans in a clean table — HDFC Bank and Bajaj Finserv — with quick action buttons to edit, delete, or generate a letter directly from here.
>
> This dashboard gives Rahul instant clarity on his financial position — something he'd otherwise need a financial advisor to compute for him."

**[Action: Point to each metric card, hover over the Recovery Score to show tooltip explanation, scroll down to show loan table]**

---

### Scene 3 — Add Loan & Financial Analysis
**Presenter:** Kusume Raju | **Duration:** 4 minutes

**[Kusume Raju speaks]**

> "I'm Kusume Raju. I built the Dashboard layout you just saw, and the Analysis page with all the charts using Recharts library. Let me first show you how easy it is to add a loan.
>
> [Click 'Add Loan' button]
>
> This form lets users enter their loan details — lender name, loan type, principal amount, interest rate, tenure, and any missed payments. The monthly income is set in the profile page. Notice the form has real-time validation — watch what happens when I try to enter a negative interest rate. [demonstrate validation]
>
> Now let me navigate to the Analysis page. [Click Analysis in sidebar]
>
> Here we have two Recharts visualizations. The donut pie chart on the left shows the debt breakdown by loan type — we can see Personal Loan is the dominant category. The bar chart on the right compares monthly EMI for each loan relative to Rahul's income, making it visually obvious which loan is the biggest burden.
>
> Below the charts, we have a detailed breakdown table showing outstanding balance, total interest remaining, estimated payoff date, and contribution to total debt burden for each loan. This analysis is computed entirely by our Financial Engine in real-time from the stored loan data — no manual calculations required."

**[Action: Show add loan form, demonstrate validation, navigate to Analysis, point to charts, scroll through analysis table]**

---

### Scene 4 — AI Settlement Engine
**Presenter:** Siva Manikanta Akula | **Duration:** 4 minutes

**[Siva Manikanta speaks]**

> "I'm Siva Manikanta. I built the Settlement page and the Letters page, and set up the API client that connects our React app to the FastAPI backend. This scene showcases the most powerful feature of FinRelief AI — the AI Settlement Engine.
>
> [Navigate to Settlement in sidebar]
>
> Here you see the strategy toggle — Snowball versus Avalanche. Our system has already analyzed Rahul's portfolio and recommends Avalanche, because Bajaj Finserv's 22% interest rate is the most expensive debt mathematically. Snowball is better for borrowers who need quick psychological wins — it targets the smallest balance first.
>
> I'll click 'Generate Settlement Plan' now. Watch — our backend sends Rahul's complete loan portfolio to Google Gemini 2.0 Flash, which analyzes it and generates a personalized month-by-month recovery plan.
>
> [Click Generate — wait ~3 seconds for Gemini response]
>
> Here's the result. Gemini has produced a 6-month action plan. In Month 1, Rahul should make the minimum payment on HDFC Bank (₹5,124) and direct all extra money — let's say ₹3,000 — to Bajaj Finserv to attack that 22% rate. Each subsequent month shows the projected balance reduction and an estimated debt-free milestone.
>
> This is the kind of personalized advice that would cost ₹2,000-₹5,000 for a single consultation with a financial advisor. We provide it instantly, for free."

**[Action: Show strategy toggle, explain each option, click Generate, wait for AI response, scroll through generated plan]**

---

### Scene 5 — AI Letter Generator
**Presenter:** Harsha Vardhan Gorle | **Duration:** 3 minutes

**[Harsha Vardhan speaks]**

> "I'm Harsha Vardhan. I built the History page, the Borrower Rights page, and was responsible for testing the application. Let me show you the Letter Generator — a feature unique to FinRelief AI among student projects.
>
> [Navigate to Letters in sidebar]
>
> When a borrower is in distress, they need to communicate with lenders formally. A hardship letter requests temporary relief — reduced EMIs, moratorium, waiver of penalties. A settlement offer letter proposes a one-time payment to close the loan for less than the outstanding balance. These letters, written professionally, can be the difference between a lender agreeing to restructure and initiating legal proceedings.
>
> I'll select 'Hardship Letter' and choose the HDFC Bank loan. [Click Generate Letter]
>
> Gemini 2.0 Flash generates a complete, professional hardship letter addressed to HDFC Bank, referencing Rahul Sharma's specific loan details, explaining the financial hardship, and formally requesting a 3-month moratorium. The letter includes the correct date, formal salutation, structured paragraphs, and a professional sign-off.
>
> This button copies the entire letter to the clipboard. Rahul can paste it directly into an email to his loan manager. [Click Copy, show toast notification]
>
> The Borrower Rights page [navigate briefly] provides legal information about SARFAESI Act protections, RBI Fair Practices Code, and what lenders are and are not allowed to do during collection — all summarized in plain language."

**[Action: Navigate to Letters, select type and loan, generate, show letter, copy to clipboard, briefly show Borrower Rights page]**

---

### Scene 6 — Conclusion & Architecture
**Presenter:** Yeleti Joel Prasanna Kumar | **Duration:** 3 minutes

**[Joel speaks]**

> "To summarize what you've seen: FinRelief AI is a complete, production-deployed platform that combines:
>
> — A FastAPI backend with 7 RESTful API modules, JWT authentication, SQLAlchemy ORM, and Google Gemini 2.0 Flash integration.
> — A React 18 + Vite frontend with Recharts visualization, deployed on Vercel with a 89/100 Lighthouse score.
> — 90% backend test coverage, 20 unit tests, 8 integration tests — all passing.
> — Zero critical security vulnerabilities — SQL injection blocked by ORM, unauthorized access blocked by ownership checks.
>
> [Show architecture diagram on slide]
>
> Our roadmap includes PostgreSQL migration, a React Native mobile app, and eventually ML-based credit recovery prediction.
>
> The GitHub repository is fully public. The Swagger API documentation is live. The application is live and usable right now.
>
> We believe FinRelief AI is not just a student project — it's a solution to a real problem affecting millions of Indian families.
>
> Thank you. We're happy to take your questions."

**[Action: Switch to slide with architecture diagram, then open Q&A]**

---

## 6. Time Allocation

| Scene | Presenter | Topic | Duration | Cumulative |
|---|---|---|---|---|
| Scene 1 | Joel | Intro + Live URL | 3 min | 3 min |
| Scene 2 | Kusuma Saisri | Dashboard | 3 min | 6 min |
| Scene 3 | Kusume Raju | Add Loan + Analysis | 4 min | 10 min |
| Scene 4 | Siva Manikanta | AI Settlement | 4 min | 14 min |
| Scene 5 | Harsha Vardhan | Letter Generator | 3 min | 17 min |
| Scene 6 | Joel | Conclusion | 3 min | 20 min |
| **Q&A** | All members | Questions | 10 min | 30 min |
| **Buffer** | — | Technical issues buffer | 5 min | 35 min |

**Total Allocated Time: 35 minutes**

> [!IMPORTANT]
> Assign Kusuma Saisri as timekeeper. She will hold up a sign (or send a chat message in virtual meetings) at the 2-minute mark for each scene to signal the current presenter to begin wrapping up.

---

## 7. Backup Plan (Offline Contingency)

### Scenario A: Live Backend is Down (Render cold start fails)

**Action:** Switch to local backend.
1. Kusume Raju immediately starts the local backend: `uvicorn main:app --reload`
2. Joel updates the frontend API URL by temporarily switching to local build.
3. Alternatively, switch to Kusume Raju's laptop which has the local full-stack running.
4. Continue demo using `http://localhost:8000` as backend.

### Scenario B: Gemini API Rate Limited or Errors

**Action:** Use pre-generated response.
1. Siva Manikanta opens the file `demo_backup/settlement_plan_response.json` (stored locally).
2. Display the pre-generated settlement plan from the file.
3. Explain: "For this demo, we're showing a previously generated plan — this is a typical response from Gemini 2.0 Flash."
4. For letters: Show pre-generated letter from `demo_backup/hardship_letter.txt`.

### Scenario C: No Internet Connection

**Action:** Full offline demo.
1. Kusume Raju runs the full application locally (backend + frontend both running locally).
2. Siva Manikanta switches screen sharing to his laptop running on localhost.
3. Use pre-generated AI responses (Scenarios B backup).
4. **Pre-recorded demo video** (2-minute highlights) available as last resort: `demo_backup/finrelief_demo.mp4`.

### Scenario D: Presenter Absent

| Absent Member | Backup Presenter |
|---|---|
| Kusuma Saisri (Scene 2) | Joel covers Scene 2 |
| Kusume Raju (Scene 3) | Harsha Vardhan covers Scene 3 |
| Siva Manikanta (Scene 4) | Joel covers Scene 4 |
| Harsha Vardhan (Scene 5) | Kusuma Saisri covers Scene 5 |

All team members are expected to be familiar with all scenes and capable of presenting any scene if needed.

---

## 8. Q&A Preparation

### Expected Questions and Prepared Answers

**Q1: Why did you choose FastAPI over Django or Flask?**

> **A (Joel):** FastAPI was chosen for three reasons: it provides automatic Swagger documentation generation (which we use in our API docs URL), it's built on Pydantic for automatic request/response validation eliminating boilerplate, and it's asynchronous by design — critical for non-blocking Gemini API calls. Django is heavier than needed for an API-only backend, and Flask lacks automatic data validation.

**Q2: How do you ensure the AI gives accurate financial advice?**

> **A (Siva Manikanta):** The AI doesn't give advice in a vacuum — it receives structured, verified data: exact loan amounts, interest rates, and income from our database. The prompt explicitly instructs Gemini to base all recommendations on the specific numbers provided, not generic advice. We also display a disclaimer that the platform is for educational purposes and encourages consulting a certified financial advisor for major decisions.

**Q3: What happens to user data? Is it secure?**

> **A (Joel):** All passwords are hashed with bcrypt — never stored in plain text. JWTs expire after 24 hours and contain minimal information (only the user's email). All loan data is accessed through ORM queries, preventing SQL injection. Each user can only access their own loans — we have ownership checks on every update and delete endpoint. In production, we would add HTTPS-only enforcement and move to PostgreSQL with encrypted backups.

**Q4: Why SQLite? Is that production-ready?**

> **A (Kusume Raju):** SQLite is our current development/demo database because it requires zero configuration and works perfectly for a single-server deployment. We're aware of its limitations — particularly on Render's free tier where the file system isn't persistent. Our Phase 1 roadmap (0–3 months) explicitly includes migrating to PostgreSQL with connection pooling via pgBouncer. The application code uses SQLAlchemy ORM, so swapping databases is a one-line configuration change.

**Q5: How does the Recovery Score work?**

> **A (Kusuma Saisri):** The Recovery Score is a proprietary metric we designed — it starts at 100 and applies penalties: the Debt-to-Income ratio causes up to a 50-point deduction (high DTI = bigger penalty), each missed payment deducts 5 points, and having more than 3 loans deducts additional points. The score is bounded between 0 and 100. Users with scores below 50 are steered toward the Snowball strategy for psychological wins; scores above 50 get the mathematically optimal Avalanche strategy.

**Q6: Can this scale to thousands of users?**

> **A (Joel):** The architecture is designed for horizontal scalability. The backend is stateless (no server-side sessions — JWT handles state) so multiple backend instances can run behind a load balancer without coordination. The primary bottleneck at scale would be the SQLite database and Gemini API rate limits — both addressed in our roadmap: PostgreSQL + Redis caching for the database layer, and Gemini Pro or a paid tier with higher rate limits for the AI layer. Deploying on Google Cloud Run would give auto-scaling capability.

**Q7: How long did each feature take to build?**

> **A (Joel):** Backend auth system: 2 days. Financial calculation engine: 3 days. Settlement engine + Gemini integration: 4 days. Letter generator: 2 days. Frontend (all pages): 8 days across 3 members. Testing: 3 days. Documentation: 2 days. Total: approximately 6 weeks of part-time development alongside college coursework.

**Q8: What makes this different from just using ChatGPT?**

> **A (Siva Manikanta):** Three key differences. First, ChatGPT doesn't know your specific loans — you'd have to manually type everything each time. FinRelief AI stores your complete portfolio and sends it automatically. Second, the AI output is integrated into an actionable UI — settlement plans are rendered as formatted monthly cards, letters are ready to copy. Third, we add a proprietary computation layer (our Financial Engine and Settlement Engine) that does precise mathematical calculations before the AI sees the data, making the AI's job reasoning-only rather than calculation-heavy.

**Q9: How did you learn to use the Gemini API?**

> **A (Joel):** We used Google AI Studio to experiment with prompts interactively before coding. The SmartBridge mentors guided us on the `google-generativeai` Python SDK. The key learning was prompt engineering — structuring prompts with clear role definitions, structured data injection, and explicit output format requirements. This was the most intellectually interesting part of the project.

**Q10: What would you build next if you had 6 more months?**

> **A (Joel):** The immediate next step is PostgreSQL migration and mobile app development (React Native). The most impactful future feature would be bank statement PDF upload — letting users upload their bank statement and having Gemini automatically extract and populate all loan details. Long-term, we envision integrating with credit bureau APIs to fetch real CIBIL scores and provide real-time debt-to-creditworthiness recommendations. Eventually, we'd like to open the platform to NGOs and credit counseling centers via a white-labeled SaaS model.

---

*Demo Planning Document prepared by Team FinRelief AI | Vishnu Institute of Technology, Bhimavaram | July 2026*
