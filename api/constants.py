# Skill weights per job role
JOB_ROLE_SKILLS_WEIGHT_MAP = {
    'Data Science': {
        'python': 0.9, 'machine learning': 0.9, 'data analysis': 0.8, 'pandas': 0.7, 'numpy': 0.7,
        'sql': 0.8, 'tensorflow': 0.9, 'keras': 0.8, 'pytorch': 0.8, 'scikit-learn': 0.8,
        'matplotlib': 0.6, 'seaborn': 0.6, 'statistics': 0.7, 'data visualization': 0.7,
        'deep learning': 0.9
    },
    'Web Development': {
        'html': 0.8, 'css': 0.8, 'javascript': 0.9, 'react': 0.9, 'angular': 0.8, 'vue.js': 0.8,
        'node.js': 0.9, 'express.js': 0.8, 'php': 0.7, 'laravel': 0.8, 'django': 0.8,
        'flask': 0.7, 'sql': 0.7, 'mongodb': 0.7, 'git': 0.6
    },
    'Mobile App Development': {
        'java': 0.9, 'kotlin': 0.9, 'swift': 0.9, 'objective-c': 0.8, 'flutter': 0.8,
        'react native': 0.8, 'xcode': 0.7, 'android studio': 0.7, 'firebase': 0.7,
        'dart': 0.7, 'ui/ux design': 0.6
    },
    'UI/UX Design': {
        'adobe xd': 0.9, 'figma': 0.9, 'sketch': 0.8, 'invision': 0.7, 'photoshop': 0.8,
        'illustrator': 0.8, 'prototyping': 0.8, 'wireframing': 0.8, 'user research': 0.7,
        'usability testing': 0.7, 'interaction design': 0.7
    },
    'Cybersecurity': {
        'network security': 0.9, 'information security': 0.9, 'penetration testing': 0.8,
        'ethical hacking': 0.8, 'firewalls': 0.7, 'encryption': 0.7, 'vulnerability assessment': 0.8,
        'incident response': 0.8, 'security protocols': 0.7, 'siem': 0.7
    },
    'Cloud Computing': {
        'aws': 0.9, 'azure': 0.9, 'google cloud': 0.9, 'devops': 0.8, 'docker': 0.8,
        'kubernetes': 0.8, 'terraform': 0.7, 'ci/cd': 0.8, 'cloud architecture': 0.8,
        'serverless': 0.7
    },
    'DevOps': {
        'jenkins': 0.8, 'ansible': 0.8, 'docker': 0.9, 'kubernetes': 0.9, 'terraform': 0.8,
        'ci/cd': 0.9, 'git': 0.8, 'linux': 0.7, 'monitoring': 0.7, 'scripting': 0.7
    },
    'Digital Marketing': {
        'seo': 0.9, 'sem': 0.9, 'google analytics': 0.8, 'content marketing': 0.8,
        'social media marketing': 0.8, 'email marketing': 0.7, 'ppc': 0.7, 'adwords': 0.7,
        'marketing automation': 0.7, 'crm': 0.6
    },
    'Project Management': {
        'project planning': 0.9, 'agile': 0.9, 'scrum': 0.8, 'kanban': 0.7, 'jira': 0.7,
        'risk management': 0.8, 'budgeting': 0.7, 'stakeholder management': 0.8,
        'communication': 0.8, 'leadership': 0.8
    },
    'Business Analysis': {
        'business process modeling': 0.8, 'requirement gathering': 0.9, 'data analysis': 0.8,
        'sql': 0.7, 'excel': 0.7, 'power bi': 0.7, 'tableau': 0.7, 'stakeholder communication': 0.8,
        'documentation': 0.7, 'problem-solving': 0.8
    },
    'Graphic Design': {
        'photoshop': 0.9, 'illustrator': 0.9, 'indesign': 0.8, 'coreldraw': 0.7, 'creativity': 0.8,
        'typography': 0.8, 'branding': 0.8, 'layout design': 0.7, 'color theory': 0.7,
        'visual communication': 0.8
    },
    'Accounting & Finance': {
        'accounting principles': 0.9, 'financial analysis': 0.9, 'budgeting': 0.8, 'forecasting': 0.8,
        'quickbooks': 0.7, 'excel': 0.8, 'taxation': 0.8, 'auditing': 0.8, 'payroll': 0.7,
        'compliance': 0.8
    },
    'Human Resources': {
        'recruitment': 0.9, 'employee relations': 0.8, 'performance management': 0.8,
        'training and development': 0.8, 'hr policies': 0.7, 'compliance': 0.8, 'payroll': 0.7,
        'benefits administration': 0.7, 'hr software': 0.7, 'onboarding': 0.8
    },
    'Sales': {
        'lead generation': 0.9, 'crm': 0.8, 'negotiation': 0.8, 'sales strategy': 0.8,
        'customer relationship management': 0.8, 'market research': 0.7, 'cold calling': 0.7,
        'product knowledge': 0.8, 'salesforce': 0.7, 'closing deals': 0.9
    },
    'Customer Service': {
        'communication': 0.9, 'problem-solving': 0.8, 'crm': 0.8, 'customer support': 0.9,
        'conflict resolution': 0.8, 'empathy': 0.8, 'product knowledge': 0.8,
        'ticketing systems': 0.7, 'multitasking': 0.7, 'feedback handling': 0.7
    },
    'Content Writing': {
        'seo': 0.9, 'copywriting': 0.9, 'editing': 0.8, 'proofreading': 0.8, 'content strategy': 0.8,
        'wordpress': 0.7, 'research': 0.8, 'grammar': 0.9, 'creativity': 0.8, 'storytelling': 0.8
    },
    'Data Entry': {
        'typing': 0.9, 'data accuracy': 0.9, 'excel': 0.8, 'attention to detail': 0.9,
        'database management': 0.8, 'time management': 0.8, 'ms office': 0.8,
        'data validation': 0.8, 'organization': 0.8, 'confidentiality': 0.8
    },
    'Teaching & Education': {
        'lesson planning': 0.9, 'classroom management': 0.9, 'curriculum development': 0.8,
        'assessment': 0.8, 'communication': 0.9, 'patience': 0.8, 'subject expertise': 0.9,
        'technology integration': 0.7, 'student engagement': 0.8, 'adaptability': 0.8
    },
    'Healthcare': {
        'patient care': 0.9, 'medical terminology': 0.9, 'clinical skills': 0.9, 'emr': 0.8,
        'vital signs monitoring': 0.8, 'infection control': 0.8, 'medication administration': 0.8,
        'communication': 0.8, 'compassion': 0.9, 'teamwork': 0.8
    },

    'Machine Learning Engineering': {
        'python': 0.9, 'scikit-learn': 0.9, 'tensorflow': 0.9, 'keras': 0.8, 'pytorch': 0.8,
        'mlops': 0.8, 'docker': 0.7, 'kubernetes': 0.7, 'data preprocessing': 0.8,
        'model deployment': 0.8, 'feature engineering': 0.8
    },

    'AI Research': {
        'deep learning': 0.9, 'transformers': 0.9, 'nlp': 0.9, 'cv': 0.8, 'pytorch': 0.9,
        'research papers': 0.8, 'fine-tuning': 0.8, 'huggingface': 0.9,
        'tensorflow': 0.8, 'GANs': 0.7, 'LLMs': 0.9
    },

    'Technical Writing': {
        'documentation': 0.9, 'markdown': 0.8, 'api documentation': 0.9, 'communication': 0.9,
        'git': 0.8, 'html': 0.6, 'seo': 0.7, 'proofreading': 0.8, 'content structure': 0.8,
        'editing': 0.8
    },

    'Game Development': {
        'unity': 0.9, 'c#': 0.9, 'game design': 0.8, 'physics engine': 0.8, '3d modeling': 0.7,
        'blender': 0.7, 'animation': 0.7, 'multiplayer networking': 0.7, 'ui/ux': 0.6,
        'graphics rendering': 0.8
    },

    'Robotics': {
        'ros': 0.9, 'python': 0.9, 'c++': 0.9, 'control systems': 0.8, 'robot kinematics': 0.8,
        'lidar': 0.8, 'sensors': 0.7, 'machine vision': 0.8, 'opencv': 0.7, 'embedded systems': 0.7
    },
}

