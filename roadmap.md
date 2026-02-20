# Roadmap SmartEvent — Moteur Devis / Planification / Logistique (Wedding)
Date: 2026-02-20  
Équipe: 2 Full‑Stack + 1 Data  
Objectif: Livrer un MVP “génération devis + plan + tâches + recommandations simples” utilisable en production, puis évoluer vers IA.

---

## 0) Hypothèses & principes (pour avancer malgré les “pas encore décidé”)
### Hypothèses MVP (recommandées)
- **Devis = estimation** (fourchettes + avertissements), pas un prix engageant.
- **Validation humaine** (optionnelle) avant envoi au client: mode “Draft → Review → Sent”.
- **Prestataires au début = catalogue interne minimal** + option “prix moyens” si pas de données.
- **Entrées minimales client** (MVP):
  - Date (ou mois/année)
  - Ville / région
  - Nombre d’invités
  - Budget OU gamme (Eco/Standard/Premium)

### Principes techniques
- “IA plus tard” : **Règles + templates** d’abord, car c’est explicable, testable, rapide.
- Design “data-ready” : dès le MVP, journaliser les choix et résultats pour entraîner des modèles plus tard.

---

## 1) Stack & architecture (choix technos)
### Frontend Web
- **Next.js (React)** + TypeScript
- UI: TailwindCSS (ou MUI si déjà choisi)
- State: React Query (TanStack Query)
- Auth: JWT (access + refresh)

### Backend
- **NestJS (Node.js)** + TypeScript
- API: REST (GraphQL option plus tard)
- Validation: class-validator
- Jobs async: BullMQ + Redis
- Notifications: FCM (push) plus tard

### Base de données
- **PostgreSQL**
- ORM: Prisma (ou TypeORM si standard Nest déjà en place)

### Data / IA
- Python (FastAPI) **optionnel au MVP**  
  - MVP: règles codées côté NestJS
  - IA: microservice Python plus tard pour modèles
- Feature store simple: tables Postgres + exports parquet (phase 2)

### DevOps
- Docker + docker-compose (dev)
- CI: GitHub Actions
- Deploy: AWS (ECS/Fargate) ou Azure (App Service/Container Apps)

---

## 2) Rôles & responsabilités (qui fait quoi)
### Full‑Stack Dev A (FS-A) — “Backend + Domain”
- Conçoit le **modèle de données** (Prisma/SQL)
- Implémente les **APIs NestJS** (auth, events, budget, timeline, quote-engine)
- Implémente le **moteur règles + templates** (Quote/Plan generator v1)
- Met en place BullMQ/Redis (si besoin d’async)
- Tests unitaires backend + intégration DB

### Full‑Stack Dev B (FS-B) — “Frontend + Product flows”
- Implémente le **frontend Next.js** (écrans, formulaires, dashboards)
- Intègre auth (JWT), appels API, state management
- UX des parcours:
  - “Créer événement”
  - “Demander un devis”
  - “Voir plan/timeline + tâches”
  - “Ajuster paramètres” (budget/guest/style)
- Tests e2e (Playwright) + composants

### Data/AI Dev (DATA) — “Data model + Analytics + IA readiness”
- Définit les **événements de tracking** (audit log) et la qualité des données
- Spécifie la **taxonomie** (catégories dépenses, types services, niveaux prestataires)
- Propose les **règles/ratios** (prix par invité, saisonnalité, région) + versioning
- Met en place les premières analyses (KPIs) et dashboards internes
- Phase 2: modèles prédictifs (risque dépassement, retards)
- Phase 3: recommandation / assistant conversationnel

---

## 3) Roadmap par étapes (scénario complet)

# Phase 1 — Foundations (Semaine 1)
## Objectif
Avoir une base solide: auth, événements, structure timeline/budget, et socle “Quote/Plan Engine”.

### Étape 1.1 — Cadrage technique & specs (2–3 jours)
**Livrables**
- Spécification “Entrées → Sorties” du moteur (v1)
- Décisions MVP documentées: devis estimatif, validation humaine, inputs minimaux
- Liste de règles initiales (table de ratios)

**Qui**
- FS-A: modèle données initial + endpoints nécessaires
- FS-B: wireframes écrans (form + résultats)
- DATA: taxonomie + règles de base + tracking plan

---

### Étape 1.2 — Setup projet & CI/CD (2 jours)
**Implémentation**
- Repo mono (apps/web + apps/api) ou multi repo (selon choix)
- Docker compose: postgres + redis + api + web
- GitHub Actions: lint + test + build

