# EAM 3
Σάμιος Γρηγόρης 1115201500141 

Γιατράκος  Γεώργιος 1115201600036

Ιωαννίδης Γεώργιος-Αλέξανδρος 1115201500049

## Υλοποιημένα Ζητούμενα:
- #### Η δομή του ιστοχώρου γενικά  έγινε ως εξής:
    - AppBar και NavigationBar(smaller screens) είναι σταθερό και βρίσκονται βασικά λινκς για ευκολότερη πλόηγηση στην ιστοσελίδα
    - Contnent που αλλάζει με βάση την σελίδα που βρίσκεται ο χρήστης
    - Footer είναι σταθερό και έχει γενικές πληροφορίες 

- #### Αρχική
    - Στην αρχική(/) τοποθετήσαμε την φόρμα αναζήτησης διαδρομής και την παρουσιάση πληροφορίας για καθυστερήσεις δρομολογίων.
    
- #### Σελίδα/ες με πληροφορίες για βασικές υπηρεσίες της διαδικτυακής διεπαφής
    - Το λινκ "ROUTES" σε οδήγει σε σελίδα (/maps/bus) που παρουσιάζονται πληροφορίες για διαφορετιά δρομολόγια
    - Τιμες εισητηριων: Παρουσίαση των προϊόντων εισητηρίων με radio buttons, και τελικό κόστος που αναγράφεται στο checkoutpage 
    - Το λινκ "ABOUT" οδηγεί σε σελίδα με πληροφορίες σχετικά σε ποιόν οργανισμό υπάγονται τα μέσα.
- #### Διεπαφή παρουσίασης δρομολογίων   
    - Το λινκ "ROUTES" σε οδήγει σε σελίδα (/maps/bus) που παρουσιάζονται πληροφορίες για διαφορετικά δρομολόγια και στάσεις πάνω στον χάρτη όπου ο χρήστης επιέλεγει στασή η δρομολόγιο.<br/>
    Με την επιλογή του δρομολογίου πγαίνει σε νέα σελίδα (/bus/route/id) όπου εφανίζονται οι στάσεις του συγκερκιμένου δρομολογίου καθώς και το που βρίσκονται στον χάρτη.<br/>
     Επιλέγοντας της "Πληροφορίες" από μια γραμμή της λίστας στάσεων ο χρήστης μεταβαίνει σε σελίδα (/stop/id) με πληροφορίες για την συγκεκριμένη στάση. 
- #### Παρουσίαση αποτελεσμάτων αναζήτησης
    - Ο χρήστης εισάγωντας πεδία "Από" και "Προς" στην αρχική  μεταβαίνει στην σελίδα ααναζήτησης διαδρομής(/SearchRoutes).<br/>
    - Εκεί μπορεί να αλλάξει προτεινόμενη διαδρομή μέσω επιλογών και επιπλεόν είναι ορατή η διαδρομή που θα κάνει στο χάρτη.Τέλος εμφανίζεται και λινκ που τον οδηγεί στην αγορά εισητηρίων
 - #### Η λειτουργία ηλεκτρονικής αγοράς εισιτηρίου ή φόρτισης εισιτηρίου για εγγεγραμμένους χρήστες αλλά και για μη εγγεγραμμένους χρήστες.
      Εγγεγραμμένοι και μή εγγεγραμμένοι χρήστες μπορούν να αγοράσουν απλά εισητήρια. Αν πρόκειται για εγγεγραμένο χρήστη το σύστημα αυτοσυμπληρώνει τις φόρμες για τον χρήστη. 
      Υλοποιήθηκε η λειτουργία έκδοσης και αγοράς ηλεκτρονικής κάρτας (με αυτοσυμπληρώμενες φόρμες), αλλά όχι η φόρτιση.
- #### Παρουσίαση της πληροφορίας που αφορά σε άτομα με αναπηρία
    - Η πληροφορία για το ποιές στάσεις ειναι προσβάσιμες σε ΑμεΑ  γίνεται με χρησή χαρακτηριστικού εικονιδίου δίπλα από κάθε στάση που είναι προσβάσιμη
- #### Λειτουργία σύνδεσης στη διαδικτυακή εφαρμογή
    - Σελίδα με φόρμα εγγγραφής χρήστη "SIGN UP" (/signup),και σύνδεσης "LOGIN" (/login).
- #### Δυνατότητα επεξεργασίας του προφίλ
    - Μετά το login ο χρήστς μπορεί να μεταβεί σε σελίδα μέσω του λινκ "HI (username)!" για την επεξεργασία του προφιλ του,και μπορεί να κάνει και LOGOUT.  
- #### Αγορα εισητηριων
    - Στο (/tickets) προσφερεται η λειτουργικοτητα αγορας εισητηριων 
    - Ο χρηστης μπορει να επιλεξει αγορα προσωποποιημενης καρτας οποτε και δινεται η δυνατοτητα επαναφορτισης
    - Σε περιπτωση που ο χρηστης ειναι εγγεγραμενος οι πληροφοριες που αφορουν τα στοιχεια αγορας ειναι προ-συμπληρωμενες
    - Διαφορετικα καλειται να τις συμπληρωσει
    - Ο χρηστης μπορει να αγορασει μεμονομενα εισητηρια . Επιλεγει τον τυπο του εισητηριου και τον αριθμο και υπολογιζεται         το κοστος που καλειται να πληρωσει .

## Links

### Passwords

Δοκιμαστικος χρηστης email = emilia password = emilia

### Διεπαφη αναζητησης διαδρομης

Παταμε το κουμπι στην αρχικη οθονη :
![Image](https://i.imgur.com/y9Wv108.png)
![Image](https://i.imgur.com/0SwP4HM.png)

### Παρουσιαση δρομολογιων και σταθμων

![Image](https://i.imgur.com/BFudxeA.png)

#### Παρουσιαση Δρομολογιου

![Image](https://i.imgur.com/O9CQKFF.png)

#### Παρουσιαση Στασης

![Imgur](https://i.imgur.com/hNAf6Ac.png)

#### Επιλογη Αγορας Εισητηριου

![Imgur](https://i.imgur.com/TmbHJ01.png)

#### Επαναφορτιση Καρτας ως συνδεδεμενος χρηστης

![Imgur](https://i.imgur.com/lVRjTkL.png)

#### Επαναφορτιση Καρτας ως μη συνδεδεμενος χρηστης

![Imgur](https://i.imgur.com/6ORoNyF.png)

#### Προβολη Προφιλ

![Imgur](https://i.imgur.com/Gk9dMcT.png)

#### Επεξεργασια Προφιλ

![Imgur](https://i.imgur.com/qI2bcJr.png)

#### Εγγραφη Νεου Χρηστη

![Imgur](https://i.imgur.com/Ukiovvn.png)

#### Εισοδος Νεου Χρηστη

![Imgur](https://i.imgur.com/uubr20g.png)


## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

## Api Setup
Create virtual environment using Python-3
```
cd api
python3 -m venv venv
```

Activate 
```
. venv/
```

Install requirements
```
pip install -r requirements.txt
```

### Run api
```
python api.py
```

## Quick Guide

### /components

Εδω μπαινουν τα components της viue

### /views

Εδω μπαινουν τα view που ειναι components . Μια σελιδα αντιστοιχει σε ενα vue
οπου μπορουμε να βαλουμε πολλαπλα components (πχ. μενου , navigation , breadcrumb)

### /router

Εδω γινεται το routing για καθε σελιδα . Δηλαδη , καλειται το αντιστοιχο view που θελουμε.

### App.vue / main.js

Αρχεια config

### Run API
. venv/bin/activate

python api.py


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