# Action Verbs
ACTION_WORDS = {
    "led", "developed", "created", "built", "managed", "designed", "increased", "reduced",
    "launched", "optimized", "streamlined", "implemented", "executed", "initiated", "improved",
    "deployed", "architected", "engineered", "automated", "formulated", "facilitated",
    "achieved", "enhanced", "resolved", "supervised", "orchestrated", "coordinated",
    "monitored", "analyzed", "proposed", "revamped"
}

# Soft Skills
SOFT_SKILLS = {
    "teamwork", "communication", "leadership", "collaboration", "adaptability", "problem-solving",
    "critical thinking", "time management", "creativity", "decision making", "emotional intelligence",
    "negotiation", "conflict resolution", "presentation", "attention to detail", "multitasking"
}

# Hard Skills
HARD_SKILLS = {
    # Programming Languages
    "python", "java", "c++", "c", "c#", "go", "rust", "javascript", "typescript", "kotlin", "swift", "ruby", "r", "matlab", "scala", "perl", "bash",

    # Web Development
    "html", "css", "javascript", "jquery", "node.js", "react", "angular", "vue.js", "next.js", "svelte", "bootstrap", "tailwind", "sass", "wordpress", "shopify",

    # Backend & Frameworks
    "django", "flask", "spring", "express.js", "fastapi", "laravel", "dotnet", "ruby on rails", "nestjs",

    # Databases
    "mysql", "postgresql", "mongodb", "oracle", "sqlite", "redis", "cassandra", "elasticsearch", "dynamodb", "firebase",

    # DevOps / Cloud
    "docker", "kubernetes", "jenkins", "github actions", "circleci", "ansible", "terraform", "prometheus", "grafana", 
    "aws", "azure", "gcp", "heroku", "digitalocean", "cloudflare",

    # Data Science & ML
    "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "keras", "pytorch", "opencv", "huggingface", 
    "xgboost", "lightgbm", "mlflow", "airflow", "nltk", "spacy", "transformers", "yolov5",

    # Data/BI/Analytics
    "sql", "power bi", "tableau", "looker", "superset", "google data studio", "excel", "dash", "plotly", 
    "snowflake", "bigquery", "databricks", "hadoop", "spark",

    # Tools & Platforms
    "git", "github", "gitlab", "bitbucket", "jira", "confluence", "notion", "postman", "figma", "canva", "vs code", 
    "pycharm", "eclipse", "android studio", "xcode", "unity", "blender",

    # Cybersecurity
    "kali linux", "wireshark", "burp suite", "metasploit", "nmap", "nessus", "osint", "siem", "splunk",

    # Soft Skills / Management
    "communication", "teamwork", "leadership", "time management", "problem solving", "adaptability", 
    "critical thinking", "conflict resolution", "creativity", "collaboration", "emotional intelligence",

    # Business / Finance / Product
    "agile", "scrum", "kanban", "lean", "business analysis", "market research", "competitive analysis", 
    "product management", "user research", "project management", "stakeholder management", "financial modeling",

    # Writing / Content
    "technical writing", "content writing", "seo", "copywriting", "blogging", "editing", "proofreading", 
    "social media management",

    # Design / UX
    "figma", "adobe xd", "photoshop", "illustrator", "indesign", "ux design", "ui design", "wireframing", 
    "prototyping", "user flows", "design systems",

    # Misc
    "linux", "bash", "shell scripting", "api development", "web scraping", "automation", 
    "chatgpt", "llm", "web3", "blockchain", "solidity", "nft", "metaverse", "firebase",
    
    # Testing
    "unit testing", "integration testing", "jest", "mocha", "selenium", "cypress", "pytest", "junit",

    # Languages & Certifications
    "english", "hindi", "french", "german", "ielts", "toefl", "pmp", "cfa", "aws certified", "google certified", "scrum certified"
}


