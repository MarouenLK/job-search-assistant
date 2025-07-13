from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import requests
import re
from datetime import datetime, timedelta
import json

job_search_bp = Blueprint('job_search', __name__)

# Données d'exemple pour la démonstration
SAMPLE_JOBS = [
    {
        "id": 1,
        "title": "Ingénieur Systèmes Embarqués Freertos - Paris H/F",
        "company": "Astek",
        "location": "Paris - 75",
        "contract": "CDI",
        "publishedDate": "il y a 1 jour",
        "description": "Participer au développement de logiciels temps réel avec FreeRTOS. Conception et développement de logiciels embarqués (C/C++, RTOS).",
        "skills": ["C/C++", "FreeRTOS", "Systèmes embarqués", "RTOS"],
        "url": "https://example.com/job1"
    },
    {
        "id": 2,
        "title": "Ingénieur FPGA (secteur aéronautique) F/H",
        "company": "SERMA Ingénierie",
        "location": "Valence - 26",
        "contract": "CDI",
        "salary": "42 - 60 k€ brut annuel",
        "publishedDate": "30/06/2025",
        "description": "Développement FPGA pour l'aéronautique. Conception et développement de modules VHDL pour systèmes critiques.",
        "skills": ["VHDL", "FPGA", "Aéronautique", "Quartus", "ModelSim"],
        "url": "https://example.com/job2"
    },
    {
        "id": 3,
        "title": "Ingénieur Développement Firmware H/F",
        "company": "Tech Solutions Inc.",
        "location": "Île-de-France",
        "contract": "CDI",
        "publishedDate": "il y a 3 jours",
        "description": "Développement firmware pour systèmes IoT. Expérience avec ESP32, communication LoRa et protocoles IoT.",
        "skills": ["C/C++", "ESP32", "IoT", "Firmware", "LoRa", "Python"],
        "url": "https://example.com/job3"
    },
    {
        "id": 4,
        "title": "Ingénieur Électronique Numérique - FPGA/VHDL (H/F)",
        "company": "MCA Groupe",
        "location": "Orsay - 91",
        "contract": "CDI",
        "salary": "A partir de 50 k€ brut annuel",
        "publishedDate": "il y a 1 semaine",
        "description": "Conception et développement de systèmes électroniques numériques. Maîtrise des outils de CAO électronique.",
        "skills": ["VHDL", "FPGA", "Électronique numérique", "Altium", "KiCad"],
        "url": "https://example.com/job4"
    }
]

