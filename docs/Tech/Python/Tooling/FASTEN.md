
## Interesting (?) artefacts

- https://github.com/fasten-project/quality-analyzer


## Mail sent to g.gousios@tudelft.nl. Never answered


Hi,

I understand from browsing the Fasten website and GitHub repo that you have worked on tools that "propose a new way to solve modern software dependency management issues", and that some of this work was conducted in the context of the Python programming language.

However, I couldn't find concrete and actionable information on how to use this work (still in the context of Python - don't get me started on Java!).

So my questions are:

- what are the relevant projects (repositories) and software artifacts (e.g. PyPI releases) ?
- where are the tutorials / getting started / howtos on how to use them ?

As I can only imagine that such work has been produced during (and after?) the project, and must be hidden somewhere (maybe in the mountain of "deliverables" that are only useful for the Commission and not for actual users or researchers).

Regards,


il y a je pense un élément du 
projet Fasten qui concerne Python qui peut être réutilisé de manière 
autonome : c'est le générateur de graphe d'appel statique qui est 
disponible dans le dossier "cg-producer" et qui se trouve ici : 
[https://github.com/fasten-project/pypi-tools](https://github.com/fasten-project/pypi-tools) (mais j'ai l'impression 
que le développement est plutôt actif sur 
[https://github.com/vitsalis/PyCG](https://github.com/vitsalis/PyCG), à vérifier).

(Les deux projets m'ont l'air d'être structurés très différemment, j'ai du mal à faire le lien.)

Ce composant est seulement une brique de Fasten qui dans l'idée :
- scan tout le contenu de PyPI,
- génère des graphs d'appel pour tout ce qu'il trouve,
- fait le lien entre les différents graphs d'appels générés,
- associe des métadonnées (CVE, license, qualité,…) aux nœuds (qui 
représente des fonctions) de ces graphs
- permet d'exploiter les infos collectées pour déterminer s’il existe 
un chemin entre le code d'un projet quelconque (ou le code d'une lib 
publiée sur PyPI) et une fonction identifiée comme vulnérable (et 
également d'autre scénarios liés aux licences, qualité,…)

Le déploiement de l'ensemble n'est pas trivial (cf 
[https://github.com/fasten-project/fasten/wiki/Deployment](https://github.com/fasten-project/fasten/wiki/Deployment)) et comme l'a 
indiqué Catherine sur Python ça n'a pas vraiment atteint l'objectif 
initialement fixé.


→ Ca me semble intéressant sur le papier, mais du coup est-ce qu'il y a des retombées pratiques ?

L'ensemble semble être une usine à gaz non testée.



<!-- Keywords -->
#repositories #github #software #tools #projects
<!-- /Keywords -->