**Qui**
- FS-A: setup API Nest + DB + migrations
- FS-B: setup Next + UI kit
- DATA: conventions tracking + schéma tables “event_log”

---

# Phase 2 — MVP “Générer devis + plan” (Semaines 2–3)
## Objectif
Un client saisit 4 infos → obtient estimation + plan + tâches + alertes.

## Étape 2.1 — Modèle de données MVP (2–3 jours)
**Tables minimales**
- users
- events (date, location, guests, style, budget)
- budgets (total, currency)
- budget_items (category, estimated_min, estimated_max, chosen_value)
- timeline_phases
- tasks (status, due_date, dependencies)
- providers (optionnel MVP)
- quote_requests (inputs + version_rules)
- quote_results (json + totals)
- event_log (tracking)

**Qui**
- FS-A: Prisma schema + migrations + seed
- DATA: catégories budget + dictionnaire services (référentiel)
- FS-B: aligne les champs du formulaire sur le schéma

---

## Étape 2.2 — API NestJS (4–6 jours)
**Endpoints**
- POST /auth/login, /auth/register, /auth/refresh
- POST /events, GET /events/:id
- POST /events/:id/quote (génère devis + plan)
- GET /events/:id/quote/latest
- PATCH /events/:id (update inputs et regénération)
- GET/POST tasks (listing + update status)

**Moteur v1 (rules-based)**
- Entrées: date, région, invités, budget/gamme
- Sorties:
  - breakdown par catégories
  - fourchettes min/max
  - timeline phases + tâches standard
  - alertes (budget insuffisant, délai court)

**Qui**
- FS-A: implémentation endpoints + engine v1
- DATA: fournit règles sous forme de JSON versionné (ex: rules/v1.json)
- FS-B: spécifie besoins exacts de réponses API pour affichage

---

## Étape 2.3 — Frontend Next.js parcours complet (4–6 jours)
**Écrans**
- Login/Register
- Create Event (form)
- Quote Wizard (inputs + “Generate”)
- Quote Result (cards budget, total min/max, alertes)
- Timeline view + Task list
- Simple dashboard organisateur (avancement tâches + budget)

**Qui**
- FS-B: UI + intégration API + validations
- FS-A: support backend pour filtres/tri tâches
- DATA: KPI definitions (completion rate, budget risk)

---

## Étape 2.4 — Validation humaine (option MVP + recommandé) (2–3 jours)
**Fonction**
- Statuts quote: DRAFT → REVIEW → SENT
- Un “organisateur/admin” peut ajuster des postes avant envoi

**Qui**
- FS-A: modèle + endpoints (PATCH quote status, update line items)
- FS-B: écran “Review quote” + actions
- DATA: règles d’audit log (“qui a modifié quoi”)

---

## Étape 2.5 — Tests & Qualité (2–4 jours)
**Implémentation**
- Backend: tests unitaires engine + integration DB
- Frontend: e2e Playwright sur parcours (create event → generate quote → view tasks)
- Observabilité: logs structurés + trace id

**Qui**
- FS-A: tests backend + seed data
- FS-B: e2e + validations UI
- DATA: tests de cohérence des règles + checks data quality

---

# Phase 3 — Prestataires & Matching simple (Semaine 4)
## Objectif
Associer des prestataires “compatibles” au devis/plan.

## Étape 3.1 — Module prestataires (MVP) (4–6 jours)
**Données prestataire**
- type_service (traiteur, photo, déco…)
- région
- capacité (nb évènements/mois, max invités)
- level (1–5)
- pricing_model (forfait / €/invité)
- disponibilités (simple: dates bloquées)

**API**
- CRUD providers
- GET providers/recommendations?eventId=...

**Matching v1 (règles)**
- Filtre: région + disponibilité + capacité
- Score: level + proximité budget estimé

**Qui**
- FS-A: backend providers + matching v1
- FS-B: UI liste prestataires + “proposer/assigner”
- DATA: scoring spec + normalisation des tarifs

---

# Phase 4 — Data instrumentation & KPIs (Semaines 5–6)
## Objectif
Rendre le système mesurable et “AI-ready”.

## Étape 4.1 — Tracking complet (2–4 jours)
**Événements**
- quote_generated
- quote_adjusted
- quote_sent
- budget_over_threshold_shown
- task_completed
- provider_assigned
- user_feedback_submitted (plus tard)

**Qui**
- DATA: schéma event_log + docs + contrôles
- FS-A: instrumentation backend
- FS-B: instrumentation frontend (si nécessaire)