# Resume Section Headers
HEADERS = {
    "experience", "professional experience", "work experience", "education", "skills", "technical skills",
    "projects", "certifications", "summary", "profile", "contact", "contact information",
    "achievements", "publications", "interests", "languages", "extracurricular", "volunteering"
}

# Avoid Personal Pronouns
BAD_PRONOUNS = {
    "i", "me", "my", "mine", "we", "us", "our", "ours", "your", "you're", "you", "am"
}

# Regex Patterns
EMAIL_REGEX = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
PHONE_REGEX = r"\b(\+?\d{1,3}[-.\s]?)?(\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b"
LINKEDIN_REGEX = r"\b(?:https?:\/\/)?(?:www\.)?linkedin\.com\/in\/[a-zA-Z0-9-_%]+\b"
GITHUB_REGEX = r"\b(?:https?:\/\/)?(?:www\.)?github\.com\/[a-zA-Z0-9-]+\b"
PORTFOLIO_REGEX = r"\b(?:https?:\/\/)?[a-zA-Z0-9.-]+\.(dev|tech|me|xyz|site|portfolio|com)\b"

# Known Job Titles
COMMON_JOB_TITLES = {
    "software engineer", "data analyst", "data scientist", "web developer", "backend engineer",
    "frontend developer", "ml engineer", "ai engineer", "product manager", "research intern",
    "cloud engineer", "full stack developer", "devops engineer", "qa engineer", "ui/ux designer"
}

# Bonus Keywords
EXTRA_KEYWORDS = {
    "agile", "scrum", "jira", "rest api", "graphql", "oop", "microservices", "design patterns",
    "unit testing", "ci/cd", "postman", "swagger", "firebase", "mongodb", "postgresql", "redis"
}

