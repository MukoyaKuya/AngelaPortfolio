from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Profile photo (square recommended)")
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('ANALYTICS', 'Analytics & Technical Tools'),
        ('ENGINEERING', 'Data Engineering & Governance'),
        ('BI', 'Business Intelligence & Strategy'),
    ]
    name = models.CharField(max_length=200) # Increased length just in case
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    details = models.TextField(help_text="Comma separated details", blank=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description[:50]

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100)
    description = models.TextField(help_text="Bullet points separated by newlines")
    company_logo = models.FileField(upload_to='experience/logos/', blank=True, null=True, help_text="Company logo (PNG, JPG, or SVG)")
    work_image = models.ImageField(upload_to='experience/images/', blank=True, null=True, help_text="Project screenshot or relevant visual")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    LEVEL_CHOICES = [
        ('PRIMARY', 'Primary School'),
        ('SECONDARY', 'Secondary School'),
        ('TERTIARY', 'University/College'),
        ('POSTGRAD', 'Postgraduate'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='TERTIARY')
    degree = models.CharField(max_length=200, help_text="Degree name or certificate (e.g., KCPE, KCSE, BSc)")
    institution = models.CharField(max_length=200)
    grade = models.CharField(max_length=100, blank=True, help_text="Grade/Score (e.g., A, B+, First Class)")
    year = models.CharField(max_length=20)
    logo = models.FileField(upload_to='education/logos/', blank=True, null=True, help_text="Institution logo (PNG, JPG, or SVG)")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_level_display()} - {self.degree}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    logo = models.FileField(upload_to='certifications/logos/', blank=True, null=True, help_text="Issuer logo (PNG, JPG, or SVG)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
