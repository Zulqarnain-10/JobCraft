# JobCraft — AI Agent Job Search Platform

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.1-1C3C3C?logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-vector%20search-005571)
![License](https://img.shields.io/badge/License-MIT-green)

> An AI job-search copilot that reads your resume, finds and ranks matching roles across major job boards, and drafts tailored interview prep — all in one Streamlit app.

## Problem

A job hunt is fragmented across tools: one place to tune your resume, separate searches on LinkedIn, Indeed, and Glassdoor, and yet another step to work out how your background lines up with each posting and what to prepare for interviews. Doing this by hand across dozens of roles is slow and inconsistent.

## Approach

JobCraft runs the whole loop inside a single Streamlit app organized into four tabs — **Resume Analysis**, **Job Search**, **Interview Preparation**, and **Saved Jobs** — backed by three specialized agents:

- **Resume agent** — parses PDF/DOCX resumes with spaCy NER and, when an OpenAI key is configured, a LangChain retrieval pipeline over a FAISS index built from OpenAI embeddings, extracting skills, experience, and a structured profile.
- **Job-search agent** — pulls live listings from LinkedIn, Indeed, Glassdoor, and other boards via SerpAPI, then uses an OpenAI model to compare each posting against the resume and return a match score, key matches, gaps, and recommendations (with a keyword-overlap fallback when the LLM is unavailable).
- **Interview agent** — generates role- and skill-specific interview questions you can save and revisit.

## Results

From a single uploaded resume, JobCraft:

- extracts skills and experience and builds a searchable vector index of the resume text;
- aggregates job listings across multiple platforms from one query;
- returns a per-job match analysis — score (0–100), aligned skills, gaps, and tailored next steps;
- generates targeted interview questions and saves jobs and question sets locally.

> **Note on the match score:** scores are produced by the language model at request time as a relative guide — not a benchmarked accuracy figure. A labeled evaluation set is on the roadmap.

## Tech stack

`Python` · `Streamlit` · `LangChain` · `OpenAI API (gpt-3.5-turbo)` · `FAISS` · `spaCy` · `SerpAPI` · `PyPDF2` · `python-docx` · `BeautifulSoup` · `pandas`

## Demo

_Screenshot / short GIF coming soon — run locally (below) and capture the Resume Analysis and Job Search tabs here._

## How to run

```bash
# 1. Clone
git clone https://github.com/Zulqarnain-10/JobCraft.git
cd JobCraft

# 2. Environment + dependencies
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_lg

# 3. API keys
cp .env.example .env                                  # then add your OpenAI + SerpAPI keys

# 4. Launch
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Deployment

JobCraft ships with a **Dockerfile** and a **GitHub Actions** workflow
(`.github/workflows/deploy.yml`) for CI/CD to **AWS EC2** via a self-hosted runner:
build the image → push to **Amazon ECR** → run the container behind an **Nginx** reverse proxy.

To deploy, set these repository secrets and push to `main`:

| Secret | Purpose |
| --- | --- |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | IAM user with ECR + EC2 access |
| `AWS_REGION` | e.g. `us-east-1` |
| `ECR_REPOSITORY` | Amazon ECR repository name |
| `OPENAI_API_KEY` / `SERPAPI_API_KEY` | injected into the running container |

Run locally (above) to confirm everything works before deploying.

## Roadmap

- Add a labeled test set to measure real resume-to-job match quality.
- Upgrade the default model and extend retrieval to job descriptions.
- Add user accounts and database-backed saved jobs.

## License

MIT — see [LICENSE](LICENSE).