# Score Thresholds
FUZZY_HEADER_THRESHOLD = 80
MAX_HEADER_SCORE = 10
MAX_ACTION_VERB_SCORE = 15
MAX_SKILLS_SCORE = 20
MAX_CONTACT_SCORE = 12
MAX_READABILITY_SCORE = 10
MAX_SPELLING_SCORE = 10
MAX_PRONOUN_SCORE = 5
MAX_WORDCOUNT_SCORE = 10
MAX_JOBTITLE_SCORE = 8
MAX_NEGATIVE_PENALTY = 10

#course catalog
COURSE_CATALOG = {
    # Data Science
    "python": "https://www.coursera.org/specializations/python",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "data analysis": "https://www.coursera.org/specializations/data-analysis",
    "pandas": "https://www.datacamp.com/courses/pandas-foundations",
    "numpy": "https://www.datacamp.com/courses/intro-to-python-for-data-science",
    "sql": "https://www.coursera.org/learn/sql-for-data-science",
    "tensorflow": "https://www.coursera.org/learn/introduction-tensorflow",
    "keras": "https://www.coursera.org/learn/deep-neural-networks-with-keras",
    "pytorch": "https://www.udacity.com/course/deep-learning-pytorch--ud188",
    "scikit-learn": "https://www.datacamp.com/courses/supervised-learning-with-scikit-learn",
    "matplotlib": "https://www.datacamp.com/courses/introduction-to-data-visualization-with-python",
    "seaborn": "https://www.datacamp.com/courses/introduction-to-data-visualization-with-seaborn",
    "statistics": "https://www.coursera.org/learn/basic-statistics",
    "data visualization": "https://www.coursera.org/specializations/data-visualization",
    "deep learning": "https://www.coursera.org/specializations/deep-learning",

    # Web Development
    "html": "https://www.freecodecamp.org/learn/responsive-web-design/",
    "css": "https://www.codecademy.com/learn/learn-css",
    "javascript": "https://www.codecademy.com/learn/introduction-to-javascript",
    "react": "https://www.codecademy.com/learn/react-101",
    "angular": "https://www.coursera.org/learn/single-page-web-apps-with-angularjs",
    "vue.js": "https://www.udemy.com/course/vuejs-2-the-complete-guide/",
    "node.js": "https://www.coursera.org/learn/server-side-nodejs",
    "express.js": "https://www.udemy.com/course/the-complete-nodejs-developer-course-2/",
    "php": "https://www.codecademy.com/learn/learn-php",
    "laravel": "https://www.udemy.com/course/php-with-laravel-for-beginners-become-a-master-in-laravel/",
    "django": "https://www.coursera.org/learn/django",
    "flask": "https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/",
    "mongodb": "https://www.mongodb.com/learn/mongodb-university",
    "git": "https://www.codecademy.com/learn/learn-git",

    # Mobile App Development
    "java": "https://www.udemy.com/course/java-the-complete-java-developer-course/",
    "kotlin": "https://www.udacity.com/course/kotlin-for-android-developers--ud888",
    "swift": "https://www.udacity.com/course/ios-developer-nanodegree--nd003",
    "objective-c": "https://www.udemy.com/course/objective-c-for-beginners/",
    "flutter": "https://www.udemy.com/course/flutter-bootcamp-with-dart/",
    "react native": "https://www.coursera.org/learn/react-native",
    "xcode": "https://developer.apple.com/xcode/",
    "android studio": "https://developer.android.com/studio",
    "firebase": "https://firebase.google.com/docs",
    "dart": "https://dart.dev/codelabs",
    "ui/ux design": "https://www.coursera.org/specializations/ui-ux-design",

    # UI/UX Design
    "adobe xd": "https://www.udemy.com/course/ui-ux-web-design-using-adobe-xd/",
    "figma": "https://www.udemy.com/course/learn-figma/",
    "sketch": "https://www.udemy.com/course/sketch-app-course/",
    "invision": "https://www.udemy.com/course/invision-course/",
    "photoshop": "https://www.udemy.com/course/adobe-photoshop-cc-essentials-training-course/",
    "illustrator": "https://www.udemy.com/course/adobe-illustrator-course/",
    "prototyping": "https://www.coursera.org/learn/prototyping-and-design",
    "wireframing": "https://www.coursera.org/learn/wireframing",
    "user research": "https://www.coursera.org/learn/user-research",
    "usability testing": "https://www.coursera.org/learn/usability-testing",
    "interaction design": "https://www.coursera.org/specializations/interaction-design",

    # Cybersecurity
    "network security": "https://www.coursera.org/learn/network-security",
    "information security": "https://www.coursera.org/learn/information-security-data",
    "penetration testing": "https://www.udemy.com/course/penetration-testing/",
    "ethical hacking": "https://www.udemy.com/course/learn-ethical-hacking-from-scratch/",
    "firewalls": "https://www.coursera.org/learn/firewalls",
    "encryption": "https://www.coursera.org/learn/cryptography",
    "vulnerability assessment": "https://www.udemy.com/course/vulnerability-assessment/",
    "incident response": "https://www.coursera.org/learn/incident-response",
    "security protocols": "https://www.coursera.org/learn/security-protocols",
    "siem": "https://www.udemy.com/course/siem-security-information-event-management/",
    
    # Cloud Computing
    "aws": "https://www.coursera.org/specializations/aws-fundamentals",
    "azure": "https://www.coursera.org/learn/introduction-to-azure",
    "google cloud": "https://www.coursera.org/specializations/gcp-fundamentals",
    "devops": "https://www.coursera.org/specializations/devops",
    "docker": "https://www.udemy.com/course/docker-mastery/",
    "kubernetes": "https://www.udemy.com/course/kubernetes-mastery/",
    "terraform": "https://www.udemy.com/course/terraform-beginner-to-advanced/",
    "ci/cd": "https://www.coursera.org/learn/continuous-integration",
    "cloud architecture": "https://www.coursera.org/learn/cloud-architecture",
    "serverless": "https://www.coursera.org/learn/serverless-applications",

    # DevOps
    "jenkins": "https://www.udemy.com/course/jenkins-from-zero-to-hero/",
    "ansible": "https://www.udemy.com/course/ansible-for-the-absolute-beginner/",
    "linux": "https://www.udemy.com/course/linux-for-beginners/",
    "monitoring": "https://www.coursera.org/learn/monitoring-and-logging",
    "scripting": "https://www.udemy.com/course/shell-scripting-tutorial-for-beginners/",

    # Digital Marketing
    "seo": "https://www.coursera.org/learn/seo-fundamentals",
    "sem": "https://www.coursera.org/learn/sem",
    "google analytics": "https://analytics.google.com/analytics/academy/",
    "content marketing": "https://www.coursera.org/learn/content-marketing",
    "social media marketing": "https://www.coursera.org/specializations/social-media-marketing",
    "email marketing": "https://www.coursera.org/learn/email-marketing",
    "ppc": "https://www.udemy.com/course/ppc-advertising/",
    "adwords": "https://skillshop.withgoogle.com/",
    "marketing automation": "https://www.coursera.org/learn/marketing-automation",
    "crm": "https://www.coursera.org/learn/crm",

    # Project Management
    "project planning": "https://www.coursera.org/learn/project-planning",
    "agile": "https://www.coursera.org/learn/agile-methodology",
    "scrum": "https://www.coursera.org/learn/scrum-methodology",
    "kanban": "https://www.coursera.org/learn/kanban",
    "jira": "https://www.udemy.com/course/jira-tutorial-a-complete-guide-for-beginners/",
    "risk management": "https://www.coursera.org/learn/risk-management",
    "budgeting": "https://www.coursera.org/learn/project-budgeting",
    "stakeholder management": "https://www.coursera.org/learn/stakeholder-management",
    "communication": "https://www.coursera.org/learn/communication-skills",
    "leadership": "https://www.coursera.org/learn/leadership-skills",

    # Business Analysis
    "business process modeling": "https://www.coursera.org/learn/business-process-modeling",
    "requirement gathering": "https://www.coursera.org/learn/requirement-gathering",
    "excel": "https://www.coursera.org/learn/excel",
    "power bi": "https://www.coursera.org/learn/power-bi",
    "tableau": "https://www.coursera.org/learn/tableau",
    "stakeholder communication": "https://www.coursera.org/learn/stakeholder-communication",
    "documentation": "https://www.coursera.org/learn/documentation",
    "problem-solving": "https://www.coursera.org/learn/problem-solving",

    # Graphic Design
    "photoshop": "https://www.udemy.com/course/adobe-photoshop-cc-essentials-training-course/",
    "illustrator": "https://www.udemy.com/course/adobe-illustrator-course/",
    "indesign": "https://www.udemy.com/course/indesign-course/",
    "coreldraw": "https://www.udemy.com/course/coreldraw-course/",
    "creativity": "https://www.coursera.org/learn/creative-thinking",
    "typography": "https://www.coursera.org/learn/typography",
    "branding": "https://www.coursera.org/learn/branding",
    "layout design": "https://www.coursera.org/learn/layout-design",
    "color theory": "https://www.coursera.org/learn/color-theory",
    "visual communication": "https://www.coursera.org/learn/visual-communication",

    # Accounting & Finance
    "accounting principles": "https://www.coursera.org/learn/accounting-basics",
    "financial analysis": "https://www.coursera.org/learn/financial-analysis",
    "budgeting": "https://www.coursera.org/learn/project-budgeting",
    "forecasting": "https://www.coursera.org/learn/forecasting",
    "quickbooks": "https://www.udemy.com/course/quickbooks-online/",
    "excel": "https://www.coursera.org/learn/excel",
    "taxation": "https://www.udemy.com/course/taxation-fundamentals/",
    "auditing": "https://www.coursera.org/learn/auditing",
    "payroll": "https://www.udemy.com/course/payroll-accounting/",
    "compliance": "https://www.coursera.org/learn/compliance",

    # Human Resources
    "recruitment": "https://www.coursera.org/learn/recruitment",
    "employee relations": "https://www.coursera.org/learn/employee-relations",
    "performance management": "https://www.coursera.org/learn/performance-management",
    "training & development": "https://www.coursera.org/learn/training-development",
    "hr policies": "https://www.udemy.com/course/hr-policies-for-beginners/",
    "compliance": "https://www.coursera.org/learn/compliance",
    "payroll": "https://www.udemy.com/course/payroll-accounting/",
    "benefits administration": "https://www.coursera.org/learn/benefits-administration",
    "hr software": "https://www.udemy.com/course/hr-information-systems/",
    "onboarding": "https://www.coursera.org/learn/onboarding",

    # Sales
    "lead generation": "https://www.udemy.com/course/lead-generation-for-beginners/",
    "crm": "https://www.coursera.org/learn/crm",
    "negotiation": "https://www.coursera.org/learn/negotiation-skills",
    "sales strategy": "https://www.coursera.org/learn/sales-strategy",
    "customer relationship management": "https://www.coursera.org/learn/crm",
    "market research": "https://www.coursera.org/learn/market-research",
    "cold calling": "https://www.udemy.com/course/cold-calling-mastery/",
    "product knowledge": "https://www.udemy.com/course/product-knowledge/",
    "salesforce": "https://trailhead.salesforce.com/en/content/learn/modules/starting-with-salesforce",
    "closing deals": "https://www.udemy.com/course/sales-closing-techniques/",

    # Customer Service
    "communication": "https://www.coursera.org/learn/communication-skills",
    "problem-solving": "https://www.coursera.org/learn/problem-solving",
    "crm": "https://www.coursera.org/learn/crm",
    "customer support": "https://www.udemy.com/course/customer-service-excellence/",
    "conflict resolution": "https://www.coursera.org/learn/conflict-resolution-skills",
    "empathy": "https://www.coursera.org/learn/empowering-empathy",
    "product knowledge": "https://www.udemy.com/course/product-knowledge/",
    "ticketing systems": "https://www.udemy.com/course/help-desk-software-training/",
    "multitasking": "https://www.udemy.com/course/multitasking-tips/",
    "feedback handling": "https://www.udemy.com/course/handling-customer-feedback/",

    # Content Writing
    "seo": "https://www.coursera.org/learn/seo-fundamentals",
    "copywriting": "https://www.udemy.com/course/copywriting-for-beginners/",
    "editing": "https://www.coursera.org/learn/copy-editing",
    "proofreading": "https://www.udemy.com/course/proofreading-masterclass/",
    "content strategy": "https://www.coursera.org/learn/content-strategy",
    "wordpress": "https://www.udemy.com/course/wordpress-for-beginners-course/",
    "research": "https://www.coursera.org/learn/research-methods",
    "grammar": "https://www.udemy.com/course/english-grammar-bootcamp/",
    "creativity": "https://www.coursera.org/learn/creative-thinking",
    "storytelling": "https://www.coursera.org/learn/storytelling",

    # Data Entry
    "typing": "https://www.typingclub.com/",
    "data accuracy": "https://www.udemy.com/course/data-accuracy-and-data-quality/",
    "excel": "https://www.coursera.org/learn/excel",
    "attention to detail": "https://www.udemy.com/course/attention-to-detail-training/",
    "database management": "https://www.coursera.org/learn/database-management",
    "time management": "https://www.coursera.org/learn/work-smarter-not-harder",
    "ms office": "https://www.udemy.com/course/microsoft-office-training-course/",
    "data validation": "https://www.udemy.com/course/excel-data-validation/",
    "organization": "https://www.coursera.org/learn/organization-skills",
    "confidentiality": "https://www.udemy.com/course/data-privacy-and-confidentiality/",

    # Teaching & Education
    "lesson planning": "https://www.coursera.org/learn/lesson-planning",
    "classroom management": "https://www.coursera.org/learn/classroom-management",
    "curriculum development": "https://www.coursera.org/learn/curriculum-development",
    "assessment": "https://www.coursera.org/learn/educational-assessment",
    "communication": "https://www.coursera.org/learn/communication-skills",
    "patience": "https://www.udemy.com/course/patience-training/",
    "subject expertise": "https://www.coursera.org/learn/subject-specific-teaching",
    "technology integration": "https://www.coursera.org/learn/educational-technology",
    "student engagement": "https://www.coursera.org/learn/student-engagement",
    "adaptability": "https://www.udemy.com/course/adaptability-and-flexibility/",

    # Healthcare
    "patient care": "https://www.coursera.org/learn/patient-care",
    "medical terminology": "https://www.udemy.com/course/medical-terminology-course/",
    "clinical skills": "https://www.coursera.org/learn/clinical-skills",
    "emr": "https://www.udemy.com/course/electronic-medical-records-emr-training/",
    "vital signs monitoring": "https://www.coursera.org/learn/vital-signs",
    "infection control": "https://www.coursera.org/learn/infection-control",
    "medication administration": "https://www.udemy.com/course/medication-administration/",
    "communication": "https://www.coursera.org/learn/communication-skills",
    "compassion": "https://www.udemy.com/course/compassion-in-healthcare/",
    "teamwork": "https://www.coursera.org/learn/teamwork-skills",

    #ML ENGINEER
    "mlops": "https://www.coursera.org/learn/mlops-introduction",
    "data preprocessing": "https://www.udemy.com/course/data-preprocessing/",
    "model deployment": "https://www.coursera.org/learn/ml-model-deployment",
    "feature engineering": "https://www.coursera.org/learn/feature-engineering",

    #TECHNICAL WRITING
    "markdown": "https://www.markdowntutorial.com/",
    "api documentation": "https://www.coursera.org/learn/documenting-apis",
    "content structure": "https://www.udemy.com/course/content-strategy-for-beginners/",
    "editing": "https://www.coursera.org/learn/copy-editing",

    #GAME DEV
    "unity": "https://learn.unity.com/",
    "c#": "https://learn.microsoft.com/en-us/dotnet/csharp/",
    "game design": "https://www.coursera.org/specializations/game-design",
    "physics engine": "https://learn.unity.com/tutorial/physics",
    "3d modeling": "https://www.udemy.com/course/blender-3d-modeling/",
    "blender": "https://www.blender.org/support/tutorials/",
    "animation": "https://www.udemy.com/course/animation-masterclass/",
    "multiplayer networking": "https://www.udemy.com/course/multiplayer-game-development/",
    "graphics rendering": "https://www.udemy.com/course/computer-graphics-with-modern-opengl/",

    #ROBOTICS
    "ros": "https://www.coursera.org/learn/robot-operating-system",
    "control systems": "https://www.coursera.org/learn/control-of-mobile-robots",
    "robot kinematics": "https://www.udemy.com/course/robotics-kinematics/",
    "lidar": "https://www.coursera.org/learn/robotics-perception",
    "sensors": "https://www.udemy.com/course/sensors-and-sensor-circuits/",
    "machine vision": "https://www.udemy.com/course/computer-vision-opencv/",
    "embedded systems": "https://www.coursera.org/learn/introduction-embedded-systems",
}

