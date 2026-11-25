"""
Standalone AI Career Assistant for Jayalekshmi S Nair's Portfolio.
Provides intelligent answers about Jayalekshmi's background, qualities,
skills, projects, experience, and contact details using a high-fidelity
built-in knowledge and semantic query matching engine.
100% self-contained with zero external API dependencies or external services.
"""

import re

# Structured Knowledge Base
PORTFOLIO_DATA = {
    "name": "Jayalekshmi S Nair",
    "role": "Python Developer & Data Science Enthusiast",
    "education": {
        "degree": "Bachelor of Technology (B.Tech)",
        "major": "Computer Science and Engineering",
        "college": "Kottayam Institute of Technology & Science",
        "university": "APJ Abdul Kalam Technological University (KTU)",
        "years": "2022 — 2026",
    },
    "key_qualities": [
        "Strong Problem-Solving & Analytical Mindset: Skilled at breaking down complex requirements into clean, scalable software logic.",
        "Versatile Tech Blend: Combines robust backend development (Python, Django, SQL) with practical data analytics and visualization (Pandas, NumPy, Power BI).",
        "Proven Hands-on Experience: Successfully completed 3 technical internships across Python, Data Science, and AI domains.",
        "Rapid Learner & Adaptable: Quick to master emerging frameworks, tools, and best engineering practices.",
        "Commitment to Quality: Prioritizes clean code, user-centric interfaces, and reliable data integrity.",
        "Collaborative Team Player: Experienced working in professional environments with mentors, peers, and stakeholders."
    ],
    "skills": {
        "programming": ["Python (Core & Advanced)", "JavaScript (Basic)", "C (Basic)"],
        "web": ["Django", "HTML5", "CSS3", "REST APIs"],
        "data_analytics": ["Pandas", "NumPy", "Advanced Excel", "Power BI"],
        "databases": ["MySQL", "SQLite"],
        "gui_tools": ["Tkinter", "Git & GitHub"]
    },
    "projects": [
        {
            "name": "BankEase",
            "type": "Smart Banking System",
            "stack": "Python, Django, HTML, CSS, SQLite",
            "summary": "A secure, user-friendly digital banking web application designed to manage financial accounts, transactions, and secure authentication.",
            "status": "In active development"
        },
        {
            "name": "Medicore",
            "type": "Healthcare Appointment System",
            "stack": "Python, Django, HTML, CSS, SQLite",
            "summary": "A modern healthcare portal connecting patients with verified doctors, specialty browsing, and automated appointment scheduling.",
            "status": "In active development"
        },
        {
            "name": "CopDesk",
            "type": "PoliceConnect Complaint Portal",
            "stack": "Python, Django, HTML, CSS, SQLite",
            "summary": "A civic-tech complaint management system enabling citizens to submit grievances, select local jurisdictions, and track case resolution in real time.",
            "status": "In active development"
        },
        {
            "name": "Sales & Revenue Analytics",
            "type": "Data Analytics System",
            "stack": "Python, Tkinter, MySQL, Excel, Power BI",
            "summary": "An enterprise analytics application to extract, transform, and visualize large sales datasets with revenue metrics and forecasting dashboards.",
            "status": "In active development"
        }
    ],
    "experience": [
        {
            "role": "Data Science & AI Intern",
            "company": "SCOPE INDIA",
            "period": "July 2026 — Present",
            "location": "Trivandrum, Kerala",
            "details": "Working with data analysis pipelines, exploratory data analysis, and AI/ML model foundations."
        },
        {
            "role": "Python Intern",
            "company": "RISS Technologies",
            "period": "September 2025 — February 2026",
            "location": "Kochi, Kerala",
            "details": "Developed Python applications, database integration, and backend components."
        },
        {
            "role": "Python and Data Science Intern",
            "company": "SCOPE INDIA",
            "period": "July 2024 — August 2024",
            "location": "Trivandrum, Kerala",
            "details": "Hands-on foundation in Python programming, NumPy, Pandas, and data processing workflows."
        }
    ],
    "certifications": [
        "AI Fundamentals:Foundations For Understanding AI-IBM SkillsBuild (Nov 2026)",
        "AI Tools Workshop-Be10X (Nov 2026)",
        "GenAI Powered Data Analytics Job Simulation — Forage (Nov 2026)",
        "Python & Data Science — Suffix E Solutions (Aug 2024)",
        "Advanced Excel and Power BI — Suffix E Solutions (Sep 2026)",
        "Academic Internship in Python — RISS Technologies (Feb 2026)",
        "Rail Safe Park Project Completion — RISS Technologies (Feb 2026)",
        "Digital Marketing Workshop — Core Institute of Technology (Feb 2025)"
    ],
    "contact": {
        "email": "jayalekshmisnair121@gmail.com",
        "phone": "+91 9645601965",
        "location": "Trivandrum, Kerala, India (Open to Relocate / Remote)",
        "linkedin": "https://www.linkedin.com/in/jayalekshmi-s-n/",
        "github": "https://github.com/jayalekshminair80-png",
        "availability": "Actively looking for full-time entry-level Python Developer, Software Engineer, or Data Analyst roles. Immediate joiner."
    }
}


