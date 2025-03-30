# Knowledge Learning 🎓

**Knowledge Learning** est une plateforme e-learning développée avec Django REST Framework (back-end) et React (front-end). Elle permet aux utilisateurs de s'inscrire, acheter des leçons ou cursus, suivre leurs progrès, valider des cours, et obtenir des certifications.

---

## 📁 Structure du projet

/KLfolder │ ├── backend/ → Projet Django REST │ ├── api/ → App principale (models, views, serializers, tests) │ └── ... │ └── frontend/ → Application React └── src/


---

## ⚙️ Prérequis

- Python 3.10+
- Node.js 18+
- MySQL Server
- Git

---

## 🐍 Installation du back-end (Django)

```bash
# 1. Se placer dans le dossier backend
cd KLfolder/backend

# 2. Créer et activer un environnement virtuel
python3 -m venv mon_env
source mon_env/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Créer la base de données MySQL (si pas encore faite)
mysql -u root -p
CREATE DATABASE knowledge_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit

# 5. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 6. Créer un superutilisateur (facultatif)
python manage.py createsuperuser

# 7. Lancer le serveur
python manage.py runserver



⚛️ Installation du front-end (React)
bash
Copier
Modifier
# 1. Se placer dans le dossier frontend
cd ../frontend

# 2. Installer les dépendances
npm install

# 3. Lancer le serveur React
npm start


