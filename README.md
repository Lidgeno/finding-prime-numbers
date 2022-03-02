# finding-prime-numbers
EN/FR attempt to make clever and efficient algorithms that seek the prime numbers in a given range (0 to max)
Tentative d'ecriture d'algorithmes fûtés et efficaces qui cherchent les nombres premiers dans un intervalle donné

Hey welcome to this project, check license directives below

About this project,
it issued from a discussion i had with a roommate about a formula giving prime number distribution percentage
we had two different views on the way to retrieve the list of prime numbers within a given range
mine was to multiply each prime number by a regular integer in order to reduce the number of calculation
It is actually based on a previous idea/code i did on my old ti82 and it's written in python even though it meant to be c

MATHS
- a prime number cannot be calculated from other of its kind
- each integer can be seen as (integer = a^n * b^o * c^p * ...) where a,b,c are different prime and n,o,p integers
- it means that each integer written ( a^n * b^o * c^p * ...) can also be written from this unique manner ( a^n * k), where k is integer
- 2 is the only even number which is prime, to increment by 2 (on odd numbers) reduce calculation accordingly

INSIGHT
- given that, i was willing to do a for loop for every number in given range, we suppose this number is prime
- but for loop of our list of prime numbers, if it can be calculated then it is not prime
- to do this, for a loop of integer until calculation reaches over the number we check, check if number is found
- every number below this number have been calculated so we can keep record of the integer we just used to check it
- if we write number as ( a^n * b^o * c^p * ...) with a < b < c, there will be no redundancy in calculation

OBSERVATION
- We will still have loss of calculation over the number up to 1/prime/integer so we could store that value in an array and check if i fits
- whether we check if value is in array or order array to give only first result
- However even though we lose no calculation, to compute a search in array seems to cost more
- Furthermore CPU is not fully used and we could use threads to investigate multiple numbers (if number is high enough)
- We could also split this task between computers in a given network

---------------------------------------------------------------------------------------------------------------------------------------------

MATHS
- un nombre premier ne peut pas etre trouve par d autres nombres premiers
- tout entier peut s'ecrire (entier = a^n * b^o * c^p * ...) ou a,b,c nombres premiers et n,o,p entiers en exposant
- on en deduit qu'un entier ( a^n * b^o * c^p * ...) peut s'ecrire de maniere unique ( a^n * k), ou k est simplement entier
- 2 est le seule nombre pair a etre premier, donc on incrémente par 2 sur les nombres impairs pour réduire le nombre de calcul à effectuer

INTUITION
- donc, POUR chaque entier contenu dans les limites, on suppose qu'il est premier
- mais POUR chacun des nombres premiers deja trouvé, si on calcule ce nombre avec, alors il n'est pas premier
- pour ce faire, POUR chaque nombre jusqu'a ce que entier soit depasse, on teste si entier est calculé
- Tous les nombres en dessous de cet entier ont ete calcules, on peut donc conserver pour chaque nombre premier le dernier nombre entier utilise
- si on écrit l'entier ( a^n * b^o * c^p * ...) avec a < b < c, l'entier est écrit de manière unique

OBSERVATION
- Il y aura toujours une perte jusqu'à 1calcul/premier/entier, pour contrer ca on peut stocker le resultat dans un tableau et y comparer l'entier en premier
- on pourrait ordonnancer le tableau ou trouver dans le tableau si l'entier existe
- mais le gain en calcul n'est pas suffisant pour justifier une recherche pour chaque entier dans le tableau
- de plus le CPU n'est pas utilise a 100% et on pourrait separer la tache en threads pour tester plusieurs entiers (si on a assez de nombres premiers)
- on pourrait alors repartir les taches sur un reseau de CPU

----------------------------------------------------------------------------------------------------------------------------------------------

LICENSE, i don't understand them, so here's mine
Everyone is welcome to use, distribute or modify this project in any way they want. Whether it is a Commercial, educationnal or private use.
However patterns including this project shall not restrict in any case uses of this project nor its development.
- If you plan to use it for evil purposes, please don't.
Keep this notice within the project, including thanks to the authors and contributors.
- If you are thankful enough to give money for the project or authors and contributors day to day expenses, great !
- If you feel like quoting authors and contributors there and there, that's good too !
Lastly,
As you don't pay for this, (and even so), this project provides no guarantee about its goal, effectiveness nor issues that the user could encounter

LICENCE D'UTILISATION, etant donne que je n'y comprends absolument rien, j'ai etabli ces quelques regles
Ce projet est libre d'utilisation, de modification et de distribution pour n'importe quelle raison. Il peut etre utilise a des fins commerciales, d'education ou privees.
Cependant, tout brevet depose incluant ce projet ne devra pas entraver son utilisation, ni son eventuelle evolution.
- Vous ne devriez pas l'utiliser a des fins malfaisantes
Gardez cette notice avec le projet, ceci vaut aussi pour la liste des auteurs et contributeurs
- Si vous voulez encourager les auteurs et contributeurs en donnant de l'argent pour le projet ou pour leur quotidien, genial !
- Si vous parlez d'eux autour de vous c'est bien aussi !
Enfin,
Etant donne que ce projet est libre d'utilisation (et quand bien meme il en serait autrement),
soyez informes qu'il est sans garantie de fonctionnement, de but ou de problemes pour l'utilisateur.
