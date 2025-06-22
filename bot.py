
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Launcher automatique pour le code obfusqu�
"""

import sys
import os

def main():
    try:
        # Import and run the obfuscated code
        import obfuscated
        print("[INFO] Code obfusqu� ex�cut� avec succ�s!")
    except ImportError:
        print("[ERREUR] Fichier obfuscated.py non trouv�!")
        sys.exit(1)
    except Exception as e:
        print(f"[ERREUR] Erreur lors de l'ex�cution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
        
