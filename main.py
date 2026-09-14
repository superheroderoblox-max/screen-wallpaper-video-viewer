import os
import sys
import ctypes
import time
import subprocess
from PIL import Image
import cv2

# Configuration
WALLPAPER_IMAGE = "Capture2.png"
VIDEO_FILE = "video1.mp4"
IMAGES_TO_DISPLAY = [
    "Capture1.png",
    "Capture2.png",
    "Capture3.png",
    "Capture4.png",
    "Capture5.png",
    "Capture6.png"
]

def change_wallpaper(image_path):
    """Change le fond d'écran Windows"""
    if not os.path.exists(image_path):
        print(f"Erreur: L'image {image_path} n'existe pas!")
        return False
    
    # Utiliser le chemin absolu
    absolute_path = os.path.abspath(image_path)
    
    try:
        # Windows
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 0)
        print(f"✓ Fond d'écran changé avec: {image_path}")
        return True
    except Exception as e:
        print(f"✗ Erreur lors du changement de fond d'écran: {e}")
        return False

def play_video(video_path):
    """Lance la vidéo"""
    if not os.path.exists(video_path):
        print(f"Erreur: La vidéo {video_path} n'existe pas!")
        return False
    
    try:
        # Utiliser VLC ou le lecteur par défaut
        os.startfile(video_path)
        print(f"✓ Vidéo lancée: {video_path}")
        return True
    except Exception as e:
        print(f"✗ Erreur lors du lancement de la vidéo: {e}")
        return False

def display_images_slideshow(image_list):
    """Affiche les images en diaporama"""
    valid_images = []
    
    for img_path in image_list:
        if os.path.exists(img_path):
            valid_images.append(img_path)
        else:
            print(f"⚠ Attention: {img_path} n'existe pas!")
    
    if not valid_images:
        print("✗ Aucune image valide à afficher!")
        return False
    
    try:
        cv2.namedWindow('Diaporama', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Diaporama', 800, 600)
        
        print(f"✓ Affichage du diaporama ({len(valid_images)} images)")
        print("Appuyez sur ESC pour fermer le diaporama")
        
        for img_path in valid_images:
            img = cv2.imread(img_path)
            if img is not None:
                cv2.imshow('Diaporama', img)
                print(f"  Affichage: {img_path} (appuyez sur une touche pour continuer)")
                
                # Attendre 3 secondes ou jusqu'à ce qu'une touche soit pressée
                key = cv2.waitKey(3000)
                if key == 27:  # ESC
                    break
            else:
                print(f"  ✗ Impossible de charger: {img_path}")
        
        cv2.destroyAllWindows()
        return True
        
    except Exception as e:
        print(f"✗ Erreur lors de l'affichage des images: {e}")
        return False

def main():
    """Fonction principale"""
    print("=" * 50)
    print("GESTIONNAIRE D'ÉCRAN ET VIDÉO")
    print("=" * 50)
    
    # Vérifier que tous les fichiers existent
    all_files = [WALLPAPER_IMAGE, VIDEO_FILE] + IMAGES_TO_DISPLAY
    missing_files = [f for f in all_files if not os.path.exists(f)]
    
    if missing_files:
        print("\n⚠ Fichiers manquants:")
        for f in missing_files:
            print(f"  - {f}")
        print("\nAssurez-vous que tous les fichiers sont dans le même dossier que le script!")
    
    print("\nDémarrage...")
    
    # 1. Changer le fond d'écran
    print("\n1️⃣  Changement du fond d'écran...")
    change_wallpaper(WALLPAPER_IMAGE)
    time.sleep(1)
    
    # 2. Lancer la vidéo
    print("\n2️⃣  Lancement de la vidéo...")
    play_video(VIDEO_FILE)
    time.sleep(2)
    
    # 3. Afficher les images en diaporama
    print("\n3️⃣  Affichage du diaporama...")
    display_images_slideshow(IMAGES_TO_DISPLAY)
    
    print("\n" + "=" * 50)
    print("✓ Programme terminé!")
    print("=" * 50)

if __name__ == "__main__":
    main()
    input("\nAppuyez sur ENTRÉE pour fermer...")
