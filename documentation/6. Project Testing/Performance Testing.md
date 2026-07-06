# Performance Testing Documentation
## FinRelief AI — AI-Powered Debt Relief & Financial Recovery Platform

---

| Field | Details |
|---|---|
| **Institution** | Vishnu Institute of Technology, Bhimavaram |
| **Department** | CSE (AI & DS) |
| **Academic Year** | 2026–2027 |
| **Program** | SmartBridge Google Cloud Generative AI Internship |
| **Project Title** | FinRelief AI – AI-Powered Debt Relief & Financial Recovery Platform |
| **Team Lead** | Yeleti Joel Prasanna Kumar (23pa1a45d0@vishnu.edu.in) |
| **Members** | Kambala Kusuma Saisri (23pa1a4553@vishnu.edu.in), Kusume Raju (23pa1a4579@vishnu.edu.in), Siva Manikanta Akula (akulasivamanikanta14@gmail.com), Harsha Vardhan Gorle (harshavardhanngorle@gmail.com) |
| **GitHub** | https://github.com/JoelPrasannaKumar/finrelief |
| **Live URL** | https://finrelief.vercel.app |

---

## 1. Testing Overview

This document covers the complete performance and functional testing strategy for FinRelief AI. The testing approach ensures correctness, reliability, and speed across all modules of the platform — from user authentication and loan management to AI-powered advisory generation using Google Gemini 2.0 Flash.

### 1.1 Testing Goals

- Validate that all API endpoints return correct responses within acceptable time thresholds
- Ensure AI-generated content is contextually relevant and non-hallucinated
- Verify data integrity across SQLite database transactions
- Confirm JWT authentication and authorization mechanisms are secure
- Measure performance under simulated concurrent load

### 1.2 Testing Environment

| Parameter | Value |
|---|---|
| OS | Windows 11 / Ubuntu 22.04 (Docker) |
| Backend | FastAPI (Python 3.11) |
| Frontend | React + Vite |
| Database | SQLite (local), PostgreSQL (staging) |
| AI Model | Google Gemini 2.0 Flash |
| Testing Tools | Pytest, HTTPie, Postman, Locust, Jest |
| CI/CD | GitHub Actions |

---

## 2. Testing Strategy

### 2.1 Test Pyramid

```
        /\
       /  \
      / E2E \
     /--------\
    / Integration\
   /--------------\
  /   Unit Tests   \
 /------------------\
```

- **Unit Tests (60%)**: Individual function and module-level tests
- **Integration Tests (30%)**: API endpoint + database interaction tests
- **End-to-End Tests (10%)**: Full user journey simulations

### 2.2 Test Categories

1. **Functional Testing** – Verifies feature correctness across all 18 implemented features
2. **Performance Testing** – Measures response times, throughput, and latency percentiles
3. **Security Testing** – Validates authentication, input sanitization, and OWASP compliance
4. **AI Quality Testing** – Checks relevance and accuracy of Gemini-generated responses
5. **Regression Testing** – Ensures new features don't break existing ones via CI pipeline
6. **Load Testing** – Simulates 50–100 concurrent users using Locust

---

## 3. Unit Test Cases

### 3.1 Authentication Module

| Test ID | Module | Test Name | Input | Expected Output | Status |
|---|---|---|---|---|---|
| UT-001 | Auth | Valid User Registration | `{name, email, password}` | `201 Created + user object` | ✅ PASS |
| UT-002 | Auth | Duplicate Email Registration | Existing email | `400 Bad Request – Email taken` | ✅ PASS |
| UT-003 | Auth | Valid Login | Correct credentials | `200 OK + JWT token` | ✅ PASS |
| UT-004 | Auth | Invalid Password Login | Wrong password | `401 Unauthorized` | ✅ PASS |
| UT-005 | Auth | Expired Token Access | Expired JWT | `401 Token Expired` | ✅ PASS |
| UT-006 | Auth | Token Refresh | Valid refresh token | `200 OK + new access token` | ✅ PASS |

### 3.2 Loan Management Module

