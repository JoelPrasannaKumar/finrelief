# Define Problem Statements
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

## 1. Executive Summary

The Indian personal debt ecosystem is fundamentally broken for the borrower. Despite decades of financial inclusion initiatives, the average Indian borrower — particularly those in the lower-middle-income segment — lacks access to:

1. **Personalized financial counseling** to manage multiple concurrent loans
2. **Knowledge of legal settlement options** (OTS, debt restructuring) available to them
3. **Tools to negotiate directly with lenders** in an informed, assertive manner
4. **Clear, data-driven recovery roadmaps** tailored to their unique financial situation

FinRelief AI exists to close this gap using the power of Google's Gemini 2.0 Flash Generative AI.

---

## 2. Formal Problem Statement

> **"Indian borrowers with multiple active loans — particularly those facing repayment stress — lack access to affordable, personalized, and actionable debt relief guidance. Existing financial tools focus on credit acquisition rather than debt recovery, leaving millions of borrowers without clear pathways to financial freedom. There is no widely accessible, AI-powered platform that can analyze an individual's complete debt profile, generate legally informed OTS (One-Time Settlement) negotiation letters, and provide a personalized step-by-step financial recovery plan."**

### Problem Statement Decomposition

| Dimension | Description |
|---|---|
| **Who** | Indian salaried employees, gig workers, and small business owners with 2+ active loans |
| **What** | Lack of personalized debt relief guidance, OTS knowledge, and negotiation tools |
| **When** | When borrowers experience repayment stress (missed EMIs, salary cuts, job loss) |
| **Where** | Across urban, semi-urban, and rural India where formal financial advisors are unavailable |
| **Why** | Financial illiteracy, absence of affordable advisory services, opaque banking processes |
| **How** | AI-driven analysis, automated letter generation, personalized roadmaps |

---

## 3. Target Users

### Primary Target Users: Indian Borrowers in Repayment Stress

**Age Range:** 22–55 years  
**Segments:**

| Segment | Description | Estimated Size |
|---|---|---|
| Salaried Employees | IT/non-IT workers with personal + home + vehicle loans | ~4.2 crore |
| Gig Economy Workers | Delivery executives, freelancers with microfinance loans | ~1.8 crore |
| Small Business Owners | MSMEs with business + personal loans | ~2.1 crore |
| Recent Graduates | Education loan borrowers with unstable early careers | ~0.9 crore |
| Rural Borrowers | Agricultural + MFI loan holders | ~3.0 crore |

### User Demographics Profile

| Attribute | Details |
|---|---|
| **Age** | 22–55 years (primary: 28–42) |
| **Income Range** | ₹25,000 – ₹1,00,000 per month |
| **Education** | Graduates and above (for primary persona); some secondary for rural segment |
| **Tech Literacy** | Mobile-first users; comfortable with apps like PhonePe, CRED |
| **Geography** | Tier-1, Tier-2, and Tier-3 Indian cities |
| **Language** | Primarily English and Hindi; future support for 10+ regional languages |
| **Loan Types** | Personal loans, education loans, home loans, vehicle loans, credit card debt |
| **Common Lenders** | SBI, HDFC, ICICI, Axis, Bajaj Finance, Muthoot, MFI lenders |

### Secondary Users

| User Type | Need |
|---|---|
| **Financial Counselors** | Tool to quickly analyze client debt profiles |
| **NGOs (debt relief)** | Bulk analysis and letter generation for clients |
| **Legal Aid Providers** | Draft standardized settlement communication |

---

## 4. Detailed Pain Points

### Pain Point 1: Complete Lack of Awareness About Settlement Options
**Severity: Critical** 🔴

Over 88% of distressed borrowers are unaware that they can legally negotiate a One-Time Settlement (OTS) with their lender. Banks are not obligated to proactively inform borrowers of this option. The RBI has issued guidelines on fair practices, but enforcement at ground level is minimal.

**Impact:** Borrowers continue paying high-interest EMIs or default entirely, destroying their credit score — when a negotiated settlement could have been the better path.

### Pain Point 2: Unaffordable Professional Financial Advice
**Severity: High** 🟠

Certified Financial Planners (CFPs) and debt counselors charge ₹2,000–₹10,000 per session. For a borrower already struggling with EMIs, this cost is prohibitive. Free government schemes (like DRT - Debt Recovery Tribunals) are complex, time-consuming, and not designed for individual small-ticket borrowers.

**Impact:** Borrowers make uninformed financial decisions — often taking new loans to repay old ones (debt trap spiral).

