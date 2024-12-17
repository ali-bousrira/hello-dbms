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
       { "id_commande": 102, "produit": "Stylo", "prix": 5 }  
   ]  
}  
Ici, les informations clients et commandes sont stockées dans un seul document sans besoin de tables séparées.
Exemples de SGBD non relationnels :  
MongoDB (documents JSON), Cassandra (colonnes larges), Redis (clés-valeurs), Neo4j (graphes).  

Les bases de données relationnelles sont idéales pour des applications nécessitant des relations complexes entre données et une structure rigide.  
Les bases de données non relationnelles sont adaptées pour des environnements flexibles, scalables et des applications modernes avec des données volumineuses ou non structurées.  
Le choix dépend des besoins de l’application, des performances souhaitées et de la nature des données.  
