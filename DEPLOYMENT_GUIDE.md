# Guide de Déploiement - Assistant Recherche d'Emploi

## Description

Cette application web complète vous aide dans votre recherche d'emploi en tant qu'ingénieur systèmes embarqués. Elle comprend :

- **Recherche d'offres d'emploi** : Interface pour rechercher des offres correspondant à votre profil
- **Génération de CV adaptatifs** : Adaptation automatique de votre CV selon les offres
- **Lettres de motivation personnalisées** : Génération automatique de lettres sur mesure
- **Suivi des candidatures** : Tableau de bord pour suivre toutes vos candidatures

## Architecture

L'application est composée de :
- **Frontend** : Interface React avec Tailwind CSS et shadcn/ui
- **Backend** : API Flask avec base de données SQLite
- **Intégration** : Frontend compilé et servi par Flask

## Prérequis

- Python 3.11+
- Node.js 20+ (pour les modifications du frontend)
- Git

## Installation Locale

1. **Cloner le projet** :
   ```bash
   git clone <votre-repo>
   cd job-search-assistant
   ```

2. **Activer l'environnement virtuel** :
   ```bash
   source venv/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application** :
   ```bash
   python src/main.py
   ```

5. **Accéder à l'application** :
   Ouvrez votre navigateur sur `http://localhost:5000`

## Options de Déploiement

### Option 1 : Heroku (Recommandé)

1. **Créer un compte Heroku** : https://heroku.com

2. **Installer Heroku CLI** : https://devcenter.heroku.com/articles/heroku-cli

3. **Créer une application Heroku** :
   ```bash
   heroku create votre-app-name
   ```

4. **Créer un fichier Procfile** :
   ```bash
   echo "web: python src/main.py" > Procfile
   ```

5. **Déployer** :
   ```bash
   git add .
   git commit -m "Deploy job search assistant"
   git push heroku main
   ```

### Option 2 : Railway

1. **Créer un compte Railway** : https://railway.app

2. **Connecter votre repository GitHub**

3. **Railway détectera automatiquement votre application Flask**

4. **L'application sera déployée automatiquement**

### Option 3 : Render

1. **Créer un compte Render** : https://render.com

2. **Créer un nouveau Web Service**

3. **Connecter votre repository GitHub**

4. **Configurer** :
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python src/main.py`

### Option 4 : DigitalOcean App Platform

1. **Créer un compte DigitalOcean** : https://digitalocean.com

2. **Utiliser App Platform**

3. **Connecter votre repository GitHub**

4. **Configurer l'application Flask**

## Configuration pour la Production

### Variables d'Environnement

Créez un fichier `.env` ou configurez les variables suivantes :

```bash
FLASK_ENV=production
SECRET_KEY=votre-clé-secrète-très-sécurisée
DATABASE_URL=sqlite:///app.db
```

### Sécurité

1. **Changez la clé secrète** dans `src/main.py` :
   ```python
   app.config['SECRET_KEY'] = 'votre-nouvelle-clé-très-sécurisée'
   ```

2. **Désactivez le mode debug** pour la production :
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

## Personnalisation

### Modifier le Profil Utilisateur

Éditez le fichier `src/routes/job_search.py` pour mettre à jour :
- Vos informations personnelles
- Vos compétences
- Vos projets
- Votre expérience

### Ajouter de Vraies Sources d'Offres

Remplacez les données d'exemple dans `SAMPLE_JOBS` par des appels à de vraies APIs :
- Indeed API
- LinkedIn API
- Pôle Emploi API
- APIs d'entreprises spécifiques

### Personnaliser l'Interface

Le frontend est dans `job-search-frontend/src/`. Pour modifier :

1. **Installer les dépendances** :
   ```bash
   cd job-search-frontend
   pnpm install
   ```

2. **Modifier les composants** dans `src/`

3. **Reconstruire** :
   ```bash
   pnpm run build
   ```

4. **Copier dans le backend** :
   ```bash
   cp -r dist/* ../job-search-assistant/src/static/
   ```

## Fonctionnalités Avancées à Implémenter

### Intégrations API Réelles

- **Indeed API** : Pour récupérer de vraies offres
- **LinkedIn API** : Pour la recherche et le networking
- **Email API** : Pour l'envoi automatique de candidatures
- **Calendar API** : Pour la planification des relances

### Améliorations IA

- **Analyse sémantique** : Meilleure correspondance offres/profil
- **Génération de contenu** : CV et lettres plus sophistiqués
- **Recommandations** : Suggestions d'offres personnalisées

### Base de Données

- **PostgreSQL** : Pour une base de données plus robuste
- **Authentification** : Système de comptes utilisateurs
- **Sauvegarde** : Système de backup automatique

## Support et Maintenance

### Logs

Les logs de l'application sont disponibles via :
```bash
heroku logs --tail  # Pour Heroku
```

### Monitoring

Configurez des alertes pour :
- Erreurs d'application
- Performance
- Disponibilité

### Mises à Jour

Pour déployer des mises à jour :
```bash
git add .
git commit -m "Mise à jour"
git push heroku main  # Ou votre plateforme de déploiement
```

## Troubleshooting

### Problèmes Courants

1. **Erreur de dépendances** :
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

2. **Problème de base de données** :
   ```bash
   rm src/database/app.db
   python src/main.py  # Recrée la base
   ```

3. **Erreur de CORS** :
   Vérifiez que `flask-cors` est installé et configuré

### Contact

Pour toute question ou problème :
- Email : merouane@lakdim.com
- LinkedIn : https://www.linkedin.com/in/marouen-lakdim-0a92861b3

---

**Bonne chance dans votre recherche d'emploi !** 🚀