def get_ai_response(user_message: str) -> str:
    """
    Intelligent conversational engine that parses visitor queries
    and provides accurate, recruiter-facing answers from the knowledge base.
    """
    user_message = user_message.strip()
    if not user_message:
        return "Hello! I am Jayalekshmi's AI Assistant. How can I help you today? Feel free to ask about her key qualities, skills, projects, or how to hire her!"

    msg = user_message.lower()

    # Greetings
    if re.search(r'\b(hi|hello|hey|greetings|hola|good\s*(morning|afternoon|evening))\b', msg):
        return (
            "Hello! 👋 I am Jayalekshmi's AI Portfolio Assistant. "
            "I can answer questions about her **key qualities**, **technical skills**, "
            "**internship experience**, **featured projects**, and **availability for hire**. "
            "What would you like to know?"
        )

    # Key Qualities / Strengths / Why Hire
    if any(k in msg for k in ['quality', 'qualities', 'strength', 'strengths', 'why hire', 'why should we hire', 'stand out', 'value', 'soft skill', 'attitude']):
        qualities_str = "\n".join([f"• **{q.split(':')[0]}**: {q.split(':')[1]}" for q in PORTFOLIO_DATA['key_qualities']])
        return (
            f"Here are **Jayalekshmi's top key qualities** that make her an exceptional hire:\n\n"
            f"{qualities_str}\n\n"
            "Would you like to know more about her projects or internship experience?"
        )

    # Skills / Technologies
    if any(k in msg for k in ['skill', 'skills', 'technolog', 'tech stack', 'python', 'django', 'power bi', 'sql', 'tools', 'languages']):
        skills = PORTFOLIO_DATA['skills']
        return (
            "Here is an overview of **Jayalekshmi's technical expertise**:\n\n"
            f"• **Programming**: {', '.join(skills['programming'])}\n"
            f"• **Web Development**: {', '.join(skills['web'])}\n"
            f"• **Data Analytics & BI**: {', '.join(skills['data_analytics'])}\n"
            f"• **Databases**: {', '.join(skills['databases'])}\n"
            f"• **GUI & Tools**: {', '.join(skills['gui_tools'])}\n\n"
            "She specializes in integrating Python backend applications with data analytics workflows!"
        )

    # Projects
    if any(k in msg for k in ['project', 'projects', 'portfolio work', 'bankease', 'pulsepoint', 'copdesk', 'sales']):
        if 'bankease' in msg:
            p = PORTFOLIO_DATA['projects'][0]
            return f"🏦 **BankEase** ({p['type']}):\n{p['summary']}\n• **Tech Stack**: {p['stack']}\n• **Status**: {p['status']}."
        if 'pulsepoint' in msg:
            p = PORTFOLIO_DATA['projects'][1]
            return f"🩺 **PulsePoint** ({p['type']}):\n{p['summary']}\n• **Tech Stack**: {p['stack']}\n• **Status**: {p['status']}."
        if 'copdesk' in msg:
            p = PORTFOLIO_DATA['projects'][2]
            return f"🛡️ **CopDesk** ({p['type']}):\n{p['summary']}\n• **Tech Stack**: {p['stack']}\n• **Status**: {p['status']}."
        if 'sales' in msg or 'revenue' in msg:
            p = PORTFOLIO_DATA['projects'][3]
            return f"📊 **Sales & Revenue Analytics** ({p['type']}):\n{p['summary']}\n• **Tech Stack**: {p['stack']}\n• **Status**: {p['status']}."
        
        proj_lines = "\n".join([f"• **{p['name']}** ({p['type']}) — Built with {p['stack']}. {p['summary']}" for p in PORTFOLIO_DATA['projects']])
        return (
            f"Jayalekshmi has developed 4 major projects showcasing full-stack and analytics capabilities:\n\n"
            f"{proj_lines}\n\n"
            "Ask me about any specific project (e.g., *'Tell me about BankEase'* or *'Sales Analytics'*) for deeper details!"
        )

    # Experience / Internships
    if any(k in msg for k in ['experience', 'intern', 'internship', 'work', 'job', 'scope india', 'riss']):
        exp_lines = "\n".join([
            f"• **{e['role']}** at **{e['company']}** ({e['period']}, {e['location']})\n  _{e['details']}_"
            for e in PORTFOLIO_DATA['experience']
        ])
        return (
            f"Jayalekshmi has practical industry exposure through **3 technical internships**:\n\n"
            f"{exp_lines}\n\n"
            "Her internship experiences gave her hands-on proficiency in building real Python applications and analyzing datasets."
        )

    # Education / Degree / College
    if any(k in msg for k in ['education', 'degree', 'btech', 'college', 'university', 'study', 'graduation', 'academic']):
        edu = PORTFOLIO_DATA['education']
        return (
            f"🎓 **Academic Background**:\n\n"
            f"• **Degree**: {edu['degree']} in {edu['major']}\n"
            f"• **Duration**: {edu['years']}\n"
            f"• **College**: {edu['college']}\n"
            f"• **Affiliation**: {edu['university']}\n\n"
            "She has built a solid foundation in computer science fundamentals, data structures, and software engineering."
        )

    # Certifications
    if any(k in msg for k in ['certificat', 'credential', 'course', 'training', 'forage']):
        certs = "\n".join([f"• {c}" for c in PORTFOLIO_DATA['certifications']])
        return f"📜 **Certifications & Professional Credentials**:\n\n{certs}"

    # Availability / Relocation / Immediate Joiner
    if any(k in msg for k in ['availab', 'join', 'hire', 'relocat', 'remote', 'full time', 'opportunity', 'immediate']):
        return (
            "🟢 **Availability Status**:\n\n"
            "Jayalekshmi is **actively seeking entry-level opportunities** as a **Python Developer**, "
            "**Software Engineer**, or **Data Analyst**. She is available as an **immediate joiner**, "
            "based in Trivandrum, Kerala, and fully open to **relocation** or **remote work** worldwide."
        )

    # Resume / CV
    if any(k in msg for k in ['resume', 'cv', 'pdf', 'download resume']):
        return (
            "📄 You can view and download Jayalekshmi's complete updated resume anytime by clicking the "
            "**'Download Resume'** button in the hero section or top navigation bar, or directly at "
            "`/static/files/resume.pdf`!"
        )

    # Contact / Email / Phone / LinkedIn / GitHub
    if any(k in msg for k in ['contact', 'email', 'phone', 'call', 'reach', 'connect', 'linkedin', 'github', 'message']):
        c = PORTFOLIO_DATA['contact']
        return (
            "📬 **Here is how you can connect with Jayalekshmi directly**:\n\n"
            f"• **Email**: [{c['email']}](mailto:{c['email']})\n"
            f"• **Phone**: [{c['phone']}](tel:{c['phone'].replace(' ', '')})\n"
            f"• **LinkedIn**: [linkedin.com/in/jayalekshmi-s-n]({c['linkedin']})\n"
            f"• **GitHub**: [github.com/jayalekshminair80-png]({c['github']})\n"
            f"• **Location**: {c['location']}"
        )

    # General / About Me summary
    if any(k in msg for k in ['who are you', 'about', 'bio', 'introduce', 'overview', 'summary']):
        return (
            f"**{PORTFOLIO_DATA['name']}** is a **{PORTFOLIO_DATA['role']}** and B.Tech CSE graduate (2026). "
            "She is passionate about creating robust web applications with Python & Django and extracting actionable "
            "insights from data using Pandas, SQL, and Power BI. She has completed 3 internships and is ready for full-time opportunities!\n\n"
            "Try asking about her **key qualities**, **projects**, or **how to contact her**!"
        )

    # Default friendly fallback
    return (
        f"Thank you for asking! Jayalekshmi is a {PORTFOLIO_DATA['role']} passionate about software engineering and data analytics.\n\n"
        "You can ask me about:\n"
        "• Her **Key Qualities & Strengths** 🌟\n"
        "• Her **Technical Skills & Stack** 💻\n"
        "• Her **Projects** (BankEase, PulsePoint, CopDesk, Sales Analytics) 🚀\n"
        "• Her **3 Internships & Experience** 💼\n"
        "• Her **Contact details & Availability** 📬\n\n"
        "Or reach her directly at [jayalekshmisnair121@gmail.com](mailto:jayalekshmisnair121@gmail.com)!"
    )