# COURSE_CATALOG = {
#     # Data Science
#     "python": ["https://www.coursera.org/specializations/python"],
#     "machine learning": ["https://www.coursera.org/learn/machine-learning"],
#     "data analysis": ["https://www.coursera.org/specializations/data-analysis"],
#     "pandas": ["https://www.datacamp.com/courses/pandas-foundations"],
#     "numpy": ["https://www.datacamp.com/courses/intro-to-python-for-data-science"],
#     "sql": ["https://www.coursera.org/learn/sql-for-data-science"],
#     "tensorflow": ["https://www.coursera.org/learn/introduction-tensorflow"],
#     "keras": ["https://www.coursera.org/learn/deep-neural-networks-with-keras"],
#     "pytorch": ["https://www.udacity.com/course/deep-learning-pytorch--ud188"],
#     "scikit-learn": ["https://www.datacamp.com/courses/supervised-learning-with-scikit-learn"],
#     "matplotlib": ["https://www.datacamp.com/courses/introduction-to-data-visualization-with-python"],
#     "seaborn": ["https://www.datacamp.com/courses/introduction-to-data-visualization-with-seaborn"],
#     "statistics": ["https://www.coursera.org/learn/basic-statistics"],
#     "data visualization": ["https://www.coursera.org/specializations/data-visualization"],
#     "deep learning": ["https://www.coursera.org/specializations/deep-learning"],

