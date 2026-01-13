from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Experience, Education, Certification, Achievement

class Command(BaseCommand):
    help = 'Seeds the database with portfolio data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Achievement.objects.all().delete()

        # Profile
        Profile.objects.create(
            name="Anjela Mercy Andeo",
            title="Business Intelligence & Data Analytics Specialist",
            summary="Data Analytics Specialist with 4+ years of experience transforming operational, financial, and distribution data into actionable insights that strengthen strategic decision-making. Advanced expertise in Power BI, SQL, Python, data modelling and ETL automation, with a strong ability to translate business requirements into scalable analytics solutions. Proven track record in driving digital transformation and enabling self-service BI across teams. Adept at developing dashboards, performance trackers and automated reporting frameworks that enhance organizational efficiency, compliance, and growth.",
            location="Nairobi, Kenya",
            email="anjelaandeo@gmail.com",
            phone="+254791679849",
            github="https://github.com/",
            linkedin="https://linkedin.com/"
        )

        # Skills
        skills_data = [
            ('ANALYTICS', 'Power BI', 'DAX, Power Query M, Data Modelling'),
            ('ANALYTICS', 'SQL', 'Analysis, ETL, Optimization, Data Validation'),
            ('ANALYTICS', 'Python', 'Pandas, Numpy, Matplotlib'),
            ('ENGINEERING', 'ETL Development & Orchestration', ''),
            ('ENGINEERING', 'Data Pipeline Automation', ''),
            ('ENGINEERING', 'Data Quality Assessment', ''),
            ('ENGINEERING', 'Data Documentations & SOPs', ''),
            ('ENGINEERING', 'Data Integrity & Compliance', ''),
            ('BI', 'Performance & Incentive Analytics', ''),
            ('BI', 'Stakeholder Management', ''),
            ('BI', 'Growth Measurement Frameworks', ''),
            ('BI', 'Process Improvement', ''),
            ('BI', 'Data Storytelling & Visualization', ''),
        ]
        for cat, name, details in skills_data:
            Skill.objects.create(category=cat, name=name, details=details)

        # Achievements
        achievements = [
            "Developed a Streamlit automation engine replacing manual spreadsheet workflows, enhancing transparency and reducing turnaround time across award and incentive processes.",
            "Built a Python-based incentive and commission engine, streamlining reward calculation and enhancing accuracy in sales compensation.",
            "Led Power BI enablement workshops across business teams, increasing self-service adoption and data-driven decision-making by 75%.",
            "Automated SQL- and Python-based reporting pipelines, cutting manual reporting effort by 60%.",
        ]
        for ach in achievements:
            Achievement.objects.create(description=ach)

        # Experience
        # DTB
        dtb_desc = """- Lead the design, development, and implementation of Business Intelligence dashboards and reports in Power BI, ensuring alignment with business KPIs, regulatory requirements, and strategic goals.
- Translate business and use-case requirements into robust data models, ETL logic, and reporting workflows, ensuring analytical outputs directly support decision-making across Marketing, Cards Operations, Finance, and Executive leadership.
- Conduct deep-dive analyses on transaction trends, product performance, and partnership activity, identifying patterns that improved client acquisition, retention, and operational efficiency.
- Implemented automated data pipelines using SQL and Python, reducing manual reporting time by 60%.
- Collaborate with data engineering teams to enhance data quality, improve warehouse integration, and optimize ETL processes, ensuring consistency, governance, and adherence to compliance standards.
- Conduct Power BI training workshops and UAT testing sessions for business users, enabling smooth adoption of BI tools and ensuring dashboards meet user expectations.
- Perform data filtering, cleansing, and validation to maintain reporting accuracy and identify code or data structure issues.

**Data Quality Analyst**
- Conducted data profiling, anomaly detection, and root cause analysis to improve accuracy, completeness, and integrity of data used in operational and financial reporting.
- Championed data governance practices and facilitated internal workshops promoting data literacy and responsible data usage.
- Partnered with engineering teams to automate data validation checks and streamline data flow across critical business systems.

**Data Engineering Collaboration**
- Working with analytics engineer to create scalable data architectures and distributed systems to enhance performance, availability, and flexibility of data pipelines."""

        Experience.objects.create(
            role="Business Intelligence Developer",
            company="Diamond Trust Bank",
            date_range="July 2023 - To date",
            description=dtb_desc,
            order=1
        )

        # ASAP
        asap_desc = """- Collaborated with stakeholders to gather data requirements and translate business needs into usable insights and analytical solutions.
- Identified inefficiencies and risks in financial data by ensuring they followed the Anti-Money Laundering Policy and Procedures.
- Trained new employees on due diligence software, including PEP lists, credit check systems, and the BRS portal, to enhance the quality and efficiency of financial investigations.
- Carried out detailed background checks and fraud screening processes using structured datasets to guide risk mitigation strategies.
- Maintained data integrity by following precision, consistency, and reliability of measurements of business performance and compliance."""
        
        Experience.objects.create(
            role="Data Analyst",
            company="ASAP Information Services Limited",
            date_range="Sept 2021 - June 2023",
            description=asap_desc,
            order=2
        )

        # Kantar
        kantar_desc = """- Assessed Monitored and analyzed customer service performance metrics, improving operational efficiency by 80%.
- Monitored performance metrics, ensuring adherence to regulatory compliance and policy standards.
- Compiled and digitized survey and interview results, ensuring accurate data collection and entry."""

        Experience.objects.create(
            role="Quantitative Analyst",
            company="Kantar TNS Kenya",
            date_range="June 2020 – Aug 2021",
            description=kantar_desc,
            order=3
        )

        # Education
        Education.objects.create(
            degree="Bachelor of Science in Mathematics (Applied Mathematics and Statistics)",
            institution="Jomo Kenyatta University of Agriculture and Technology",
            grade="Second Class Upper Division",
            year="2021",
            order=1
        )

        # Certifications
        certs = [
            ("Cyber Shujaa Data Protection Masterclass", "USIU", "2025"),
            ("Azure Data Fundamentals (DP 900)", "Microsoft", "2024"),
            ("Microsoft Power BI", "Datacamp", "2024"),
            ("SQL for data analysis", "Udemy", "2023"),
            ("Python for Data analysis", "ALX Africa", "2022"),
        ]
        for name, issuer, year in certs:
            Certification.objects.create(name=name, issuer=issuer, year=year)

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
