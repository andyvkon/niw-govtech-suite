# NIW GovTech Suite — Public-Benefit Projects (EN/UA/RU)

This repository hosts three small, production-ready, **public-interest** projects you can deploy and reference in an **EB2‑NIW** petition:

1) **helpmap/** — Multilingual map (Leaflet + OSM) for social resources (food banks, shelters, IDHS offices, clinics).  
2) **benefit-api/** — Minimal **FastAPI** backend serving resource data and anti‑scam education for seniors.  
3) **eldershield-course/** — Mini course (Markdown lessons) for senior anti‑scam literacy (for libraries/churches/NGOs).

> Goal: demonstrate **national importance**, **access & equity**, and your ability to build and deploy govtech tools.

---

## Quick Start

### 1) HelpMap (static website)
- Stack: **HTML + Leaflet (OpenStreetMap)**. No backend required.
- Deploy: Enable **GitHub Pages** on the `helpmap` folder (or copy it to a standalone repo).  
- Add points: edit `helpmap/data/resources.sample.json` (or inline array in `index.html`).  

### 2) Benefit API (FastAPI)
```bash
cd benefit-api
pip install -r requirements.txt
uvicorn main:app --reload
# open http://127.0.0.1:8000/docs
```
- Endpoints:  
  - `GET /resources?type=food|shelter|idhs|clinic&near=lat,lon&radius=10&q=term`  
  - `GET /education/anti-scam`  

### 3) ElderShield Course
- Print Markdown lessons or serve them from GitHub.  
- Conduct a 20–30 min session; collect a photo and short feedback quotes.  
- Attach as evidence to NIW (Exhibits: curriculum + photos).

---

## Evidence Checklist (for NIW)
- ✅ Public URL (GitHub Pages) for **helpmap** + screenshots (README + PDF Exhibit).  
- ✅ Local or cloud demo for **benefit-api** (`/docs` Swagger screenshots).  
- ✅ Photos & sign-in sheet for **eldershield-course** session; attendee feedback.  
- ✅ 1–2 LinkedIn posts summarizing impact/use case.  
- ✅ Optional: letter(s) of support from NGO/library/community center.

---

## Tools
- `tools/sheet_to_json.py` — CSV/TSV to JSON converter for `helpmap` resources.

---

## Languages
- English default; Ukrainian/Russian labels built into HelpMap.
