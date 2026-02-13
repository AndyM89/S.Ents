"""
Module 0.1 - Premier script Python
Objectif : Vérifier que l'environnement fonctionne
"""

def hello_ml():
    """Fonction simple pour tester"""
    message = "🚀 Hello ML ! Environnement prêt pour l'IA."
    print(message)
    return message

def check_packages():
    """Vérifie que les packages sont installés"""
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import sklearn
        
        print("✅ NumPy version:", np.__version__)
        print("✅ Pandas version:", pd.__version__)
        print("✅ Matplotlib version:", plt.matplotlib.__version__)
        print("✅ Scikit-learn version:", sklearn.__version__)
        print("\n🎉 Tous les packages sont installés correctement !")
        return True
    except ImportError as e:
        print("❌ Erreur:", e)
        return False

if __name__ == "__main__":
    hello_ml()
    print()
    check_packages()