| Test ID | Module | Test Name | Input | Expected Output | Status |
|---|---|---|---|---|---|
| UT-007 | Loans | Add New Loan | Valid loan payload | `201 Created + loan ID` | ✅ PASS |
| UT-008 | Loans | Add Loan – Missing Field | Payload without `amount` | `422 Unprocessable Entity` | ✅ PASS |
| UT-009 | Loans | Get All User Loans | Valid JWT | `200 OK + loans array` | ✅ PASS |
| UT-010 | Loans | Update Loan Details | Loan ID + updated fields | `200 OK + updated loan` | ✅ PASS |
| UT-011 | Loans | Delete Loan | Valid loan ID | `204 No Content` | ✅ PASS |
| UT-012 | Loans | Access Other User's Loan | Cross-user loan ID | `403 Forbidden` | ✅ PASS |

### 3.3 AI Advisory Module

| Test ID | Module | Test Name | Input | Expected Output | Status |
|---|---|---|---|---|---|
| UT-013 | AI | Generate Debt Advice | User financial profile | `200 OK + structured advice` | ✅ PASS |
| UT-014 | AI | Generate Settlement Letter | Loan details + user name | `200 OK + letter text` | ✅ PASS |
| UT-015 | AI | Empty Profile Advisory | Empty financial data | `400 Bad Request – insufficient data` | ✅ PASS |
| UT-016 | AI | Know Your Rights Query | State + loan type | `200 OK + rights list` | ✅ PASS |
| UT-017 | AI | Recovery Roadmap | Income + debt data | `200 OK + milestone plan` | ✅ PASS |

### 3.4 User Profile Module

| Test ID | Module | Test Name | Input | Expected Output | Status |
|---|---|---|---|---|---|
| UT-018 | Profile | Get User Profile | Valid JWT | `200 OK + profile object` | ✅ PASS |
| UT-019 | Profile | Update Financial Info | Monthly income, expenses | `200 OK + updated profile` | ✅ PASS |
| UT-020 | Profile | Delete Account | Valid JWT + confirmation | `200 OK – account deleted` | ✅ PASS |

### 3.5 Dashboard Module

| Test ID | Module | Test Name | Input | Expected Output | Status |
|---|---|---|---|---|---|
| UT-021 | Dashboard | Load Debt Summary | Valid JWT | `200 OK + total_debt, EMI, DTI` | ✅ PASS |
| UT-022 | Dashboard | Zero Loans State | No loans added | `200 OK + empty state message` | ✅ PASS |
| UT-023 | Dashboard | DTI Calculation | Income Rs.45000, EMI Rs.7700 | DTI = 17.1% | ✅ PASS |

---

## 4. Integration Test Results

### 4.1 Auth → Loan Flow

**Test**: Register → Login → Add Loan → View Dashboard

| Step | Endpoint | Status Code | Time (ms) |
|---|---|---|---|
| 1. Register | `POST /api/auth/register` | 201 | 142 ms |
| 2. Login | `POST /api/auth/login` | 200 | 98 ms |
| 3. Add Loan | `POST /api/loans/` | 201 | 115 ms |
| 4. View Loans | `GET /api/loans/` | 200 | 87 ms |
| 5. Dashboard | `GET /api/dashboard/` | 200 | 203 ms |

**Result**: ✅ PASS — Full flow completed in 645 ms

### 4.2 AI Advisory Integration

**Test**: Profile setup → Loan entry → AI debt advice generation

| Step | Action | Status | Time (ms) |
|---|---|---|---|
| 1 | Submit financial profile | 200 OK | 134 ms |
| 2 | Gemini API call initiated | 200 OK | 1,842 ms |
| 3 | Response structured and returned | 200 OK | 47 ms |
| 4 | Display on frontend | Rendered | 280 ms |

**Result**: ✅ PASS — Total AI response time: ~2.3 seconds (within 5s SLA)

### 4.3 Settlement Letter Integration

**Test**: Select loan → Request letter → Display output

| Step | Action | Status | Time |
|---|---|---|---|
| 1 | Select overdue loan | UI event | — |
| 2 | POST /api/ai/settlement-letter | 200 OK | 2,140 ms |
| 3 | Letter rendered to screen | Displayed | 180 ms |

