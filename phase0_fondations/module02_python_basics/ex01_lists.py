"""
Exercice 1 : Manipulation de listes
Objectif : Maîtriser les opérations basiques sur les listes
"""

# --- PARTIE 1 : Création et accès ---

# Crée une liste de nombres de participants pour 10 événements
participants = [45, 78, 23, 156, 89, 34, 67, 120, 55, 91]

print("📊 Données des participants:", participants)
print("Nombre d'événements:", len(participants))
print("Premier événement:", participants[0])
print("Dernier événement:", participants[-1])
print("3 premiers événements:", participants[:3])
print("3 derniers événements:", participants[-3:])


# --- PARTIE 2 : Opérations statistiques basiques ---

def calculer_stats(data):
    """
    Calcule des statistiques basiques sans utiliser de bibliothèque
    
    Args:
        data (list): Liste de nombres
        
    Returns:
        dict: Dictionnaire contenant les statistiques
    """
    if not data:
        return None
    
    # Moyenne
    moyenne = sum(data) / len(data)
    
    # Min et Max
    minimum = min(data)
    maximum = max(data)
    
    # Médiane (version simplifiée)
    data_sorted = sorted(data)
    n = len(data_sorted)
    if n % 2 == 0:
        mediane = (data_sorted[n//2 - 1] + data_sorted[n//2]) / 2
    else:
        mediane = data_sorted[n//2]
    
    return {
        "moyenne": moyenne,
        "mediane": mediane,
        "min": minimum,
        "max": maximum,
        "etendue": maximum - minimum
    }

stats = calculer_stats(participants)
print("\n📈 Statistiques:")
for cle, valeur in stats.items():
    print(f"  {cle}: {valeur:.2f}")


# --- PARTIE 3 : Filtrage ---

# Événements avec plus de 70 participants
grands_events = [p for p in participants if p > 70]
print(f"\n🎯 Événements avec >70 participants: {grands_events}")
print(f"   Nombre: {len(grands_events)}")

# Événements avec 50-100 participants
moyens_events = [p for p in participants if 50 <= p <= 100]
print(f"\n📊 Événements avec 50-100 participants: {moyens_events}")


# --- TON TOUR ---
# TODO 1: Crée une fonction qui retourne le nombre d'événements avec moins de 50 participants
# TODO 2: Crée une fonction qui calcule le pourcentage d'événements dépassant un seuil donné
# TODO 3: Crée une fonction qui normalise les valeurs (min-max entre 0 et 1)

def compter_petits_events(data, seuil=50):
    """
    Compte le nombre d'événements sous un seuil
    
    Args:
        data (list): Liste de participants
        seuil (int): Seuil de participants
        
    Returns:
        int: Nombre d'événements sous le seuil
    """
    # TON CODE ICI
    pass

def pourcentage_au_dessus(data, seuil):
    """
    Calcule le % d'événements au-dessus d'un seuil
    
    Args:
        data (list): Liste de participants
        seuil (int): Seuil de participants
        
    Returns:
        float: Pourcentage (0-100)
    """
    # TON CODE ICI
    pass

def normaliser_min_max(data):
    """
    Normalise les données entre 0 et 1
    Formule: (x - min) / (max - min)
    
    Args:
        data (list): Liste de nombres
        
    Returns:
        list: Liste normalisée
    """
    # TON CODE ICI
    pass


# Tests (décommente quand tu as terminé)
# print("\n🧪 Tests:")
# print(f"Petits événements (<50): {compter_petits_events(participants)}")
# print(f"% au-dessus de 80: {pourcentage_au_dessus(participants, 80):.1f}%")
# print(f"Données normalisées: {normaliser_min_max(participants)}")