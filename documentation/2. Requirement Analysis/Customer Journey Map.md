# Customer Journey Map
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

## 1. Introduction to Customer Journey Mapping

A Customer Journey Map visualizes the end-to-end experience a user has with a product — from the first moment they become aware of it, through every touchpoint, to the ultimate goal of achieving their desired outcome. It captures user **actions**, **emotions**, **pain points**, and **opportunities** at each stage.

### Journey Map Persona
- **User:** Rahul Sharma, 34, Senior Software Engineer, Mumbai
- **Goal:** Get out of debt stress — understand settlement options, get personalized plan, generate OTS letter
- **Entry Channel:** Google search → FinRelief AI website
- **Device:** Mobile (Android) and Desktop (Chrome)

### Journey Stages Overview

```
AWARENESS → REGISTRATION → PROFILE SETUP → LOAN ENTRY → ANALYSIS → SETTLEMENT → LETTER GENERATION → RECOVERY
    (1)           (2)             (3)            (4)          (5)         (6)             (7)              (8)
```

---

## 2. Stage-by-Stage Journey

---

### STAGE 1: AWARENESS 🔍

> *"Rahul is searching late at night for 'how to reduce EMI burden India' after a stressful month."*

#### User Actions
1. Types "how to negotiate with bank to reduce loan EMI India" into Google at 11:30 PM
2. Clicks through several generic banking blog posts — none helpful
3. Finds a Reddit thread mentioning FinRelief AI as an AI-powered tool
4. Clicks the FinRelief AI link → lands on homepage
5. Reads the hero section headline: *"AI-Powered Debt Relief — Your Path to Financial Freedom"*
6. Watches the 60-second explainer video on the homepage
7. Reads the "How It Works" section — 4 simple steps

#### Emotional State
- **Before:** Anxious 😟, exhausted, hopeless
- **After landing on site:** Curious 🤔, cautiously hopeful
- **Emotional intensity:** High anxiety, slight relief at finding something promising

#### Touchpoints
- Google Search Results
- Reddit (r/personalfinanceindia mention)
- FinRelief AI Homepage
- Explainer Video
- "How It Works" Section

#### Pain Points at This Stage
1. ❌ Generic search results return generic, unhelpful advice
2. ❌ Most debt-related sites push new loan products (conflict of interest)
3. ❌ Discovery is accidental — no active marketing reached Rahul

#### Opportunities for FinRelief AI
1. ✅ SEO-optimize landing page for high-intent debt relief queries
2. ✅ Clear, benefit-focused hero section that immediately communicates value
3. ✅ Social proof: "Join 500+ borrowers on their path to financial freedom"
4. ✅ Credibility markers: Technology partners, security badges, real user testimonials
5. ✅ Community presence: Engage on Reddit, Quora with helpful content

#### Design Requirements
- Homepage loads in < 2 seconds
- Hero headline speaks directly to the emotional pain ("Drowning in EMIs?")
- No immediate push to register; let users explore first
- Trust signals prominently visible (SSL, privacy policy link)

---

### STAGE 2: REGISTRATION 📝

> *"Rahul decides to try it. He clicks 'Get Started Free' and sees a registration form."*

#### User Actions
1. Clicks "Get Started Free" CTA on homepage
2. Sees registration form: Name, Email, Password fields
3. Notices "No credit card required" and "Free to use" badges — feels reassured
4. Considers Google Sign-In option
5. Chooses to register with email (more private)
6. Enters details: Name (Rahul Sharma), Email, creates password
7. Receives OTP or email verification link
8. Verifies email
9. Lands on onboarding welcome screen

#### Emotional State
- **Before:** Hopeful but cautious (worried about data privacy)
- **During form fill:** Mildly anxious (what will they do with my data?)
- **After verification:** Relieved ✅, engaged

#### Touchpoints
- Registration form
- Email verification
- Welcome/onboarding screen
- Privacy policy (may click to read)

#### Pain Points at This Stage
1. ❌ Concern about sharing personal financial data with an unknown platform
2. ❌ Friction from email verification (extra step)
3. ❌ Worried about spam/marketing emails
4. ❌ Unclear what data will be used for

#### Opportunities for FinRelief AI
1. ✅ "We never share your data with banks or third parties" prominently displayed
2. ✅ Offer Google OAuth for one-click registration (reduces friction)
3. ✅ Explain data usage clearly in plain language (not legal jargon)
4. ✅ GDPR/data protection compliance badge
5. ✅ Verify only via email (no phone OTP unless needed — reduces friction)
6. ✅ Welcome email sets expectation: "Here's exactly what you'll do next"

#### Technical Requirements
- JWT-based authentication system
- Secure password hashing (bcrypt)
- Email verification flow
- Rate limiting on registration endpoint
- HTTPS enforced

