# 📘 DOCUMENTATION FONCTIONNELLE & DATA MODEL

## SaaS de Gestion d'Événements de Mariage

------------------------------------------------------------------------

# 1️⃣ ARCHITECTURE GÉNÉRALE DU SaaS

## 🎯 Objectif

Plateforme web multi-tenant permettant : - Gestion complète d'un
mariage - Collaboration entre mariés, organisateurs et prestataires -
Centralisation budgétaire et logistique - Suivi opérationnel et
planning - Exploitation future en Data Analytics & IA

------------------------------------------------------------------------

# 2️⃣ MODÈLE DATA (VISION ARCHITECTURE)

## 🏢 Organization (Tenant)

Représente une entité métier : - Couple (client) - Prestataire - Agence
d'organisation

### Champs

-   id (UUID)
-   name
-   type (client \| vendor \| agency)
-   created_at
-   updated_at
-   deleted_at

------------------------------------------------------------------------

## 👤 User

-   id (UUID)
-   firstname
-   lastname
-   email (unique)
-   password_hash
-   organization_id (FK)
-   created_at
-   updated_at
-   status

------------------------------------------------------------------------

## 🔐 Roles

### roles

-   id
-   name (admin, planner, vendor, client)

### user_roles

-   user_id
-   role_id
-   event_id (optionnel si rôle spécifique à un mariage)

------------------------------------------------------------------------

## 💍 Event (Mariage)

-   id (UUID)
-   title
-   wedding_date
-   ceremony_location
-   reception_location
-   status (draft \| planning \| confirmed \| completed)
-   budget_expected
-   budget_actual
-   organization_id (FK vers couple)
-   created_at
-   updated_at

------------------------------------------------------------------------

## 🤝 Event_Vendors

-   id
-   event_id
-   vendor_org_id
-   contract_status
-   agreed_price
-   deposit_amount
-   final_payment_due_date
-   notes

------------------------------------------------------------------------

## 📋 Task (Planning)

-   id
-   event_id
-   title
-   description
-   assigned_to (user_id)
-   start_date
-   due_date
-   priority
-   status
-   dependencies

------------------------------------------------------------------------

## 💰 BudgetCategory

-   id
-   event_id
-   name
-   allocated_amount

------------------------------------------------------------------------

## 💳 Expense

-   id
-   event_id
-   vendor_id
-   category_id
-   amount
-   status
-   payment_date
-   invoice_reference

------------------------------------------------------------------------

## 🎟 Guest

-   id
-   event_id
-   firstname
-   lastname
-   email
-   phone
-   rsvp_status
-   meal_choice
-   plus_one_allowed
-   table_assignment

------------------------------------------------------------------------

## 📊 ActivityLog

-   id
-   organization_id
-   event_id
-   user_id
-   action_type
-   entity_type
-   entity_id
-   timestamp

------------------------------------------------------------------------

# 3️⃣ INFORMATIONS À COLLECTER AUPRÈS DES MARIÉS

## 👰 Informations personnelles

-   Noms complets
-   Coordonnées
-   Budget total estimé
-   Nombre estimé d'invités
-   Date(s) envisagée(s)
-   Style souhaité (traditionnel, moderne, bohème...)
-   Thème
-   Couleurs dominantes
-   Contraintes culturelles ou religieuses

------------------------------------------------------------------------

## 📍 Informations logistiques

-   Lieu cérémonie
-   Lieu réception
-   Plan B météo
-   Hébergement invités
-   Transport prévu
-   Horaires détaillés de la journée

------------------------------------------------------------------------

## 💰 Informations budgétaires détaillées

-   Budget global
-   Budget par catégorie :
    -   Lieu
    -   Traiteur
    -   Photographe
    -   Vidéaste
    -   DJ / groupe
    -   Décoration
    -   Robe & costume
    -   Alliances
    -   Papeterie
    -   Fleurs
    -   Animation
    -   Sécurité
    -   Assurance

------------------------------------------------------------------------

## 🎯 Priorités stratégiques

-   Ce qui est non négociable
-   Ce qui est flexible
-   Niveau de luxe attendu
-   Expérience recherchée pour les invités

------------------------------------------------------------------------

# 4️⃣ INFORMATIONS UTILES POUR CHOISIR UN PRESTATAIRE

## 📊 Critères financiers

-   Fourchette tarifaire
-   Modalités de paiement
-   Politique d'annulation
-   Dépôt requis
-   Frais cachés

------------------------------------------------------------------------

## 📁 Portfolio & crédibilité

-   Photos de réalisations
-   Vidéos
-   Avis clients vérifiés
-   Références
-   Certifications

------------------------------------------------------------------------

## 🕒 Disponibilité

-   Dates libres
-   Capacité maximale
-   Temps d'installation
-   Contraintes techniques

------------------------------------------------------------------------

## 🔎 Spécialisation

-   Type de mariage maîtrisé
-   Taille d'événements habituels
-   Culture spécifique

------------------------------------------------------------------------

## 📃 Aspects contractuels

-   Contrat formel
-   Assurance professionnelle
-   Responsabilité civile
-   Conditions générales

------------------------------------------------------------------------

# 5️⃣ INFORMATIONS QUE LES PRESTATAIRES DOIVENT FOURNIR

## 🏢 Profil entreprise

-   Nom légal
-   Numéro d'enregistrement
-   Adresse
-   Assurance
-   Statut juridique

------------------------------------------------------------------------

## 📸 Présentation commerciale

-   Description détaillée
-   Positionnement (premium, accessible...)
-   Valeur ajoutée
-   Équipe & expérience
-   Années d'activité

------------------------------------------------------------------------

## 💼 Offres & Packages

-   Détail des prestations
-   Tarification claire
-   Options additionnelles
-   Capacité maximale
-   Zones géographiques couvertes

------------------------------------------------------------------------

## 📆 Opérationnel

-   Processus de réservation
-   Délai de réponse moyen
-   Planning type d'intervention
-   Équipement fourni
-   Besoins techniques

------------------------------------------------------------------------

## 📊 Données analytiques utiles

-   Taux de satisfaction
-   Nombre d'événements réalisés
-   Budget moyen géré
-   Catégorie dominante

------------------------------------------------------------------------

# 6️⃣ ÉVOLUTION DATA & IA FUTURE

## 🔮 Cas d'usage IA

-   Prédiction dépassement budget
-   Recommandation prestataire automatique
-   Optimisation planning
-   Analyse comportement RSVP
-   Score de compatibilité couple/prestataire

------------------------------------------------------------------------

# 7️⃣ BONNES PRATIQUES TECHNIQUES

-   UUID partout
-   Soft delete
-   Index sur toutes les FK
-   Historisation des modifications
-   Séparation base transactionnelle / base analytique
-   Logs complets pour audit
-   Architecture scalable (PostgreSQL recommandé)

------------------------------------------------------------------------

# 📌 CONCLUSION

Ce document constitue : - La base du modèle data - Le cadrage
fonctionnel métier - La préparation pour une évolution IA - Une
fondation solide SaaS multi-tenant
