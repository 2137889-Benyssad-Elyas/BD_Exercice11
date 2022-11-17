DELIMITER $
CREATE PROCEDURE InsererSauvegarde(feuille_aventure int, livre int, chapitre int, date_sauvegarde date)
BEGIN
   insert into sauvegarde_progression (id_feuille_aventure, id_livre, id_chapitre, date) values (feuille_aventure, livre, chapitre, date_sauvegarde);
END$
DELIMITER ;

DELIMITER $
CREATE PROCEDURE SupprimerSauvegarde(id_sauvegarde int)
BEGIN
   delete from sauvegarde_progression where id = id_sauvegarde;
END$
DELIMITER ;