### Pain Point 3: Complexity of Multi-Loan Management
**Severity: High** 🟠

A borrower with 3–5 active loans (home loan, personal loan, credit card, vehicle loan, education loan) must juggle multiple EMI dates, interest rates, outstanding balances, lender contacts, and repayment schedules. There is no single platform that aggregates this information and provides a holistic view.

**Impact:** Borrowers miss EMI due dates, incur late payment penalties, and experience score degradation — accelerating their debt spiral.

### Pain Point 4: Psychological and Emotional Distress
**Severity: High** 🟠

Studies by NIMHANS and Suicide Prevention India Foundation link financial stress to mental health deterioration. Borrowers report:
- Constant anxiety about calls from recovery agents
- Social shame preventing them from seeking help
- Decision paralysis when facing multiple debt obligations
- Hopelessness — the feeling that there's "no way out"

**Impact:** Mental health deterioration reduces work performance, further impacting income and repayment capacity.

### Pain Point 5: Inability to Draft Professional Negotiation Communication
**Severity: Medium-High** 🟡

Even borrowers who know about OTS or restructuring options often cannot draft a professional, legally appropriate letter to their bank. They lack knowledge of:
- Regulatory language (SARFAESI Act references, RBI Fair Practices Code)
- Proper format for OTS proposals
- What documentation to attach
- Tone and framing that increases approval likelihood

**Impact:** Amateur or poorly worded settlement requests are rejected by lenders, leaving borrowers worse off.

### Pain Point 6: No Personalized Recovery Roadmap
**Severity: Medium** 🟡

Generic financial advice ("spend less, save more") is useless for someone with ₹8 lakh in debt and ₹55,000 monthly income. Borrowers need specific, actionable plans:
- Which loan to prioritize (avalanche vs. snowball method)?
- How much to negotiate off the principal in an OTS?
- What's the realistic timeline to become debt-free?
- How to rebuild credit score post-settlement?

**Impact:** Without a roadmap, borrowers feel lost and unmotivated, making recovery slower or impossible.

---

## 5. Current Solutions & Their Gaps

| Solution | What It Offers | Critical Gaps |
|---|---|---|
| **CRED** | Credit score monitoring, bill payments, reward points | No debt relief guidance; focuses on premium card users only |
| **Paisabazaar** | Loan comparison, credit score tracking | Loan acquisition focused; no repayment/recovery tools |
| **BankBazaar** | Financial product marketplace | No AI analysis; no debt management features |
| **MoneyControl** | Portfolio tracking, market data | No debt management; no AI advisory |
| **CIBIL App** | Credit score reports | Shows the problem (score) but offers no solution |
| **DRT (Govt)** | Debt recovery for banks | Designed for lenders, not borrowers; complex process |
| **Financial Advisors** | Personalized counseling | Expensive (₹2K-10K/session); not scalable; geography-limited |
| **WhatsApp Recovery Groups** | Peer support, informal advice | Unreliable, potentially legally incorrect advice |

### The Critical Gap

**No existing solution combines:**
1. ✅ Complete multi-loan aggregation
2. ✅ AI-powered debt severity analysis
3. ✅ OTS negotiation letter generation
4. ✅ Personalized financial recovery roadmap
5. ✅ Accessible pricing (free/freemium)
6. ✅ Non-judgmental, empathetic user experience

---

## 6. How AI Solves These Gaps

### AI Capability → Problem Mapping

| AI Capability | Problem Solved | FinRelief AI Feature |
|---|---|---|
| **Natural Language Generation** | Cannot draft negotiation letters | OTS Letter Generator |
| **Contextual Analysis** | No personalized advice | Debt Severity Analyzer |
| **Pattern Recognition** | Complex multi-loan scenarios | Recovery Roadmap Generator |
| **Conversational AI** | No 24/7 financial guidance | AI Financial Advisor Chat |
| **Document Understanding** | Cannot interpret loan agreements | Loan Document Explainer (v2) |
| **Multilingual Support** | Language barriers | Regional Language Support (v2) |

### Why AI is the Right Tool

Traditional rule-based systems cannot handle the **variability** of personal debt situations:
- Every borrower has a unique combination of loan types, lenders, interest rates, and life circumstances
- The language used in negotiation letters must be tailored to each specific loan account and lender
- Recovery timelines depend on dozens of interconnected financial variables

Generative AI — specifically Gemini 2.0 Flash — can process all these variables simultaneously and generate genuinely personalized, contextually appropriate responses that feel human-crafted but are generated at scale.

