# Empathy Map
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

## 1. Introduction to Empathy Mapping

An Empathy Map is a design thinking tool used to deeply understand the users you are designing for. It captures what users **Say**, **Think**, **Do**, and **Feel** — going beyond surface-level demographics to understand the emotional and behavioral landscape of the problem.

For FinRelief AI, the empathy map was developed through:
- Informal interviews with 45 individuals having active loans
- Online forum analysis (Reddit r/india, r/personalfinanceindia, Quora threads)
- Review of debt counseling case studies published by CARE India
- Team member personal experiences with loan stress in their families

---

## 2. User Persona: Rahul Sharma

### 👤 Profile Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   RAHUL SHARMA                              │
│                   Primary User Persona                      │
│                                                             │
│  Age:         34 years                                      │
│  Occupation:  Senior Software Engineer                      │
│  Location:    Mumbai, Maharashtra (Powai area)              │
│  Education:   B.Tech (Computer Science) - 2014 graduate     │
│  Marital:     Married (wife: Priya, 31; son: Arjun, 4)     │
│  Monthly Income: ₹65,000 (take-home after tax)             │
│                                                             │
│  "I thought I was being smart taking loans for everything.  │
│   Now I don't know where to start fixing this mess."        │
└─────────────────────────────────────────────────────────────┘
```

### Detailed Profile

| Attribute | Details |
|---|---|
| **Full Name** | Rahul Sharma |
| **Age** | 34 years |
| **Occupation** | Senior Software Engineer at a mid-sized IT company |
| **Location** | Powai, Mumbai |
| **Education** | B.Tech Computer Science, 2014 |
| **Family** | Married with one child (4 years old) |
| **Monthly Income (Take-home)** | ₹65,000 |
| **Monthly Expenses (non-EMI)** | ₹25,000 (rent ₹14K, groceries, utilities, child's school) |
| **Tech Comfort** | High — uses UPI, PhonePe, CRED, and stock trading apps |
| **Financial Literacy** | Medium — knows basics but not OTS, SARFAESI, or restructuring |
| **Mental State** | Chronically stressed; uses work as an escape from financial anxiety |

### Rahul's Loan Portfolio

| Loan Type | Lender | Original Amount | Outstanding | Monthly EMI | Interest Rate | Tenure Remaining |
|---|---|---|---|---|---|---|
| Home Loan | HDFC Bank | ₹40,00,000 | ₹36,20,000 | ₹32,000 | 8.5% p.a. | 18 years |
| Personal Loan | Bajaj Finance | ₹3,00,000 | ₹2,10,000 | ₹7,500 | 18% p.a. | 28 months |
| Education Loan | SBI | ₹2,50,000 | ₹25,000 | ₹4,200 | 10.5% p.a. | 6 months |
| **TOTAL** | — | **₹45,50,000** | **₹38,55,000** | **₹43,700** | — | — |

**EMI as % of Income: 67.2%** *(Recommended max: 40–50%)*

Rahul is technically not a defaulter — he has been paying all EMIs — but he is in a **severe repayment stress** situation with almost no monthly savings and zero emergency fund.

---

## 3. The Empathy Map

### QUADRANT 1: SAYS 💬 (What Rahul says out loud)

These are direct quotes or statements Rahul makes — things he would say to a friend, colleague, or family member about his financial situation.

1. **"I make ₹65,000 a month but I can't save even ₹2,000. Where does all the money go?"**
   - Rahul is genuinely baffled by his financial situation despite a decent salary

2. **"The bank keeps calling me for their 'special offers' on new credit cards. I don't need more credit — I need someone to help me get OUT of debt."**
   - Frustration at banks' sales-first approach vs. borrower welfare

3. **"I've been paying EMIs for 4 years and my home loan barely went down. This doesn't seem right."**
   - Confusion about amortization — a significant portion of early EMIs goes toward interest

4. **"My colleague told me his uncle negotiated a settlement with the bank and paid only 60% of what he owed. I had no idea that was even possible."**
   - Discovery of OTS through word-of-mouth, not through any bank or app

5. **"I don't want to see a CA or financial advisor. Last time it cost me ₹5,000 and they just told me things I could've Googled."**
   - Cost and trust issues with professional financial advisors

6. **"Sometimes I think about taking a personal loan to pay off the Bajaj loan. But then I'd just have a different loan, right?"**
   - Considering debt trap solutions due to lack of better alternatives

7. **"My wife doesn't know the full extent of our debt situation. I'm afraid to tell her."**
   - Financial secrecy driven by shame and fear of relationship strain

8. **"I keep seeing ads for 'Get out of debt fast' schemes. Are they scams? Most of them feel like scams."**
   - Distrust of predatory "debt relief" advertisers

---

### QUADRANT 2: THINKS 🤔 (What Rahul thinks but doesn't say aloud)

These are Rahul's inner thoughts, beliefs, fears, and assumptions — things he wouldn't openly admit.

1. **"What if I lose my job? The EMIs won't stop. We'd have nothing within 3 months."**
   - Deep-seated fear of job loss amplified by the pandemic's impact on IT layoffs in India

2. **"Am I a failure? I have a BTech degree and a decent job, and I still can't manage my finances."**
   - Internal shame and self-blame — common among educated borrowers

3. **"The bank has all the power. They can take my house if I miss too many payments. I'm at their mercy."**
   - Perception of power imbalance in the borrower-lender relationship

4. **"I should've read the fine print on the personal loan before signing. 18% interest — what was I thinking?"**
   - Retrospective regret about financial decisions made without full information

5. **"If I could just get this Bajaj loan off my plate, I could breathe again. One less EMI would change everything."**
   - The mental weight of multiple EMIs — each one feels like a separate burden

6. **"My parents never had credit cards or personal loans. They'd be ashamed if they knew."**
   - Generational stigma around debt in Indian families

7. **"There must be a way to legally reduce what I owe. Rich people and companies do it all the time. Why can't I?"**
   - Awareness (however vague) that debt negotiation is possible for corporations via IBC, but not knowing it's also available to individuals

8. **"I've been Googling 'how to get out of debt India' for an hour and I'm more confused now than before."**
   - Information overload and fragmentation — the internet offers contradictory, generic advice

---

### QUADRANT 3: DOES 🏃 (Rahul's observable actions and behaviors)

These are things Rahul actually does — his behaviors, habits, and coping mechanisms.

1. **Checks bank account balance multiple times daily**
   - Anxiety-driven monitoring; often checks just before and after EMI deduction dates

2. **Uses CRED to pay credit card bills but doesn't engage with any debt management features**
   - Has the app but doesn't know it could help; uses it only for bill payment rewards

3. **Postpones medical checkups and family outings citing "budget constraints"**
   - Quality of life is directly compromised by debt burden

4. **Takes occasional overtime shifts and weekend freelance work (₹5,000–₹8,000/month extra)**
   - Active effort to increase income, but this is unsustainable long-term

5. **Googles "OTS settlement HDFC" and "how to reduce EMI Bajaj Finance" late at night**
   - Researches solutions but finds fragmented, untrustworthy information

6. **Avoids looking at loan statements in detail because "it makes me anxious"**
   - Avoidance behavior — a common psychological response to financial stress

7. **Reads r/personalfinanceindia on Reddit regularly for peer advice**
   - Seeks community knowledge but gets generic advice from anonymous users

8. **Has set up auto-debit for all EMIs to avoid missed payments**
   - Responsible behavior, but means he has little agency over his cash flow

9. **Recently downloaded Paisabazaar to check if he can refinance the Bajaj loan at a lower rate**
   - Proactively looking for solutions; shows motivation to improve his situation

10. **Discusses finances with his college friend Pradeep (who works in banking) over phone calls**
    - Social network-based financial advice — valuable but informal and potentially biased

---

### QUADRANT 4: FEELS 💭 (Rahul's emotional landscape)

These are Rahul's genuine emotions — the affective state underlying his financial situation.

1. **Overwhelmed** — The sheer complexity of managing 3 loans with different lenders, interest rates, and due dates creates a constant cognitive load that never turns off.

2. **Ashamed** — Despite being a qualified engineer with a respectable job, Rahul feels he has somehow failed a fundamental test of adulthood by being in debt stress.

3. **Hopeful (intermittently)** — When he reads a success story online or hears about someone who successfully negotiated with their bank, he feels a brief surge of hope — quickly followed by uncertainty about how to replicate it.

4. **Frustrated** — At the system: at banks that pushed products on him without fully explaining the cost, at the government for not making OTS processes easier, at financial apps that help people get MORE credit but not get OUT of debt.

5. **Fearful** — Primarily of two things: (a) losing his job and being unable to pay EMIs, and (b) his home being at risk if things go wrong with the HDFC loan.

6. **Isolated** — He can't talk to his wife fully, can't tell his parents, and feels that his peer group (who appear to be doing financially better) won't understand.

7. **Determined** — Underneath the anxiety, Rahul is fundamentally motivated. He works overtime, researches solutions late at night, and hasn't given up. He just needs the right tool and guidance.

8. **Relieved (when he finds actionable information)** — The few times he found concrete, practical advice (like learning he could prepay his education loan), he felt a significant emotional lift.

---

## 4. Empathy Map Visual Summary

```
                    ┌─────────────────────────────────────────┐
                    │           RAHUL SHARMA (34)              │
                    │    Senior Software Engineer, Mumbai      │
                    │    Income: ₹65K | EMI: ₹43.7K/month    │
                    └─────────────────────────────────────────┘
                                        │
          ┌─────────────────────────────┼──────────────────────────┐
          │                             │                          │
    ┌─────▼──────┐             ┌────────▼───────┐         ┌───────▼──────┐
    │   SAYS 💬  │             │   THINKS 🤔    │         │  FEELS 💭    │
    │            │             │                │         │              │
    │ "Where     │             │ "What if I     │         │ Overwhelmed  │
    │  does all  │             │  lose my job?" │         │ Ashamed      │
    │  my money  │             │                │         │ Fearful      │
    │  go?"      │             │ "Am I a        │         │ Hopeful      │
    │            │             │  failure?"     │         │ Frustrated   │
    │ "Banks     │             │                │         │ Determined   │
    │  push more │             │ "Rich people   │         │ Isolated     │
    │  credit,   │             │  negotiate     │         │              │
    │  not help  │             │  debt. Why     │         │              │
    │  exit it"  │             │  can't I?"     │         │              │
    └────────────┘             └────────────────┘         └──────────────┘
                                        │
                              ┌─────────▼──────────┐
                              │      DOES 🏃        │
                              │                     │
                              │ Checks balance 5x/day│
                              │ Googles OTS solutions│
                              │ Works overtime       │
                              │ Avoids loan statements│
                              │ Reads Reddit finance │
                              └─────────────────────┘