#     # Web Development
#     "html": ["https://www.freecodecamp.org/learn/responsive-web-design/"],
#     "css": ["https://www.codecademy.com/learn/learn-css"],
#     "javascript": ["https://www.codecademy.com/learn/introduction-to-javascript"],
#     "react": ["https://www.codecademy.com/learn/react-101"],
#     "angular": ["https://www.coursera.org/learn/single-page-web-apps-with-angularjs"],
#     "vue.js": ["https://www.udemy.com/course/vuejs-2-the-complete-guide/"],
#     "node.js": ["https://www.coursera.org/learn/server-side-nodejs"],
#     "express.js": ["https://www.udemy.com/course/the-complete-nodejs-developer-course-2/"],
#     "php": ["https://www.codecademy.com/learn/learn-php"],
#     "laravel": ["https://www.udemy.com/course/php-with-laravel-for-beginners-become-a-master-in-laravel/"],
#     "django": ["https://www.coursera.org/learn/django"],
#     "flask": ["https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/"],
#     "mongodb": ["https://www.mongodb.com/learn/mongodb-university"],
#     "git": ["https://www.codecademy.com/learn/learn-git"],

#     # Mobile App Development
#     "java": ["https://www.udemy.com/course/java-the-complete-java-developer-course/"],
#     "kotlin": ["https://www.udacity.com/course/kotlin-for-android-developers--ud888"],
#     "swift": ["https://www.udacity.com/course/ios-developer-nanodegree--nd003"],
#     "objective-c": ["https://www.udemy.com/course/objective-c-for-beginners/"],
#     "flutter": ["https://www.udemy.com/course/flutter-bootcamp-with-dart/"],
#     "react native": ["https://www.coursera.org/learn/react-native"],
#     "xcode": ["https://developer.apple.com/xcode/"],
#     "android studio": ["https://developer.android.com/studio"],
#     "firebase": ["https://firebase.google.com/docs"],
#     "dart": ["https://dart.dev/codelabs"],
#     "ui/ux design": ["https://www.coursera.org/specializations/ui-ux-design"],