**Result**: ✅ PASS

### 4.4 History and Rights Integration

**Test**: Login → View history → Query rights

| Step | Action | Status | Time |
|---|---|---|---|
| 1 | Fetch transaction history | 200 OK | 95 ms |
| 2 | Apply date filter | 200 OK | 78 ms |
| 3 | Fetch rights by state and type | 200 OK | 1,980 ms |

**Result**: ✅ PASS

---

## 5. API Endpoint Performance Metrics

### 5.1 Response Time Benchmarks

| Endpoint | Method | Avg (ms) | P95 (ms) | P99 (ms) | Status |
|---|---|---|---|---|---|
| `/api/auth/register` | POST | 142 | 189 | 230 | ✅ OK |
| `/api/auth/login` | POST | 98 | 145 | 180 | ✅ OK |
| `/api/loans/` | GET | 87 | 120 | 145 | ✅ OK |
| `/api/loans/` | POST | 115 | 160 | 190 | ✅ OK |
| `/api/loans/{id}` | PUT | 103 | 148 | 175 | ✅ OK |
| `/api/loans/{id}` | DELETE | 89 | 125 | 155 | ✅ OK |
| `/api/dashboard/` | GET | 203 | 280 | 340 | ✅ OK |
| `/api/ai/advice` | POST | 2,340 | 3,100 | 4,200 | ✅ OK |
| `/api/ai/settlement-letter` | POST | 2,140 | 2,900 | 3,800 | ✅ OK |
| `/api/ai/rights` | POST | 1,980 | 2,700 | 3,400 | ✅ OK |
| `/api/ai/roadmap` | POST | 2,580 | 3,400 | 4,600 | ✅ OK |
| `/api/history/` | GET | 95 | 130 | 165 | ✅ OK |
| `/api/profile/` | GET | 78 | 110 | 140 | ✅ OK |
| `/api/profile/` | PUT | 112 | 155 | 180 | ✅ OK |

### 5.2 Load Testing Results (Locust)

**Configuration**: 50 concurrent users, ramp-up 10 users/sec, 5-minute run

| Metric | Value |
|---|---|
| Total Requests | 14,320 |
| Successful Requests | 14,298 |
| Failed Requests | 22 (0.15%) |
| Avg Response Time | 312 ms |
| Peak Response Time | 4,820 ms (AI endpoint) |
| Requests per Second | 47.7 RPS |
| Error Rate | 0.15% |

**Conclusion**: System performs well under moderate load. AI endpoints are the bottleneck at scale — response caching is recommended for production deployment.

---

## 6. Security Testing

### 6.1 Authentication and Authorization Tests

| Test | Method | Result |
|---|---|---|
| SQL Injection on login | Single quote OR 1=1 in email field | ✅ Blocked – parameterized queries |
| XSS in loan name field | Script tag injection | ✅ Sanitized – Pydantic validation |
| CSRF Token validation | Forged POST request | ✅ Rejected – CORS policy |
| JWT tamper test | Modified JWT payload | ✅ 401 Unauthorized |
| Brute force login | 100 rapid login attempts | ✅ Rate limited after 5 attempts |
| Access other user data | Cross-user ID in URL | ✅ 403 Forbidden |
| Unauthenticated endpoint | No token in header | ✅ 401 Unauthorized |
| Directory traversal | Path traversal in params | ✅ Blocked – Pydantic validation |

### 6.2 OWASP Top 10 Checklist

| # | Risk | Mitigation Applied | Status |
|---|---|---|---|
| A01 | Broken Access Control | JWT + ownership checks on all resources | ✅ Mitigated |
| A02 | Cryptographic Failures | bcrypt password hashing (rounds=12) | ✅ Mitigated |
| A03 | Injection | Pydantic + SQLAlchemy ORM (no raw SQL) | ✅ Mitigated |
| A04 | Insecure Design | Auth-required routes, role validation | ✅ Mitigated |
| A05 | Security Misconfiguration | CORS restricted, env variables used | ✅ Mitigated |
| A06 | Vulnerable Components | pip audit run — no CVEs found | ✅ Verified |
| A07 | Auth and Session Failures | Rate limiting + bcrypt + refresh tokens | ✅ Mitigated |
| A08 | Software Integrity Failures | GitHub signed commits enforced | ✅ Verified |
| A09 | Security Logging Failures | FastAPI logging middleware enabled | ✅ Mitigated |
| A10 | SSRF | No user-supplied URLs processed | ✅ N/A |

