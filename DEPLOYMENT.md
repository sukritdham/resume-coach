# Deployment Guide

## 1. Overview
This project is distributed as a **ZIP file** that contains everything required to run the application locally using **Docker**.

**High-level steps:**
1. Unzip the project files
2. Navigate to the Docker folder
3. Run a single Docker command
4. Access the application in a browser

No source code modification is required.

---

## 2. Prerequisites

### 2.1 Supported Platforms
- macOS (Intel or Apple Silicon)
- Windows 10 / 11

---

### 2.2 Required Software

#### Docker

Docker must be installed and running before proceeding.

##### macOS
1. Install **Docker Desktop for Mac**  
   https://www.docker.com/products/docker-desktop/
2. After installation, open Docker Desktop
3. Wait until Docker Desktop shows **“Docker is running”**

##### Windows
1. Install **Docker Desktop for Windows**  
   https://www.docker.com/products/docker-desktop/
2. During installation:
   - Enable **WSL 2** if prompted
   - Restart the machine if required
3. Open Docker Desktop and confirm it is running

---

### 2.3 Verify Docker Installation

Open a terminal (macOS) or PowerShell (Windows), navigate **_resume_coach_** folder and run:

shell prompt> cd deployment
shell prompt> docker --version
shell prompt> docker compose up --build
Access application at http://localhost:7860

To bring application down while in deployment folder run:

shell prompt> docker compose down