#     # UI/UX Design
#     "adobe xd": ["https://www.udemy.com/course/ui-ux-web-design-using-adobe-xd/"],
#     "figma": ["https://www.udemy.com/course/learn-figma/"],
#     "sketch": ["https://www.udemy.com/course/sketch-app-course/"],
#     "invision": ["https://www.udemy.com/course/invision-course/"],
#     "photoshop": ["https://www.udemy.com/course/adobe-photoshop-cc-essentials-training-course/"],
#     "illustrator": ["https://www.udemy.com/course/adobe-illustrator-course/"],
#     "prototyping": ["https://www.coursera.org/learn/prototyping-and-design"],
#     "wireframing": ["https://www.coursera.org/learn/wireframing"],
#     "user research": ["https://www.coursera.org/learn/user-research"],
#     "usability testing": ["https://www.coursera.org/learn/usability-testing"],
#     "interaction design": ["https://www.coursera.org/specializations/interaction-design"],

#     # Cybersecurity
#     "cybersecurity": ["https://www.coursera.org/specializations/ibm-cybersecurity-analyst"],
#     "network security": ["https://www.coursera.org/learn/it-security"],
#     "ethical hacking": ["https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"],

#     # Cloud Computing
#     "cloud computing": ["https://www.coursera.org/specializations/cloud-computing"],
#     "aws": ["https://www.coursera.org/specializations/aws-fundamentals"],
#     "azure": ["https://learn.microsoft.com/en-us/training/azure/"],
#     "gcp": ["https://www.coursera.org/professional-certificates/cloud-architecture-google-cloud"],

#     # DevOps
#     "devops": ["https://www.coursera.org/specializations/devops"],
#     "docker": ["https://www.udemy.com/course/docker-mastery/"],
#     "kubernetes": ["https://www.udemy.com/course/kubernetes-from-a-to-z/"],
#     "jenkins": ["https://www.udemy.com/course/jenkins-from-zero-to-hero/"],

#     # Project Management
#     "project management": ["https://www.coursera.org/specializations/project-management"],
#     "agile": ["https://www.coursera.org/learn/agile-meets-design-thinking"],
#     "scrum": ["https://www.udemy.com/course/scrum-certification/"],

#     # Human Resource
#     "human resource": ["https://www.coursera.org/specializations/human-resource-management"],
#     "recruitment": ["https://www.coursera.org/learn/recruiting-hiring-onboarding-employees"],
#     "talent management": ["https://www.udemy.com/course/talent-management-practices/"]
# }
