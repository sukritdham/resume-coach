# Resume Coach
An AI-powered resume assessment and coaching tool that evaluates a candidate’s resume against a job description and provides structured feedback and guidance.

## Problem Statement
Job applicants often struggle to understand how well their resumes align with specific job descriptions. Feedback is typically generic, manual, or inconsistent.
This project explores how large language models can be used to provide structured, actionable resume assessments and coaching at scale.

## What This Project Does
- Compares a resume against a job description
- Classifies alignment (YES / MAYBE / NO)
- Provides a structured assessment of strengths and gaps
- Offers rewrite suggestions or coaching guidance
- Supports interactive follow-up questions via chatbot

## High-Level Architecture
- Frontend UI for user input
- Backend API for orchestration and validation
- LLM-based services for assessment and coaching
- Dockerized for consistent local execution

## Running the Project
This project is packaged as a ZIP file and runs locally using Docker.

➡️ See [DEPLOYMENT.md](./DEPLOYMENT.md) for full setup and execution instructions.

## Example Workflow
1. User submits resume text and job description
2. System returns an job match classification and assessment
3. User reviews suggestions or rewritten resume
4. User asks follow-up coaching questions in chatbot

## Documentation
- [DESIGN.md](./DESIGN.md) – Architecture and design decisions
- [DEPLOYMENT.md](./DEPLOYMENT.md) – Setup and execution instructions

## Tech Stack
- Frontend: [Gradio]
- Backend: [Python]
- LLM: [OpenAI/Replicate]
- Containerization: Docker