## Étape 4.2 — Tableaux KPIs (2–4 jours)
- Taux de complétion tâches
- Écart budget estimé vs budget cible
- Temps moyen “brief → devis”
- Taux d’acceptation prestataires proposés

**Qui**
- DATA: requêtes SQL + dashboard (Metabase / Superset)
- FS-A: endpoints KPI (option)
- FS-B: affichage KPIs dans dashboard (option)

---

# Phase 5 — IA (progressive) (Semaines 7–10)
## Objectif
Passer de règles à modèles: prédire risques + recommander mieux.

## Étape 5.1 — Modèle “risque dépassement budget” (2–3 semaines)
**Données**
- budget total, invités, région, saison, choix services, historique

**Approche**
- Baseline: régression / XGBoost
- Sortie: probabilité dépassement + top facteurs

**Déploiement**
- Microservice Python FastAPI (si besoin)
- Ou batch scoring + stockage Postgres

**Qui**
- DATA: pipeline + modèle + évaluation
- FS-A: intégration API scoring + stockage
- FS-B: UI des alertes “risque élevé” + recommandations

## Étape 5.2 — Recommandations prestataires (2–3 semaines)
- Learning-to-rank léger (ou rules + bandits au début)
- Feedback loop: acceptation/refus, satisfaction

**Qui**
- DATA lead
- FS-A intégration
- FS-B UI

---

# Phase 6 — Assistant conversationnel (Semaines 11–14)
## Objectif
Un assistant qui collecte les infos manquantes et propose ajustements.

**Fonctions**
- Questionnaire intelligent: clarifie budget, priorités, style
- Génère plan/quote “explainable”
- Feedback au client (“si tu réduis déco de 10%…“)

**Qui**
- DATA: design prompts + guardrails + évaluation
- FS-A: orchestrateur + sécurité (rate limit, audit)
- FS-B: UI chat + résumés

---

## 4) Détails techniques — moteur “Quote/Plan Engine” v1
### Entrée (DTO)
- event_date
- location_region
- guests_count
- budget_total (nullable si gamme)
- package_level (eco|standard|premium)
- preferences (optional): priorité photo, déco, etc.

### Sortie (JSON)
- total_estimated_min / max
- breakdown:
  - venue
  - catering
  - photo_video
  - decoration
  - music
  - logistics
  - admin_contingency
- timeline:
  - phases (J-6m, J-3m, J-1m, semaine J, jour J, post-event)
  - tasks (id, title, due_date, dependencies, owner_role)
- alerts:
  - “budget trop faible pour X invités”
  - “délai < 60 jours”
- metadata:
  - rules_version
  - generated_at

### Implémentation (MVP)
- Un dossier `rules/` versionné (v1.json) contenant:
  - ratios €/invité par catégorie et gamme
  - coefficients région/saison
  - templates de tâches par type d’évènement
- Génération deterministic + tests snapshot (entrée → sortie)

---

## 5) Definition of Done (DoD) MVP
- Générer un devis + plan avec 4 entrées minimales
- Résultats affichés sur web
- Sauvegarde en DB + historique des générations (versions)
- Tests backend (engine) + e2e parcours
- Observabilité minimale (logs + tracking events)

---

## 6) Backlog initial (tickets types)
### Backend (FS-A)
- [ ] NestJS init + modules Auth/Event/Quote/Timeline/Tasks
- [ ] Prisma schema + migrations
- [ ] Quote engine v1 + rules v1.json
- [ ] Endpoint POST /events/:id/quote
- [ ] Quote status workflow (draft/review/sent)
- [ ] Provider module (phase 3)

### Frontend (FS-B)
- [ ] Next.js init + auth pages
- [ ] Create event form
- [ ] Quote wizard (inputs) + result page
- [ ] Timeline view + tasks list
- [ ] Review quote UI (if validation)

### Data (DATA)
- [ ] Taxonomie budget + services
- [ ] Rules v1 (ratios + coefficients)
- [ ] event_log spec + data quality checks
- [ ] KPI SQL queries + dashboard

---

## 7) Décisions à valider (à faire trancher par chef de projet)
1) Devis: **estimation** vs **prix final**
2) Workflow: envoi auto vs validation humaine
3) Prestataires: catalogue interne dès MVP vs plus tard
4) Entrées minimales exactes côté client
5) Niveau de personnalisation (style, priorité, contraintes) dès MVP ou phase 2

---
Fin du document.