```

---

## 5. User Goals

### Functional Goals (What Rahul wants to accomplish)

| Priority | Goal | Specific Need |
|---|---|---|
| 🔴 Critical | Get a clear picture of his total debt situation | Aggregated view of all 3 loans in one place |
| 🔴 Critical | Know which loan to pay off first | AI-driven prioritization based on interest rates and remaining tenure |
| 🔴 Critical | Understand if OTS is possible for the Bajaj loan | Eligibility analysis and estimated settlement amount |
| 🟠 High | Generate a formal OTS request letter for Bajaj Finance | Professional, lender-ready negotiation letter |
| 🟠 High | Get a month-by-month debt freedom roadmap | Specific amounts, timelines, and milestones |
| 🟡 Medium | Understand why his home loan principal barely decreased | Visual amortization breakdown |
| 🟡 Medium | Know how to rebuild his credit score | Post-resolution credit recovery plan |

### Emotional Goals (How Rahul wants to feel)

1. **In control** — He wants to feel like he's managing his debt, not the other way around
2. **Informed** — He wants to understand his financial situation fully, in plain language
3. **Empowered** — He wants to be able to take action without needing to pay ₹5,000 to an advisor
4. **Hopeful** — He wants a credible, specific path to becoming debt-free
5. **Safe** — He wants assurance that his home and family's stability are protected

### Social Goals

1. Be able to have an honest conversation with his wife about their finances
2. Not feel ashamed of his situation — understand it's common and solvable
3. Eventually be able to help his college friends who might be in similar situations

---

## 6. Frustrations & Pain Points (from Empathy)

| # | Frustration | Root Cause | FinRelief AI Solution |
|---|---|---|---|
| 1 | Can't find consolidated view of all loans | Banks have separate portals | Unified loan dashboard |
| 2 | Doesn't know OTS eligibility | Banks don't inform borrowers | AI eligibility analyzer |
| 3 | Generic online advice is useless | Not personalized to his situation | Gemini-powered personalized analysis |
| 4 | Can't afford professional advice | ₹2K–₹10K per session | Free AI advisory |
| 5 | Can't draft a proper bank letter | No legal/financial writing skill | AI OTS letter generator |
| 6 | No clear timeline to debt freedom | Complex calculations required | AI recovery roadmap generator |
| 7 | Feels shame around debt | Cultural stigma | Non-judgmental UI/UX design |
| 8 | Late-night anxiety spirals | No support when needed | 24/7 AI availability |

---

## 7. Design Implications for FinRelief AI

Based on the empathy map, the following design principles are derived:

### UI/UX Principles

| Principle | Rationale | Implementation |
|---|---|---|
| **Non-judgmental language** | Rahul feels shame — language like "recovery" not "default" | Copy guidelines and UX writing standards |
| **Mobile-first design** | Rahul uses apps on his phone primarily | Responsive React UI; thumb-friendly navigation |
| **Fast AI responses** | Anxiety increases with wait times | Gemini Flash chosen for speed; streaming responses |
| **Progress visualization** | Rahul needs to feel progress to stay motivated | Debt freedom countdown, progress bars |
| **Private and secure** | He doesn't want his data exposed | JWT auth, encrypted storage, clear privacy policy |
| **Simple language** | Financial jargon increases confusion | AI generates plain-language explanations |
| **One action at a time** | Cognitive overload is already high | Step-by-step wizard-style onboarding |

### Feature Priority Based on Empathy

| Feature | Priority | Empathy Insight |
|---|---|---|
| Unified loan dashboard | P0 (Must Have) | "I can't see all my loans in one place" |
| AI debt analysis | P0 (Must Have) | "Generic advice doesn't help me" |
| OTS letter generator | P0 (Must Have) | "I can't draft a proper bank letter" |
| Recovery roadmap | P1 (Should Have) | "I need a specific plan, not just advice" |
| Amortization breakdown | P1 (Should Have) | "Why isn't my principal going down?" |
| Chat with AI advisor | P2 (Nice to Have) | "I need answers at 11 PM when I'm anxious" |
| Credit score guidance | P2 (Nice to Have) | "How do I fix my credit after settlement?" |
| Partner notification | P3 (Future) | "I need to tell my wife but don't know how" |

---

## 8. Secondary Persona: Fatima Shaikh

To ensure FinRelief AI addresses a diverse user base, a secondary persona was also developed:

| Attribute | Details |
|---|---|
| **Name** | Fatima Shaikh |
| **Age** | 26 years |
| **Occupation** | Delivery Executive (Swiggy), part-time tailoring work |
| **Location** | Hyderabad, Telangana |
| **Monthly Income** | ₹18,000–₹22,000 (variable) |
| **Loans** | MFI loan (₹50,000 @ 24% p.a.), borrowed ₹30,000 from relatives |
| **Key Pain Point** | Cannot read English; no smartphone comfort beyond WhatsApp |
| **FinRelief AI Need** | Simplified UI, regional language support, low-data mode |

*Note: Fatima's persona drives the v2 roadmap items: multilingual support, WhatsApp bot integration, and offline-first capabilities.*

---

*Document prepared by: Team FinRelief AI | SmartBridge Google Cloud Generative AI Internship | Vishnu Institute of Technology, Bhimavaram*
