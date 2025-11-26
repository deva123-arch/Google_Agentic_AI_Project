📘 Study Assistant AI Agent
===========================

### Google Agents Intensive — Capstone Project

**Powered by Google Gemini API**

✨ Overview
----------

The **Study Assistant AI Agent** is a command-line intelligent learning assistant utilizing Google’s **Gemini API** to help students study efficiently.

It functions as a personalized tutor that can summarize content, explain topics, generate quizzes, build flashcards, create study plans, and provide motivational guidance.

🚀 Features
-----------

*   ✔️ **Summarize Text:** Condense long articles or text into concise bullet points.
    
*   ✔️ **Explain Topics:** Get simple, clear explanations for complex subjects.
    
*   ✔️ **Generate Quizzes:** Create Multiple Choice Question (MCQ) quizzes with answers.
    
*   ✔️ **Create Flashcards:** Auto-generate flashcards for rapid revision.
    
*   ✔️ **Study Plans:** structured, day-by-day study schedules.
    
*   ✔️ **Motivation:** Motivational messages to keep you focused.
    
*   ✔️ **Chat Mode:** Free conversational chat for general queries.
    

🧠 Technology Used
------------------

*   **Python** (3.8+)
    
*   **Google Gemini API**
    
*   **python-dotenv** (Environment management)
    
*   **google-generativeai** (Google AI client library)


🔧 Installation & Setup
-----------------------

### Prerequisites

*   Python 3.8+ installed on your system.
    
*   A valid Google Gemini API key.
    

### 1️⃣ Install Dependencies

Run the following command in your terminal:

```bash pip install google-generativeai python-dotenv   ```

_Alternatively, you can create a requirements.txt file (see below) and run pip install -r requirements.txt._

### 2️⃣ Configure Environment

Create a .env file in your project root folder and add your API key:

```bash GEMINI_API_KEY=YOUR_API_KEY_HERE   ```

> **Security Note:** Your key stays private and is never hard-coded inside the Python script.

▶️ Running the Application
--------------------------

Run the main script:
```bash
python study_agent.py 
```
You will see the welcome screen:
```bash  ======================================     STUDY ASSISTANT AI (Gemini Only)     ======================================  Type 'menu' to see options, 'exit' to quit.   ```

🧩 Usage Commands (Menu System)
-------------------------------

Inside the app, type menu to see the options:

**Command**

**Action**

**1** Summarize text

**2** Explain topic

**3** Generate quiz

**4** Create flashcards

**5** Study plan

**6** Motivation

**7** Chat with AI

**menu** - Show options

**exit** - Quit application

💡 Example Usage
----------------

**Summarize Text**
> 1  Paste text: Artificial intelligence is...   `

**Explain a Topic**
> 2  Topic: Quantum computing   `

**Generate Quiz**

> 3  Topic: Operating Systems  No. of questions: 5   `

**Create Study Plan**

> 5  Subject: Machine Learning  Days: 7   `

🛠 Error Handling
-----------------

**If API key is missing:**
```bash
❗ ERROR: Gemini API key not found in .env  Please add: GEMINI_API_KEY=xxxxx to your .env file
```

**If Gemini API connection fails:**

```bash
    [ERROR contacting Gemini API: ...]
```

🎓 Educational Impact
---------------------

*   ✔️ Helps students learn faster and more efficiently.
    
*   ✔️ Supports self-study and last-minute revision.
    
*   ✔️ Creates personalized learning content on demand.
    
*   ✔️ Functions like a 24/7 private tutor.
    
*   ✔️ Useful for schools, colleges, and coaching centers.
    

🧾 dependencies (requirements.txt)
----------------------------------

To replicate this environment, your requirements.txt should contain:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   google-generativeai  python-dotenv   `

⭐ Future Enhancements
---------------------

*   \[ \] **Web UI Interface** (Streamlit/Flask)
    
*   \[ \] **User Profiles** to track individual progress
    
*   \[ \] **Memory** to recall previous conversations
    
*   \[ \] **Quiz Grading** & Performance Analytics
    
*   \[ \] **Multi-language Support**
    

🙌 Acknowledgments
------------------

*   **Google Gemini API**
    
*   **Google Agents Intensive Program — Capstone**
    
*   **AI Developer Community**
    

👨‍🎓 Author
------------

**Harshith Deva** _AI Developer | Student | Innovator_ _India_

📜 License
----------

This project is open for educational, academic, and personal use.