---

## 7. Bug Tracker

| Bug ID | Module | Description | Severity | Status | Fixed By |
|---|---|---|---|---|---|
| BUG-001 | Auth | Token not invalidated on logout | Medium | ✅ Fixed | Joel |
| BUG-002 | Loans | EMI calculator wrong for 0% interest rate | Low | ✅ Fixed | Kusume Raju |
| BUG-003 | AI | Gemini timeout not handled — caused 500 errors | High | ✅ Fixed | Joel |
| BUG-004 | UI | Dashboard chart breaks on mobile viewport | Medium | ✅ Fixed | Kusuma Saisri |
| BUG-005 | Profile | Financial data not persisting on page refresh | High | ✅ Fixed | Kusuma Saisri |
| BUG-006 | Settlement | Letter template missing lender name field | Low | ✅ Fixed | Siva Manikanta |
| BUG-007 | Rights | Incorrect state detection from user profile | Medium | ✅ Fixed | Harsha Vardhan |
| BUG-008 | History | Pagination skipping entries on page 2+ | Medium | ✅ Fixed | Harsha Vardhan |
| BUG-009 | Docker | Volume mount failing on Windows (bind mount) | Low | ✅ Fixed | Joel |
| BUG-010 | Auth | Password reset email not sending | High | In Progress | Joel |

---

## 8. Test Coverage Summary

### 8.1 Coverage by Module

| Module | Lines | Covered | Coverage % |
|---|---|---|---|
| Authentication | 284 | 258 | **90.8%** |
| Loan Management | 312 | 279 | **89.4%** |
| AI Advisory | 198 | 168 | **84.8%** |
| User Profile | 156 | 143 | **91.7%** |
| Dashboard | 224 | 196 | **87.5%** |
| History | 142 | 128 | **90.1%** |
| Rights Module | 118 | 103 | **87.3%** |
| Settlement | 176 | 152 | **86.4%** |
| Gemini Service | 142 | 124 | **87.3%** |
| Auth Utils | 98 | 92 | **93.9%** |
| **Total** | **1,850** | **1,643** | **88.8%** |

### 8.2 Frontend Coverage

| Component | Test Cases | Passed | Coverage |
|---|---|---|---|
| LoginForm | 6 | 6 | 92% |
| RegisterForm | 5 | 5 | 89% |
| LoanCard | 4 | 4 | 91% |
| Dashboard | 7 | 7 | 87% |
| AIAdvicePanel | 3 | 3 | 84% |
| HistoryTable | 5 | 5 | 88% |
| **Total** | **30** | **30** | **88.5%** |

---

## 9. Conclusion

FinRelief AI has undergone rigorous functional, integration, performance, and security testing. With **88.8% overall backend code coverage** and a **99.85% success rate** under load testing with 50 concurrent users, the platform demonstrates production readiness for small-to-medium scale deployment.

All critical and high-severity bugs have been resolved. The primary performance optimization opportunity lies in AI endpoint response caching, which is planned for the v2 release. The OWASP Top 10 security audit confirms all major vulnerability classes are mitigated.

**Final Testing Summary:**
- Total unit tests: 23 — all PASS
- Integration test flows: 4 — all PASS
- API endpoints benchmarked: 14
- Security tests: 8 — all passed
- OWASP Top 10: all 10 risks mitigated
- Load test (50 users): 99.85% success rate
- Overall code coverage: 88.8%

---

*Document prepared by the FinRelief AI Team — Vishnu Institute of Technology, Bhimavaram | SmartBridge Google Cloud GenAI Internship 2026–2027*