---

## 7. "How Might We" (HMW) Statements

HMW statements are a design thinking tool that reframe problems as opportunities for creative solutions.

### HMW Statement 1
> **"How might we make debt settlement knowledge as accessible as checking a WhatsApp message?"**

*Inspiration: The complexity of OTS processes should be hidden from the user; AI handles the complexity.*

### HMW Statement 2
> **"How might we help a borrower with three loans understand exactly which debt to attack first and why, in under 2 minutes?"**

*Inspiration: Speed and clarity are critical when users are anxious. The AI must be fast (Gemini Flash) and provide clear, unambiguous prioritization.*

### HMW Statement 3
> **"How might we replace the shame and stigma of debt with confidence and actionability?"**

*Inspiration: UI/UX must be non-judgmental. Terms like "debt relief" and "recovery" rather than "defaulters" or "overdue." Encouraging progress tracking.*

### HMW Statement 4
> **"How might we draft a bank negotiation letter that sounds like it was written by a ₹5,000/hour financial lawyer?"**

*Inspiration: The quality of AI-generated letters must be indistinguishable from expert-drafted ones to be taken seriously by lenders.*

### HMW Statement 5
> **"How might we give a borrower a clear, date-specific roadmap to financial freedom — one they can actually follow without a finance degree?"**

*Inspiration: The recovery plan must be actionable, not theoretical. Specific dates, amounts, and steps.*

### HMW Statement 6
> **"How might we ensure the AI never gives advice that could legally or financially harm the user?"**

*Inspiration: Critical for trust. AI responses must include appropriate disclaimers and never claim to be legal or financial advice.*

### HMW Statement 7
> **"How might we help a borrower track their emotional and financial recovery simultaneously?"**

*Inspiration: Debt relief is as much psychological as financial. Future versions could integrate wellbeing tracking with financial milestones.*

---

## 8. Success Metrics

### User Adoption Metrics

| Metric | Target (3 months post-launch) | Measurement Method |
|---|---|---|
| Registered Users | 500+ | Database user count |
| Active Monthly Users | 200+ | Login frequency tracking |
| Loans Entered | 1,500+ | Loan record count |
| AI Analyses Completed | 1,000+ | Analysis request logs |
| OTS Letters Generated | 300+ | Letter generation logs |

### User Satisfaction Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| User Satisfaction Score (CSAT) | ≥ 4.2/5.0 | In-app feedback form |
| Net Promoter Score (NPS) | ≥ 45 | Post-use survey |
| Task Completion Rate | ≥ 85% | Analytics tracking |
| Average Session Duration | ≥ 8 minutes | Analytics |
| Return User Rate | ≥ 60% | Login frequency |

### Technical Performance Metrics

| Metric | Target | Measurement Method |
|---|---|---|
| API Response Time (P95) | < 3 seconds | Server monitoring |
| AI Response Time | < 8 seconds | Gemini API latency logs |
| System Uptime | ≥ 99.5% | Uptime monitoring |
| TTFB (Time to First Byte) | < 500ms | Lighthouse audits |
| Lighthouse Score | ≥ 90 | Google Lighthouse |

### Business Impact Metrics (Long-term Vision)

| Metric | Vision |
|---|---|
| Users who successfully negotiated OTS | Track via optional success sharing |
| Average debt reduction facilitated | Survey-based estimation |
| Credit score improvement post-use | Optional credit score sharing |
| NGO partnerships | 5+ in Year 1 |

---

## 9. Problem Statement Validation

### Validation Methods Used

1. **Desk Research**: Analysis of RBI Annual Reports (2022–2024), CIBIL Quarterly Reports, SEBI Fair Practices guidelines
2. **Team Survey**: 5 team members conducted informal interviews with 8–10 people each (total ~45 interviews) with individuals who have active loans
3. **App Store Analysis**: Reviews of CRED, Paisabazaar, and MoneyControl apps — identifying recurring complaints about lack of debt relief features
4. **Academic Research**: Referenced papers on financial stress and mental health in India (NIMHANS, IIT research)

### Key Validation Findings

- **78% of interviewees** said they had no idea they could negotiate an OTS with their bank
- **91% of interviewees** said they would use a free AI tool if it could help manage their loans
- **64% of interviewees** reported significant anxiety related to loan repayment
- **Only 22% of interviewees** had ever consulted a financial advisor (primarily due to cost)

---

*Document prepared by: Team FinRelief AI | SmartBridge Google Cloud Generative AI Internship | Vishnu Institute of Technology, Bhimavaram*
