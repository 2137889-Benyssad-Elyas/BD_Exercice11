CREATE DATABASE if not exists Exercice11_LDVELH;
use Exercice11_LDVELH;
CREATE TABLE objet
(
    id INT auto_increment,
    nom VARCHAR(255),
    bool_special tinyint, 
    primary key (id)
);

CREATE TABLE arme
(
    id INT auto_increment,
    nom VARCHAR(255),
    primary key (id)
);

CREATE TABLE discipline_kai
(
    id INT auto_increment,
    nom varchar(255),
    primary key (id)
);

CREATE TABLE feuille_aventure
(
    id int auto_increment,
    nom_joueur varchar(255),
    habilite int,
    endurance int, 
    bourse int,
    primary key (id)

);

CREATE TABLE feuille_aventure_objet
(
    id INT auto_increment,
    id_feuille_aventure int,
    id_objet int,
    primary key (id),
    foreign key (id_feuille_aventure) REFERENCES feuille_aventure (id),
    foreign key (id_objet) REFERENCES objet (id)
);

CREATE TABLE feuille_aventure_arme
(
    id INT auto_increment,
    id_feuille_aventure int,
    id_arme int,
    primary key (id),
    foreign key (id_feuille_aventure) REFERENCES feuille_aventure (id),
    foreign key (id_arme) REFERENCES arme (id)
);

CREATE TABLE feuille_aventure_discipline_kai
(
    id INT auto_increment,
    id_feuille_aventure int,
    id_discipline_kai int,
    note int,
    primary key (id),
    foreign key (id_feuille_aventure) REFERENCES feuille_aventure (id),
    foreign key (id_discipline_kai) REFERENCES discipline_kai (id)
);

CREATE TABLE livre
(
    id int auto_increment,
    nom VARCHAR(255),
    nombre_chapitre int,
    nombre_page int,
    primary key (id)
    
);
CREATE TABLE chapitre
(
    id int auto_increment,
    numero_chapitre int,
    texte varchar (255),
    numero_page_debut int,
    primary key (id)
);
CREATE TABLE livre_chapitre
(
    id INT auto_increment,
    id_livre INT,
    id_chapitre INT,
    primary key (id),
    foreign key (id_livre) REFERENCES livre (id),
    foreign key (id_chapitre) REFERENCES chapitre (id)
);
CREATE TABLE sauvegarde_progression
(
    id int auto_increment,
    id_feuille_aventure int,
    id_livre int,
    id_chapitre int,
    date_sauvegarde date,
    primary key (id),
    foreign key (id_feuille_aventure) REFERENCES feuille_aventure (id),
    foreign key (id_livre) REFERENCES livre_chapitre (id_livre),
    foreign key (id_chapitre) REFERENCES livre_chapitre (id_chapitre)
);

CREATE TABLE lien_chapitre
(
	id int auto_increment,
	no_chapitre_origine int,
    no_chapitre_destination int,
    primary key (id),
    foreign key (no_chapitre_origine) REFERENCES chapitre (numero_chapitre)
);