---

### STAGE 3: PROFILE SETUP 👤

> *"Rahul is now logged in and sees a profile setup wizard. He's asked for basic financial info."*

#### User Actions
1. Views profile setup wizard (Step 1 of 3)
2. Enters basic info: Age (34), City (Mumbai), Occupation (Software Engineer)
3. Step 2: Monthly Income — enters ₹65,000
4. Step 3: Monthly Non-EMI Expenses — enters ₹25,000 (estimated)
5. Sees a "Financial Health Snapshot" preview with basic metrics
6. Completes profile — lands on main dashboard

#### Emotional State
- **During profile setup:** Engaged and willing (this feels personalized)
- **After seeing Financial Snapshot:** Surprised 😮 — "Only 10% savings ratio? That's alarming but real"
- **Emotional:** Mix of discomfort (reality check) and appreciation for honesty

#### Touchpoints
- Profile Setup Wizard (3 steps)
- Progress bar showing completion percentage
- Financial Health Snapshot preview
- Main Dashboard (first view)

#### Pain Points at This Stage
1. ❌ Not sure what "monthly non-EMI expenses" means — needs clear examples
2. ❌ Worried about accuracy — income varies (bonuses, freelance)
3. ❌ Profile feels incomplete without loan data added

#### Opportunities for FinRelief AI
1. ✅ Inline tooltips explaining each field
2. ✅ Allow income range instead of exact number for privacy comfort
3. ✅ Progress indicator showing "3 steps to your first AI analysis"
4. ✅ Celebrate profile completion with positive micro-interaction
5. ✅ Show immediate value: Even before loans are added, show basic financial health score

---

### STAGE 4: LOAN ENTRY 💳

> *"Rahul adds his 3 loans to the platform — home loan, personal loan, education loan."*

#### User Actions
1. Clicks "Add Loan" button on dashboard
2. Selects loan type from dropdown (Home Loan)
3. Enters: Lender (HDFC Bank), Original Amount (₹40,00,000), Outstanding (₹36,20,000), EMI (₹32,000), Interest Rate (8.5%), Tenure Started (2022)
4. Saves — sees Loan 1 card appear on dashboard
5. Repeats for Bajaj Finance Personal Loan
6. Repeats for SBI Education Loan
7. Views consolidated dashboard: Total Debt ₹38.55L, Total EMI ₹43.7K
8. Sees Debt-to-Income ratio: 67.2% — highlighted in red

#### Emotional State
- **During entry:** Focused but somewhat anxious (seeing all loans together for first time)
- **After completing all 3 loans:** Shock 😨 mixed with clarity — "I've never seen this all together before"
- **The truth is uncomfortable but necessary**

#### Touchpoints
- Add Loan Form
- Loan type selection (dropdown with common Indian loan types)
- Dashboard updating in real-time as loans are added
- Debt-to-Income ratio visualization
- Total Debt Summary card

#### Pain Points at This Stage
1. ❌ Needs exact figures — Rahul doesn't remember all details off the top of his head
2. ❌ Multiple loans means multiple form-fill sessions
3. ❌ Intimidating to see all debt aggregated — emotional difficulty
4. ❌ Not sure what "outstanding principal" means vs. "outstanding total with interest"

