# 🎬 Script Wallpaper & Vidéo en EXE

Script Python qui :
- ✅ Change le fond d'écran avec `Capture2.png`
- ✅ Lance la vidéo `video1.mp4`
- ✅ Affiche un diaporama des images : Capture1.png à Capture6.png

## 📋 Prérequis

- Python 3.8+
- Les bibliothèques listées dans `requirements.txt`
- Windows (pour changer le fond d'écran)

## 🚀 Installation & Utilisation

### Méthode 1 : Exécuter le script Python directement

```bash
pip install -r requirements.txt
python main.py
```

### Méthode 2 : Transformer en EXE (recommandé)

#### Étape 1 : Installer les dépendances
```bash
pip install -r requirements.txt
```

#### Étape 2 : Créer l'EXE avec PyInstaller
```bash
pyinstaller main.spec
```

L'EXE sera créé dans le dossier `dist/main.exe`

#### Étape 3 : Utiliser l'EXE
- Copier `main.exe` dans le même dossier que vos fichiers médias
- Mettre dans le même dossier :
  - `Capture1.png` à `Capture6.png`
  - `Capture2.png` (fond d'écran)
  - `video1.mp4`
- Double-cliquer sur `main.exe`

## 📁 Structure des fichiers

```
/
├── main.py                 # Script principal
├── main.spec              # Configuration PyInstaller
├── requirements.txt       # Dépendances Python
├── Capture1.png          # Image du diaporama
├── Capture2.png          # Fond d'écran
├── Capture3.png          # Image du diaporama
├── Capture4.png          # Image du diaporama
├── Capture5.png          # Image du diaporama
├── Capture6.png          # Image du diaporama
└── video1.mp4            # Vidéo à lancer
```

## ⚙️ Configuration

Modifiez les variables en haut du fichier `main.py` si besoin :

```python
WALLPAPER_IMAGE = "Capture2.png"
VIDEO_FILE = "video1.mp4"
IMAGES_TO_DISPLAY = [
    "Capture1.png",
    "Capture2.png",
    ...
]
```

## 🎯 Fonctionnalités

1. **Changement de fond d'écran** : Utilise l'API Windows pour changer le wallpaper
2. **Lancement vidéo** : Ouvre la vidéo avec le lecteur par défaut
3. **Diaporama** : Affiche les images une par une (3 secondes chacune)
4. **Gestion d'erreurs** : Vérifie l'existence des fichiers et affiche des messages clairs

## 💡 Astuces

- Pour personnaliser le temps d'affichage des images, modifier la ligne :
  ```python
  key = cv2.waitKey(3000)  # 3000 ms = 3 secondes
  ```

- Appuyer sur **ESC** pendant le diaporama pour fermer l'application

## 📝 Licence

Libre d'utilisation

---

**Créé pour** : Transformer le fond d'écran et afficher des médias simplement
