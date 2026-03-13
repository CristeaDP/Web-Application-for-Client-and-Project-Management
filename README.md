# 📊 Sistem de Gestiune Clienți și Proiecte (PIBD)

[cite_start]Acest proiect a fost dezvoltat pentru disciplina **Programarea Interfețelor pentru Baze de Date** și propune o soluție completă pentru gestionarea relației dintre clienți și proiectele unei companii[cite: 3, 35].

## 📑 Cuprins
- [Descrierea Aplicației](#descrierea-aplicației)
- [Tehnologii Utilizate](#tehnologii-utilizate)
- [Structura Bazei de Date](#structura-bazei-de-date)
- [Funcționalități](#funcționalități)
- [Arhitectura Codului](#arhitectura-codului)

---

## 📝 Descrierea Aplicației
[cite_start]Obiectivul principal este permiterea utilizatorilor să efectueze operațiuni de gestionare a datelor (vizualizare, adăugare, modificare și ștergere) într-un mediu interconectat[cite: 19]. [cite_start]Aplicația gestionează distribuția clienților pe proiecte, oferind o interfață intuitivă bazată pe web[cite: 35, 36].

## 🛠 Tehnologii Utilizate
[cite_start]Proiectul integrează următoarele tehnologii conform cerințelor academice:

* [cite_start]**Java & Spring Boot:** Framework-ul principal pentru logica de back-end și dezvoltarea RESTful[cite: 25, 27].
* [cite_start]**MySQL:** Sistemul de gestionare a bazei de date relaționale[cite: 22].
* [cite_start]**Python:** Utilizat pentru implementarea unei interfețe alternative de acces la date sau scripturi de procesare[cite: 17].
* [cite_start]**Front-end:** HTML, CSS și framework-ul Bootstrap pentru un design modern și responsiv[cite: 28, 30, 33].
* [cite_start]**Thymeleaf:** Motor de template-uri pentru inserarea datelor dinamice în paginile HTML[cite: 100, 101].
* [cite_start]**Lombok:** Librărie pentru simplificarea codului prin generarea automată de getteri/setteri[cite: 240, 272].

## 🗄 Structura Bazei de Date
[cite_start]Baza de date este compusă din trei tabele principale, gestionând o relație de tip **M:N** (Many-to-Many)[cite: 38, 39]:

1.  [cite_start]**clienti:** Stochează ID-ul, numele, email-ul și telefonul clientului[cite: 42, 43, 44, 45, 46].
2.  [cite_start]**proiecte:** Include denumirea proiectului și datele de desfășurare[cite: 48, 49, 50, 51].
3.  [cite_start]**clienti_proiecte:** Tabelă intermediară care face legătura între clienți și proiecte, specificând și rolul clientului[cite: 53, 54, 57].

> [cite_start]**Notă:** Integritatea datelor este menținută prin constrângeri `ON DELETE CASCADE`[cite: 62, 63].

## 🚀 Funcționalități
* [cite_start]**Dashboard:** Pagina principală pentru navigare rapidă către secțiunile de gestiune[cite: 301, 378].
* **Gestiune CRUD:** Interfețe dedicate pentru Adăugare, Editare și Ștergere clienți/proiecte[cite: 157, 237].
* [cite_start]**Asociere Dinamică:** Posibilitatea de a aloca un client unui proiect dintr-o listă predefinită (dropdown)[cite: 137, 364, 365].
* [cite_start]**Validare:** Formularele includ câmpuri obligatorii și validări de format (ex: email)[cite: 89, 399, 404].

## 📂 Arhitectura Codului (Spring Boot)
[cite_start]Aplicația respectă modelul MVC[cite: 86, 90]:

* [cite_start]**Controller:** Gestionează rutele HTTP (ex: `clientiController`, `pageController`)[cite: 199, 295].
* **Entity:** Maparea tabelelor în clase Java utilizând adnotarea `@Entity`[cite: 249, 267].
* [cite_start]**Repository:** Interfețe ce extind `JpaRepository` pentru interogări automate[cite: 280, 282].
* [cite_start]**Templates:** Fișiere `.html` procesate pe server înainte de livrare[cite: 102].

---
[cite_start]**Autor:** Cristea Denis-Petrisor [cite: 4]  
**Coordonator:** Ș.l. Dr. Ing. [cite_start]Pupezescu Valentin [cite: 6]