#### Opportunities for FinRelief AI
1. ✅ Show "You're doing great — most users feel better after adding all loans"
2. ✅ Smart defaults and auto-calculation where possible
3. ✅ Glossary tooltips for financial terms
4. ✅ Allow saving and resuming loan entry (don't lose progress)
5. ✅ After all loans added, show encouraging message: "Now let AI analyze your situation"
6. ✅ Visual debt composition chart (pie chart: Home vs. Personal vs. Education)

---

### STAGE 5: AI ANALYSIS 🤖

> *"Rahul clicks 'Generate AI Analysis'. The system sends his data to Gemini 2.0 Flash and shows results."*

#### User Actions
1. Reviews loan summary on dashboard
2. Clicks "Get AI Analysis" button
3. Sees loading animation: "Gemini AI is analyzing your financial profile..."
4. After 5–8 seconds, analysis report appears
5. Reads: Debt Severity Score (7.2/10 — High), Priority Recommendation, Month-by-month recovery plan
6. Sees AI recommendation: "Pay off Education Loan in 6 months (remaining ₹25K), then redirect ₹4,200 to Bajaj Loan"
7. Reads: "Your Bajaj Finance Personal Loan at 18% p.a. is your most expensive debt — prioritize after education loan"
8. Clicks "Explain This" on any section — AI provides deeper explanation
9. Downloads analysis as PDF

#### Emotional State
- **Before analysis:** Nervous anticipation
- **During loading:** Anxious
- **After seeing results:** Surprised and relieved 😮‍💨 — "This is actually helpful! It makes sense"
- **Emotional peak:** Gratitude — "Someone finally gave me a real plan"

#### Touchpoints
- "Generate Analysis" CTA
- Loading screen with informative messages
- AI Analysis Report (structured, scannable)
- Debt Severity Score visualization
- Recovery roadmap timeline
- "Explain This" interactive tooltip
- PDF download option

#### Pain Points at This Stage
1. ❌ 5–8 second wait feels long (mitigated by informative loading messages)
2. ❌ Analysis might be too detailed — information overload risk
3. ❌ What if the AI is wrong? No way to verify independently
4. ❌ Recommendations require action — what's the next step?

#### Opportunities for FinRelief AI
1. ✅ Loading animation shows progress ("Analyzing income vs. expenses...", "Calculating optimal payoff order...")
2. ✅ Analysis structured with clear hierarchy: Summary → Details → Actions
3. ✅ Always include disclaimer: "This is AI-generated guidance, not financial advice"
4. ✅ Add "What does this mean for me?" plain-language sections
5. ✅ Clear CTAs after analysis: "Generate OTS Letter" or "View Recovery Roadmap"

---

### STAGE 6: SETTLEMENT ELIGIBILITY 📊

> *"Rahul explores OTS settlement options for his Bajaj Finance personal loan."*

#### User Actions
1. Clicks "Explore Settlement Options" on the Bajaj Finance loan card
2. AI assesses: "Your personal loan (18% p.a., ₹2.1L outstanding) may qualify for OTS settlement"
3. Reads AI explanation of what OTS is and how it works
4. Views estimated settlement range: ₹1.26L – ₹1.68L (60%–80% of outstanding)
5. Reads AI assessment: "Bajaj Finance typically accepts OTS for accounts 90–180 days past due or proactively offered"
6. Sees prerequisites checklist: Financial hardship documentation, income proof, 3-month bank statements
7. Clicks "Generate OTS Request Letter" button

#### Emotional State
- **Before:** Uncertain — "Is settlement even possible for me?"
- **After seeing OTS range:** Hopeful 🌟 — "I could potentially pay ₹1.26L instead of ₹2.1L?"
- **Emotional:** Excitement tempered by practical concern ("But my credit score...")

#### Touchpoints
- Loan-specific action panel
- OTS Eligibility Assessment (AI-generated)
- OTS Amount Range Calculator
- Prerequisites Checklist
- "Generate OTS Letter" CTA

#### Pain Points at This Stage
1. ❌ Rahul doesn't know if OTS will hurt his credit score (it will, somewhat)
2. ❌ Not sure what documentation he needs to prepare
3. ❌ Worried about lender's reaction — "Will they think I'm defaulting on purpose?"

#### Opportunities for FinRelief AI
1. ✅ Explain credit score impact clearly and honestly (short-term dip, long-term recovery)
2. ✅ Provide documentation checklist in downloadable format
3. ✅ Reassure: "Banks prefer OTS over full default — you have negotiating power"
4. ✅ Show success stories (anonymized): "User X settled ₹3L Bajaj loan for ₹1.8L"
5. ✅ Link to RBI Fair Practices Code for borrowers (external validation)

---

### STAGE 7: OTS LETTER GENERATION ✉️

> *"Rahul uses FinRelief AI to generate a professional OTS negotiation letter for Bajaj Finance."*

#### User Actions
1. Fills letter generation form: Borrower name, loan account number (optional), settlement offer amount
2. Enters context: "Facing financial hardship due to medical expenses of spouse"
3. Clicks "Generate Letter"
4. Gemini AI generates professional, formal OTS request letter in ~5 seconds
5. Reads letter — impressed by professional language and structure
6. Sees letter includes: Loan account reference, hardship explanation, specific offer (₹1.4L), request for response timeline, RBI Fair Practices Code reference
7. Edits one paragraph to adjust the offered amount
8. Copies letter / downloads as PDF / downloads as Word (.docx)
9. Sends letter to Bajaj Finance customer care via email

#### Emotional State
- **During form fill:** Focused, engaged
- **After seeing generated letter:** Amazed 🤩 — "This is better than what I could've written"
- **Before sending:** Nervous but empowered — "I'm actually doing this"
- **After sending:** Significant emotional relief — the action has been taken

#### Touchpoints
- Letter Generation Form
- Loading animation ("Gemini AI is drafting your letter...")
- Generated Letter Preview (editable rich text)
- Edit/Customize functionality
- Download options (PDF, DOCX)
- Copy to Clipboard
- "Share via Email" integration

#### Pain Points at This Stage
1. ❌ Needs loan account number — may not have it handy
2. ❌ Uncertainty about the right settlement amount to offer
3. ❌ Worried the letter alone won't be enough

#### Opportunities for FinRelief AI
1. ✅ Make loan account number optional — use lender name + borrower name instead
2. ✅ AI suggests optimal offer amount range with justification
3. ✅ Provide follow-up guidance: "What to do if they don't respond in 14 days"
4. ✅ Track sent letters: "Letter sent on [date] — follow up recommended by [date+14 days]"
5. ✅ Template library for different scenarios (hardship, proactive settlement, debt restructuring)

---

### STAGE 8: FINANCIAL RECOVERY 📈

> *"Over the following months, Rahul returns to FinRelief AI to track his recovery progress."*

#### User Actions
1. Returns to app 2 weeks after sending OTS letter
2. Updates loan status: "Bajaj Finance responded — negotiating"
3. Follows AI's recovery roadmap: Redirects freed-up EMI funds to home loan prepayment
4. Marks education loan as "CLOSED" after final payment
5. Sees "Loan Paid Off! 🎉" celebration animation
6. Updates income (got a raise to ₹72,000) — AI recalculates roadmap
7. Checks updated Debt Severity Score: 6.1/10 → trending down
8. Uses AI chat to ask: "What's the best way to improve my credit score after OTS settlement?"
9. Refers FinRelief AI to a colleague facing similar issues
10. Eventually marks personal loan as settled — celebrates financial milestone

#### Emotional State
- **Returning to app:** Hopeful and committed
- **At each milestone:** Celebrating small wins 🎊
- **Overall trajectory:** From anxiety (7.2/10 severity) to empowerment (3.5/10 severity) over months
- **Emotional endpoint:** Grateful, financially confident, recommends app to others

#### Touchpoints
- Dashboard (recurring visits)
- Loan status update functionality
- Progress celebration animations
- Updated debt severity score
- AI recovery chat
- Referral program

#### Pain Points at This Stage
1. ❌ Motivation may drop between milestones (months of slow progress)
2. ❌ Income changes or unexpected expenses can derail the roadmap
3. ❌ Credit score recovery is slow (6–18 months post-OTS)

#### Opportunities for FinRelief AI
1. ✅ Push notifications for EMI due dates and milestone reminders
2. ✅ Weekly progress email digest
3. ✅ "Re-analyze" feature when income/expenses change
4. ✅ Credit score improvement tracker (partner with CIBIL API)
5. ✅ Community forum: Connect users who've completed recovery (peer support)
6. ✅ Referral incentive program: "Help a friend, earn features"
7. ✅ Success certificate: "Debt-Free Milestone" shareable badge

---

## 3. Full Journey Summary Table

| Stage | User Goal | Key Actions | Emotion (Peak) | Top Pain Point | Top Opportunity |
|---|---|---|---|---|---|
| **1. Awareness** | Find a solution to debt stress | Google search → landing page | Anxious → Hopeful | Generic results | SEO + empathetic hero section |
| **2. Registration** | Create account safely | Sign up → email verify | Cautious → Relieved | Data privacy concern | Clear privacy promise |
| **3. Profile Setup** | Set financial baseline | Enter income/expenses | Engaged → Surprised | Unclear terminology | Tooltips + instant insights |
| **4. Loan Entry** | See all debts together | Add 3 loans | Focused → Shocked | Seeing total debt | Encouraging copy + charts |
| **5. AI Analysis** | Get personalized plan | Generate analysis | Anxious → Grateful | Wait time | Streaming responses + clear results |
| **6. Settlement** | Understand OTS options | Explore settlement | Uncertain → Hopeful | Credit score impact | Honest, complete explanation |
| **7. Letter Gen.** | Create formal OTS letter | Fill form → generate → send | Nervous → Empowered | Getting letter right | Professional AI output + editing |
| **8. Recovery** | Track debt freedom journey | Return visits, updates | Anxious → Celebrating | Staying motivated | Milestones + community |

---

## 4. Overall Emotional Journey (Satisfaction Curve)

```
Satisfaction
     ▲
  5  │         ●─────●                              ●─────●
     │       /         \                          /         \
  4  │      ●           ●                        ●           ●
     │    /               \                    /
  3  │   ●                 ●                  ●
     │                       \              /
  2  │                         ●────────●
     │
  1  │●
     │
     └────────────────────────────────────────────────────────────▶
       Aware  Regist  Profile  Loans  Analysis  Settle  Letter  Recovery
```

*Key insight: There is a significant emotional dip at the Loan Entry stage (seeing all debt consolidated for the first time). FinRelief AI must design carefully around this moment — providing immediate reassurance and a "this is the first step to solving it" framing.*

---

*Document prepared by: Team FinRelief AI | SmartBridge Google Cloud Generative AI Internship | Vishnu Institute of Technology, Bhimavaram*