@job_search_bp.route('/search', methods=['POST'])
@cross_origin()
def search_jobs():
    """Recherche d'offres d'emploi basée sur des mots-clés"""
    try:
        data = request.get_json()
        keywords = data.get('keywords', '').lower()
        location = data.get('location', 'Île-de-France').lower()
        
        # Simulation de recherche - filtrage des offres d'exemple
        filtered_jobs = []
        for job in SAMPLE_JOBS:
            # Recherche dans le titre, description et compétences
            searchable_text = f"{job['title']} {job['description']} {' '.join(job['skills'])}".lower()
            location_text = job['location'].lower()
            
            if (not keywords or any(keyword.strip() in searchable_text for keyword in keywords.split(','))) and \
               (not location or location in location_text):
                filtered_jobs.append(job)
        
        return jsonify({
            'success': True,
            'jobs': filtered_jobs,
            'total': len(filtered_jobs)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@job_search_bp.route('/generate-cv', methods=['POST'])
@cross_origin()
def generate_adapted_cv():
    """Génère un CV adapté pour une offre spécifique"""
    try:
        data = request.get_json()
        job_description = data.get('job_description', '')
        job_title = data.get('job_title', '')
        company = data.get('company', '')
        
        # Profil de base de l'utilisateur
        base_profile = {
            "name": "Merouane LAKDIM",
            "title": "Ingénieur en systèmes embarqués",
            "email": "merouane@lakdim.com",
            "phone": "07 45 65 41 94",
            "location": "Paris, France",
            "portfolio": "https://merouane.lakdim.com",
            "linkedin": "https://www.linkedin.com/in/marouen-lakdim-0a92861b3",
            "skills": {
                "langages": ["Python", "C", "C++", "VHDL", "Assembleur", "HTML", "CSS", "Java"],
                "outils_fpga": ["Quartus Prime", "ModelSim", "MAX+PLUS II"],
                "cartes": ["ESP32", "Raspberry Pi", "LoRa", "GPS"],
                "logiciels": ["Altium", "KiCad", "Proteus", "Cadence Virtuoso", "MATLAB", "LTSpice"]
            }
        }
        
        # Analyse des compétences pertinentes
        relevant_skills = []
        job_text = f"{job_title} {job_description}".lower()
        
        for category, skills in base_profile["skills"].items():
            for skill in skills:
                if skill.lower() in job_text:
                    relevant_skills.append(skill)
        
        # Génération du CV adapté
        adapted_cv = {
            "profile": base_profile,
            "highlighted_skills": relevant_skills,
            "adaptation_note": f"CV adapté pour le poste de {job_title} chez {company}",
            "generated_at": datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'adapted_cv': adapted_cv
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@job_search_bp.route('/generate-cover-letter', methods=['POST'])
@cross_origin()
def generate_cover_letter():
    """Génère une lettre de motivation personnalisée"""
    try:
        data = request.get_json()
        job_title = data.get('job_title', '')
        company = data.get('company', '')
        sector = data.get('sector', '')
        job_description = data.get('job_description', '')
        
        # Template de lettre de motivation
        letter_template = f"""Objet : Candidature au poste d'{job_title}

Madame, Monsieur,

C'est avec un grand intérêt que j'ai découvert votre offre d'emploi pour le poste d'{job_title}. Jeune diplômé d'un Master en systèmes embarqués de l'Université de Lorraine, je suis vivement intéressé par les défis techniques proposés et convaincu que mes compétences correspondent parfaitement aux exigences de ce poste.

Votre entreprise, {company}, est un acteur reconnu dans le secteur {sector}, un domaine qui me passionne particulièrement. Vos projets innovants témoignent de votre engagement envers l'excellence technologique et la recherche de solutions de pointe.

Au cours de mes expériences, j'ai développé une solide expertise en conception et développement de systèmes embarqués. Mon projet de fin d'études, axé sur la création d'un système d'IA pour l'optimisation du trafic, m'a permis de maîtriser des technologies telles que l'ESP32, la communication LoRa et l'intégration de solutions d'IA sur des plateformes comme la Raspberry Pi.

Ma maîtrise des langages VHDL, C/C++ et Python, ainsi que mon expérience avec des outils de CAO électronique comme Altium et KiCad, me permettront d'être rapidement opérationnel et de contribuer efficacement à vos projets.

Je suis persuadé que mon enthousiasme, ma rigueur et ma capacité à travailler en équipe seront des atouts pour votre entreprise. Je serais ravi de vous rencontrer pour vous exposer plus en détail ma motivation et l'adéquation de mon profil avec ce poste.

Dans l'attente de votre retour, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Merouane LAKDIM
merouane@lakdim.com
07 45 65 41 94"""
        
        return jsonify({
            'success': True,
            'cover_letter': letter_template,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@job_search_bp.route('/applications', methods=['GET', 'POST'])
@cross_origin()
def manage_applications():
    """Gestion des candidatures"""
    if request.method == 'GET':
        # Retourner la liste des candidatures (simulation)
        applications = [
            {
                "id": 1,
                "company": "Tech Solutions Inc.",
                "position": "Ingénieur Développement Firmware H/F",
                "applicationDate": "2025-07-13",
                "followUpDate": "2025-07-27",
                "status": "En attente"
            }
        ]
        return jsonify({
            'success': True,
            'applications': applications
        })
    
    elif request.method == 'POST':
        # Ajouter une nouvelle candidature
        try:
            data = request.get_json()
            new_application = {
                "id": len([]) + 1,  # Simulation d'ID
                "company": data.get('company'),
                "position": data.get('position'),
                "applicationDate": datetime.now().strftime('%Y-%m-%d'),
                "followUpDate": (datetime.now() + timedelta(weeks=2)).strftime('%Y-%m-%d'),
                "status": "En attente"
            }
            
            return jsonify({
                'success': True,
                'application': new_application
            })
        
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

