# Gated Prompting Framework for Analogical Reasoning

## Overview
This project implements a 3-stage pipeline to improve analogical reasoning in LLMs using Structure-Mapping Theory.

## Components
- Stage 1: Relational extraction
- Stage 2: Constraint verification
- Stage 3: Target mapping

## Features
- YAML-based prompt config
- JSON predicate representation
- Exclusion lexicon
- RAS scoring metric


````markdown
## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/angelaunique/CS6795TermProject.git
cd CS6795TermProject
````

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows (PowerShell)**

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Up API Key (Required for LLM Calls)

This project uses the Anthropic API.

#### Step 1: Get API Key

Go to:
[https://console.anthropic.com](https://console.anthropic.com)

* Create an account
* Navigate to **API Keys**
* Generate a new key

---

#### Step 2: Export API Key

**Mac/Linux**

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

**Windows (PowerShell)**

```powershell
setx ANTHROPIC_API_KEY "your_api_key_here"
```

---

### 5. Run the Pipeline

```bash
python run.py
```

---

### 6. Optional: Mock Mode (No API Key)

If no API key is set, the system will automatically run in **mock mode**, using placeholder outputs instead of real LLM responses.
