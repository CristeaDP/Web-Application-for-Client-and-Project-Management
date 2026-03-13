# 📊 Sistem de Gestionare Clienți și Proiecte (PIBD)

Acest proiect a fost dezvoltat pentru disciplina **Programarea Interfețelor pentru Baze de Date** (Universitatea Națională de Științe și Tehnologie Politehnica București) și propune o soluție completă pentru gestionarea relației dintre clienți și proiectele unei companii.

## 📑 Cuprins
- [Descrierea Aplicației](#descrierea-aplicației)
- [Tehnologii Utilizate](#tehnologii-utilizate)
- [Structura Bazei de Date](#structura-bazei-de-date)
- [Funcționalități](#funcționalități)
- [Arhitectura Codului](#arhitectura-codului)

---

## 📝 Descrierea Aplicației
Obiectivul principal al proiectului este de a permite utilizatorilor să efectueze operațiuni de gestionare a datelor (vizualizare, adăugare, modificare și ștergere) într-un mediu interconectat. Aplicația gestionează distribuția clienților pe proiectele companiei, oferind o interfață web intuitivă și eficientă.

## 🛠 Tehnologii Utilizate
Proiectul integrează următoarele tehnologii:

* **Java & Spring Boot:** Framework-ul principal folosit pentru dezvoltarea rapidă a aplicației, oferind configurare minimală și suport pentru API-uri RESTful.
* **MySQL:** Sistemul de gestionare a bazelor de date relaționale, utilizat pentru stocarea robustă și sigură a informațiilor.
* **Python:** Utilizat pentru diversificarea interfețelor de acces la baza de date, conform cerințelor proiectului.
* **Front-end:** HTML, CSS și framework-ul **Bootstrap** pentru crearea unei interfețe moderne, responsive și ușor de navigat.
* **Thymeleaf:** Motor de template-uri utilizat pentru procesarea server-side și afișarea dinamică a datelor în paginile HTML.
* **Lombok:** Librărie Java utilizată pentru simplificarea codului sursă (generarea automată de getteri, setteri și constructori).

## 🗄 Structura Bazei de Date
Baza de date a fost realizată în MySQL Workbench și este compusă din trei tabele principale care gestionează o relație de tip **M:N** (Many-to-Many):

1.  **Tabela clienti:** Stochează informațiile de contact (nume, email, telefon).
2.  **Tabela proiecte:** Înregistrează detaliile despre proiectele companiei (denumire, data start, data final).
3.  **Tabela clienti_proiecte:** Tabelă intermediară care gestionează asocierile și rolul specific al fiecărui client în cadrul unui proiect.

> **Integritate:** S-a implementat mecanismul `ON DELETE CASCADE` pentru a asigura eliminarea automată a legăturilor atunci când un client sau un proiect este șters.

## 🚀 Funcționalități
* **Vizualizare Date:** Liste complete pentru clienți, proiecte și asignările dintre aceștia.
* **Gestiune CRUD:** Formulare dedicate pentru adăugarea de noi înregistrări, editarea celor existente și ștergerea datelor inutile.
* **Interfață Intuitivă:** Navigare simplă între pagini și butoane de acțiune rapidă (Edit/Delete) integrate în tabele.
* **Automatizare:** Deschiderea automată a browserului la lansarea aplicației Spring Boot pe `localhost:8080`.

## 📂 Arhitectura Codului
Aplicația respectă modelul de design **MVC** (Model-View-Controller):

* **Controller:** Gestionează cererile HTTP și direcționează utilizatorul către vizualizările corecte (ex: `clientiController`, `pageController`).
* **Entity:** Clase Java mapate direct pe tabelele din baza de date folosind JPA.
* **Repository:** Interfețe care extind `JpaRepository` pentru a efectua operații CRUD fără a scrie interogări SQL explicite.
* **Templates:** Fișiere HTML (Thymeleaf) care definesc structura vizuală și interacțiunea cu utilizatorul.

---
**Student:** Cristea Denis-Petrisor  
**Grup:** 434E  
**Prof. Coordonator:** Ş.l. Dr. Ing. Pupezescu Valentin
