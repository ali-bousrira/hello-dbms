# hello-dbms

# Veille

## A. 
Une donnée est une information à l'état brute qui peut être stocké, extraite et traité. Elle peut être sous n'importe quelle forme (numérique, alphabétique, visuelle).  

## B. 
Les critères de mesure de qualité des données sont :  
La précision, à quel point les données sont vraies;  
La complétude, quel pourcentage de données sont manquantes (moins il y en a mieux c'est);  
La cohérence, que les tables ne se contredisent pas;  
L'unicité, qu'il y est le moins de doublon au sein d'un jeu de données;  
L'accessibilité, que les données soit accessibles rapidement par les presonnes voulus.  

## C. 
Un data lake est un espace de stockage qui permet de centraliser beaucoup de données structurées ou non.  
Une data warehouse est un espace de stockage qui organise et nettoye des données structurées.  
Un lake house est un espace de stockage hybride entre un data lake est une data warehouse.  
Là où un data lake va pouvoir stocké énormément de données diverses, elles seront plus compliqué à analyser ne répondant pas à des requêtes complexe. Contrairement au data warehouse qui ne propose pas une grande diversité de données à stocker mais qui permettra une analyse beaucoup plus poussé. Le coût et également supérieur au data lake demandant une technologie plus avancé que ce dernier. Le lake house étant un hybride des deux il s'impose comme un juste milieux des critères précendent.  

![alt text](https://github.com/ali-bousrira/hello-dbms/blob/main/datawarehouseschema.png?raw=true)  

## D.
Un Système de Gestion de Bases de Données (SGBD) est un logiciel qui permet de créer, organiser, gérer et manipuler des bases de données. Il permet de stocker les données de manière structurée, ajouter, supprimer, modifier et consulter les données, assurer la sécurité et optimisé les preformances des requêtes.  
Il existe différent types de SGBD :  

SGBD relationnel (RDBMS)  
Les données sont organisées en tables (lignes et colonnes) avec des relations entre elles.
Exemple : MySQL, Oracle Database, PostgreSQL, SQL Server.  

SGBD non relationnel (NoSQL)  
Adapté pour des données non structurées, volumineuses et distribuées.
Exemple : MongoDB, Cassandra, Redis, CouchDB.  

SGBD hiérarchique
Les données sont organisées en une structure parent-enfant, sous forme d’arbre.
Exemple : IBM Information Management System (IMS).  

SGBD orienté objet
Combine les concepts de base de données et de programmation orientée objet.
Exemple : db4o, ObjectDB.  

SGBD en mémoire (In-Memory)
Stocke les données directement dans la mémoire vive (RAM) pour des performances accrues.
Exemple : SAP HANA, Redis.  

![alt text](https://github.com/ali-bousrira/hello-dbms/blob/main/SGBD.jpg?raw=true)  

## E.  
Une base de données relationnelle (RDB - Relational Database) est une base de données organisée en tables contenant des lignes (enregistrements) et des colonnes (attributs). Ces tables sont liées entre elles grâce à des relations, définies par des clés primaires et des clés étrangères.  
Modèle de données : Structuré et basé sur des relations.  
Langage d’interrogation : Utilisation du langage SQL (Structured Query Language) pour manipuler et interroger les données.  
Structure : Données normalisées, organisées dans des tables avec des relations logiques.  
Exemple :  
Dans une base de données pour une boutique en ligne :

Table Clients
| ID_Client | Nom | Prénom | Email |
|-----------|----------|--------|-----------------|
| 1 | Houtan | Laurent | laurent@mail.com |
| 2 | Peuplu | Jean | jean@mail.com |

Table Commandes
| ID_Commande | ID_Client | Produit | Prix |
|-------------|-----------|-----------|------|
| 101 | 1 | Livre | 20 |
| 102 | 2 | Stylo | 5 |

Relation : La colonne ID_Client dans la table Commandes est une clé étrangère liée à la clé primaire ID_Client de la table Clients. Cela permet d’associer les commandes aux clients.
Exemples de SGBD relationnels :
MySQL, PostgreSQL, Oracle Database, SQL Server.  

Une base de données non relationnelle (ou NoSQL) est une base de données qui ne suit pas le modèle tabulaire traditionnel des bases relationnelles. Elle est conçue pour gérer des données non structurées ou semi-structurées, avec une grande flexibilité et scalabilité.  
Modèle de données : Les données sont stockées sous différentes formes :  
Documents (JSON, XML),  
Clés-valeurs,  
Colonnes larges,  
Graphes.  
Langage d’interrogation : Généralement propriétaire, mais souvent basé sur des formats comme JSON.  
Structure : Les données ne nécessitent pas de schéma fixe et peuvent évoluer librement.  
Exemple :  
Dans une base de données NoSQL pour une boutique en ligne utilisant MongoDB (stockage en documents JSON) :    
Document Client :  
{  
   "_id": 1,  
   "nom": "Peuplu",  
   "prénom": "Jean",  
   "email": "jean@mail.com",  
   "commandes": [  
       { "id_commande": 101, "produit": "Livre", "prix": 20 },  
       { "id_commande": 102, "produit": "Stylo", "prix": 5 }  ]  
}  
Ici, les informations clients et commandes sont stockées dans un seul document sans besoin de tables séparées.
Exemples de SGBD non relationnels :  
MongoDB (documents JSON), Cassandra (colonnes larges), Redis (clés-valeurs), Neo4j (graphes).  

Les bases de données relationnelles sont idéales pour des applications nécessitant des relations complexes entre données et une structure rigide.  
Les bases de données non relationnelles sont adaptées pour des environnements flexibles, scalables et des applications modernes avec des données volumineuses ou non structurées.  
Le choix dépend des besoins de l’application, des performances souhaitées et de la nature des données.  

## F.
La clé primaire est un identifiant unique pour chaque ligne (ou enregistrement) dans une table d’une base de données relationnelle. Elle garantit que chaque enregistrement peut être identifié de manière unique et qu’il n’y a pas de doublon dans cette colonne.  
La clé étrangère est une colonne ou un ensemble de colonnes dans une table qui référence la clé primaire d’une autre table. Elle établit une relation entre deux tables, permettant d’assurer l’intégrité référentielle.  

## G.
Les propriétés ACID sont un ensemble de règles fondamentales qui garantissent la fiabilité et l’intégrité des transactions dans une base de données relationnelle. Elles sont essentielles pour maintenir la cohérence des données, en particulier dans les systèmes transactionnels.  
Le terme ACID est un acronyme pour :  
Atomicité (Atomicity)  
Cohérence (Consistency)  
Isolation (Isolation)  
Durabilité (Durability)  

## H.
La méthode Merise est une méthode d'analyse, de conception et de gestion de projets informatiques utilisée principalement dans la modélisation des bases de données. Elle permet de décrire de manière structurée les systèmes d'information.  
L’UML est un langage de modélisation standardisé utilisé pour visualiser, décrire, spécifier et documenter les systèmes logiciels. UML est souvent utilisé dans la conception orientée objet.  

Utilité dans le monde informatique : 
Merise :  
- Conception et gestion des bases de données.  
- Appropriée pour les systèmes transactionnels.  
- Structure les données et les traitements en phases claires et méthodiques.  
UML :  
- Conception orientée objet des logiciels et applications.  
- Communication entre les développeurs, architectes et parties prenantes.  
- Visualisation des systèmes complexes via des diagrammes pour toutes les étapes.  

Exemple de Merise : Conception d’une base de données d'une bibliothèque  
Niveau Conceptuel (MCD) :  
On utilise un Modèle Conceptuel des Données pour décrire les entités et leurs relations.  
Entités : Livre, Adhérent, Auteur.  
Association : Un adhérent peut emprunter plusieurs livres (relation 0,n).  
Cardinalités :  
Chaque livre peut être emprunté au plus une fois (1,1 côté Livre).  
Un adhérent peut emprunter plusieurs livres (0,n).  
Niveau Logique (MLD) :  
On traduit les entités en tables.  
Table Livre : ID_Livre (PK), Titre, Auteur.  
Table Adhérent : ID_Adhérent (PK), Nom, Prénom.  
Table Emprunt : ID_Emprunt (PK), ID_Livre (FK), ID_Adhérent (FK), Date_Emprunt.  
Niveau Physique :  
Création des tables avec un langage SQL.  

Exemple d’UML : Conception d’un système de gestion de commandes  
Diagramme de cas d’utilisation :  
Représente les interactions entre les acteurs et le système.   
Acteurs : Client, Admin.  
Cas d’utilisation : Passer une commande, Consulter l’historique, Gérer les stocks.  
Diagramme de classes :  
Permet de représenter les classes et leurs relations.  
Classes : Client, Commande, Produit.  
Relations :  
Un client peut passer plusieurs commandes (1,n).  
Une commande peut contenir plusieurs produits (1,n).  
Diagramme de séquence :  
Montre l’ordre d’exécution des interactions entre les objets.  

## I. 
Le SQL (Structured Query Language) est un langage de programmation utilisé pour la création, la manipulation et la gestion des bases de données relationnelles. Il permet d’interagir avec des systèmes de gestion de bases de données (SGBD) comme MySQL, PostgreSQL, SQL Server ou Oracle.  

