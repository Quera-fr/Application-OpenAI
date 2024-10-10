# Projet Streamlit - Fonctionnalités OpenAI

Ce projet **Streamlit** présente plusieurs fonctionnalités d'OpenAI à travers différentes pages. L'application permet d'explorer des outils comme **DALL-E**, **Whisper**, et d'effectuer des analyses d'images, ainsi que du fine-tuning de modèles.

## Pages du Projet

### 1. `Dall-E.py`
Cette page permet de générer des images en utilisant le modèle **DALL-E** d'OpenAI. En entrant une description textuelle, l'utilisateur peut créer des images à partir de cette description, en exploitant la puissance de la génération par IA.

### 2. `Whisper.py`
Cette page propose un service de **transcription audio** grâce à **Whisper**, l'outil de reconnaissance vocale d'OpenAI. Vous pouvez uploader un fichier audio, et l'application retournera la transcription du contenu audio.

### 3. `Entrainement fin.py`
Cette page est dédiée au **fine-tuning** d'un modèle. Vous pouvez utiliser vos propres jeux de données pour ajuster un modèle pré-entraîné, optimisant ainsi ses performances pour des tâches spécifiques.

### 4. `Image Analyse.py`
Cette page vous permet d'**analyser des images** à l'aide des capacités d'OpenAI. Vous pouvez soumettre une image pour obtenir des insights, des annotations ou d'autres analyses basées sur l'IA.

---

## Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/Quera-fr/Application-OpenAI.git
   ```

2. Installez les dépendances nécessaires via `pip` :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application Streamlit :
   ```bash
   streamlit run Home-E.py
   ```

## Prérequis

- **Python 3.7+**
- **Streamlit** doit être installé (voir `requirements.txt` pour toutes les dépendances)
- Accès aux API d'OpenAI pour les fonctionnalités (DALL-E, Whisper, etc.)

---

## Fonctionnalités principales

- **Génération d'images** avec DALL-E
- **Transcription audio** avec Whisper
- **Fine-tuning** d'un modèle avec vos propres données
- **Analyse d'images** via l'intelligence artificielle

---

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez ajouter de nouvelles fonctionnalités ou améliorer les pages existantes, n'hésitez pas à soumettre des **pull requests**.

---

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer selon les termes de la licence.

---

## Auteur

Ce projet a été réalisé dans le cadre d'une présentation des fonctionnalités d'OpenAI à travers une application **Streamlit**.
