# -*- coding: utf-8 -*-

from random import randint

data = [
{ "word": "Aboulie", "definition": """Nom féminin.
Du grec aboulia qui signifie irréflexion dérivé de boulesthai qui
signifie vouloir.
Pathologie mentale qui se traduit par une chute ou une disparition
complète de la volonté et qui aboutit à une incapacité de faire des
choix, de prendre des décisions ou de passer à l’action.""" },
{ "word": "Açaï", "definition": """Nom masculin.
Du portugais « açai » issu du Tupi-Guarani « ïwasa’i » qui signifie
fruit qui pleure – qui donne de l’eau-.
Fruit du palmier pinot « Euterpe oleracea » qui pousse en Amazonie,
Brésil et Trinidad, rouge pourpre tirant sur le violet. Il évoque la
myrtille ou le cassis par son aspect et sa taille, le chocolat par son goût.
C’est un antioxydant puissant.""" },
{ "word": "Acanthe", "definition": """Nom féminin.
Du grec « acanthos » du nom de la nymphe Acanthe.
Dans la mythologie grecque Akantha était une nymphe qu’Appolon le D.ieu du soleil
voulut enlever. Elle se défendit en le griffant au visage.
Il se vengea en la métamorphosant en une plante épineuse qui porte son nom.
Le mot « acanthos » serait la recomposition de deux mots :
« Akanos » nom de la tête épineuse de certaines plantes
« Anthos  » qui signifie fleur.
1- En botanique :
Plante méditerranéenne de la famille des acanthacées, aux feuilles découpées
qui se recourbent naturellement, aux fleurs en épis.
Elle pousse dans les lieux frais.
2- En architecture :
Ornement imité de la feuille d’acanthe dans le châpiteau corinthien
de l’architecture grecque.""" },
{ "word": "Acathiste", "definition": """Adjectif.
Du grec moderne acathistos : non-assis. 
En théologie chrétienne orthodoxe, un hymne acathiste est un hymne chanté debout dans les églises byzanthines.   """ },
{ "word": "Accrétion", "definition": """Nom féminin.
Du latin « accretio » qui signifie l’action d’augmenter.
Augmentation de la masse d’un corps par un apport de matière.
En astronomie: se dit d’un astre qui capture de la matière sous
l’effet de la gravitation.
En géologie: augmentation d’un espace de terre ou de mer par ajout de
matériaux extérieurs.""" },
{ "word": "Acédie", "definition": """Nom féminin.
Du latin « acédia » qui signifie dégoût, indifférence. Lui-même issu du
grec « akêdéo » qui signifie « ne pas prendre soin de soi »
Dans le Christianisme, péché de la tristesse et de la désolation
spirituelle. Mais aussi ennui, morosité, abattement, manque
d’enthousiasme et d’intérêt.
S’applique à quelqu’un qui néglige de prendre soin de lui-même et
finit par se désintéresser de tout.
L’acidie ou paresse est l’un des sept péchés capitaux établis au Moyen-Age.
C’est un cas singulier d’anxio-dépression dans l’Eglise. Une
indifférence religieuse. Une véritable dépression religieuse et
spirituelle. .""" },
{ "word": "Ache", "definition": """Nom féminin.
Du latin « apia » pluriel de « apium » qui signifie ache ou persil.
Ce terme désigne certaines plantes de la famille des Apiaceae ou
ombellifères classées avec le cèleri et le persil dans le genre Apium
Il comprend entre autres, le cèleri ou ache des marais « Apium
graveolens » et la livèche ou ache des montagnes « Levisticum
officinale ».
Cette dernière est connue comme diurétique. D’autres espèces sont
connues comme aphrodisiaques et peuvent traiter les impuissances.
D’autres encore peuvent être utilisées dans la neurasthénie.
Dans la Grèce antique, une couronne de ces feuilles était offerte au
vainqueur des jeux isthmiques.
Au Moyen-âge, la feuille était utilisée comme ornement dans l’art
religieux mais aussi dans les fleurons des couronnes ducales.""" },
{ "word": "Acheuléen", "definition": """Adjectif et nom masculin.
De Saint-Acheul localité de la Somme.
Période du paléolithique caractérisée par des silex de grande taille
taillés en bifaces.""" },
{ "word": "Achigan", "definition": """Nom masculin.
D’un mot algonquin qui signifie « celui qui se débat ».
Au Canada, poisson nommé perche noire.""" },
{ "word": "Achopper", "definition": """Verbe transitif indirect.
Du suffixe a- et « chopper » qui signifie buter.
1- Dans un sens littéraire ou vieilli, buter du pied contre un
obstacle, trébucher.
Par exemple: « Vous achoppez encore sur vos conjugaisons latines!  »
2- S’achopper, verbe pronominal. Dans un sens figuré et littéraire, se heurter.
Par exemple: « Il s’achoppe toujours aux mêmes difficultés financières. »""" },
{ "word": "Achrome", "definition": """Adjectif.
Du grec « a » qui signifie sans et « khrôma » qui signifie couleur.
Se dit d’un objet sans couleur, incolore.
Les peintures achromes de Piero Manzoni.""" },
{ "word": "Aciculaire", "definition": """Adjectif.
Du latin « acicula » qui signifie petite aiguille.
1- En minéralogie, se dit de certains minéraux qui se présente en
aiguilles ou en baguettes comme certains silicates.
2- En botanique, se dit de ce qui est aigu ou piquant comme une
aiguille. Les aiguilles de sapin sont des organes aciculaires.""" },
{ "word": "Acribologie", "definition": """Nom féminin.
Du grec « acribologia » qui signifie exactitude, précision rigoureuse
mais aussi examen approfondi.
Choix rigoureux d’un mot dans le langage parlé ou écrit. Précision
dans le style.""" },
{ "word": "Acrophobie", "definition": """Nom féminin.
Du grec « akron » qui signifie pic, sommet ou hauteur.
Phobie du vide.""" },
{ "word": "Acrostiche", "definition": """Nom masculin.
Vient du mot grec « acrostikhos » lui même composé de
deux radicaux « akros » qui signifie extrémité et stikhos qui signifie vers.
Un acrostiche est une forme poétique dont les lettres initiales
de chaque vers forment un mot qui peut se lire de haut en bas.
On trouve un exemple d’acrostiche dans le poème de Guillaume Apollinaire
qui s’intitule « Adieu ».
Ce poème est un ensemble de cinq strophes de trois vers chacune dont les
initiales sont a chaque fois L O U. LOU était le grand amour du poète.
Voici la première strophe :
L‘amour est libre il n’est jamais soumis au sort.
O LOU le mien est plus fort que la mort.
Un cœur le mien te suit dans ton voyage au nord.""" },
{ "word": "Actinotropisme", "definition": """Nom masculin.
Du grec aktis, aktinos : reyon.
Tendance des plantes à s’orienter vers la lumière.""" },
{ "word": "Acuminé", "definition": """Adjectif.
Du latin « acuminatus » issu de acutus qui signifie aigu.
En botanique, se dit d’une extrémité qui se termine en pointe fine et allongée.
La feuille de l’orme champêtre est acuminée.""" },
{ "word": "Adelphique", "definition": """Adjectif.
Du grec « adelphikos » qui signifie fraternel.
1- Fraternel.
Par exemple: « Les relations fraternelles ou relations adelphiques. »
2- En anthropologie, qualifie les liens entre frères et sœurs.
Plus précisément.
a- Qualifie la forme de polyandrie où l’épouse est mariée à deux ou
plusieurs frères.
b- Qualifie la forme de polygynie où l’époux est marié à deux ou
plusieurs sœurs.
c- Qualifie également le mariage entre frères et sœurs.
Par exemple: « En Egypte ancienne, chez les pharaons, le mariage
adelphique était la règle. »""" },
{ "word": "Adobe", "definition": """Nom masculin.
De l’espagnol « adobe » issu de l’arabe « at-tub » qui signifie brique.
Brique d’argile non cuite, obtenue par simple séchage au soleil.
L’argile est mélangée d’eau et d’une faible quantité de paille hachée
ou d’un autre liant, puis façonnée en briques séchées au soleil.
Par exemple, on dit: « Au Mexique, pour l’habitat traditionnel, on
utilise des adobes pour construire des maisons. »""" },
{ "word": "Adventice", "definition": """Adjectif et nom féminin.
Du latin « adventicius » qui signifie qui s’ajoute, supplémentaire.
A- En tant qu’adjectif :
1- En philosophie, une idée adventice est une idée qui n’est pas
innée, qui vient des sens.
2- En botanique, se dit d’une plante qui colonise par accident un
territoire qui lui est étranger, sans y avoir été volontairement
semée.
Se dit aussi d’une plante indésirable, présente dans la culture d’une
autre espèce. Les plantes adventices sont de mauvaises herbes. Le
coquelicot ou le liseron sont des mauvaises herbes.
3- Au figuré, se dit de ce qui ne fait pas partie de la chose, qui
s’ajoute accessoirement.
Par exemple: » L’espérance et l’inquiétude sont des pensées adventices
à la vie même. »
B- En tant que nom :
En anatomie, membrane externe d’un vaisseau ou d’un conduit.""" },
{ "word": "Aérolithe", "definition": """Nom féminin.
Du grec « aero » qui signifie atmosphère et « lithos » qui signifie pierre.
Météorite principalement formée de silicates.""" },
{ "word": "Afantaisie", "definition": """Nom féminin.
Du grec « phantasia » qui signifie apparition qui donne en latin
« phantasia » qui signifie imagination mais aussi, idée, conception de
l’esprit. Avec le préfixe a- qui est privatif.
En médecine, pathologie qui empêche ou coupe chez le patient tout
accès à une visualisation interne.
Néologisme forgé à partir de la définition de fantaisie par Aristote.
Pour le philosophe la fantaisie c’est la faculté par laquelle les
images et les représentations mentales appelées fantasmes arrivent
à notre esprit. 
L’afantaisie est le contraire de la fantaisie.""" },
{ "word": "Affidé", "definition": """Adjectif.
Du latin « affidare » issu de « fides » qui signifie foi.
1- Dans un sens vieilli, à qui l’on peut se fier ou se confier.
Substantif.
1- Confident.
2- Dans un sens péjoratif, qui est de tous les mauvais coups.""" },
{ "word": "Affixe", "definition": """1- Nom masculin.
Du latin « affixus » issu de « affigerere » qui signifie attacher.
Elément susceptible d’être incorporé à un mot, avant, dans ou après le
radical (préfixe, infixe ou suffixe) pour en modifier le sens ou la
fonction.
2- Nom féminin.
Du latin « affixus » de même sens.
En mathématique, nombre complexe représentant un point du plan.""" },
{ "word": "Affres", "definition": """Nom féminin pluriel.
De l’ancien provençal  « affre »  qui signifie horreur; issu du radical
germanique « aifr- » qui signifie horrible, terrible.
Dans un cadre littéraire exprime le tourment, la torture.""" },
{ "word": "Agalmatophilie", "definition": """Nom féminin.
Du grec « agalma » qui signifie statue et « philia » qui signifie amour.
Paraphilie (trouble sexuel fantaisiste et récurrent) qui concerne
l’attirance sexuelle envers les statues; les poupées ou d’autres
objets similaires.
L’agalmatophilie a rapport avec « le pygmalionisme » ou « mythe de
Pygmalion » qui décrit le sentiment d’amour pour un objet de sa propre
création.
Le contraire de ce mot est « l’agalmatorémaphobie » qui est la peur, par
exemple, lors d’une visite de musée, que les statues se mettent à
parler.
Pour approfondir le sujet on peut citer un ouvrage :
« De l’agalmatophilie ou l’amour des statues » de Laura Bossi, Paris
L’Echoppe 2012""" },
{ "word": "Agapes", "definition": """Nom féminin pluriel.
Du grec « agapé » qui signifie amour désintéressé.
1-  Chez les premiers chrétiens, c’était un repas à caractère
religieux qui avait lieu dans le but d’entretenir l’amour entre les
hommes. Il se tenait dans une église.
Les pauvres y étaient invités par les riches. C’était un repas de charité.
2- Plus tardivement, dans la tradition judéo-chrétienne, les agapes
devinrent un repas quotidien qui était suivi d’une forme christianisée
du « birkat ha-mazon » ou actions de grâces.
On pense que les agapes étaient un synonyme du rite de « fraction de pain ».
3- Dans la franc-maçonnerie, les agapes sont le nom donné au repas qui
suit une assemblée de frères dans le temple.
4- De nos jours les agapes sont un repas joyeux et copieux, amical ou
fraternel. Un festin partagé.""" },
{ "word": "Agaric", "definition": """Nom masculin.
Du latin « agaricum » qui signifiait champignon arboricole et
arborescent. En Europe cette définition correspondait à Amillaria
mellea et Cantharellus olearius. Le mot « Agaricum » est attesté depuis Pline.
Les agarics sont appelés aussi psallliotes. Il n’y a pas de consensus
chez les mycologues concernant l’appellation préférable.
Ce sont des champignons basidomycètes du genre Agaricus qui
appartiennent à la famille des agaricacées. Il en existe 200 espèces
dans le monde qui se ressemblent fortement.
Elles sont toutes comestibles à l’exception de l’Agaric jaunissant ou
Agaric xanthodermus qui est toxique.
L’espèce la plus consommée est Agaricus bisporus cultivé de façon
industrielle en champignonnière, c’est le champignon de Paris.
Les espèces sauvages croissent de façon abondante dès les premières
pluies de l’été dans les près et les taillis et parfois dans les bois
clairs.
Ce champignon a des lamelles libres roses à brun noir voire noires
quand il est vieillit. Ses spores son brun-noirâtre ou noirs, son
chapeau est charnu, lisse et blanc lorsqu’il est
jeune. Il se recouvre de fibrilles ou de squames de couleur ocre à
mesure qu’il s’ouvre.  Le pied est au départ rattaché au chapeau par
un voile qui se transforme en anneau. Cet
anneau permet entre autres de distinguer l’agaric des amanites
blanches mortelles mais aussi de certaines lépiotes bien que ces
dernières aient des lamelles et des spores blanches.
L’agaric était un des constituants de la thériaque de la pharmacopée
maritime occidentale du XVIII ème siècle.""" },
{ "word": "Agélaste", "definition": """Nom masculin.
Terme inventé par Rabelais. Du grec « a » privatif et « gelos » qui signifie rire.
Se dit de celui qui ne rit pas ou qui n’a pas le sens de l’humour.""" },
{ "word": "Âgisme", "definition": """Nom masculin.
De « âge » avec le suffixe « – isme » sur le modèle de sexisme.
Depuis 1969, ce mot désigne la discrimination touchant les personnes
les plus âgées. Mais aujourd’hui ce terme s’applique à toutes les
formes de discrimination ou de ségrégation fondées sur l’âge.""" },
{ "word": "Agnation", "definition": """Nom féminin.
Du latin « agnatio » de « ad » qui signifie passage d’un état à un autre
et « gnatus » qui signifie né.
Parenté par les hommes uniquement. elle est aussi appelée parenté
civile et c’est la seule qui est reconnue en droit romain.
Elle s’oppose à cognation  qui est la parenté naturelle.""" },
{ "word": "Agnotologie", "definition": """Nom féminin.
Du grec « gnôsis » qui signifie savoir et « logos » qui signifie étude.
Le préfixe « a » est tiré du grec et exprime la négation « pas » ou la privation
« sans ». Le « a »est dit privatif.
Science de l’ignorance et de sa production. Elle analyse les mécanismes
cognitifs de la formation du doute.
Les lobbyistes s’en servent pour semer le doute lorsque la science menace
leurs intérêts. Ce concept a été théorisé par Robert N. Proctor professeur
d’Histoire des Sciences à l’université de Stanford.
Je remercie Romuald Tribois, professeur de philosophie, qui m’a suggéré ce
mot et m’en a fourni la définition.""" },
{ "word": "Agoraphobie", "definition": """Nom féminin.
Du grec « agora » qui signifie assemblée, place publique.
Phobie des espaces libres et des lieux publics.""" },
{ "word": "Agriffer", "definition": """Verbe transitif.
De l’allemand « greifen » qui signifie saisir, précédé du « a » qui vient
du latin « ad » qui marque le but.
1- Prendre avec les griffes, saisir.
Verbe pronominal « s’agriffer »
2- S’attacher avec les griffes.
Le chat s’agriffa au pantalon du facteur.
3- Familier. S’attacher avec les mains.""" },
{ "word": "Akathisie", "definition": """Nom féminin.
Du grec « a » qui est privatif et signifie « sans » et « khatizein » qui
signifie s’asseoir ou faire asseoir.
Impatience, impossibilité de s’asseoir ou de rester en position
assise. Besoin irrépressible d’agitation.
Ce terme a été créé par un neuro-psychiatre tchèque pour décrire
certains symptômes en 1901.
Ces symptômes peuvent exister dans certaines pathologies et aussi
faire partie d’effets secondaires de certains neuroleptiques de
première génération.""" },
{ "word": "Alastrim", "definition": """Nom masculin.
Du portugais « alastar » qui signifie se répandre.
En médecine, forme mineur de variole, observée surtout en Amérique et
en Afrique.""" },
{ "word": "Albarelle", "definition": """Nom féminin.
De l’italien albarello: blanc ou bois. Origine incertaine.
Champignon comestible qui pousse sur le chataîgnier ou sur le peuplier blanc.
Petit vase de pharmacie destiné à recueillir une préparation. 
Un exemplaire d’un tel vase est présenté dans les collections permanentes
de L’institut du Monde Arabe.""" },
{ "word": "Albédo", "definition": """Du latin albedo : blancheur. Nom masculin.
Portion de l’énergie du soleil que renvoie un milieu depuis sa surface. Par exemple l’albedo renvoyé par une surface enneigée.
La valeur de l’albedo est comprise entre 0 et 1. Plus une surface est réfléchissante plus son albedo se rapproche de 1. 
A titre d’exemple l’albedo de la neige fraîche est compris entre 0,75 et 0,90.
Seul un miroir parfait réfléchirait un maximum de lumière et son albedo serait égal à 1.""" },
{ "word": "Albugo", "definition": """Nom masculin.
Du latin « albuginis » issu de « albus » qui signifie blanc.
Tache blanche de la cornée.
Tache blanche des ongles.""" },
{ "word": "Alchémille", "definition": """Nom féminin.
Du latin « alchemilla » issu du radical « alchimie » en raison des vertus
attribuées par les alchimistes qui croyaient que la rosée récoltée sur
cette plante permettait de transmuer les métaux vils en or.
Plante vivace de la famille des rosacées, à petites fleurs apétales vert jaune.""" },
{ "word": "Alépine", "definition": """Nom féminin.
De « Alep » ville de Syrie.
Tissu de soie et de laine.""" },
{ "word": "Aléthique", "definition": """Adjectif.
Du grec « alêthês » qui signifie réel, vrai.
En logique, les modalités aléthiques sont des modalités logiques
modales selon lesquelles les propositions sont considérées comme
vraies ou fausses, possibles ou impossibles, plausibles ou contestables,
nécessaires ou contingentes.""" },
{ "word": "Alexithymie", "definition": """Nom féminin.
Du grec « a » qui signifie sans « lexis » qui signifie mot et « thumos » qui
signifie affectivité, humeur.
Difficulté à identifier, différencier et exprimer ses émotions ou
parfois celles d’autrui. Ce trait est particulièrement observé chez
les patients présentant des troubles psychosomatiques.""" },
{ "word": "Algidité", "definition": """Nom féminin.
Du latin « algidus » qui signifie froid.
Refroidissement avec sensation de froid et tendance au collapsus.
C’est à dire un malaise soudain et intense avec une baisse de la
tension artérielle, une accélération du pouls et des sueurs froides.""" },
{ "word": "Aliquante", "definition": """Adjectif féminin.
Du latin « aliquantus » qui signifie d’une certain grandeur.
Partie aliquante, qui n’est pas contenue un nombre exact de fois dans un tout.
L’antonyme de ce mot est aliquote.""" },
{ "word": "Aliquote", "definition": """Adjectif féminin.
Du latin « aliquot » qui signifie « un certain nombre de ».
Partie aliquote, qui est contenue un certain nombre de fois dans un tout.
L’antonyme de ce mot est aliquante.""" },
{ "word": "Allélophage", "definition": """Nom masculin.
Du grec « allêlôn » qui signifie l’un, l’autre, terme qui marque la
réciprocité; et ‘phagéin » qui signifie manger.
Etre vivant qui mange un autre être vivant de la même espèce.
A l’exception de l’homme qui utilise le terme « anthropophage ».""" },
{ "word": "Aloyère", "definition": """Nom féminin.
De « aloi » qui est un alliage et désignait parfois une monnaie faite d’alliage.
Bourse en cuir, velours ou satin, parfois brodée. Elle était portée à
la ceinture et renfermait argent, papiers et bijoux.""" },
{ "word": "Ambon", "definition": """Nom masculin.
Du grec « ambôn » qui signifie proéminence.
Tribune surélevée placé à l’entrée du chœur de certaines basiliques et
églises anciennes. Cette tribune était la chaire en haut de laquelle
étaient lus des textes sacrés et des sermons.
Par exemple: »Les ambons sont souvent au nombre de deux, un du côté de
l’évangile, l’autre du côté de l’épître. »""" },
{ "word": "Amharique", "definition": """Nom masculin.
Du latin « amharicus » issu de « Amhara » province centrale de l’Éthiopie.
Langue sémitique du groupe méridional parlée dans la majeure partie du
haut plateau abyssin.
L’amharique est la langue officielle parlée dans l’actuelle Éthiopie.""" },
{ "word": "Amict", "definition": """Nom masculin.
Du latin amictus de même signification.
Rectangle de toile fine que le prêtre se passe autour du cou avant de
revêtir l’aube.""" },
{ "word": "Amiral", "definition": """Nom masculin.
De « émir » issu de l’arabe « âmir » qui signifie chef.
1-Nom masculin.
Anciennement, commandant d’une force navale. Dignité équivalent à
celle de maréchal.
Dans un sens moderne, Officier de grade le plus élevé dans la marine,
correspondant au titre de général d’armée.
2- Adjectif.
Vaisseau amiral: ayant a son bord un amiral, le chef d’une formation navale.
S’emploie aussi concernant le siège d’une société. Par exemple: « Le
vaisseau amiral de cette banque d’affaires se situe dans le quartier
de la Défense à Paris. »
3- Nom féminin. Amirale
Femme d’un amiral.""" },
{ "word": "Ampélographie", "definition": """Nom féminin.
Du grec « ampelos » qui signifie vigne.
Science des différentes variétés de vignes.""" },
{ "word": "Amphibologie", "definition": """Nom féminin.
Du grec « amphibolos » qui signifie ambigu et « logos » qui signifie
parole, discours.
Double sens pour un mot ou pour une proposition.
Par exemple: « On peut noter l’amphibologie du mot DOUVE qui est un
fossé rempli d’eau autour d’un château mais aussi un ver plat parasite
de certains mollusques puis des hommes ou des animaux qui les consomment.""" },
{ "word": "Amphicrine", "definition": """Adjectif.
Du grec  « amphi » qui signifie des deux côtés, en double ou autour, et
« krinein » qui signifie sécréter.
Glande composée de deux types de cellules, exocrine et endocrine.
Par exemple le pancréas.""" },
{ "word": "Amphictyonie", "definition": """Nom féminin.
Du grec « amphiktyones » qui signifie ceux qui sont voisins, ceux qui
habitent autour d’un lieu donné.
Le terme viendrait d’Amphiktyon, fils de Deucalion et de Pyrrha,
fondateur de l’amphiktyonie de Delphes et frère d’Hellen ancêtre des
grecs.
Désigne dans l’antiquité grecque une ligue à vocation sacrée qui a la
charge de l’administration d’un sanctuaire. Ces associations
célébraient les fêtes et empêchaient toute hostilité.
Chacune des peuples membres envoyait ses députés désignés par les cités-Etats
selon un système de roulement.""" },
{ "word": "Amphitryon", "definition": """Nom masculin.
Des vers de Molière, « Le véritable Amphitryon est l’Amphitryon où
l’on dîne » dans la comédie de ce nom. Du grec « Amphitruôn » chef
thébain.
Hôte qui offre à dîner.
On peut aussi dire « une amphitryonne ».""" },
{ "word": "Ampholyte", "definition": """Nom masculin.
Du grec « ampho » qui signifie tous les deux et « lutos » qui signifie qui
peut-être libéré ou dissous.
En chimie, substance protidique qui peut agir selon les cas soit comme
un acide ou soit comme une base.""" },
{ "word": "Amplectif", "definition": """Adjectif.
Du latin « amplecti » qui signifie entourer.
En botanique, se dit d’un organe qui enveloppe un autre organe.""" },
{ "word": "Anacardier", "definition": """Nom masculin.
Du grec « ana » qui signifie nouveau et « kardia » qui signifie cœur.
En botanique, arbre tropical de la famille des anacardiacées aussi
appelé acajou à pommes et qui donne la noix de cajou comestible.""" },
{ "word": "Anaclitique", "definition": """Adjectif.
Du grec « anaklinein » qui signifie replier sur soi-même.
En psychopathologie, une dépression anaclitique est l’arrêt de
développement qui survient dans la première année d’un enfant
brutalement séparé de sa mère.""" },
{ "word": "Anacoluthe", "definition": """Nom féminin.
Provient du grec anacoluthon: »Absence de suite. »
Rupture dans la construction d’une phrase.
Il est huit heures, je vais à la piscine.""" },
{ "word": "Anadrome", "definition": """Adjectif.
Du grec « anadromos » qui signifie qui court en remontant.
En zoologie, se dit des poissons de mer qui remontent le fleuve pour y pondre.
Le saumon est un poisson anadrome.""" },
{ "word": "Anaglyptique", "definition": """Adjectif.
Du latin « anaglypticus » qui signifie ciselé en relief.
1- Se dit d’une écriture ou d’une impression en relief à l’usage des aveugles.
2- En photographie, procédé qui donne l’impression de voir en relief.""" },
{ "word": "Anamorphose", "definition": """Nom féminin du grec anamorphoun : transformer.
Image d’un objet qui est déformée par un miroir courbe. 
Figure ou dessin transformé qui peut sous un certain angle ou grâce à une lentille reprendre son aspect initial. 
En zoologie, métamorphose d’une larve qui naît avec un nombre de segments inférieur à celui qu’elle aura lorsqu’elle deviendra adulte.  """ },
{ "word": "Anaphore", "definition": """Nom féminin.
Du grec anaphora.
Figure de style qui consiste à placer le même mot en tête de différentes phrases pour renforcer le propos. 
On se souvient des propos de François Hollande :  « Moi, Président, je…»
                                                  « Moi, Président, je…»""" },
{ "word": "Anastatique", "definition": """Adjectif.
Du grec « anastasis » qui signifie résurrection.
En imprimerie procédé chimique qui reproduit un texte imprimé.""" },
{ "word": "Anastylose", "definition": """Nom féminin.
Du grec ancien « anastallein » qui signifie remonter.
En archéologie, ce terme signifie la reconstruction pierre à pierre d’un objet.""" },
{ "word": "Angarie", "definition": """Nom féminin.
Du latin « angaria » qui signifie corvée de charroi.
En droit international. Droit pour un État belligérant, de recueillir
des navires neutres se trouvant sur ses eaux territoriales.""" },
{ "word": "Anone", "definition": """Nom féminin.
1- Arbre tropical de la famille des Annonaceae qui pousse surtout en
Amérique. Cet arbre rappelle le pommier. Le nom de genre anone dérive
de « Annon » en langue Taino (les Tainos étaient un peuple indien qui vivait
aux Antilles, à Porto Rico et à Cuba qui fut victime d’un génocide au
XVIème siècle et qui a totalement disparu.)
Annona cherimola est le cherimolier.
Annona glabra est le mamier.
Annona muricata est le corrosolier.
Annona reticulata est le cœur de bœuf ou cachiman.
Annona squamosa est l’attier ou pomme-canelle.
2- Fruit issu de l’arbre Annona cherimola ou cherimolier.""" },
{ "word": "Antienne", "definition": """Nom féminin.
Du latin médiéval « antefana » altération du latin ecclésiastique
d’origine grecque « antiphona » de « anti » qui signifie en face, contre
et « phonos » qui signifie son.
En musique liturgique, refrain repris par le chœur entre chaque verset
d’un psaume, ou chanté seulement avant et après le psaume. Un recueil
d’antienne est dit un antiphonnaire.
De manière figurée et vieillie, affirmation que l’on répète sans
cesse, que l’on ressasse.""" },
{ "word": "Antiphonaire", "definition": """Nom masculin.
Du latin « antiphona » qui signifie « antienne », refrain de psaume.
Livre liturgique catholique rassemblant les partitions grégoriennes
des heures canoniales c’est à dire du Bréviaire.""" },
{ "word": "Antonomase", "definition": """Nom féminin.
Du grec « antonomasia » issu de « anto » qui signifie à la place de et
« onoma »qui signifie nom.
Figure du discours, qui consiste à désigner un personnage par un nom
commun ou par une périphrase qui le caractérise ou bien à l’inverse, à
désigner un individu par le personnage dont il rappelle le caractère typique.
Par exemple, on peut dire, un Don Juan pour désigner un séducteur ou
le grand timonier pour désigner Mao Tsé Toung.""" },
{ "word": "Aoriste", "definition": """Nom masculin.
Du grec « aoristos » qui signifie indéfini.
En grammaire grecque, temps de conjugaison ayant valeur de passé, mais
n’indiquant pas une datation précise, notamment dans le cas de
l’aoriste gnomique, c’est à dire celui que l’on emploie dans les proverbes et les dictons.""" },
{ "word": "Apagogie", "definition": """Nom féminin.
Du grec « apagogé » qui signifie réduction à l’impossible.
Terme de rhétorique. Raisonnement par lequel on démontre la vérité
d’une proposition en prouvant l’impossibilité ou l’absurdité de la
proposition contraire.
Raisonnement par l’absurde.""" },
{ "word": "Apex", "definition": """Nom masculin.
Du matin « apex » qui signifie pointe. Cîmier des casques romains.
1- Partie sommitale d’un organe. Par exemple: »L’apex de la langue. »
En zoologie, sommet de l’enroulement hélicoïdal de la coquille des
gastéropodes.
2- Dans les inscriptions latines, (sur des vestiges romains par
exemple), sorte d’accent aigu marquant la quantité longue d’une
voyelle.
3- En astronomie. Point du ciel vers lequel semble se diriger le
Soleil, par rapport aux étoiles voisines de notre galaxie.""" },
{ "word": "Aphairétique", "definition": """Adjectif.
Du grec « aphairesis » qui signifie abstraction.
Approche philosophique fondée sur l’abstraction.
La théologie négative peut procéder par démarche aphairétique comme
elle peut procéder par démarche apophatique (voir ce mot défini
précédemment).""" },
{ "word": "Aphanisis", "definition": """Nom féminin.
Du grec « aphanisis » qui signifie faire disparaître.
Littéralement « aphanisis du désir ».
Défaut d’apparition ou disparition du désir sexuel chez l’homme ou
chez la femme. Son origine est physiologique ou psychologique.
Ce terme a été introduit par Ernest Jones qui fut l’un des pères
fondateurs de la psychanalyse en Grande- Bretagne.""" },
{ "word": "Apoastre", "definition": """Nom masculin.
Du grec « apo » qui signifie loin de et du mot astre.
Position d’un satellite ou d’une planète lorsqu’il ou elle est sur son
orbite à la distance maximale de l’astre autour duquel il gravite.""" },
{ "word": "Apocope", "definition": """Nom féminin.
Du grec « apokoptein » retrancher.
Retranchement d’une ou plusieurs syllabes à la fin d’un mot.
Par exemple on dit radio pour radiographie ou métro pour métropolitain.
Au contraire quand le retranchement intervient au début d’un mot on
dit que c’est une aphérèse.
Aphérèse est un nom féminin qui vient du grec « aphaeresis » de « apo » au
loin et « hairein » prendre.
Par exemple on dit route pour autoroute.""" },
{ "word": "Apocryphe", "definition": """Adjectif.
Vient du grec « apocryphos » qui signifie caché.
Un écrit apocryphe est un récit dont l’authenticité n’est pas reconnue.
Exemple: les évangiles apocryphes.""" },
{ "word": "Apodictique", "definition": """Adjectif.
Du grec « apodistikos » qui signifie qui  démontre, qui prouve.
Dans le cadre de la logique d’Aristote, ce qui représente un caractère
d’universalité et de nécessité absolue.
Une proposition apodictique est nécessairement vraie où que l’on soit.
Par exemple, en géométrie euclidienne, par un point passe un nombre
infini de droites est une proposition apodictique.
En philosophe, le « cogito de Descartes » est apodictique.
Apodictique s’oppose à dialectique.""" },
{ "word": "Apologie", "definition": """Nom féminin.
Du latin « apologia » qui signifie justification, défense.
Discours qui vise à faire l’éloge d’une personne ou d’une chose.""" },
{ "word": "Apophatique", "definition": """Adjectif.
Du grec « apophasis » issu de « apophêmi » qui signifie nier.
Approche philosophique fondée sur la négation.
On peut dire que la théologie négative procède d’une démarche apophatique.
Cette théologie consiste à envisager Dieu dans ce qu’il n’est pas
plutôt que dans ce qu’il est. Ceci est contraire à ce qui est enseigné
dans les religions monothéistes. 
En effet, dans l’Ancien Testament livre de L’Exode, Dieu
dit de lui-même: « je suis ce qui est » c’est une théologie positive.""" },
{ "word": "Apophtegme", "definition": """Nom masculin.
Du grec « apophtegma » qui signifie précepte, sentence.
Parole ou phrase mémorable qui a valeur de maxime""" },
{ "word": "Aporie", "definition": """Nom féminin.
Provient du grec « aporia » qui signifie absence de passage, embarras.
Impasse dans un raisonnement. Impossibilité de trouver une issue dans
une argumentation.""" },
{ "word": "Aposiopèse", "definition": """Nom féminin.
Du grec « apisopêsis » issu de « aposiopein » qui signifie se taire.
Interruption brusque d’une phrase qui laisse la pensée en suspens et
qui traduit une émotion, une hésitation ou une menace.
Cette interruption se traduit souvent par des points de suspension.
Par exemple: « Il a beaucoup de fièvre et ne sait plus…il ne sait
réellement plus ce qu’il dit. » Georges Bernanos""" },
{ "word": "Apostasie", "definition": """Nom féminin.
Du grec apostasis « se tenir loin de.  »
Rejet de la vie et de la foi chrétienne.
Celui qui bascule dans l’apostasie est un apostat.""" },
{ "word": "Apostille", "definition": """Du latin postea : ensuite.
Ajoût de quelques mots en marge d’une lettre ou d’un écrit.
Post scriptum en est le synonyme.""" },
{ "word": "Apothicaire", "definition": """Nom masculin.
Du grec « apotêkê » qui signifie réservoir.
Dans un langage vieilli, pharmacien.
Par exemple, l’expression: »Des comptes d’apothicaire. » signifie des
comptes compliqués, mesquins ou des comptes surévalués.""" },
{ "word": "Aquilon", "definition": """Nom masculin.
Provient du latin aquilo: vent du nord rapide comme l’aigle en latin aquila.
Vent du nord froid et violent. S’utilise plutôt dans un contexte poétique.""" },
{ "word": "Arcanson", "definition": """Nom masculin.
De l’ancien français « arguenson » altération de la ville d’Arcachon.
Résine qui provient de la distillation de la térébenthine, comme la « colophane ».""" },
{ "word": "Archière", "definition": """Nom féminin.
Formé à partir du mot « arc ».
Ouverture pratiquée dans les fortifications pour permettre le tir à
l’arc ou à l’arbalète, comme une meurtrière.
On peut dire aussi « archère ».""" },
{ "word": "Aréquier", "definition": """Nom masculin.
Du portugais « arequero », de nom scientifique Areca catechu.
Grand palmier d’Asie équatoriale, Inde et Malaisie, de la famille des
Arecaceae. Son fruit, rouge orangé, est la noix d’arec. Son amande
contient du cachou et entre broyée dans la composition du bétel. 
Son nom est aussi palmier à bétel. Sa fleur est cuisinée à Taîwan.
Le bourgeon terminal de cet arbre est le cœur de palmier ou chou
palmiste et il est comestible.""" },
{ "word": "Arétologie", "definition": """Nom féminin.
Du grec « areté » qui signifie vertu et « logos » qui signifie discours.
En philosophie, hymne ou récit  à la gloire du dieu et de ses vertus.
Récit de miracles.
Par extension, récit de choses merveilleuses et agréables.
De manière péjorative, discours sur le bien et le mal. Bavardage philosophique.""" },
{ "word": "Argus", "definition": """Nom masculin.
Nom propre d’un géant de la mythologie qui avait cent yeux.
1- Dans un langage vieilli et littéraire. Surveillant, espion vigilant
difficile à tromper.
2- Publication qui fournit des renseignements spécialisés. Par
exemple, l’argus de l’automobile permet de connaître les prix des
voitures selon leur année de fabrication.
3- Oiseau exotique de la famille des phasianidées qui a la taille d’un faisan.""" },
{ "word": "Argyronète", "definition": """Nom féminin.
Du grec « arguros » qui signifie argent et « nèo » qui signifie je file.
Araignée aquatique qui tisse dans l’eau une sorte de cloche qu’elle
remplit d’air.""" },
{ "word": "Argyrose", "definition": """Nom féminin.
Du grec « arguros » qui signifie argent et de « osis » qui set à former
des noms de maldie non inflammatoires.
1-  Minerai d’argent présent sous forme de sulfure d’argent.
2-  Coloration grise ou brunâtre de la peau ou des muqueuses due à une
imprégnation par des sels d’argent au cours d’un contact professionnel
ou d’un traitement médical prolongé.""" },
{ "word": "Arille", "definition": """Nom masculin.
Du bas latin « arillus » qui signifie grain de raisin.
Enveloppe charnue ou membraneuse de certaines graines auxquelles elle
n’adhère qu’en un seul point le hile.
Par exemple l’arille est l’enveloppe de la noix muscade.""" },
{ "word": "Aristoloche", "definition": """Nom féminin.
Du grec « aristo » qui signifie excellent, meilleur et « locheia » qui
signifie accouchement. Cette plante signifie « excellent accouchement »
en référence à ses vertus analgésiques lors des accouchements.
Plante herbacée de type liane qui comporte plus de 300 espèces.
De cette plante est extrait l’acide aristolochique qui est une
substance cancérigène et néphrotoxique.""" },
{ "word": "Armillaire", "definition": """Adjectif.
Du latin « armillarius » issu de « armilla » qui signifie bracelet.
Une sphère armillaire est un globe formé d’anneaux ou de cercles
représentant le ciel et les astres dans l’ancienne astronomie.""" },
{ "word": "Armoise", "definition": """Nom féminin.
Du latin « artemisia » issu d’un mot grec qui signifie plante d’Artémis.
Artémis était la déesse de la chasse.
Plante herbacée aromatique de la famille des composées. elle peut être
appelée artémise. Plusieurs espèces de cette famille ont des usages
médicaux.
L’armoise maritime est un puissant vermifuge.
La grande absinthe, l’estragon, la citronnelle et le génépi sont des armoises.""" },
{ "word": "Arpète", "definition": """Nom féminin.
Mot régional issu probablement de l’allemand « Arbeiter » qui signifie
travailleur.
Familièrement, jeune apprentie couturière.""" },
{ "word": "Arrobe", "definition": """Nom féminin.
De l’espagnol « arroba » issu de l’arabe « ar-roub » qui signifie le
quart. Cette unité de poids représentait le quart de 50 kg.
1-Unité de poids ou de volume qui était utilisée en Espagne et en
Amérique latine.
Elle valait de 11,5 à 14,7 Kg ou de 12 à 16 litres.
2- Dans l’adresse d’un courrier électronique c’est le @ (on dit aussi
arrobase) qui sépare le nom de l’utilisateur de celui du fournisseur
d’accès à la messagerie.
Synonymes:
Arobas.
Arobase.
Arrobas.
Arrobase.""" },
{ "word": "Artiodactyle", "definition": """Nom masculin.
Du grec « artios » qui signifie pair et « daktylos » qui signifie doigt.
En zoologie, animal appartenant à un ordre des mammifères ongulés
caractérisés par un nombre pair de doigts.
Il comporte les bovidés, les camélidés, les cervidés…
Par exemple: »Les artiodactyles sont plus nombreux que les
périssodactyles [nombre impair de doigts]. »""" },
{ "word": "Aruspice", "definition": """Nom masculin.
Du latin « haruspex » qui signifie devin.
Dans l’antiquité romaine, devin qui examinait les entrailles des
victimes de sacrifice pour en tirer des présages.""" },
{ "word": "Aryténoïde", "definition": """Adjectif et nom masculin.
Du grec « arutainoeidês » qui signifie en forme d’aiguière.
En anatomie, ce sont les cartilages latéraux du larynx sur lesquels
s’insèrent les cordes vocales.
On peut dire: « les cartilages aryténoïdes » ou bien les aryténoïdes.""" },
{ "word": "Asbeste", "definition": """Nom masculin.
Du latin « asbestos » mot grec qui signifie incombustible.
Autre nom pour l’amiante.""" },
{ "word": "Ascensumophobie", "definition": """Nom féminin.
Du mot français « ascenseur », du latin « ascensum », issu de ascendere
qui signifie monter.
Phobie de l’ascenseur.""" },
{ "word": "Askos", "definition": """Nom masculin.
Du grec « askos » qui signifie outre.
Petit vase à versoir latéral, muni d’une anse de panier dont la forme
dérive de la gourde.
Il était employé par les Grecs antiques et les Etrusques.
Ce nom est moderne; on ignore le nom donné par les Grecs à cette forme.
En art étrusque, l’askos est souvent zoomorphe.""" },
{ "word": "Assertorique", "definition": """Adjectif.
Du mot « assertion » issu du latin « assertio » qui signifie affirmer.
En philosophie et surtout d’après Kant, un jugement assertorique
énonce une vérité de fait et non pas une vérité nécessaire.
Par exemple: « Napoléon est né en Corse. » Cette proposition est
assertorique puisque Napoléon aurait pu naître à Paris. C’est une
vérité de fait mais elle n’est pas nécessaire.""" },
{ "word": "Astéisme", "definition": """Nom masculin.
Du grec « asteismos » qui signifie urbanité.
Figure de style qui consiste en un badinage délicat et ingénieux par
lequel on loue ou on flatte avec l’apparence du blâme ou du reproche.
Par exemple:
 » Il paraît que tu ne comprends
   Pas les vers que je te soupire
   Tu les inspires, c’est bien pire. »
   VERLAINE
ou bien autre exemple:
« Quoi! encore un nouveau chef d’œuvre! N’était-ce pas assez de ceux
que vous avez publiés? Vous voulez donc désespérer tout à fait vos
rivaux ?
 VOITURE cité par Fontainier
L’astéisme suppose une certaine connivence entre les interlocuteurs
et se pratique surtout entre amis.
La locution: « A charge de revanche.  » (après un service rendu) est un astéisme.""" },
{ "word": "Asticoter", "definition": """Verbe transitif.
De l’ancien français « dasticoter » qui signifie jargonner, contredire, ennuyer.
Issu de l’allemand  » das dich Gott…! qui signifie que Dieu te… que
l’on a traduit par « d’asticot » influencé par le mot « estiquer » qui
signifie piquer par le néerlandais « steecken ».
Familièrement, agacer, harceler quelqu’un pour des choses insignifiantes.""" },
{ "word": "Astrakan", "definition": """Nom masculin.
De la ville de Russie d’Astrakan.
Fourrure à poils bouclés, d’agneau caracul, tué dans son très jeune âge.""" },
{ "word": "Asyndète", "definition": """Nom masculin ou féminin.
Du grec « asundeton » qui signifie style sans conjonctions. Issu de a-
qui signifie sans, et du verbe « sundein » qui signifie lier ensemble.
Issu de « sun » qui signifie avec et donnera syn et « dein » qui signifie lier.
Figure du discours oral ou écrit. Sorte d’ellipse par laquelle on
retranche les conjonctions de coordination qui doivent lier les
parties d’une phrase.
Les éléments apparaissent les uns après les autres sans liens,
juxtaposés, comme dans une énumération.""" },
{ "word": "Ataman", "definition": """Nom masculin
Du turc « ata » qui signifie père accolé au suffixe augmentatif « man ».
Chef des cosaques au moment de leur indépendance.
Ce mot est souvent confondu avec le mot « hetman » qui a la même
signification mais dont l’origine étymologique diffère. 
Vient du haut-allemand « hauptmann », de « haupt » qui signifie tête
et « mann » qui signifie homme.""" },
{ "word": "Ataraxie", "definition": """Nom féminin.
Du grec « ataraxia » qui signifie absence de trouble.
Tranquillité de l’âme. Chez les stoïciens, état d’une âme que rien ne
trouble. Tranquillité du sage.""" },
{ "word": "Atellanes", "definition": """Nom féminin pluriel.
Du latin « atellana » issu de la ville d’Atella qui était une ville
d’Italie ancienne située en Campanie entre Naples et Capoue.
Elle possédait une forme de théâtre improvisé et masqué, les
atellanes, d’où dérive sans doute la commedia dell’arte.
Dans l’Antiquité romaine, petites pièces de théâtre bouffon.""" },
{ "word": "Atermoyer", "definition": """Verbe transitif ou intransitif selon le sens.
De a- privatif qui signifie sans et de l’ancien français « termoyer »
-issu de terme- qui signifie tarder, ajourner.
1- En tant que verbe transitif. Dans un sens vieilli, renvoyer un
paiement à un terme plu éloigné.
2- En tant que verbe intransitif. Chercher à gagner du temps par des
faux-fuyants ou des faux-semblants.""" },
{ "word": "Athanor", "definition": """Nom masculin.
De l’arabe « al tannur » qui signifie le fourneau.
En alchimie, grand alambic à combustion lente.
Par exemple: « Un feu terrible sortait d’un athanor. »""" },
{ "word": "Athénée", "definition": """Nom masculin.
Du grec « athenaeum » qui signifie temple d’Athéna, lieu où se
disputaient des concours de poésie dans la Grèce antique.
1- Etablissement destiné à des lectures ou à des leçons publiques en
Suisse et en Belgique.
2- En Belgique, établissement secondaire d’enseignement public.""" },
{ "word": "Athermane", "definition": """Adjectif.
Le mot vient du grec « thermainein » qui signifie chauffer précédé du
« a » privatif élément tiré du grec qui signifie sans.
En langage technique se dit d’un matériau qui est parfaitement
imperméable à la chaleur.
Le contraire de ce mot est « diathermane ».""" },
{ "word": "Atlante", "definition": """Nom  masculin.
De l’italien « atlante » issu du grec Atlas.
Figure d’homme portant un entablement, à la manière du dieu Atlas
portant le ciel sur ses épaules.""" },
{ "word": "Atrabilaire", "definition": """Adjectif.
Du latin « atra » qui signifie noire et « bilis » qui signifie bile.
Dans la médecine ancienne, se dit de ce qui a rapport avec l’humeur
noire ou atrabile.
Au figuré et dans un sens vieilli, un caractère, une humeur ou un
tempérament atrabilaire est plutôt porté à la mauvaise humeur, à
l’irritation et à la colère.
« Le Misanthrope » de Molière a pour sous-titre « l’Atrabilaire Amoureux ».""" },
{ "word": "Attrition", "definition": """Nom féminin.
Du latin attritio: frottement.
En physique: action de deux corps qui provoque une perte de substance.
En médecine : écorchure due à un frottement. Synonyme de contusion.
En théologie: regret d’avoir offensé Dieu par honte ou crainte de l’enfer.
Attrition est opposée à contrition qui est le regret d’avoir offensé
Dieu par le péché même.""" },
{ "word": "Aubour", "definition": """Nom masculin.
Deux définitions.
1- Du latin « alburnum » issu de « albus » qui signifie blanc.
En botanique, désigne l’aubier qui est la partie tendre et blanchâtre
située entre l’écorce et le duramen.
2- Du latin « laburnum » apparenté à « labrum » qui signifie lèvre, chose
pendante. Avec le sens de l’arbre à feuilles pendantes.
En botanique, désigne la cytise qui est une plante de la famille des
légumineuses.""" },
{ "word": "Aurélie", "definition": """Nom féminin.
De l’italien « aurelio » qui signifie doré, issu du latin « aurum » qui signifie or.
Méduse cnidaire appartenant à la super classe des Scyphozoaires. Son
nom dans la classification scientifique est Aurélia aurita. 
On l’appelle aussi méduse bleue ou méduse lune. 
Elle peut-être aussi rose, blanche ou mauve et elle est fréquente dans toutes
les mers du monde excepté les mers du pôle sud ou de l’antarctique.""" },
{ "word": "Aurige", "definition": """Nom masculin.
Du latin « auriga » qui signifie cocher. Ce mot fut popularisé à la fin
du XIX ème siècle par les découvertes faites à Delphes.
Dans l’antiquité, conducteur de char dans les courses.
L’aurige de Delphes est un bronze célèbre trouvé dans le sanctuaire.""" },
{ "word": "Autunite", "definition": """Nom masculin.
De « Autun » ville de France.
En minéralogie, phosphate naturel d’uranium et de calcium.""" },
{ "word": "Avatar", "definition": """Nom masculin.
Du sanskrit « avatâra » qui signifie descente.
1- Dans la religion hindoue. chacune des incarnations du dieu Vishnou.
2- Métamorphose, transformation.
3- Par contresens et le plus souvent employé au pluriel: mésaventure, malheur.""" },
{ "word": "Aviceptologie", "definition": """Nom féminin.
Du latin « avis » qui signifie oiseau, « capere » qui signifie prendre et
du grec « logos » qui signifie discours.
Dans un sens vieilli, art de prendre les oiseaux.""" },
{ "word": "Avoirdupoids", "definition": """Nom masculin.
De « avoir-du-pois » de même signification.
Mot anglais emprunté au français au XVème siècle.
Système de mesure de masse, des pays anglo-saxons, qui s’applique à toutes les marchandises autres que les métaux précieux et les médicaments. La livre y vaut 453,59 g""" },
{ "word": "Axénique", "definition": """Adjectif.
De « a » élément du grec qui signifie sans et du grec « xénos » qui signifie étranger.
En bactériologie, se dit de se qui se développe ou est cultivé en milieu stérile. Ou bien de ce qui est totalement dépourvu de germes saprophytes ou pathogènes.""" },
{ "word": "Azimut", "definition": """Nom masculin.
De l’arabe « az-samt » qui signifie le chemin.
1- En astronomie, angle formé par le plan vertical d’un astre et le
plan méridien du point d’observation.
   En physique, angle que fait le grand axe d’une vibration
elliptique avec une direction de référence du plan d’onde.
2- La locution familière: « dans tous les azimuts » signifie dans toutes
les directions, dans tous les sens.
Dans un sens figuré, « tous azimuts » signifie qui utilise tous les
moyens et a les objectifs les plus variés.
Par exemple, une campagne de publicité tous azimuts.""" },
{ "word": "Bachi-bouzouk", "definition": """Nom masculin.
Du turc signifiant littéralement mauvaise tête.
Dans l’armée turque, cavalier qui était enrôlé en temps de guerre.""" },
{ "word": "Badin", "definition": """Adjectif.
D’un mot provençal qui signifie niais et qui serait issu de « badar »
qui a donné badaud.
Dans un sens littéraire, qui aime à rire, à plaisanter.
Dans un sens moderne la locution « une humeur badine » indique une
humeur enjouée, légère,
Nom masculin.
De « Badin » nom de l’inventeur.
Anémomètre qui sert à indiquer la vitesse relative d’un avion.""" },
{ "word": "Bagout", "definition": """Nom masculin.
Déverbal de l’ancien français « bagouler » qui signifie railler, issu de
« bagos » qui signifie bavardage. Le mot résulte du croisement du verbe
en français « bavarder » et du nom commun en ancien français « goule »
qui signifie bouche. 
La transcription « -gout » provient d’un rapprochement erroné avec « goût ».
Dans un langage populaire, familier. Se dit d’un bavardage qui mêle la
hardiesse et l’effronterie dans un but d’illusionner ou de duper.
Par exemple: « Ce vendeur à la sauvette a beaucoup de bagout. »""" },
{ "word": "Baguenaude", "definition": """Nom féminin.
Du languedocien « baganaudo » issu de « baga » qui signifie poche, sac.
1- Fruit du baguenaudier, qui se présente sous forme d’une petite
gousse remplie d’air, qui éclate avec un bruit sec quand on la presse.
2- Dans un sens vieilli, niaiserie à laquelle on perd son temps.
3- Familier et plus moderne mais peu utilisé, promenade où l’on flane.""" },
{ "word": "Baille", "definition": """Nom féminin.
Du latin « bajula » qui signifie chose qui porte; récipient renfermant
une substance.
1- En marine. Baquet. Bateau qui n’avance pas vite.
2- En argot marin. Eau.
Par extension en argot courant, l’eau, la mer.
Par exemple: »La grande baille. »
3- « Navire-école »
Surnom de l’École navale.""" },
{ "word": "Bamboula", "definition": """Nom masculin et féminin.
Dérivé est dérivé de « kam-bumbulu » et de « ba m’bula » en langues
bantoues qui signifie tambour.
1- Nom masculin.
Dans un sens vieilli, tam-tam.
2- Nom  féminin.
Dans un sens vieilli, série de danses africaines exécutées au son du
bamboula pendant un après-midi et la nuit qui le suit.
3- Nom féminin.
A l’origine en argot militaire. Dans un sens familier et vieilli.
L’expression « faire la bamboula » signifie faire la fête.""" },
{ "word": "Baresthésie", "definition": """Nom féminin.
Du grec « baros » qui signifie pesanteur et « aisthésis » qui signifie
sensation, sensibilité.
Sensibilité profonde à l’apesanteur ou à la pression.""" },
{ "word": "Barnum", "definition": """Nom masculin.
Du nom de Phineas Taylor Barnum entrepreneur de spectacle américain et
fondateur du cirque Barnum.
Toutes les définitions sont en lien avec le cirque ou l’idée que l’on s’en fait.
1- Dans un sens péjoratif: Forain qui présente le spectacle d’un
artiste ou un phénomène spectaculaire.
Par exemple: « Le barnum voulait être riche grâce à ce prodige de
l’acrobatie qui attirait les foules. »
Par métonymie (la partie désignant le tout).
2- Type d’abri de jardin qui ressemble à une tente ou à un chapiteau.
Par exemple: « Le barnum nous préservera de la pluie. »
3- Abri des commerçants sur un marché non couvert.
Par exemple: « Sous son barnum, il vend toutes sortes d’articles pour
la cuisine. »
4- Kiosque abritant une seule personne qui vend des journaux.
Par exemple: « Bien à l’abri sous son barnum, il nous vend toutes les
nouvelles du monde. »
5- Dans un langage familier, se dit d’un tapage ou d’un grand
désordre, qui peut évoquer le cirque ou le spectacle de foire.
Par exemple: « Ils ont fait le barnum jusque dans la rue. »""" },
{ "word": "Baudruche", "definition": """Nom féminin.
De la racine indo-européenne « bod- » qui désigne ce qui est enflé,
gonflé, boursouflé. Forme allongée de « baudrée » qui signifie vieux
morceau de cuir ou « baudré » en forme de baudrier, de bourse.
« Baudrée » ou « baudré » est tirée de « baudru » qui dans le Berry signifie
ventru en parlant de bêtes à cornes.
1- Pellicule extraite de l’intestin du bœuf ou du mouton et qui sert à
recouvrir ou à fabriquer certains objets. Cette pellicule est préparée
par les parcheminiers. Elle est dite aussi « peau divine » parce qu’on
l’applique sur les coupures à l’instar du taffetas d’Angleterre.
Par analogie, fine pellicule de caoutchouc utilisée entre autres pour
fabriquer des ballons.
2- Au figuré, personne qui n’a que les apparences des mérites qu’on
lui prête et qui se dégonfle aisément.
Par exemple: « Il n’a pas tenu sa promesse. Il s’est dégonflé comme un
ballon de baudruche. »""" },
{ "word": "Bayadère", "definition": """Nom féminin.
Du portugais « balladeira » issu de « ballar » qui signifie danser.
1- Danseuse sacrée de l’Inde.
2- Par apposition, un tissu bayadère est un tissu à larges rayures
multicolores dans le sens de a chaîne.""" },
{ "word": "Bégueter", "definition": """Verbe intransitif.
De l’ancien français « béguer » qui signifie bégayer.
Dans un usage rare, pousser son cri pour une chèvre.
On emploie plus facilement, bêler ou chevroter.""" },
{ "word": "Béguine", "definition": """Nom féminin.
Du néerlandais « beggaert » qui signifie moine mendiant.
Religieuse de Belgique et des Pays-Bas soumise à la vie d’un couvent
mais qui n’a pas encore prononcé ses vœux.""" },
{ "word": "Benjoin", "definition": """Nom masculin.
Du catalan « benjui » lui-même emprunté à l’arabe « luban djawi » qui
signifie encens de Java. Le nom ancien est storax.
Substance aromatique et résineuse qui provient des incisions sur
l’arbre « Styrax benjoin » qui pousse en Extrème-Orient.
Différentes espèces de Styrax sont repérées en Indochine, en Indonésie
 et en Turquie.
Les arômes issus de cette résine sont utilisés en parfumerie. C’est la
« note orientale » des parfums. Ils sont utilisés aussi dans la
composition des cigarettes.
La teinture de benjoin est antiseptique et cicatrisante.
Le benjoin de Siam (Thaïlande) est le principal composant du Papier d’Arménie.
Le benjoin est utilisé comme encens dans l’Eglise russe orthodoxe et
dans les pays du Maghreb.""" },
{ "word": "Benthos", "definition": """Nom masculin.
Du grec « benthos » qui signifie profondeur.
Ensemble des organismes qui vivent sur le fond des mers et qui s’y
déplacent peu.""" },
{ "word": "Berlue", "definition": """Nom féminin.
De « belluer » qui signifie éblouir.
Ce mot s’emploie dans l’expression « avoir la berlue », qui signifie
avoir des visions.
Par exemple: « J’étais sûr d’avoir mis la lettre sur la commode ! Je
n’ai pas la berlue quand même !!  »
Au sens figuré la même expression signifie se faire des illusions.
Par exemple: « Il a cru à cette promotion, mais il a eu la berlue. »""" },
{ "word": "Bétyle", "definition": """Nom féminin.
Du grec « baîtulos » qui signifie pierre sacrée.
Pierre sacrée de l’Arabie préislamique qui était adorée par les
anciens comme une idole.""" },
{ "word": "Bézoard", "definition": """Nom masculin.
De l’arabe « bāzahr » issu du persan « pādzhar » qui signifie chasse-poisson. 
Amas constitué de poils ou de fragments de végétaux qui se forme dans l’estomac de certains animaux comme les ruminants ou parfois chez des êtres humains psychotiques qui avalent des matières non digestibles.
Autrefois, en Orient, le bézoard était considéré comme un antidote aux poisons et comme une protection contre les maladies infectieuses.""" },
{ "word": "Bièvre", "definition": """Nom féminin.
Du latin « beber » d’origine gauloise qui signifie castor.
Ancien nom du castor.""" },
{ "word": "Birr", "definition": """Nom masculin.
Étymologie inconnue.
Devise officielle de l’Ethiopie.""" },
{ "word": "Biwa", "definition": """Nom masculin.
D’un mot japonais.
Luth japonais utilisé dans la musique traditionnelle.""" },
{ "word": "Blandice", "definition": """Nom féminin.
Du latin « blandicia » qui signifie flatterie.
De manière littéraire et surtout au pluriel se dit de ce qui flatte ou
qui séduit.""" },
{ "word": "Bliaud", "definition": """Nom masculin.
L’origine de ce mot est incertaine. Deux hypothèses peuvent être
discutées, l’une et l’autre font difficultés. .
a- Hypothèse d’un ancien étymon franque « blîfald » qui signifie manteau
de couleur écarlate, issu de l’ancien saxon « blî » qui signifie coloré,
brillant et « -fald » a rapport avec l’ancien haut allemand « fald »
action de plier, pli ou l’ancien nordique « falder » extrémité d’un vêtement.
A rapprocher de l’ancien provençal  « faudas » pan d’un habit ou de
l’ancien provençal « fodil » tablier issu du got « falda ».
Cette hypothèse ne permet pas d’expliquer l’ancien provençal « blidal »
ou « brizal ».
b- Hypothèse d’un étymon ancien haut allemand « bridelt » participe
passé de « bridelen, britelen » tisser.
Cette hypothèse peut être écartée parce que le verbe n’est pas attesté
en ancien haut allemand mais en moyen haut allemand au sens de serrer
la bride.
1- Vêtement que les hommes et les femmes portaient au Moyen-Âge.
Pour les hommes c’était une tunique. Pour les femmes c’était une
longue robe étroite.
Des statues de femmes portant un bliaud se trouvent à la cathédrale
d’Angers et à le cathédrale de Chartres.
2- Dans sa forme moderne, blouse courte de grosse toile bleue, sans
col ni boutons, que portent sur leur pantalon les mariniers sur la
Loire.
On écrit « bliaud » ou « bliaut ».""" },
{ "word": "Bliaut", "definition": """Origine inconnue.
Longue tunique que les hommes et les femmes portaient au Moyen-Âge.""" },
{ "word": "Blitzkrieg", "definition": """Nom masculin.
De « Blitz » qui signifie éclair et « Krieg » qui signifie guerre.
Ce mot est entré dans la langue française vers l’année 1980.
1-  Guerre éclair. Ce mot était employé en Allemagne, pour qualifier
la campagne allemande de Pologne en 1939, mais aussi l’invasion
de la France en 1940.
2- En politique, attaque qui vise une victoire rapide.
Par exemple, cette phrase lue dans le Monde du 8 août 2014, à propos du livre:
« Survivants. Pourquoi nous sommes les seuls humains sur terre. » de Chris Stringer.
« L’histoire de notre espèce serait plutôt, alors, celle d’une forme de
blitzkrieg de moins de 60000 ans. »""" },
{ "word": "Boëtte", "definition": """Nom féminin.
Du breton « boued » qui signifie nourriture.
Dans le langage de la pêche, appât pour attirer les poissons""" },
{ "word": "Boniment", "definition": """Nom masculin.
De l’argot « bonir » ou « bonnir » qui signifie dire.
1- Propos que débitent les charlatans, les bateleurs pour convaincre
et attirer la clientèle.
Par extension, discours trompeur pour vanter une marchandise ou
séduire un client.
2- Se dit de tout propos mensonger qui cherche à tromper quelqu’un.""" },
{ "word": "Borasse", "definition": """Nom masculin.
Du grec « borassos » qui signifie datte.
En botanique, palmier à feuilles étalées en éventail, de la famille
des arécacées dont on fait le vin de palme et dont les bourgeons
sont comestibles (coeur de palmier). On dit aussi borassus ou rônier.
Par exemple: Le borasse pousse dans les pays méditerranéens.""" },
{ "word": "Boubouler", "definition": """Verbe intransitif.
Onomatopée.
Pousser son cri, en parlant du hibou.""" },
{ "word": "Bougnoul", "definition": """Nom masculin variable.
Du wolof « nuul » qui signifie noir, « wu nuul » qui est noir, « fas wu
nuul » cheval noir. la locution originelle est parfois injurieuse en
wolof.
Familier et péjoratif. Injure raciste.
1- Nom donné par les blancs du Sénégal, aux noirs autochtones.
2- Maghrébin, arabe.""" },
{ "word": "Boulingrin", "definition": """Nom masculin.
De l’anglais « bowling-green » qui signifie gazon pour jouer aux boules.
Parterre de gazon souvent entouré de bordures et de talus.""" },
{ "word": "Bouphonies", "definition": """Nom féminin et pluriel.
Du grec « bous » qui signifie bœuf et « phonos » qui signifie voix ou son,
peut-être pour le cri du bœuf que l’on tue.
Cérémonie de la Grèce antique qui avait lieu le 14 du mois de
scinophorion au cours des fêtes dipoliennes en été.
On y sacrifiait un bœuf en souvenir d’un autre bœuf sacrifié sur
l’autel de Zeus Polieus.
A la suite de ce meurtre, le coupable était parti en exil en
abandonnant sa hache sur place.
La hache fut mise en accusation puis acquittée au cours d’un procès.
Les Bouphonies reproduisent le meurtre et le procès.""" },
{ "word": "Bourdigue", "definition": """Nom féminin.
De l’ancien provençal « bordigo » ou « bourdigo » issu du latin
« bordigala » diminutif de « borda » qui signifie logis, demeure.
Enceinte en clayonnage qui en bord de mer sert à prendre ou à garder du poisson.""" },
{ "word": "Boustrophédon", "definition": """Nom masculin.
Du grec « bous » qui signifie bœuf et « strophein » qui signifie tourner.
Ecriture primitive, du grec et de l’étrusque principalement, dont les
lignes allaient sans interruption de gauche à droite et de droite à
gauche à la manière des sillons d’un champ.""" },
{ "word": "Boutre", "definition": """Nom masculin.
De l’arabe « but » qui signifie bateau à voile.
Petit navire à voiles, effilé à l’avant et surélevé à l’arrière.""" },
{ "word": "Bovarysme", "definition": """Nom masculin.
De « Madame Bovary » le roman de Gustave Flaubert. 1865.
Evasion dans l’imaginaire par insatisfaction.
Faculté qu’un être humain a de se concevoir autre qu’il n’est.""" },
{ "word": "Boyard", "definition": """Nom masculin.
Emprunté au russe « boiarin » qui signifie seigneur. La forme « boiar » au
génitif pluriel se déplace en français en boyard.
Dans la Russie des tsars, le boyard désignait un noble par opposition au moujik.""" },
{ "word": "Bradel", "definition": """Locution adjective ( à valeur d’adjectif ).
De Bradel, relieur.
Reliure, cartonnage à la Bradel, où le bloc de cahiers est emboîté
dans un cartonnage léger, le dos étant séparé des plats par une
rainure longitudinale.""" },
{ "word": "Bradyphasie", "definition": """Nom féminin.
Du grec « bradus » qui signifie lent et « phasis » qui signifie parole.
Trouble de la parole caractérisé par une élocution lente.""" },
{ "word": "Brahmane", "definition": """Nom masculin.
Du sanskrit « brahmana » qui signifie lié au sacré.
En Inde, membre de la caste sacerdotale, première des quatre grandes
castes traditionnelles.""" },
{ "word": "Brandebourg", "definition": """Nom masculin.
De l’État allemand de Brandebourg qui créa la mode d’un manteau orné
de passementerie.
Passementerie (galon, broderie) ornant une boutonnière.""" },
{ "word": "Bregma", "definition": """Nom masculin.
Du grec « bregma » qui signifie le haut de la tête. Issu de « bregméin »
qui signifie arroser, humecter, car chez les nouveaux-nés cette partie
est toujours humide. c’est une partie
molle appelée Fontanelle.
En anatomie. Partie de la tête que l’on appelle aussi le sinciput.
Elle est composée de deux os, nommés « bregmatis ossa » qui sont les
deux pariétaux.
Par exemple: »Le bregma est le point le plus haut de l’os frontal. »""" },
{ "word": "Bréhaigne", "definition": """Adjectif au féminin.
Au XII ème siècle une terre baraine signifiait une terre stérile. Ce
mot viendrait du pré-roman « bar » et « haigne » à rapprocher de l’ancien
français « meshaigne » qui signifie mutiler.
En ancien français le « meshain » est l’action de mutilation des
membres, de l’estropiement. Ce terme se rapprocherait de bréhaigne,
état de stérilité de la femme vécu comme une amputation des membres.
Ce terme vieilli ou littéraire signifie stérile (en parlant d’une femme).
Peut s’employer aussi pour la femelle d’un animal stérile.
Par exemple on dit: « une jument bréhaigne. »
Se dit aussi d’un poisson sans œuf, ni laitance.
Par exemple on dit : « une carpe bréhaigne ».""" },
{ "word": "Busc", "definition": """Nom masculin.
Du mot buste issu de l’italien « busco » de même radical que « bûche »
c’est à dire de « buscum » qui signifie bois.
1- Anciennement c’était une lame de métal flexible ou baleine qui
servait à maintenir le devant d’un corset.
2- Coude de la crosse d’un fusil.
3- Saillie contre laquelle viennent buter les portes d’une écluse.""" },
{ "word": "Busserole", "definition": """Nom féminin.
Du provençal « bousserolo » issu de « bouis » qui signifie buis.
Arbuste sauvage des lieux ensoleillés faisant partie de la famille des
éricacées dont le feuillage est persistant. Ses fruits sont des baies
rouges farineuses et disposées en grappe appelées : « raisin d’ours ».""" },
{ "word": "Bussinose", "definition": """Nom féminin.
Du grec « bussinos » qui signifie de lin, de coton.
En médecine, maladie pulmonaire qui atteint les ouvriers qui
travaillent le coton.""" },
{ "word": "Byssinose", "definition": """Nom féminin.
Du grec « bussinos » qui signifie de lin, de coton.
Maladie pulmonaire qui affecte les ouvriers qui travaillent le coton.""" },
{ "word": "Byssus", "definition": """Nom masculin.
Du latin « bussos » qui signifie lin très fin, coton.
Faisceau de filament soyeux, sécrété par une glande de certains
lamellibranches et qui leur permet de se fixer.
Par exemple le byssus de la moule.""" },
{ "word": "Byzantin", "definition": """Adjectif.
Du grec « Buzantion » qui signifie Byzance.
1- de Byzance, propre à Byzance et à son empire.
Empire Byzantin; du IVème siècle à 1453.
Le grec Byzantin, forme ancienne du grec employée dans la liturgie
grecque orthodoxe.
Église Byzantine à coupoles.
2- Qui évoque par son excès de subtilité, son caractère formel et
oiseux les disputes théologiques qui avaient lieu à Byzance.
Par exemple: « discuter du sexe des anges ».""" },
{ "word": "Cabiai", "definition": """Nom masculin.
Ce mot vient d’emprunts antérieurs au tupi « capligouare » du Brésil,
puis d’un mot caraïbe de Guyane que l’on peut décomposer en « cabi »
qui signifie herbe et « aica » qui signifie manger.
Mammifère semi-aquatique d’Amérique du sud qui est considéré comme le
plus grand des rongeurs. On l’appelle aussi le cochon d’eau.""" },
{ "word": "Cabus", "definition": """Adjectif masculin.
Mot provençal issu du latin « caput qui signifie tête peut-être par un
intermédiaire italien.
Un chou cabus est un chou à tête ronde et à feuilles lisses.""" },
{ "word": "Cacaber", "definition": """Verbe intransitif.
Du latin « cacabere » issu du grec « kakkabizein » qui provient de
« kakkabé » qui signifie perdrix.
Terme plutôt rare. Crier en parlant de la perdrix ou de la caille.""" },
{ "word": "Cador", "definition": """Nom masculin.
Peut-être de l’arabe « gaddour » qui signifie chef ou bien de ca(bot) et (Mé)dor.
1- En argot, c’est un chien.
2- S’utilise dans la locution « C’est un cador » qui signifie: »C’est
quelqu’un de brillant. »
Ce mot est un peu vieilli.""" },
{ "word": "Café", "definition": """Nom masculin.
Vient de l’arabe « qahweh », qui donne le « qahvé » turc puis le
« caffé » italien, dont est issu le « café » français.
Cette boisson est obtenue à partir des graines de caféier.
Le caféier est un arbuste à feuilles persistantes et à fleurs
odorantes qui pousse à l’origine au Yemen dans ce que l’on appelait
l’Arabie heureuse. Les fruits sont des fruits charnus rouges, violets
ou jaunes qui sont des cerises de café qui contiennent deux noyaux.
Chacun des deux noyaux contient un grain de café.
Le café existe depuis le XVème siècle. Mais en 1808, pour des raisons
politiques, Napoléon publia le « décret continental » qui priva la
France de sucre et de café. On parvint à remplacer le sucre de canne
par le sucre de betterave et le café par de la chicorée. Plus tard, le
décret tomba en désuétude et cette pratique ne revint que pendant les
deux guerres mondiales.
Dans son dictionnaire de cuisine, Alexandre Dumas, notait que le
meilleur café était le Moka; il était divisé en trois variétés le
baouri pour les grands seigneurs, le saki et le salabi.
Selon lui le café procurait « une excitation nerveuse ».
Voltaire en a abusé ainsi que Balzac.
On cite cette anecdote de Fontenelle qui aimait beaucoup le café et
en prenait à tous les repas :
Un jour qu’un médecin de ses amis lui disait que le café est un poison
lent, qui finit toujours par exercer une influence mauvaise pour la
santé, il répondit !
« Docteur, répondit l’académicien, je le crois comme vous. Il y a
quatre-vingts ans que j’en prends, il faut qu’il soit bien lent en
effet pour que je sois encore vivant ! »""" },
{ "word": "Cafre", "definition": """Nom masculin.
A l’origine « du Siam », « de l’Ethiopie » issu de l’arabe « kâfir » qui
signifie « infidèle ».
De la Cafrerie, c’est-à-dire d’Afrique du Sud. Les Cafres sont une
ethnie d’Afique noire australe.""" },
{ "word": "Caillebotte", "definition": """Nom féminin.
De l’ancien français « caillebotter » qui signifie réduire en caillot.
1- Masse de lait caillé.
2- Fromage frais non salé fabriqué à partir de lait de vache dans le Poitou.
Gustave Caillebotte 1848-1894
Peintre français. Nombre de ses tableaux impressionnistes sont exposés
musée d’Orsay à Paris.""" },
{ "word": "Cairn", "definition": """Nom masculin.
Du gaélique « carn » qui signifie « tas de pierre ».
1- Monticule ou tumulus celtique, fait de terre ou de pierres. Il date
en général de la période Néolithique et possède des fonctions variées.
Par exemple: « Un cairn balise le passage le long d’un glacier. »
2- Pyramide de pierres élevée par des alpinistes, des explorateurs
comme point de repère ou comme marque de leur passage.
Par exemple: « Les alpinistes ont construit un cairn au sommet de la montagne. »""" },
{ "word": "Cake-walk", "definition": """Nom masculin.
Mot américain qui signifie marche du gâteau.
Danse syncopée d’origine afro-américaine, qui était à la mode en 1900.
Par exemple: « Le morceau « Golliwogg’s cake-walk » est un morceau pour
piano de Debussy. »""" },
{ "word": "Calandre", "definition": """Nom féminin.
Du grec »kalandros » qui signifie alouette à huppe.
1- Grande alouette du sud de l’Europe.
2- Charançon prédateur des grains de céréales.
Par exemple: »La calandre du blé. »""" },
{ "word": "Caléfaction", "definition": """Nom féminin.
Du latin « calefacere » qui signifie chauffer.
Deux définitions :
-Action de chauffer.
-Phénomène observé lorsque l’on projette une goutte de liquide sur une
plaque de métal brûlant: la goutte prend une forme sphérique.""" },
{ "word": "Calife", "definition": """Nom masculin.
De l’arabe « khalifa » qui signifie successeur.
Souverain musulman, successeur de Mahomet et investi de pouvoir
spirituel et temporel.""" },
{ "word": "Callipyge", "definition": """Adjectif.
Du grec « kallos »qui signifie beauté et « pugê » qui signifie fesses.
Se dit d’une personne qui a de belles fesses ou bien des fesses très
développées.
Au musée de Naples ses trouve une Vénus callipyge.""" },
{ "word": "Cambrousse", "definition": """Nom féminin.;
Du provençal « cambrousso » qui signifie valet, femme de chambre.
Dans un langage familier et péjoratif, se dit de la campagne.
Par exemple: »Ils se sont perdus en pleine cambrousse. »""" },
{ "word": "Camomille", "definition": """Nom féminin.
Du grec » khamaimêlon » de « khamai » qui signifie à terre, nain et
« mêlon » qui signifie pomme. La camomille a une odeur de pomme.
1- Plante herbacée aromatique de la famille des composées, dont les
capitules floraux sont utilisés pour leurs propriétés médicinales.
Par exemple: »La camomille est une plante qui a été décrite pour la
première fois par Pline l’Ancien. »
2- Infusion des fleurs de cette plante.
Par exemple: » j’ai bu une tasse de camomille. »
Il existe une grande confusion dans la nomenclature des camomilles. Il
y a trois sortes de camomille médicinales:
La camomille allemande, hongroise ou matricaire. Odeur de camphre.
Azurant optique, pour la blancheur du linge. Ravive la blondeur des
cheveux blonds.
La camomille romaine.  Odeur de pomme blette. Antioxydante. Tonique.
analgésique.
La grande camomille. Odeur d’herbe frottée entre les doigts.
Antispasmodique, immunostimulante.
Dans tous les cas elle est utilisée en infusion ou en huile
essentielle des principes actifs issus de la plante et concernés.""" },
{ "word": "Campêche", "definition": """Nom féminin.
Du nom de Campeche ville du Mexique, d’où partaient au XVIIème siècle,
les bois de teintures pour l’exportation.
Arbre de l’Amérique tropicale de la famille des cesalpinées qui
fournit un bois dur et compact renfermant une matière colorante rouge.
C’est le Bois de sang.
Par métonymie, le colorant rouge issu de l’arbre est appelé campêche
ou hématine.
Ce colorant est utilisé en cosmétologie et peut être mélangé au henné
dans des shampoings. Ce colorant module sa nuance de rouge selon le
milieu dans lequel il est employé.""" },
{ "word": "Camphre", "definition": """Npom masculin.
Du latin « camphora » issu de l’arabe « kafur » lui-même issu du
malais »kapur barus » qui signifie craie de Barus
Substance blanche et semi-transparente, à odeur très forte, de saveur
amère et brûlante que l’on extarit du camphrier.
Le camphre est aussi appelé bornéol, c’est une cétone terpénique
obtenue en distillant avec de l’eau le bois du camphrier: « Laurus
camphora ».
Propriétés pharmacologiques: analgésique. expectorant.
décongestionnant des voies respiratoires.""" },
{ "word": "Canicule", "definition": """Nom féminin.
De l’italien « canicula » qui signifie petite chienne appliqué à l’étoile Sirius.
Période de grande chaleur. L’étoile Sirius ou canicule se lève et se
couche avec le soleil du 22 juillet au 22 août.""" },
{ "word": "Cannaie", "definition": """Nom féminin.
De « canne » issu du latin « canna » qui signifie roseau.
Plantation de canne à sucre ou de roseaux.""" },
{ "word": "Canopée", "definition": """Nom féminin.
De l’anglais « canopy » qui signifie baldaquin. Canopy provient d’un mot
grec qui signifie moustiquaire par l’intermédiaire de « kounoupi » qui signifie moustique.
Se dit de la partie la plus haute des arbres dans la forêt tropicale
humide. Il y vit un grand nombre d’espèces. C’est un véritable écosystème.
La conopée est un mot à l’orthographe très voisine. C’est le tissu qui
est placé au-dessus du tabernacle dans une église.""" },
{ "word": "Cantharide", "definition": """Nom féminin.
Aussi appelée mouche d’Espagne ou mouche de Milan
Du grec « kantharis. » Etymologie inconnue.
Insecte coléoptère de couleur vert doré et brillant dont le corps
desséché et réduit en poudre contient un toxique nommé la cantharidine
anciennement utilisé comme aphrodisiaque.""" },
{ "word": "Capricant", "definition": """Adjectif.
Du latin « capra » qui signifie la chèvre.
Se dit d’un rythme inégal ou saccadé qui paraît sautiller comme
sautille une chèvre.
Un pouls peut être dit capricant.""" },
{ "word": "Capucinade", "definition": """Nom féminin.
De « capucin » apparenté à capuche et capuchon issu de l’italien
« cappucino » qui signifie capucin: personne qui porte un capuchon.
C’était  la coule particulièrement voyante portée par ce religieux
de la congrégation de l’Ordre des frères mineurs. 
Un capucin était aussi un homme qui prêchait une morale ou
une dévotion de manière affectée et ridicule.
Et « ade » issu de l’occitan « ada » par le latin « ata » qui exprime le
résultat accompli d’une action.
Discours plat ou acte de dévotion qui paraît ridicule et peu sincère.""" },
{ "word": "Cardamome", "definition": """Nom féminin.
Du latin « cardamomum » issu du grec « kardamomon » juxtaposition de
« kard » qui signifie cresson de jardin amer et « amômon » qui signifie
amome qui est le nom de genre de la plante.
Plante de la famille des zingibéracées qui donne l’épice -par sa
graine- du même nom.
La graine a une saveur poivrée aromatique, elle est utilisée dans les
currys indiens et dans l’hypocras, ce vin apéritif du Moyen-Âge.
La cardamome sert aussi à parfumer le pain d’épices.""" },
{ "word": "Cariatide", "definition": """Nom féminin.
Du grec « karuatides » qui signifie femme de Karyes, ville du Péloponnèse.
En architecture, se dit d’une statue de femme soutenant une corniche
sur sa tête et/ou sur ses épaules.
On peut observer des cariatides sur la façade de certains immeubles anciens.""" },
{ "word": "Carnotset", "definition": """Nom masculin.
Mot issu du patois vaudois, probablement du radical de de « caro » qui
signifie coin.
En Suisse, local aménagé dans une cave pour manger et boire entre amis.""" },
{ "word": "Carre", "definition": """Nom masculin.
De l’occitan « caire » qui signifie quartier de pierre, pierre de
l’angle, côté, issu du latin « quadrus » qui signifie  carré.
A- Avec l’idée de carré.
 1- Dans un sens vieilli. Stature, carrure.
Par exemple: »Ce judoka » a une belle carre. »
2- Dans un sens vieilli. Angle d’un objet, bout carré d’une chaussure,
angle droit.
B- Par métonymie. Avec l’idée dominante d’angle.
1- Angle que forme la face verticale d’un objet avec sa face horizontale.
    Par exemple: « Carre d’un chapeau. »
2- En escrime. Chacune des faces d’une lame d’épée.
3- En patinage. Déplacement en courbe.
4- Par extension en ski alpin(snowboard). Partie métallique située de
part et d’autre de la semelle des skis et qui permet qu’ils
s’accrochent dans la neige.
C-Par extension. Avec une idée de mise au carré puis de doublage.
1- Dans un sens vieilli. Cartes à jouer. Au jeu de la bouillotte. Mise
avec laquelle on se carre, c’est-à-dire lorsqu’on s’assure la priorité
en doublant la mise.
2- Par extension et dans une langue argotique. Masse des enjeux
représentant la contrepartie des jetons et plaques délivrée aux
participants d’une partie clandestine, au poker
ou au baccara.
7- En menuiserie. Épaisseur de bois méplate.
Par exemple: »Le carre des planches. »
Dans un numéro récent d’Ouest France ( juin 2017), je relève à propos
d’Emmanuel Macron qui a prononcé une phrase qui fait polémique.
« On a beau s’assurer de sa stature et de sa communication la faute de
carre est toujours possible. »
« La faute de carre » en ski alpin est une erreur consistant à perdre
l’équilibre suite à l’appui de la jambe sur la carre non porteuse.""" },
{ "word": "Casimir", "definition": """Nom masculin.
De « casinire » altération anglaise « cassimer » issue de « Cassimer » qui
est le nom anglais de la province de Cachemire.
Etoffe de laine croisée, fine et légère.""" },
{ "word": "Castine", "definition": """Nom féminin.
De l’allemand « kalkstein », formé de « Kalk » qui signifie chaux et de
« Stein » qui signifie pierre.
Pierre calcaire que l’on mélange au minerai de fer pour en faciliter la fusion.""" },
{ "word": "Castoréum", "definition": """Nom masculin.
Du latin médiéval « castoréum » de même signification. Issu de castor.
Substance huileuse, à odeur forte, issue des glandes sexuelles du
castor. Elle est utilisée dans les parfums de type ambré ou oriental.
Elle est aussi utilisée pour parfumer les cigarettes, ainsi que comme
ingrédient alimentaire.
En médecine, elle a des propriétés antispasmodiques.
Par exemple: « Le castoréum est l’une des six matières premières
animales de la parfumerie. « """ },
{ "word": "Castramétation", "definition": """Nom féminin.
Du latin « castrametatio » issu de « castra » qui signifie camp et
« metari » qui signifie mesurer.
Dans l’Antiquité, art de choisir et de disposer l’emplacement d’un camp.""" },
{ "word": "Casuarina", "definition": """Nom masculin.
Du latin « casoaris » issu de « casoar » à cause des rameaux plumeux de cet arbre.
Grand arbre d’Australie et de Malaisie de la famille des
casuarinacées, dont la morphologie à des caractères primitifs.
Il est appelé bois-de-fer à cause de la dureté de son bois.""" },
{ "word": "Catalectique", "definition": """Adjectif.
Du grec « katalêktikos » issu de « katalêgein » qui signifie finir.
En poésie, se dit d’un vers grec ou latin qui se termine par un pied
auquel il manque une syllabe.""" },
{ "word": "Catamnésie", "definition": """Nom féminin.
Du grec « cata » préfixe qui marque la référence à et « mnesis » issu du
radical « mimnêsko » qui signifie « je me souviens ».
En médecine, renseignements concernant l’évolution du malade et de ses
symptômes à la suite de son traitement.""" },
{ "word": "Catatonie", "definition": """Nom féminin.
Du grec « kata » qui signie en desous et « tonos » qui signifie tension.
En psychiatrie, état instable qui alterne apathie et ‘excitation et
qui caractérise souvent la schizophrénie.""" },
{ "word": "Cathèdre", "definition": """Nom féminin.
Du latin « cathedra » qui signifie chaise à dossier; chaire.
Chaise gothique à haut dossier.""" },
{ "word": "Cauri", "definition": """Nom masculin.
Du sanskrit « kaparda » par l’hindi ou le tamoul « kauri » et l’anglais
« cowry » qui signifie cypréidé.
Petit mollusque gastéropode de la famille des cypréidés. C’est un
coquillage du groupe des porcelaines, dans l’océan indien et dans
l’océan pacifique tropical.
Anciennement, il était utilisé comme monnaie en Asie, en Afrique et en Océanie.
Il est aujourd’hui utilisé en décoration et comme objet divinatoire.""" },
{ "word": "Causinomancie", "definition": """Nom féminin.
Du grec « kaus » qui signifie brûler et « manteia » qui signifie divination.
Mode de divination par le feu qui consistait à interpréter la façon
dont brûlaient des objets jetés dans les flammes.""" },
{ "word": "Cavatine", "definition": """Nom féminin.
De l’italien « cavatina » issu de « cavata » qui signifie « action de tirer
un son » par « cavare » qui signifie creuser, graver.
En musique.
1- Dans les opéras ou les oratorios, pièce vocale assez courte,chantée
par un soliste. A l’origine elle était un prolongement plus mélodique
du récitatif accompagné, avant l’air
proprement dit. Par la suite, elle fut placée entre l’air et l’arioso,
et utilisée comme air de présentation.
Par exemple: La cavatine « Salut demeure chaste et pure dans Faust de Gounod.
2- Pièce instrumentale très mélodique, sans développement.
Par exemple: »La cavatine du 13ème quatuor de Beethoven. »
Rimbaud utilise le terme « cavatine » dans son poème: « On n’est pas
sérieux quand on a dix-sept ans. »
… »Sur vos lèvres alors meurent les cavatines »…""" },
{ "word": "Céladon", "definition": """Nom masculin et adjectif invariable.
Nom d’un personnage de l’Astrée, type d’amoureux platonique.
Le vert céladon est un vert pâle.
De manière elliptique. Par exemple: « Une robe céladon. »
La porcelaine céladon ou de manière elliptique un céladon est une
porcelaine chinoise recouverte d’émail craquelé, le plus souvent vert
pâle.""" },
{ "word": "Cenelle", "definition": """Nom féminin.
Du latin « acinella » issu de « acinus » qui signifie grain de raisin.
Baie rouge de l’aubépine et du houx.
Au Canada, l’aubépine se dit cenellier ou senellier.""" },
{ "word": "Cénésthésie", "definition": """Nom féminin.
Du grec « koinos » qui signifie commun et « aisthesis » qui signifie sensibilité.
Impression générale d’aise ou de malaise qui provient de sensations internes.""" },
{ "word": "Cénobite", "definition": """Nom masculin.
Du latin « cenobita », lui-même issu de « cœnobium » qui signifie monastère.
Religieux qui vivait en communauté dans les premiers temps de l’ère chrétienne.""" },
{ "word": "Cens", "definition": """Nom masculin.
Du latin « census » qui signifie recensement.
Ce mot a un sens historique.
1- Dans l’Antiquité, dénombrement des citoyens romains et évaluation
de leur fortune qui étaient effectués tous les cinq ans.
2- A l’époque féodale, redevance fixe que le possesseur d’une terre
payait au seigneur du fief.
3- En France, jusqu’en 1848 -où il fut abrogé- quotité d’imposition
nécessaire pour être électeur ou éligible. On disait: »Le cens
électoral. »""" },
{ "word": "Cérame", "definition": """Nom masculin.
Du grec « keramon » qui signifie argile.
En archéologie, vase grec en terre cuite.
En tant qu’adjectif. Le grès cérame est un grès cuit jusqu’à la vitrification.""" },
{ "word": "Cerfeuil", "definition": """Nom masculin.
Du grec « khairephullon » issu de « khairein qui signifie se réjouir,
être joyeux, aimer à  et « phullon » qui signifie feuille. Littéralement
le nom de la plante signifie « feuille de la joie » en référence aux vertus
d’une de ses variétés les plus communes: le cerfeuil fait partie des fines herbes.
Herbe potagère de la famille des apiacées ou ombellifères dont les
feuilles sont utilisées comme condiment. Son nom scientifique est
« Anthriscus cerefolium »
Elle est originaire de Russie méridionnale et fut introduite en Europe
par les Romains. Son goût est légèrement anisé.
Plante qui ressemble au persil, à ne pas confondre avec la petite
ciguë, qui n’a pas la même odeur agréable.
Le cerfeuil présenté un taux élevé de fer et de calcium et préserve de
l’anémie.
Dans le calendrier républicain français, le 19 ème jour du mois de
ventôse était officiellement nommé le jour de cerfeuil.""" },
{ "word": "Cespiteux", "definition": """Adjectif.
Du latin cespes, cespitis qui signifie touffe, gazon.
Se dit d’un végétal qui croit en touffes compactes.
Des plantes cespiteuses.""" },
{ "word": "Cespiteux", "definition": """Adjectif.
Du latin « cespes, cespitis » qui signifie touffe, gazon.
Se dit d’un végétal qui pousse en touffes compactes.""" },
{ "word": "Cétérach", "definition": """Nom masculin.
De l’arabe « sitrak » qui désigne la plante.
Fougère de la famille des aspléniacées, aux feuilles persistantes, en
lobes formant des rosettes denses sur les murs, enroulées pour
s’adapter à la sécheresse.""" },
{ "word": "Cétoine", "definition": """Nom féminin.
Mot d’origine inconnue.
Insecte coléoptère de la famille des scabéréidés aux vives couleurs
métalliques. La cétoine dorée est dite hanneton des roses.""" },
{ "word": "Chahuter", "definition": """Verbe.
D’origine inconnue peut-être d’origine dialectale. A rapprocher de
« cahuer » qui signifiait huer et de « cahuler » qui signifiait crier de
douleur.
1- En tant que verbe transitif :
Danser le chahut, en s’agitant et en criant. danse populaire
désordonnée et indécente qui était à la mode entre 1830 et 1850.
Faire du chahut à l’école.
Chahuter avec quelqu’un.
2- En tant que verbe intransitif.
Chahuter un professeur. . Bavarder pendant son cours.
Participe passé, adjectif.
Chahuter quelqu’un.
Bousculer pour rire.""" },
{ "word": "Chancel", "definition": """Nom masculin.
Du latin « cancelli » qui signifie treillis, barrière ou balustrade.
Clôture basse située en avant du chœur qui existait dans les églises
paléochrétiennes.""" },
{ "word": "Chandeleur", "definition": """Nom féminin.
Du latin « candelarum » issu de l’expression « festa candelarum » qui
signifie fête des chandelles.
Dans la religion catholique, fête de la présentation de Jésus-Christ
au Temple et de la purification de la Vierge Marie, qui a lieu le 2
février.""" },
{ "word": "Chauvir", "definition": """Verbe intransitif sauf aux personnes du singulier au présent de
l’indicatif et de l’impératif.
Du latin « cavannus » qui signifie chouette.
Chauvir des oreilles, les dresser en parlant de l’âne, du mulet, du cheval.
Exemples: Il chauvit. Ils chauvent des oreilles.""" },
{ "word": "Cheire", "definition": """Nom féminin. 
Terme auvergnat. 
À rapprocher de l’ancien rouergat « quier » qui signifie tas de pierre ou du forezien « cher » qui signifie amoncellement de pierres. 
Du latin « kerus » issu de la racine prê Indo européenne « kar(r) » qui signifie pierre.
Dans le Massif central coulée de laves scoriacées, constituant un terrain hérissé, rugueux et infertile.""" },
{ "word": "Chelem", "definition": """Nom masculin.
De l’anglais « slam » qui signifie écrasement.
Réunion dans la même main, de toutes les levées dans certains jeux de cartes.
Expression utilisée dans le sport: grand chelem, série de victoires en
tennis ou en rugby.""" },
{ "word": "Chélicère", "definition": """Nom féminin.
Du latin chelicera issu du grec « khêlé » qui signifie pince et « keras »
qui signifie corne.
En zoologie, nom de l’appendice céphalique des arachnides et des limules;
crochet des araignées et pince des scorpions.""" },
{ "word": "Chélidoine", "definition": """Nom féminin.
Du grec « kelidonia » issu de « khelidôn » qui signifie hirondelle. La
floraison de cette plante coïncide avec l’arrivée des oiseaux
migrateurs que sont les hirondelles.
L’étymologie populaire qui aurait voulu donner comme origine « cœli
donum » ou don du ciel, ne doit pas être retenue.
Selon certaines sources, le nom de cette plante serait dû au fait que
les hirondelles frottent les yeux de leurs petits avec des fragments
de cette plante pour les ouvrir.
Le latex caustique permettrait l’ouverture de l’ourlet de peau chez
les petites hirondelles.
En botanique, plante de la famille des papavéracées, appelée aussi
grande éclaire, herbacées à fleurs jaunes dont le latex jaune-orangé
toxique passait pour guérir les verrues.
Par exemple: »La chélidoine est aussi appelée l’herbe aux verrues. »""" },
{ "word": "Chérif", "definition": """Nom masculin.
De l’arabe « charif » qui signifie noble.
Se dit d’un prince chez les arabes.""" },
{ "word": "Chiasme", "definition": """<!--
@page { margin: 2cm } 		P { margin-bottom: 0.21cm }
-->
Nom masculin.
Ce mot vient du grec khiazein, disposer en forme de Khi c’est-à-dire de X.
Procédé littéraire ou poétique qui consiste en un croisement de termes.
Deux procédés sont à l’œuvre dans cette figure de style la répétition et l’inversion.
Dans la répétition il y a deux éléments de langage qui sont répétés.
L’inversion fait que là ou un parallélisme procèderait du même ordre AB/AB un renversement de la symétrie a lieu et fait aboutir à AB/BA.
En poésie voici un exemple de chiasme grammatical qui est le chiasme que l’on rencontre le plus fréquemment.
« Sous le sombre sommeil d’une terre première » Mallarmé
                     adjectif    nom                       nom  adjectif
Il y a un chiasme dans l’expression familière Blanc bonnet, bonnet blanc.""" },
{ "word": "Chignon", "definition": """Nom masculin.
De « châaignon » qui signifie nuque. Issu du latin « catenio » qui
signifie chaîne de vertèbres, par le latin « catena » qui signifie
chaîne.
Coiffure consistant à relever sa chevelure sur ou derrière la tête.""" },
{ "word": "Chimère", "definition": """Nom féminin.
Du grec « khimaira » qui signifie « la Chimère » monstre mythologique.
1- En mythologie. Monstre à tête et poitrail de lion, ventre de chèvre
et queue de dragon.
2- Au sens figuré. Vaine imagination. Illusion.
3- En zoologie; Poisson marin cartilagineux de la famille des
holocéphales aux dents broyeuses et qui a un aiguillon qui est parfois
venimeux.
4- En biologie. organisme créé artificiellement par greffe ou par
fécondation, à partir de deux cellules ou deux embryons ou deux
organes dont les patrimoines génétiques sont différents.""" },
{ "word": "Chiton", "definition": """Nom masculin.
Du grec « chitôn » qui signifie tunique.
1- Dans l’antiquité, tunique grecque.
2- Mollusque allongé de la famille des amphineures, qui adhère aux
rochers et aux coquilles grâce à son pied large et plat.""" },
{ "word": "Chlamyde", "definition": """Nom féminin.
Du latin « chlamys-chlamydis » qui signifie manteau luxueux, issu du
grec « khlamus » qui signifie casaque de chevalier ou manteau militaire.
En Grèce antique, manteau léger, court et fendu, agrafé sur l’épaule droite.""" },
{ "word": "Chleuasme", "definition": """Nom masculin.
Du grec « chleuasmos » qui signifie ironie, sarcasme.
Ironie tournée vers soi. Moquerie, persifflage, sarcasme dont on fait
soi-même les frais, mais en attendant de son interlocuteur au moins un
geste de protestation.
Par exemple: « Suis-je bête! ».""" },
{ "word": "Chorten", "definition": """Nom masculin.
Du tibétain « mch’od-rten ».
Monument religieux des lamas tibétains.""" },
{ "word": "Chott", "definition": """Nom masculin.
De l’arabe « chatt » qui signifie rivage.
En Afrique du Nord, lac salé aux rivages changeants situé dans des
régions semi-arides.
Par exemple, le « Chott El-Jérid » est un lac situé en Tunisie entre la
mer et le désert.""" },
{ "word": "Chrematistique", "definition": """Nom féminin.
Du grec « chrematistikos » qui signifie qui concerne la gestion ou la
négociation des affaires surtout d’argent. De « chrèmata »  qui signifie
richesse ou deniers.
Notion créée par Aristote pour décrire l’accumulation de monnaie pour
elle-même et pour son propre plaisir.
Aristote condamne cette attitude.""" },
{ "word": "Chrême", "definition": """Nom masculin.
Du grec « khrisma » qui signifie huile.
Huile consacrée, utilisée dans les onctions pour certains sacrements
et certaines cérémonies des églises catholiques et orthodoxes.
Par exemple: « On lui appliqua le Saint Chrême ».""" },
{ "word": "Chrysocale", "definition": """Nom masculin.
Du grec « chryso » qui signifie or et « khalkos » qui signifie cuivre.
Alliage de cuivre, d’étain et de zinc qui imite l’or.""" },
{ "word": "Chyle", "definition": """Nom masculin.
Du latin « chylus » issu du grec « khulos » qui signifie suc.
En physiologie, liquide d’aspect laiteux résultant de la
transformation dans l’intestin des aliments mélangés aux sucs
digestifs, qui est absorbé par les vaisseaux lymphatiques.""" },
{ "word": "Ciboire", "definition": """Nom masculin.
Du grec « kibôrion » qui signifie fruit du nénuphar d’Egypte.
Vase sacré en forme de coupe où l’on conserve les hosties consacrées
pour la communion des fidèles.""" },
{ "word": "Cicérone", "definition": """Nom masculin.
De l’italien « cicerone » issu de Cicéron. par allusion à la verbosité
des guides italiens.
Dans un sens vieilli ou plaisant, guide appointé qui explique aux
touristes les curiosités d’une ville, d’un musée ou d’un monument.
L’expression « jouer le cicerone » signifie faire le guide pour
quelqu’un dans certaines circonstances.""" },
{ "word": "Cicindèle", "definition": """Nom féminin.
Du latin « cicindela » issu de « candere » qui signifie briller.
Dans un langage vieilli, ver luisant.
Dans une langue moderne, insecte coléoptère carnassier de la famille
des cicindélidés.""" },
{ "word": "Cilice", "definition": """Nom masculin.
Du latin « cilicium » qui signifie étoffe en poil de chèvre de Cilicie.
Chemise ou ceinture de crin ou d’étoffe rude et piquante, portée par
pénitence ou par mortification.
Par exemple: « Ce pécheur a pris le cilice. »""" },
{ "word": "Cîme", "definition": """Nom féminin.
Du latin « cyma » qui signifie pousse, issu du grec « kuma » qui signifie
ce qui est gonflé.
1- Extrémité pointue d’un arbre, d’un rocher, d’une montagne.
Par exemple: « L’oiseau s’envola, jusqu’à la cîme de l’arbre. »
2- Dans un sens figuré mais vieilli, Ce qu’il y a de plus élevé, de plus noble.
Par exemple: « A la cîme des honneurs. »""" },
{ "word": "Cipaye", "definition": """Nom masculin.
Du portugais « cipay » lui-même issu du persan « sipahi » qui signifie
cavalier. A rapprocher de « spahi ».
Anciennement, soldat hindou au service d’une armée européenne.""" },
{ "word": "Cipolin", "definition": """Nom masculin.
De l’italien « cipollino » issu de « cipolla » qui signifie oignon.
Calcaire métamorphique dans lequel courent des veines serpentines.
Par extension, marbre clair formé de cristaux de calcites enchevêtrés,
homogène ou à veines ondulées.""" },
{ "word": "Circaète", "definition": """Nom masculin.
Du grec « kirkos » qui signifie faucon et « aetos » qui signifie aigle.
Oiseau rapace diurne de la famille des falconidés. Il est aussi appelé
aigle-jean-le-blanc et milan blanc.""" },
{ "word": "Cirrus", "definition": """Nom masculin.
Mot latin qui signifie filament.
Nuage d’altitude (10 km) qui se présente en flocons ou en filaments.""" },
{ "word": "Cistre", "definition": """Nom masculin.
Du latin « cithara » qui donna « citre » puis devint « cistre » par
confusion avec « sistre » (autre instrument de musique).
Instrument de musique à cordes pincées, analogue à la mandoline et qui
était en usage aux XVIème et XVIIème siècle.""" },
{ "word": "Clastique", "definition": """Adjectif.
Du grec « klastos » qui signifie brisé.
1- En géologie, qui présente des traces de fracture provoquées par l’érosion.
Par exemple: « C’est une roche clastique ».
2- En médecine, se dit de pièces anatomoiques artificielles démontables.""" },
{ "word": "Clathre", "definition": """Nom masculin.
Du latin « clathri » qui signifie barreau en raison de sa forme.
Champignon du genre Clathrus de la famille des phallaceae, qui
comporte le clathre rouge. .
Celui-ci, se présente sous la forme d’une lanterne grillagée aux
mailles polygonales, irrégulières, allongées, rouge-corail puis
orangées.
Sa toxicité n’est pas démontrée. il est pourtant délaissé par les
ramasseurs de champignons.
Il était utilisé au Moyen-Âge par les sorciers et les jeteurs de sort.
Par exemple: »Le clathre est fréquent dans le sud de la France. »""" },
{ "word": "Climactérique", "definition": """Adjectif masculin ou féminin.
Du latin « climax » qui signifie en écologie un état stable et abouti.
1- En botanique, se dit d’un fruit sensible à une certaine hormone
végétale: l’éthylène.
Chez les plantes climactériques cette phytohormone provoque la
maturation des fruits qui n’ont pas été cueillis à maturité.
Les pommes, les poires, les bananes, les avocats et les melons sont des
fruits climactériques. Ce que ne sont pas les fraises, les cerises
et les agrumes.
Cette définition n’est pas complètement satisfaisante compte tenu de
nouvelles avancées scientifiques. en voici deux exemples: il existe en
effet des melons non climactériques et pour le raisin la sensibilité
à l’éthylène varie au cours de sa maturation.
2- En astrologie, se dit d’un âge ou d’une année critique où le corps
s’altère et où les risques de maladie seraient accrus.""" },
{ "word": "Climatère", "definition": """Nom masculin.
Du grec « klimaktêr » qui signifie étape, échelon.
En médecine, étape de la vie, appelée aussi âge critique, marquant la
fin de l’activité des hormones sexuelles chez la femme (ménopause)
et chez l’homme (andropause).""" },
{ "word": "Cluse", "definition": """Nom féminin.
Du latin « clusa » issu de clausa  par « claudere » qui signifie fermer.
Géographie régionale. Dans le Jura, coupure étroite et encaissée,
creusée perpendiculairement à une chaîne de montagnes.
Par exemple, la cluse de Nantua.""" },
{ "word": "Cluster", "definition": """Nom masculin.
Mot anglais qui signifie agglomérat.
Groupement d’un petit nombre d’objets.
Par exemple: « Un cluster d’étoiles ».
Le cluster d’un A.D.N est la répétition de la même séquence de nucléotides.
En musique, résonnance de plusieurs notes jouées simultanément avec le
poing, la paume ou l’avant-bras.""" },
{ "word": "Clystère", "definition": """Nom masculin.
Du grec « klyzein » qui signifie laver.
Dans un sens vieilli, lavement administré avec une seringue ou bien
seringue de grosse taille.""" },
{ "word": "Cnémide", "definition": """Nom féminin.
Du grec « knemis » qui signifie jambière.
Dans l’Antiquité, jambière des soldats grecs.""" },
{ "word": "Cnidaire", "definition": """Nom masculin.
Du latin « cnide » qui signifie ortie de mer avec le suffixe -aire du
latin « -arius » ou « -aris » qui signifie qui se rapporte à.
1- Métazoaire aquatique,relativement simple, à symétrie radiale,
comportant une cavité interne avec un orifice unique faisant office de
bouche et d’anus et  des tentacules portant des cnidocytes.
C’est l’embranchement d’animaux diploblastiques munis de cellules
urticantes dites nématocystes.
Cet embranchement comprend les classes des hydrozoaires, dont l’hydre
fait partie, des anthozoaires, dont l’anémone de mer, le corail et les
madrépores font partie, et des acalèphes dont les grandes méduses font partie.
Par exemple: »Les cnidaires sont aussi appelés des cœlentérés. »""" },
{ "word": "Coalescence", "definition": """Nom féminin.
Du latin « coalescere » qui signifie croître avec.
1- En biologie, soudure de deux surfaces tissulaires en contact l’une
de l’autre. Par exemple les deux lèvres d’une plaie.
2- En chimie, état des particules liquides en suspension réunies en
gouttelettes plus grosses.
3- En linguistique, contraction de deux ou plusieurs éléments
phoniques en un seul. par exemple, en anglais le mot  » to sing » qui
signifie chanter, a perdu son g dans la langue moderne pour donner to sin.""" },
{ "word": "Colin", "definition": """Nom masculin.
A- Altération d’après « Colin » diminutif de Nicolas. Du moyen français
« cole », néerlandais « cool(vish) », anglais « coal(fish), qui signifient
poisson-charbon
en raison de la couleur de son dos.
1- Poisson de mer appelé aussi lieu noir.
2- Dans certaines régions, c’est le merlu.
B- De « Colin » diminutif de Nicolas.
Oiseau d’Amérique du Nord de la famille des galliformes, assez
semblable aux petits gallinacées.
Par exemple: »Le colin de Virginie. »""" },
{ "word": "Colocase", "definition": """Nom féminin.
Du latin « colocasia », lui-même issu du grec ancien « kolokasia » qui
désignait la racine d’une plante égyptienne.
En botanique plante exotique de la famille des Aracacées, Colocasia
antiquorum dont le rhizome comestible, « le taro » fournit une farine
riche en amidon.
Cette plante pousse au Sud-Est asiatique, du Myanmar à la Papouasie
Nouvelle-Guinée.
De nombreux synomymes de ce mot existent selon la situation
géographique de la plante.
Taro
Tarro.
Arouille violette: Réunion et Ile Maurice.
Songe; Réunion et Ile Maurice.
Chou de Chine: Guyane, Martinique, Guadeloupe.
Dachine: Guyane, Martinique, Guadeloupe.
Madère, Guyane, Martinique, Guadeloupe.""" },
{ "word": "Colophane", "definition": """Nom masculin.
Du latin « colophonia » d’origine grecque. « Résine de Colophon » du nom
d’une ville de Lydie: ancien pays d’Asie mineure sur la mer Egée qui
fit partie de la Grèce antique.
Cette résine est tirée de la distillation de la térébenthine. On en
frotte les crins des archets des instruments à cordes.""" },
{ "word": "Colophon", "definition": """Nom masculin.
Du latin « colophon » emprunté au grec « kolophôn » qui signifie faîte,
sommet. Au figuré signifie couronnement, achèvement.
Colophon était une ancienne cité grecque d’Ionie en Asie mineure
située au nord-est d’Ephèse. Son nom a donné naissance au terme
d’imprimerie. Les ruines de l’antique cité se trouvent près d’Izmir en Turquie.
1- En imprimerie, note finale d’un manuscrit ou d’un livre comportant
le nom de l’auteur, la date ainsi que d’autres renseignements faisant
partie du paratexte.
Par exemple: « Le colophon des livres anciens d’avant l’imprimerie est
l’ancêtre de l’achevé d’imprimer moderne. « """ },
{ "word": "Comblanchien", "definition": """Nom masculin.
Du nom d’un village, situé en Côte-d’Or dans l’arrondissement de Beaune.
Calcaire dur extrait des falaises locales et que l’on utilise en
construction et en décoration.
Par exemple: »Une terrasse en comblanchien. »""" },
{ "word": "Comminatoire", "definition": """Adjectif.
Du latin « comminatorius », issu de « minari » qui signifie menacer.
En droit, se dit de ce qui renferme la menace d’une peine légale, en
cas de contravention.
Couramment, se dit de ce qui est menaçant.
Par exemple, un ton comminatoire.""" },
{ "word": "Compendium", "definition": """Nom masculin.
Du latin « compendium » qui signifie abréviation.
Se dit d’un abrégé, d’un résumé ou d’un condensé.""" },
{ "word": "Concaténation", "definition": """Chaîne.
Enchaînement de termes.
Par exemple : une phrase est une concaténartion de mots. (les mots d’une
phrase se suivent les uns les autres.)""" },
{ "word": "Congruence", "definition": """Nom féminin.
Du latin « congruens » participe présent de « congruere » qui signifie convenir.
1- Se dit de ce qui convient, qui s’applique bien.
Par exemple: « Une solution congruente au problème posé », c’est une solution adaptée.
2- En mathématiques, des figures congruentes sont égales.""" },
{ "word": "Conirostre", "definition": """Adjectif et nom.
Du latin « conus » qui signifie cône et « rostrum » qui signifie bec.
En zoologie se dit d’un oiseau qui a le bec court et conique.
Le bouvreuil mais aussi certains passereaux sont conirostres.""" },
{ "word": "Contingence", "definition": """Nom féminin.
Du latin « contingere » qui signifie arriver par hasard.
1-Caractère de ce qui est contingent: éventualité, possibilité qu’un
évènement puise ou non se produire. Par opposition à un évènement
dont la survenue serait nécessaire.
2-Lorsqu’il est employé au pluriel: contingences.
Evènements imprévisibles ou fortuits.""" },
{ "word": "Contumax", "definition": """Nom masculin.
Mot latin qui signifie fier, obstiné, rebelle. Issu du préfixe latin
« cum- » qui signifie avec et du verbe « tumere » qui signifie être gonflé
(d’orgueil par exemple).
En droit, se dit d’un accusé en état de contumace, c’est à dire absent
ou défaillant.""" },
{ "word": "Coquecigrue", "definition": """Nom féminin.
De coq-grue croisé avec cigogne.
1- Animal fantastique et imaginaire à la fois extraordinaire et drôle.
2- Sottise, absurdité.""" },
{ "word": "Coracle", "definition": """Nom masculin.
Du gallois « corwgl ».
Type primitif de bateau, très léger de forme ronde ou ovale. Il est
constitué de tissu ou de peau tendu sur un cadran de vannerie et
goudronné pour assurer l’étanchéité.
Cette embarcation est encore utilisée dans certaines régions du monde.
Il est évoqué dans les textes anciens. On le mentionne dans une
tablette Mésopotamienne, de 3700 ans, qui décrit l’arche dans le mythe
Babylonien du déluge, antérieur à l’écriture dans la Bible du mythe de Noé.""" },
{ "word": "Corégones", "definition": """Nom masculin pluriel.
Du grec » koré » qui signifie pupille et « gonia » qui signifie angle.
Genre de poissons des lacs du Nord de l’Eurasie et de l’Amérique de la
famille des salmonidés. Ils sont très répandus et appréciés pour leur
chair ferme.
Par exemple: « Le lavaret appartient aux corégones. »""" },
{ "word": "Corindon", "definition": """Nom masculin.
Du tamoul « kuruntam » qui signifie rubis.
Alumine cristallisée, pierre très dure à usages industriels. Elle
possède des variétés colorées de toutes les nuances, du blanc au bleu
et au rouge qui sont utilisées en joaillerie.""" },
{ "word": "Coryphée", "definition": """Nom masculin.
Du grec « koruphatos » issu de « koruphê » qui signifie sommet de la tête.
1- Dans le théâtre antique, chef du chœur.
Par exemple: »Le coryphée se plaçait au centre de la scène. »
2- Personne qui tient le premier rang dans un parti, une secte, une société.
3- Deuxième des cinq échelons dans le corps de ballet de l’Opéra de Paris.""" },
{ "word": "Coryza", "definition": """Nom masculin.
Du latin « koruza » qui signifie écoulement nasal.
En médecine, inflammation de la muqueuse des fosses nasales. On peut
dire aussi rhume de cerveau.""" },
{ "word": "Cothurne", "definition": """Nom masculin.
Du latin « cothurnus » qui signifie cothurne, chaussure montante.
1- Dans l’Antiquité, chaussure montante à semelle très épaisse, portée
par les comédiens du théâtre antique.
2- En littérature, symbole du genre tragique par opposition à des
socques ou des brodequins.""" },
{ "word": "Cotidal", "definition": """Adjectif.
Du latin « cum » qui donne le préfixe -co qui signifie réunion,
adjonction, simultanéité  et de l’anglais « tide » qui signifie marée.
Une ligne ou une courbe cotidale est une ligne passant par les points
où la marée à lieu à la même heure.""" },
{ "word": "Coufique", "definition": """Adjectif.
De Coufa ou Kûfa, ville d’Irak.
L’écriture coufique, était utilisée par les Arabes avant le quatrième
siècle de l’hégire.""" },
{ "word": "Courson", "definition": """Nom masculin.
De « (a)corcier » qui signifie raccourcir.
En arboriculture, branche d’arbre fruitier taillée court afin que la
sève s’y concentre.""" },
{ "word": "Couscous", "definition": """Nom masculin.
Du berbère « rac keskes » qui signifie broyer menu. Ce terme aurait
donné par déviation phonétique « ksekou » puis « keuscass » puis « koscossou »
et ensuite « kouskoussoum ».
1- Semoule de blé dur
2- Plat issu du Maghreb composé de semoule roulée en grains et cuite
au moins deux fois à la vapeur. On le sert avec de la viande ou du poisson,
des légumes et des sauces relevées.""" },
{ "word": "Crase", "definition": """Nom féminin.
Du grec « krasis » qui signifie mélange.
1- Contraction des syllabes,- initiale et finale-, de deux mots joints.
Par exemple: Burkini est composé de la contraction de « BURqua » et « biKINI »
2- En médecine, la crase sanguine est l’étude des propriétés
coagulantes du sang.
Dans un sens vieilli, composition des humeurs organiques.""" },
{ "word": "Créophage", "definition": """Adjectif.
Du grec creos chair et phagein manger
Se dit d’un animal qui se nourrit de chair. Synonyme de carnivore.""" },
{ "word": "Créosote", "definition": """Nom féminin.
Du grec « kreas » qui signifie chair et « sôzein » qui signifie conserver.
Mélange huileux de phénols et de crésols obtenu par distillation des
goudrons de bois comme le hêtre ou le bouleau. Ce composé protège des parasites.""" },
{ "word": "Csardas", "definition": """Nom féminin.
Du hongrois « csarda » qui signifie auberge.
Danse de couple d’origine hongroise. On la retrouve dans toutes les
régions où vivent des hongrois: Hongrie, Slovaquie, Ukraine, Roumanie,
Vojvodine, Croatie, Slovénie et Autriche.
Le pas de base de la csardas est proche des anciens branles. il est
formé de pas latéraux à gauche et à droite où le couple se déplace
soit ensemble -c’est-à-dire en miroir- soit du même pied sur un petit cercle.
En général, deux pas à droite suivis de deux pas à gauche constituent une unité,
mais il existe de nombreuses variantes.
L’influence des csardas se retrouve même en danse classique. ainsi,
Marius Petipa célèbre chorégraphe a intégré à certains de ses ballets
des passages dits « folkloriques ».
On retrouve des csardas dans Le lac des Cygnes de Piotr Tchaïcovski.
Par exemple: « La Csardas de Vittorio Monti est une pièce musicale très célèbre. »""" },
{ "word": "Culière", "definition": """Nom féminin.
Du latin « culus » qui signifie cul.
Sangle qui est attachée à la naissance de la queue du cheval et qui
tient le harnais.""" },
{ "word": "Curaçao", "definition": """Nom masculin.
A l’origine nom d’une île des Antilles qui fait partie des
Iles-Sous-le-Vent et appartient aux Antilles Néerlandaises en tant
qu’état indépendant. Elle est située au large du Venezuela dans la mer
des Caraïbes.
L’île aurait été nommée Ile Corazon, l’ile cœur. Ce mot retranscrit
par les cartographes portugais serait devenu curaçau, puis curaçao.
Liqueur fabriquée à partir d’eau de vie, de l’écorce d’une petite
orange amère appelé bigarade et de sucre.
Elle est titrée entre 20° et 40°. Sa couleur peut être orange, rouge,
ambrée ou verte. Mais le plus souvent elle est d’un bleu brillant
grâce à l’ajout de colorant FCF ou E 133 qui est le trianyl méthane. 
Elle entre dans la composition de nombreux cocktails et a la particularité
de colorer les urines.""" },
{ "word": "Curcuma", "definition": """Nom masculin.
Curcuma vient de l’espagnol mais est issu de l’arabe « kourkoum » qui
signifie safran.
Grande herbe vivace appartenant aux zingiberacées et qui est appelée
aussi safran des Indes. Sa tige souterraine contient une matière
colorante jaune appelée curcuminequi entre dans la composition du curry.
Il est utilisé comme épice.
Il est à ce jour connu comme le plus puissant des anti-inflammatoires.""" },
{ "word": "Curule", "definition": """Adjectif.
De « sella curulis » siège curule du latin « currus » qui signifie chariot.
Tabouret formé de deux pieds entrecroisés sur lequel est tendu un
morceau de tissu.
La chaise curule était un siège d’ivoire réservés aux premiers
magistrats de Rome""" },
{ "word": "Cyanotype", "definition": """Nom masculin.
Du grec « kuanos » qui signifie bleu et « du latin « typus » lui-même issu
du grec « tupos » qui signifie empreinte, marque.
Procédé photographique monochrome et négatif, ancien, qui permet
d’obtenir un tirage photo bleu de Prusse ou bleu cyan.
Deux produits chimiques sont utilisés dans ce procédé:
– Le citrate d’ammonium ferrique qui est vert ou brun.
– Le ferricyanure de potassium qui est rouge.
Ce procédé fut utilisé pour la première fois par la botaniste Anne
Atkins « 1799-1871 » dans son livre: « British Algae ».""" },
{ "word": "Cyprine", "definition": """Nom féminin.
Du grec « Kupris » surnom d’Aphrodite.
Sécrétion vaginale. Signe physique de désir sexuel.
Par exemple: « L’écoulement de la cyprine.""" },
{ "word": "Dague", "definition": """Nom féminin.
Du provençal « daga » peut-être issu du latin populaire « Daca [spatha] »
qui signifie [épée] de Dacie. La Dacie étant la Moldavie et La
Valachie actuelles.
Mais le fait que « Daca spatha » ne soit pas attesté en latin (ce serait
plutôt « dacia »)  on recherche encore un étymon celte hypothétique pour
ce mot.
1- Épée courte que l’on portait au côté droit.
2- En vènerie, défense de sanglier.
Premiers bois en forme de petites cornes courbes et unies que portent
les cerfs et les daims vers leur deuxième année.""" },
{ "word": "Daguet", "definition": """Nom masculin.
De « dague ».
Jeune cerf ou jeune daim qui est dans sa deuxième année et dont les
dagues poussent""" },
{ "word": "Danaïde", "definition": """Du grec « Danaïdes ». Dans la  mythologie grecque, les Danaïdes sont les
cinquante filles du roi Danaos, roi de Lybie.
Pour éviter que ne se réalise un oracle qui prédisait qu’elles
seraient tuées par leurs époux, elles tuèrent leurs cousins qu’elles
venaient tout juste d’épouser.
Elles furent condamnées aux Enfers, à remplir sans fin un tonneau troué.
Le tonneau des Danaïdes désigne une tâche absurde sans fin ou impossible.
En zoologie, genre de papillon diurne des tropiques qui possède des
couleurs éclatantes: Ailes jaune vif à bordure noire et taches
blanches.
Par exemple: »La danaïde est un grand paillon nymphalidé. »""" },
{ "word": "Daphné", "definition": """Nom féminin.
Du grec »daphnê » qui signifie laurier.
En botanique, arbrisseau des terrains calcaires, à feuilles
persistantes et à floraison rose ou blanche.""" },
{ "word": "Darique", "definition": """Nom féminin.
De Darius roi de Perse.
Monnaie d’or des anciens Perses.""" },
{ "word": "Darse", "definition": """Nom féminin.
Du génois « darsena », issu de l’arabe « dâr-sinâ’a » qui signifie maison
de travail.
Dans un port méditerranéen, se dit d’un bassin abrité.""" },
{ "word": "Décidu", "definition": """Adjectif.
Du latin « decidua » qui signifie qui tombe.
Se dit de ce qui se détache et tombe selon un rythme saisonnier.
Par exemple une feuille décidue.""" },
{ "word": "Défervescence", "definition": """Nom féminin.
Du latin defervescere : se refroidir.
En médecine: diminution de la fièvre.""" },
{ "word": "Déictique", "definition": """Adjectif et nom masculin.
Du grec « deiktikos » qui signifie démonstratif issu de « deixis » qui
signifie désignation.
En linguistique, se dit de ce qui sert à montrer ou de ce qui est
relatif à la déixis, c’est à dire relatif aux conditions particulières
de l’énonciation, comme l’identité du locuteur, le temps et l’endroit de l’énonciation.
Par exemple: »Moi, toi, ceci, cela, maintenant sont des expressions déictiques. »""" },
{ "word": "Dème", "definition": """Nom masculin.
Du grec « demos » qui signifie peuple.
Dans l’Antiquité grecque, division territoriale et unité administrative.
Par exemple: « Le dème est lié au progrès de la démocratie à Athènes. »""" },
{ "word": "Démotique", "definition": """Adjectif.
Du grec demos : peuple.
1. Langue parlée et écriture cursive au sein du peuple des anciens Egyptiens.
2. Se dit de ce qui est en rapport avec le grec moderne, courant et parlé.
Nom féminin.
Du grec demos : peuple.
La langue grecque moderne et courante.""" },
{ "word": "Dendrochronologie", "definition": """Nom féminin.
Du grec « dendron » qui signifie arbre, « chronos » qui signifie temps et
« logos » qui signifie discours.
Méthode qui permet de dater les évènements passés ou les changements
climatiques par l’étude des anneaux de croissance des troncs d’arbres.
Ces anneaux de croissance sont visibles par une coupe transversale du tronc.""" },
{ "word": "Dénéral", "definition": """Nom masculin.
Du latin denarius: pièce de cuivre ou poids d’une drachme attique.
Poids monétaire servant à vérifier les poids des monnaies d’or. Le
dénéral peut égalment servir de modèle pour suivre les normes de poids
et de diamètre d’une monnaie.
Je remercie pour son aide précieuse Monsieur Dominique Holland
responsable du fonds des monnaies romaines et celtiques de la
Bibliothèque Nationale de France.""" },
{ "word": "Déobandi", "definition": """Forme de nom commun masculin.
De la ville de « Déoband » dans l’état de l’Uttar Pradesh au nord de l’Inde.
Ecole de pensée musulmane sunnite, très présente en Asie du sud:
Pakistan, Inde et Afghanistan.
Elle fut fondée par Abu Hanifa, juriste musulman  du VIII ème siècle.
Elle prône un islam traditionaliste et apolitique ainsi qu’une lecture
littéraliste des textes.
Par exemple: « L’école déobandi a été une source de pensée pour les
talibans afghans. »""" },
{ "word": "Déontique", "definition": """Adjectif.
Du grec « deon, deontos » qui signifie devoir.
Se dit de se qui constitue une obligation, une nécessité ou un devoir.
Par exemple: « Les signaux routiers d’interdiction ou d’obligation sont
déontiques. »""" },
{ "word": "Déprécation", "definition": """Nom masculin.
Du latin « dis » qui signifie éloignement, séparation, privation et
« precatio » qui signifie prière.
Prière faite avec soumission, pour éloigner un malheur ou pour obtenir
le pardon d’une faute.""" },
{ "word": "Déréistique", "definition": """Adjectif.
De l’allemand « dereistich » issu du latin « de re » qui signifie en
s’éloignant de la chose réelle.
En psychiatrie se dit d’un mode de pensée dominée par l’imagination,
ce qui est fréquent chez les schizophrènes.""" },
{ "word": "Détritus", "definition": """Nom masculin.
A remplacé le mot détriment; du latin « detritus » qui signifie broyé,
usé, issu de « deterere » qui signifie user en frottant.
1- En géologie et dans un emploi vieilli. Débris de roches.
2- Dans un emploi moderne. Matériaux réduits à l’état de débris, inutilisables;
Couramment. Ordures, déchets.
En médecine. déchet provenant de la nécrose d’un tissu à la suite d’un
traumatisme ou d’une infection.""" },
{ "word": "Devanagari", "definition": """Nom masculin ou adjectif.
Mot sanskrit, hindi de « deva » qui signifie dieu et « nâgari » qui
signifie de la ville.
Forme d’écriture usuelle du sanskrit.""" },
{ "word": "Diachronie", "definition": """Nom féminin.
Du grec « dia » qui  signifie à travers et « chronos » qui signifie temps.
Evolution des phénomènes linguistiques à travers le temps.""" },
{ "word": "Diadococinésie", "definition": """Nom féminin.
Du grec « diadokos » qui signifie qui succède et « kinesis » qui signifie mouvement.
Aptitude naturelle à pouvoir effectuer certains mouvements comme la
pronation -prendre un objet- et la supination -tendre la main paume en
l’air-""" },
{ "word": "Diatribe", "definition": """Nom féminin.
Du grec « diatribé » qui signifie discussion d’école.
Critique acerbe, violente et calomniatrice.""" },
{ "word": "Diaule", "definition": """Nom féminin.
Du grec « dis » qui signifie deux et « aulos » qui signifie flûte.
Flûte double des grecs de l’antiquité.
Air joué avec cet instrument.""" },
{ "word": "Dicastère", "definition": """Nom masculin.
Du grec « dikasterion » qui signifie cour de justice.
1- Subdivision de la curie romaine.
2- En Suisse, subdivision d’une administration communale.""" },
{ "word": "Dictame", "definition": """Nom masculin.
Du latin « dictamnus » qui signifie plante originaire du mont Dictos en Crête.
1- En botanique. Plante aromatique de la famille des labiées et dont
les feuilles sont laineuses.
Par exemple: « Le dictame de Crête a des propriétés vulnéraires. »
2- En poétique. Sorte de baume moral.
Par exemple:
« Car vous êtes bénie entre toutes les femmes.
Vous avez le secret des bienfaisants dictames. »
Gabrielle de Poligny""" },
{ "word": "Didascalie", "definition": """Nom féminin
Du grec « didaskalia » qui signifie enseignement.
Dans une pièce de théâtre ou un scénario c’est une indication de jeu
destinée aux acteurs ou au metteur en scène.
Par exemple dans « Les Femmes Savantes » de Molière scène 2 l’acte IV on
peut lire l’indication suivante:
Clitandre entrant doucement et évitant de se montrer""" },
{ "word": "Dieu-conduit", "definition": """Nom masculin.
Dans la marine c’est le nom qui était donné à un cadre représentant un
motif religieux (par exemple le portrait du Christ, de la Vierge Marie
ou d’un saint) sous la protection duquel le navire était placé.
Au pluriel on écrit des dieu-conduit.""" },
{ "word": "Diffluent", "definition": """Adjectif.
Provient du latin diffluere: « s’écouler en divers sens. »
Qui s’écoule, se répand.
Peut se dire de tissus presque liquides ou de manière abstraite se dit
d’un esprit qui part dans toutes les directions.""" },
{ "word": "Dionée", "definition": """Nom féminin.
Du latin botanique « dionaea » qui signifie (plante) de Dioné qui était
la mère de Vénus.
Plante carnivore d’Amérique, de la famille des droséracées, dont les
feuilles bordées de longs cils et tapissées de poils sécrétant un
liquide visqueux, emprisonnent les insectes.""" },
{ "word": "Dioptrie", "definition": """Nom féminin.
Du grec « dioptron » issu de « dia » qui signifie à travers et « optesthai »
qui signifie voir.
Unité de mesure de vergence des systèmes optiques dont le symbole est
la lettre grecque « delta » équivalant à la vergence d’un système
optique
dont la distance focale est un mètre dans un milieu dont l’indice de
réfraction est un.
La dioptrie représente la puissance du verre nécessaire pour faire
converger l’image sur la rétine.
La distance focale est la distance requise pour voir un objet avec netteté.
Par exemple: « Un myope de -1 dioptrie peut voir distinctement sans
lunettes les objets situés à l’intérieur d’une distance d’un mètre
au-delà il les verra flous. »""" },
{ "word": "Diorama", "definition": """Nom masculin.
Du grec « dia » qui signifie à travers, construit d’après le mot panorama.
Tableau vertical où sont peints des figures ou des paysages éclairés,
en vogue au XIXème siècle.""" },
{ "word": "Dipsomanie", "definition": """Nom féminin.
Du grec dipsa soif et mania folie. 
Compulsion maladive à boire des liquides alcooliques en excès. 
Exemple: Le dipsomane est un alcoolique.  """ },
{ "word": "Dirimant", "definition": """Adjectif.
Du latin « dirimere » qui signifie annuler.
Un empêchement dirimant s’oppose à la célébration d’un mariage 
ou s’il a eu lieu l’annule.
Une objection dirimante annule un raisonnement.""" },
{ "word": "Diva", "definition": """Nom féminin.
Du grec « diva » qui signifie déesse.
Cantatrice de renom.
Par extension, chanteuse célèbre.""" },
{ "word": "Docimologie", "definition": """Nom féminin.
Du grec « dokimé » qui signifie épreuve et  « logos » qui signifie discours.
En psychologie, science qui a pour objet l’appréciation des différents
moyens de contrôle des connaissances.""" },
{ "word": "Dol", "definition": """Nom  masculin.
Du latin « dolus » qui signifie ruse.
En droit, se dit de manoeuvres frauduleuses, agissements malhonnêtes,
destinés à surprendre et à tromper une personne pour lui faire prendre
un engagement qu’elle n’aurait pas pris.
Par exemple on dit : « Le dol est un vice de consentement » ou bien « Ce
contrat est entaché de dol ».""" },
{ "word": "Doldrums", "definition": """Nom masculin pluriel.
Mot anglais qui signifie calme plat.
En météorologie se dit d’une zone de basses pressions équatoriales.""" },
{ "word": "Domino", "definition": """Nom masculin.
Abréviation d’une expression latine peut-être « benedicamus domino » qui
signifie bénissons le seigneur.
I
1- Anciennement, courte pèlerine  à capuchon que les prêtres portaient en hiver.
2- Costume de bal masqué qui consistait en une robe flottante à capuchon.
II
1- A cause du fond de bois noir comparé au domino sens I 1-
Petite plaque noire au dessous et dont le dessus blanc est séparé en
deux parties dont chacune comporte de zéro à six points noirs.
Les dominos est un jeu qui utilise 28 de ces plaques pour les
assembler selon des règles précises.
2- En électricité, dispositif de raccordement pour des fils de petite section.""" },
{ "word": "Dominotier", "definition": """Nom masculin.
Du latin « domino » qui signifie papier imprimé de figures colorées.
1- Fabricant de dominoterie ou papier dominoté c’est à dire de papiers
marbrés et coloriés utilisés pour certains jeux de société comme le
jeu de l’oie, de dames ou le
loto. Mais utilisés aussi pour recouvrir l’intérieur de coffres,
d’armoires, de tiroirs ou de cartons à chapeaux.
2- Personne fabricant des plaques d’os ou d’ivoire destinées à
recouvrir les dominos.""" },
{ "word": "Drache", "definition": """Nom féminin.
Du néerlandais « draschen » qui signifie pleuvoir.
En Belgique, se dit d’une pluie battante, d’une averse.""" },
{ "word": "Dragon", "definition": """Nom masculin.
Du grec « drakôn » issu du verbe « derkomai » qui signifie regarder, fixer
alors que son sens premier était brillant.
« Drakôn » signifie celui qui regarde.
A)   1- Animal fabuleux que l’on représente généralement avec des ailes,
des griffes et une queue de serpent.
Sur les blasons, figure de fantaisie représentant un reptile à deux pieds.
     2- Dans un sens vieilli; gardien, surveillant vigilant et
intraitable ou bien femme acariâtre, violente, aux manières brutales.
     3- dans l’iconographie chrétienne, figure du démon.
     4- En  zoologie, reptile de la famille des sauriens caractérisé
par la présence d’un repli membraneux qui forme comme un parachute.
B) Étendard représentant probablement un dragon.
Soldat de cavalerie.
Régiment de blindés.""" },
{ "word": "Draille", "definition": """Nom féminin.
Du franco-provençal « draya » issu de l’ancien dauphinois « draya » qui
signifie sentier.
Dans un emploi régional, piste empruntée par les troupeaux qui
effectuent la transhumance.
Par exemple: »Les drailles cévenoles. »""" },
{ "word": "Draver", "definition": """Verbe intransitif.
Mot canadien adapté de l’anglais « drive » issu de « to drive » qui
signifie conduire.
Anglicisme. Au Canada, action de diriger le flottage du bois.""" },
{ "word": "Dravidien", "definition": """Adjectif et nom masculin.
De l’anglais « dravidian » issu du sanskrit « Dravida » qui est une
province du Sud de l’Inde.
Relatif aux populations noires du sud de la péninsule indienne.
Les langues dravidiennes sont un groupe de langues qui étaient parlées
avant l’arrivée des Aryens en Inde et qui se sont conservées au sud de l’Inde.
Entre autres, on peut citer le tamoul et le malayalam.""" },
{ "word": "Drosera", "definition": """Nom masculin.
Du latin « drosera » issu du grec « droseros » qui signifie humide de
rosée. Du grec « doros » qui signifie rosée.
Dans les plantes de ce genre, les feuilles sont couvertes de glandes
qui ressemblent à des gouttes de rosée.
En botanique, nom d’une plante carnivore qui pousse dans les
tourbiéres et qui fait partie de la famille des droséracées.
Ses feuilles en rosette sont munies de tentacules et peuvent engluer
les petits insectes qui s’en approchent.
Darwin a longuement étudié le genre « Drosera » et affirmait avoir pour
les drosera un intérêt supérieur à l’intérêt qu’il pouvait porter à
toute autre espèce dans le Monde.
On extrait de cette plante des principes actifs utiles en médecine, ce
sont des antitussifs, des antispasmodiques, des antipyrétiques et des
antiseptiques.
C’est une plante d’ornement dont certains spécimens sont
commercialisés mais qui reste difficile à cultiver.
Elle ne peut pas être utilisée comme insecticide naturel puisqu’elle
n’englue pas tous les insectes de son environnement.
Un autre nom de ce genre est « Rossolis » issu du latin « ros » qui
signifie rosée et « solis » qui signifie soleil: La rosée du soleil. .""" },
{ "word": "Drumlin", "definition": """Nom masculin.
Mot irlandais issu du gaélique « druim » qui signifie bord d’une colline.
En géographie, éminence elliptique constitué par les éléments d’une
moraine dans les pays de relief glaciaire.""" },
{ "word": "Dryade", "definition": """Nom féminin.
Du latin « dryas, dryadis » issu du grec « druas », de « drus » qui signifie chêne.
1- En mythologie, nymphe protectrice des forêts.
2- Plante dicotylédone de la famille des rosacées, vivace et à grandes
fleurs blanches, qui pousse dans les montagnes.""" },
{ "word": "Ductile", "definition": """Adjectif.
Du latin « ducere » qui signifie conduire.
Se dit d’un matériau qui peut être allongé, étiré ou étendu sans se rompre.""" },
{ "word": "Dulie", "definition": """Nom féminin.
Du grec « douléia » qui signifie servitude.
Dans la religion catholique culte rendu aux anges et aux saints.""" },
{ "word": "Duodécimain", "definition": """Adjectif.
Du latin « duodécimus » qui signifie » douzième.
Qualifie une forme d’islam chiite. Le chiisme duodécimain se réfère
aux douze imams successeurs de Mahomet.""" },
{ "word": "Duodi", "definition": """Nom masculin.
Du latin « duo » qui signifie deux auquel on a ajouté le suffixe -di
comme dans lundi, mardi, mercredi, etc.
Historiquement, deuxième jour de la décade, qui était l’espace de dix
jours qui remplaçait la semaine, dans le camendrier républicain.""" },
{ "word": "Duramen", "definition": """Nom masculin.
Du latin « durus » qui signifie dur.
En botanique, partie la plus ancienne et tout à fait lignifiée d’un
tronc d’arbre.""" },
{ "word": "Dysorexie", "definition": """Nom féminin.
Du grec « dusorexai » qui signifie appétence, issu de « oregesthai » qui
signifie aspirer, tendre.
Troubles de l’appétit. Anorexie, boulimie, certaines toxicomanies
ainsi que l’ingestion de matières non-alimentaires.""" },
{ "word": "Dysosmie", "definition": """Nom féminin.
Du préfixe grec « dus- » qui exprime l’idée de difficulté, de manque et
du grec « osmê » qui signifie odeur.
Trouble de l’olfaction.
On peut le rapprocher du mot « anosmie » qui est une diminution ou une
perte complète de l’odorat.""" },
{ "word": "Eburnéen", "definition": """Adjectif.
Du latin « eburneus » qui signifie d’ivoire.
Se dit de ce qui a l’apparence et la consistance de l’ivoire.""" },
{ "word": "Ecdotique", "definition": """Nom féminin.
Du grec ancien « ekidômi » qui signifie produire au dehors soit éditer.
Science de l’établissement des textes.""" },
{ "word": "Ecdysone", "definition": """Nom masculin.
De l’allemand « Ecdyson », de « Ecdysis » qui signifie mue; issu du grec
« ekdusis » qui signifie action de se dépouiller.
Hormone produite par les glandes du prothorax des insectes, qui
stimule la mue des larves.""" },
{ "word": "Échalote", "definition": """Nom féminin.
Altération du latin « ascalonia cepa » qui signifie oignon d’Ascalon;
ville de l’actuelle Israël connue sous le nom d’Ashkelon.
La ville d’Ascalon est une des cinq capitales des Philistins du XIIème
au Xème siècle avant J-C. Le nom d’Ascalon revient souvent dans la
Bible. Les Francs auraient rapporté les échalotes en occident après
le siège d’Ascalon à la fin de la première croisade.
Le centre d’origine de l’échalote se situe en Asie centrale.
Plante potagère de la famille des liliacées, variété d’ail dont les
bulbes sont utilisées en condiment.
La locution « la course à l’échalote » signifie la course pour le pouvoir.""" },
{ "word": "Échelier", "definition": """Nom masculin.
De « échelle ».
Dans une langue régionale, échelle à un seul montant central.
Par exemple: L’échelier doit être appuyé sur un mur pour pouvoir être utilisée.""" },
{ "word": "Echolalie", "definition": """Nom féminin.
Du grec « êkhô » qui signifie son répercuté et « lalia » qui signifie
bavardage.
En neurologie répétition automatique de paroles ou de fins de phrases
dans certains troubles de la parole.""" },
{ "word": "Eclampsie", "definition": """Nom féminin.
Du grec « eklampein » qui signifie briller soudainement ou éclater.
Syndrome qui atteint la femme enceinte. Se manifeste par des
convulsions qui peuvent s’accompagner de coma. Est souvent causé par
une brutale hypertension.""" },
{ "word": "Effendi", "definition": """Nom masculin.
Mot turc qui est une altération du grec ancien « authentès » qui signifie maître.
Ancien titre de dignitaires civils ou religieux chez les Turcs.""" },
{ "word": "Égérie", "definition": """Nom féminin.
Nom de la nymphe qui aurait été la conseillère de Numa Pompilius.
Conseillère, inspiratrice d’un homme politique, d’un artiste.""" },
{ "word": "Eglogue", "definition": """Nom féminin.
Du grec « eklogî » qui signifie choix.
Petit poème champêtre.
Virgile a composé des églogues.""" },
{ "word": "Eider", "definition": """Nom masculin.
De l’islandais « aedur » qui a donné « edre » qui signifie duvet.
Grand canard de la famille des ansériformes, qui vit dans les pays du
Nord et qui fournit un duvet apprécié.""" },
{ "word": "Eidétique", "definition": """Adjectif. 
Du grec eidos : forme,essence. 
Image éidétique : se dit d’une image très riche et détaillée
Mémoire éidétique : se dit d’une mémoire qui conserve toutes les impressions visuelles 
avec une extrême précision. """ },
{ "word": "Éléatique", "definition": """Adjectif.
Du latin « eleaticus » issu de « Elea » qui signifie « Élée », cité grecque
de la côte tyrrhénienne, en Campanie, près du golfe de Salerne.
En histoire de la philosophie, l’école Éléatique, fut fondée par
Parménide et Xénophane et suivie par Zénon d’ Élée et Mélisse.
Par exemple: »Parménide est un représentant majeur de l’école Éléatique. »""" },
{ "word": "Electrum", "definition": """Nom masculin.
Du grec « êlektron » issu de « êlektôr qui signifie brillant,
qualificatif du Soleil et épithète d’Hypérion.
En grec classique, le mot désigne presque toujours l’ambre, dont les
propriétés ont donné en français les mots électricité et électron.
En latin, le terme désigne l’alliage que les Grecs appelaient plus
couramment or blanc « leukhos khrusos ». Pline l’Ancien expliquait que
l’or qui contient de l’argent en proportion de un cinquième est appelé électrum.
Alliage composé d’or et d’argent et rencontré à l’état naturel dans
des proportions variables.
C’est un métal plus éclatant que l’argent.
En 1806, Aubin Louis Millin de Grandmaison affirma que les coupes
d’électrum naturel décelaient les poisons.
On apercevait sur une coupe en électrum qui contenait un poison des
iris semblables à l’arc-en-ciel qui se dessinaient avec le bruissement
d’une flamme.
En numismatique et en histoire de l’art, le terme désigne également un
alliage artificiel.
Très prisé dans l’Antiquité, il fut utilisé par les Égyptiens et  il
servit pour frapper monnaie en Lydie et en Grèce.""" },
{ "word": "Electuaire", "definition": """Nom masculin.
Du latin electus qui signifie choisi.
Terme vieilli.
Préparation pharmaceutique de consistance molle composée de poudres
mélangées à du sirop, des extraits végétaux ou du miel.
Le thériaque était un électuaire qui contenait de l’opium parmi
d’autres principes actifs et qui était destiné à soigner les morsures
de serpents.""" },
{ "word": "Eleis", "definition": """Nom masculin.
Du grec « elaiêeis » qui signifie huileux.
Palmier à huile cultivé en Afrique et en Malaisie.""" },
{ "word": "Elingue", "definition": """Nom féminin.
De l’ancien français utilisé dans certaines régions « egalt » qui
signifie fronde ; issu du francique « slinga ».
Terme de marine: cordage dont on entoure les fardeaux pour les
soulever ou filin garni de crocs permettant de mettre à la mer un
canot léger.""" },
{ "word": "Elution", "definition": """Nom féminin.
Du latin « elutio » issu de « eluere » qui signifie laver, rincer.
En chimie, déplacement par un solvant d’une substance adsorbée.
Par exemple: « L’élution permet de remettre en solution un ou plusieurs
anticorps fixés sur des globules rouges. Il en résulte que les
anticorps sont séparés des globules rouges. »""" },
{ "word": "Elzévir", "definition": """De Elzévi(e)r Nom d’une célèbre famille d’imprimeurs.
1. Livre imprimé en Hollande (fin XVI ème siècle-fin XVII ème siècle)
par Elzévir ou par leurs imitateurs.
2. Caractère d’imprimerie à empattements triangulaires, proche de celui
utilisé par les Elzévir.""" },
{ "word": "Embâcle", "definition": """Nom masculin.
De « embâcler » qui signifie embarrasser, d’après « débâcle »  lui même
issu de « bâcler » qui vient de « bacculare » issu de « bacculum » qui
signifie bâton. A l’origine « bâcler » signifiait fermer avec une barre
une porte ou une fenêtre.
Obstruction d’un cours d’eau par des obstacles comme des troncs, des
branches ou des pierres, mais aussi obstruction du lit d’un cours
d’eau ou d’un détroit par amoncellement de glace flottante.
Le contraire d’embâcle est débâcle.
Ce mot a été employé pour décrire les violentes inondations qui ont eu
lieu dans l’Hérault le 17 septembre 2014.""" },
{ "word": "Emblée (D’)", "definition": """Locution adverbiale.
De « en emblée » qui signifiait en cachette au XV ème siècle, issu du
latin « involare » qui signifie se précipiter sur.
Du premier coup, au premier effort pour obtenir le résultat en question.
Par exemple: « Il est revenu vers toi d’emblée. »""" },
{ "word": "Embolisme", "definition": """Nom masculin.
Du grec « embolismos » qui signifie intercalation, issu du verbe
« emballéin » qui signifie insérer, ajouter, mettre entre deux.
Les grecs appelaient ainsi l’addition qu’ils faisaient tous les deux
ou trois ans d’un treizième mois à l’année lunaire qui est de 354
jours afin de l’approcher de l’année solaire qui est de 365 jours, sans
compter quelques heures de part et d’autre.
Le mois qui était intercalé se nommait mois embolismique ou mois intercalaire.""" },
{ "word": "Emménagogue", "definition": """Adjectif et nom masculin.
Du grec « emmêna » qui signifie menstrues et « agôgos » qui signifie qui attire.
Se dit d’une substance qui favorise le cycle menstruel.
Par exemple, en tant que nom masculin: « L’armoise est un emménagogue. »
Et en tant qu’adjectif: « La jacobée est une plante emménagogue. »""" },
{ "word": "Émonctoire", "definition": """Adjectif.
Du latin « emunctum » issu du supin « emungere » qui signifie moucher.
En physiologie, organe qui élimine les substances formées au cours des
processus de désassimilation.
Par exemple: « Les reins, le nez, ou les pores de la peau sont des
émonctoires naturels. »""" },
{ "word": "Emphytéose", "definition": """Nom féminin.
Du grec « emphyteusis » issu de « phuteuein » qui signifie planter.
Droit réel de jouissance sur le bien-fonds d’autrui, accordé par un
bail de longue durée (de 18 à 99 ans)moyennat paiement d’une redevance
modique.
Par exemple: »Un bail relatif à l’emphytéose est un bail emphytéotique. »""" },
{ "word": "Empuse", "definition": """Nom féminin.
Du latin « empusa » issu du grec « empousa » nom d’un spectre de la
mythologie grecque.
1- En zoologie, insecte orthoptère marcheur voisin de la mante. La
larve de l’empuse est le diablotin.
2- En botanique, champignon siphomycète qui est parasite de certains insectes.""" },
{ "word": "Empyrée", "definition": """Nom masculin.
De l’expression de la fin du XIV ème siècle : « cieux empirées ». Du
grec « empur(i)os » qui signifie en feu.
Dans la mythologie antique c’était la plus élevée des quatre sphères
célestes qui contenait les feux éternels c’est à dire les astres et
qui était le séjour des dieux.
En littérature et au figuré, c’est le ciel ou le monde supraterrestre.""" },
{ "word": "Empyreume", "definition": """Du grec empireuma qui vient de « pur » qui signifie feu.
Saveur ou odeur âcre que prennent certaines matières organiques à
l’occasion d’une combustion.""" },
{ "word": "Emulation", "definition": """Nom féminin.
Du latin « æmulatio » qui signifie émulation, rivalité, jalousie.
1- Sentiment de rivalité qui pousse à égaler quelqu’un ou à le
surpasser, en mérite, en savoir ou en travail.
Par exemple: « L’émulation a permis à cet étudiant moins brillant
d’atteindre un niveau de connaissances aussi élevé que son camarade
major de promotion. »
2- Situation de rivalité considérée comme bénéfique à chacun des
rivaux; chacun cherchant à s’améliorer pour supasser les autres.
Par exemple:  » Danscette classe, l’émulation a amélioré les résultats
de chacun de façon notable. »
3- En informatique, et par abus de langage. Procédé qui consiste en
l’imitation ou en la simulation logicielle d’un matériel ancien ou
d’un programme non prévu pour le matériel su lequel on veut l’exécuter.
Par exemple: »Un logiciel d’émulation indispensable pour ce jeu vidéo. »""" },
{ "word": "Enallage", "definition": """Nom féminin.
Du grec « enallagê » qui  signifie interversion, transposition. Issu de
« enallassein » qui signifie échanger.
Figure de style qui consiste à remplacer un temps, un mode, un nom,
une personne, par un autre temps, un autre mode, un autre nom une
autre personne.
C’est à dire qu’elle remplace une forme grammaticale par une autre.
Par exemple: « Il voyage léger. » pour « Il voyage légèrement. »
Ou « Il a bien mangé? » où « il » est à la place de « vous ».""" },
{ "word": "Enantiomorphe", "definition": """Adjectif.
Du grec « enantios » qui signifie opposé et « morphê » qui signifie forme.
Se dit d’un objet formé de parties identiques qui sont disposées dans
un ordre inverse par rapport à un point, un axe ou un plan de
symétrie.
La main droite et la main gauche sont énantiomorphes.""" },
{ "word": "Enantiotrope", "definition": """Adjectif.
Du grec « enantios » qui signifie opposé et « tropos » qui signifie le
tour ou la direction. Du verbe « trepein » qui signifie tourner.
Propriété qu’a un corps de pouvoir se trouver sous deux formes
physiques différentes autour d’un point stable. L’une au-dessous de ce
point, l’autre au-dessus.
L’eau est énantiotrope.""" },
{ "word": "Enarthrose", "definition": """Nom féminin.
Du grec « enarthrosis » qui signifie action d’articuler.
Articulation mobile qui comporte deux surfaces sphériques l’une
convexe, l’autre concave; elle permet aux os de se mouvoir dans trois
directions principales.""" },
{ "word": "Encan (A l’)", "definition": """Locution adverbiale.
Du latin « in quantum » qui signifie pour combien.
Dans un sens vieilli, en vente aux enchères publiques. Par
exemple, »vendre à l’encan » ou « mettre à l’encan ».
Au sens figuré, livré au plus offrant. Par exemple, « la justice était
à l’encan ».""" },
{ "word": "Endogé", "definition": """Adjectif.
Du grec « endon » qui signifie en dedans et « gê » qui signifie terre.
En zoologie, se dit d’un organisme qui vit sous terre.
Par exemple : « une espèce endogée ».""" },
{ "word": "Endymion", "definition": """Nom masculin.
Du nom d’un personnage mythologique, roi ou berger grec aimé de
Séléné, qui obtint de Zeus qu’il conserverait sa beauté dans un
sommeil éternel. Ce nom rappelle l’aspect endormi de la plante.
Plante à bulbe, de la famille des liliacées dont les fleurs bleues
s’épanouissent au printemps, et qui s’appelle couramment la jacinthe
des bois.""" },
{ "word": "Engramme", "definition": """Nom masculin.
Du grec « en » qui signifie dans et « gramma » qui signifie caractère, trait.
En psychologie, trace organique, laissée dans le cerveau par un
évènement du passé individuel, et qui serait le support matériel du
souvenir.""" },
{ "word": "Entéléchie", "definition": """Nom féminin.
Du grec entelékhéia: énergie agissante et efficace.
En philosophie et selon Aristote état de l’être parfait au contraire
de l’être inachevé.""" },
{ "word": "Éosine", "definition": """Nom féminin.
Du grec « eôs » qui signifie aurore. La lumière de l’aurore a une
couleur légèrement rose. Chez Homère, on trouve l’expression « l’aurore
aux doigts de rose ».
Substance qui est colorée en rouge et qui colore en rouge les
« éosinophiles »( qui aiment l’éosine). Elle est obtenue en traitant la
fluoresceïne par du brome en présence d’alcool.
Elle est aussi utilisée en dermatologie""" },
{ "word": "Epanorthose", "definition": """Nom féminin.
Du grec « epanorthosis » qui signifie redressement.
Figure de style dite de correction. On y modifie un propos jugé trop faible .
Exemple tiré du Grand Dictionnaire Littré :
« J’espère, que dis-je ? Je suis sûr qu’on vous rendra justice. »""" },
{ "word": "Eparque", "definition": """Nom masculin.
Du grec « eparkhos » qui signifie commandant.
1- Dans le Bas-Empire romain, nom donné au gouverneur d’une province.
2- Sous l’Empire grec, nom du Préfet de Constantinople.""" },
{ "word": "Epenthèse", "definition": """Nom féminin.
Du grec « epenthésis » qui signifie action de surajouter.
Apparition au sein d’un mot d’une consonne ou d’une voyelle
[on dit un phonème] qui ne fait pas partie de l’étymologie du mot.
Par exemple l’épenthèse du b dans le mot nombre qui vient du latin « numerus ».""" },
{ "word": "Epha", "definition": """Nom masculin.
De l’hébreu « eyphah » qui provient de l’égyptien « hpya » dont la
signification est incertaine.
Mesure des grains chez les hébreux valant 18 litres 08.
Ephi est un synonyme d’épha.
Ces termes se rencontrent dans l’Ancien Testament.""" },
{ "word": "Ephyrule", "definition": """Nom féminin singulier.
En zoologie, larve de petite méduse à ombrelle découpée.""" },
{ "word": "Epicène", "definition": """Adjectif.
Du grec « epikoinos » qui signifie commun.
Dans une espèce animale désigne aussi bien le mâle que la femelle.
Par exemple la souris est un nom épicène féminin.""" },
{ "word": "Epiclèse", "definition": """Nom féminin.
Du grec « epiklésis » qui signifie invocation.
En liturgie catholique, invocation au Saint-Esprit.""" },
{ "word": "Epiploon", "definition": """Nom masculin.
Du grec « epiploon » qui signifie flottant.
En anatomie, repli du péritoine qui relie entre eux les organes abdominaux.
Le grand epiploon, unit la grande courbure de l’estomac et le côlon transverse.
Le petit epiploon, unit l’estomac au foie.
L’epiploon des animaux est la crépine.""" },
{ "word": "Epirogenèse", "definition": """Nom féminin.
Du grec « epeiros » qui signifie continent et « genesis » qui signifie
naissance, formation.
En géologie, c’est l’ensemble des mouvements lents de descente ou de
montée des continents.
On peut dire: « Un mouvement d’épirogenèse affecte les continents de
manière continue »""" },
{ "word": "Épiscope", "definition": """Nom masculin.
Du grec « épi » qui signifie sur et « skopos » issu de « skopein » qui
signifie examiner, observer.
Appareil d’optique à miroirs qui est placé à l’intérieur des chars
pour observer le terrain.""" },
{ "word": "Épithalame", "definition": """Nom masculin.
Du grec « epithalamion » qui signifie chant nuptial.
En littérature, poème composé à l’occasion d’un mariage, en l’honneur
des nouveaux mariés.""" },
{ "word": "Epithète", "definition": """Nom masculin jusqu’au XVII ème siècle. Aujourd’hui nom féminin.
Du latin « epitheton » d’origine grecque qui signifie qui est ajouté.
1- Ce que l’on ajoute à un nom, un pronom pour le qualifier.
2- Par extension qualification louangeuse ou injurieuse donnée à quelqu’un.
3- Un adjectif épithète ou de manière elliptique une épithète:
Adjectif qualificatif qui n’est pas relié au nom par un verbe( par
opposition à l’attribut).
Par exemple « Une maison bleue ».
Nom épithète: qui qualifie un autre nom.
Par exemple: « La fée clochette ».""" },
{ "word": "Epitope", "definition": """Nom masculin.
Du grec « epi » qui signifie sur et « topos » qui signifie lieu.
En immunologie, science qui étudie nos mécanismes de défense par
rapport à une agression extérieure (bactérie, virus…).
Partie d’une molécule qui a la possibilité de se combiner avec les
anticorps spécifiques correspondants.""" },
{ "word": "Epode", "definition": """Nom féminin.
Du grec « epôdos » de « epi » qui signifie sur et « ôdê » qui signifie chant.
1- Troisième couplet d’un choeur lyrique, divisé en strophe,
antistrophe et épode.
2- Couplet lyrique composé de deux vers inégaux comme un distique.
Par extension, petit poème satirique écrit en distiques.
Par exemple : Les Epodes d’Horace.""" },
{ "word": "Epoisses", "definition": """Nom masculin.
Du nom d’un village de Bourgogne.
Fromage de lait de vache, à pâte molle et à croûte lavée au marc de Bourgogne.""" },
{ "word": "Eponyme", "definition": """Adjectif.
Du grec « epi » qui signifie sur et « onoma » qui signifie nom.
Dans l’antiquité grecque. Se dit de ce qui donne son nom à quelqu’un
ou à quelque chose.
Par exemple, Athéna est la déesse éponyme d’Athènes.
A l’époque moderne: tenir le rôle éponyme d’une pièce ou d’un film.
Par exemple, le rôle d’Electre dans la pièce du même nom.""" },
{ "word": "Ergastule", "definition": """Nom masculin.
Du latin « ergastelum » adapté du mot « ergastérion » qui signifie atelier.
Prison souterraine ou cachot dans l’Antiquité romaine.""" },
{ "word": "Eromène", "definition": """Nom masculin.
Dans la Grèce classique, nom donné à un adolescent destiné à recevoir
une éducation intellectuelle et physique par un homme adulte nommé
« éraste ».
Ce statut était codifié et était le fait d’une certaine aristocratie
(ordre équestre des Curètes ou Kourètes). Il n’était pas d’un usage
général.
Un jeune garçon était susceptible de devenir éromène à partir du
moment où il sortait du quartier des femmes ou « gynécée ».
Il rejoignait ensuite la « palestre » où il pratiquait toutes sortes
d’exercices physiques (lutte, gymnastique, course, javelot…) ainsi
qu’il apprenait les bonnes manières et la discipline.
Ce statut prenait fin à l’apparition de sa première barbe au menton.
Par exemple: « L’éromène avait en général moins de seize ans. »""" },
{ "word": "Ersatz", "definition": """Nom masculin.
D’un mot allemand qui signifie remplacement.
1- Anciennement se disait d’un produit alimentaire qui en remplaçait
un autre de qualité supérieure, devenu rare.
Par exemple: Un ersatz de sucre.
2- Dans un sens figuré mais vieilli, se dit de ce qui remplace quelque
chose ou quelqu’un en moins bien.
Par exemple: Ce député est un ersatz d’homme d’État.""" },
{ "word": "Eruciforme", "definition": """Adjectif.
Du latin « eruca » qui signifie chenille et « forma » qui signifie forme.
En zoologie, se dit d’une larve qui a la forme d’une chenille.""" },
{ "word": "Erudit", "definition": """Adjectif et nom masculin.
De « erudire » qui signifie dégrossir.
En tant qu’adjectif.
1- Qui possède une instruction, un savoir.
Par exemple: « Un philosophe érudit fait une conférence. »
En tant que nom.
2-Un lettré.
Par exemple: « Ce philosophe est un érudit ».""" },
{ "word": "Erythophobie", "definition": """Nom féminin.
Du grec « ereuthein » qui signifie rougir et « phobos » qui signifie crainte, peur.
Crainte maladive de rougir en public.
Autre orthographe : éreuthophobie.""" },
{ "word": "Escobar", "definition": """Nom masculin.
Nom d’un père jésuite casuiste.
Anciennement, un casuiste hypocrite qui résout adroitement et au mieux
de ses intérêts, les cas de conscience les plus délicats.""" },
{ "word": "Escourgeon", "definition": """Nom masculin.
Du latin « corrigia » qui signifie courroie à cause de la forme des épis.
Orge hâtive qui est semé en automne.""" },
{ "word": "Escrime", "definition": """Nom féminin.
De l’ancien ‘italien « scrima », issu de l’ancien français « escremie »
par le francique « skirmjan » qui signifie protéger.
Exercice par lequel on apprend à se servir d’une arme blanche comme
l’épée, le fleuret ou le sabre.""" },
{ "word": "Estagnon", "definition": """Nom masculin.
Du provençal moderne « estagnoun », issu de « estanh » qui signifie étain.
En Afrique, récipient en fer étamé destiné à contenir de l’huile ou
des essences.""" },
{ "word": "Ester", "definition": """Verbe intransitif qui ne s’emploie à l’infinitif.
Du latin « stare » se tenir debout.
Mener une action en justice comme requérant ou défendeur.
On dit ester en justice ou ester en jugement.""" },
{ "word": "Estoppel", "definition": """Nom masculin.
De l’anglais « estoppel » issu de l’ancien français « estoupail » qui
signifie bouchon, de « estouper » qui signifie boucher, étoupper,
stopper.
En droit, désigne une règle générale de procédure en vertu de laquelle
une partie ne pourrait, après avoir adopté une position claire ou un
comportement non ambigu sur sa future conduite à l’égard de l’autre partie,
modifier ultérieurement cette position ou ce comportement d’une façon qui
affecte les rapports de droit entre les parties et conduise l’autre partie
à modifier à son tour sa position ou son comportement.
Cette règle est issue du droit anglais.
On peut la résumer de la façon suivante: C’est l’interdiction de se
contredire au détriment d’autrui. Ou bien: Principe du « non concedit
venire contra factum proprium » de la lex mercatoria.""" },
{ "word": "Etampure", "definition": """Nom féminin.
De « estamper » qui signifie écraser.
1- Chacun des trous d’un fer à cheval.
2- Evasement d’un trou percé dans une plaque de métal.""" },
{ "word": "Etésien", "definition": """Adjectif masculin.
Du grec « etêsioi [anemoi] » qui signifie [vents] périodiques, annuels,
issu de « etos » qui signifie année.
Les vents étésiens sont des vents du nord qui soufflent en
méditerranée orientale chaque année pendant la canicule.""" },
{ "word": "Eteule", "definition": """Nom féminin.
Du latin « stipula » qui signifie tige des céréales.
En agriculture, chaume qui reste dans le champ après la moisson.""" },
{ "word": "Ethmoïde", "definition": """Nom masculin.
Du grec « ethmoïdes » issu de « êthmos » qui signifie crible, tamis et
« eïdos » qui signifie aspect, forme.
En anatomie humaine, os impair situé à la base du crâne et en avant du
sphénoïde, dont la partie supérieure horizontale est criblée de trous
au travers desquels passent les nerfs olfactifs. 
Cette partie forme le plafond des fosses nasales. Quant aux
parties latérales, elles participent aux parois internes des orbites
et aux parois externes des fosses nasales.""" },
{ "word": "Etisie", "definition": """Nom féminin.
Du grec « ektikos » qui signifie habituel.
La « fièvre hectique » provoque un amaigrissement. Etisie est un mot
vieilli, c’est la consomption, l’extrême maigreur.
Il donne l’adjectif « étique » c’est à dire affecté d’une très
importante maigreur.""" },
{ "word": "Étouffe-chrétien", "definition": """Nom masculin invariable.
De étouffe et chrétien.
Dans un langage familier. Aliment ou pâtisserie de consistance épaisse
ou farineuse, difficile à avaler. [ Qui pourrait étouffer un
chrétien.]
Par exemple: « Ce gâteau est trop lourd. C’est un étouffe-chrétien. »""" },
{ "word": "Êtres", "definition": """Nom masculin pluriel.
Du latin « extera » pluriel « exterus » qui signifie ce qui est à l’extérieur.
Dans un sens vieilli, disposition des lieux dans un bâtiment.
Par exemple: »Connaître les êtres d’une maison. »""" },
{ "word": "Étrésillon", "definition": """Nom masculin.
Altération de « estésillon » qui signifie bâton servant à maintenir la
gueule ouverte d’où « baillon » attesté plus tard dans la langue.
Issu de l’ancien français « estesser » du latin « tensare » qui signifie tendre.
Dans un langage technique, pièce de bois, qui soutient les parois
d »une tranchée ou d’une galerie de mine, un mur qui se déverse ou
que l’on reprend en sous-oeuvre.
Par exemple: « L’étrésillon a cédé; la galerie s’est effondrée sans
faire de victimes. »""" },
{ "word": "Eucharistie", "definition": """Nom féminin.
Du grec « eukharistia » qui signifie action de grâce.
Sacrement essentiel du christianisme qui commémore et perpétue le
sacrifice du Christ.
Selon la doctrine catholique, le pain et le vin contiennent le corps,
le sang, l’âme et le caractère divin du Christ.
Ce postulat se traduit dans la liturgie par un « repas » d’hostie et de vin.""" },
{ "word": "Eucologie", "definition": """Nom féminin.
Du grec « eukhologion » composé de « eukhê » qui signifie prière et
‘logos » qui signifie livre.
Dans la religion chrétienne, livre de prières contenant l’office des
dimanches et des fêtes.""" },
{ "word": "Euglène", "definition": """Nom féminin.
Du grec « euglenos » qui signifie « aux beaux yeux » ou « aux belles
prunelles » ; issu de « eu » qui signifie agréable et « glenos » qui
signifie cavité.
Algue verte, unicellulaire qui vit dans les eaux douces et stagnantes.""" },
{ "word": "Euryhalin", "definition": """Adjectif.
Du grec « eurus » qui signifie large et « halos » qui signifie sel.
Se dit d’être vivants capables de vivre dans des eaux de salinité variable.
Par exemple le saumon vit selon les stades de son développement dans
les rivières dont les eaux sont douces et dans les mers dont les eaux
sont salées.
Le saumon est un poisson euryhalin.""" },
{ "word": "Eutectique", "definition": """Adjectif.
Emprunté à l’anglais « eutectic » mot créé par le physicien anglais
Frederick Guthrie en 1875, issu du grec « eutêktos » qui signifie qui
fond bien.
En chimie, mélange de deux corps purs qui fond et se solidifie à
température constante. Ce mélange se comporte comme un seul corps pur
du point de vue de la fusion.""" },
{ "word": "Évhémérisme", "definition": """Nom masculin.
De « Évhémère » philosophe grec. (Vers 340- vers 260 avant notre ère.)
Doctrine selon laquelle les dieux de la mythologie grecque étaient des
personnages humains divinisés après leur mort.
Par exemple: « Les philosophes du XVIII ème siècle appliquèrent
l’évhémérisme aux dogmes chrétiens. »""" },
{ "word": "Evzone", "definition": """Nom masculin.
Du grec « euzonos » qui signifie qui a une belle ceinture.
Soldats de l’infanterie grecque.
Par exemple: »Les evzones portaient le court jupon masculin du costume
grec qui est appelé fustanelle. »""" },
{ "word": "Exaction", "definition": """Nom féminin.
Du latin « exactio » qui signifie action d’exiger le paiement d’un
tribut ou d’un impôt.
1- Action d’exiger ce qui n’est pas dû ou plus qu’il n’est dû et
spécialement en parlant d’un agent public.
2- Par extension et au pluriel, se dit des sévices ou des mauvais
traitements provoqués par des citoyens ou par des personnes morales
(gouvernement ou régime).""" },
{ "word": "Exciper", "definition": """Verbe transitif indirect.
Du latin « excipere » qui signifie excepter.
1. En justice s’utilise lorsque l’on soulève une exception.
Par exemple: » Exciper de l’acquittement. »
2. Se servir de quelque chose pour sa défense.
Par exemple: » Exciper de son manque de temps, pour ne pas avoir
terminé un travail. »""" },
{ "word": "Exégèse", "definition": """Nom féminin.
Du grec « exêgêsis » qui signifie explication.
Interprétation philologique, historique ou doctrinale d’un texte dont
le sens et la portée sont obscurs ou sujets à discussion.
Par exemple, on peut faire l’exégèse de la Bible.""" },
{ "word": "Exigu", "definition": """Adjectif.
Rare et plaisant au XVIIIème siècle, du latin « exiguus » qui signifie
exactement pesé, issu du latin « exigere » qui signifie peser.
1- Dans un sens vieilli, se dit de ce qui est insuffisant en quantité.
2- Dans un sens moderne, se dit de ce qui a un espace insuffisant.""" },
{ "word": "Exocet", "definition": """Nom masculin.
Du grec « exôkoitos » qui signifie littéralement: qui sort de sa demeure.
1- Poisson des mers chaudes pourvu de grandes nageoires pectorales qui
lui permettent de sauter hors de l’eau et de planer un instant dans
l’air; d’où son nom de poisson volant.
Nom masculin invariable. marque déposée.
2- Missile de fabrication française, autoguidé et à trajectoire
rasante qui est utilisé pour la destruction des navires.""" },
{ "word": "Exoréique", "definition": """Adjectif.
Du grec « exo » qui signifie extérieur « rhéin » qui signifie couler.
Régions dont le réseau d’eau coule vers la mer.""" },
{ "word": "Exutoire", "definition": """Adjectif.
Du latin « exutus » participe passé de exuere qui signifie dépouiller.
1- En médecine, anciennement, ulcère artificiel destiné à entretenir
une suppuration locale.
2- Ce qui permet de se soulager, de se débarrasser d’un besoin ou d’une envie.""" },
{ "word": "Exuvie", "definition": """Nom féminin.
Du latin « exuviæ » qui signifie dépouille.
En zoologie, peau rejetée par un animal lors de la mue.""" },
{ "word": "Eyra", "definition": """Nom masculin.
Du latin « eyra » issu probablement de « ara » mot du Brésil.
De « cougouacu ara » : le cougouar ou couguar.
Petit puma vivant au Brésil.""" },
{ "word": "Factieux", "definition": """Adjectif.
Du latin « factiosus » qui signifie enclin à séparer.
Qui exerce contre le pouvoir établi une opposition violente
susceptible d’engendrer des troubles à l’ordre public.""" },
{ "word": "Fada", "definition": """Adjectif et  nom masculin.
Mot provençal qui est peut-être le participe passé de  « ensorceler,
charmer ». De « fada » qui signifie fée avec l’influence de « fadas » qui
signifie sot par « fatuus »  qui a donné fat.
Dans le parler régional du midi, un peu fou.
Par exemple: »Il a encore oublié ces clés, il est fada. »""" },
{ "word": "Fakir", "definition": """Nom masculin.
De l’arabe « faqir » qui signifie pauvre.
1- En religion ou en sociologie, ascète musulman.
En inde, ascète qui vit d’aumône et se livre à des mortifications en public.
2- Plus couramment, personne qui donne un spectacle imité de ceux des fakirs.
Par exemple: » Le fakir a traversé un tapis de verre brisé. »""" },
{ "word": "Famille", "definition": """Nom féminin.
Du latin « famulus » qui signifie serviteur, esclave.
Dans son premier sens c’est une réunion d’esclaves sous l’autorité d’un maître.
Le mot devient ensuite l’ensemble des habitants d’une maison.""" },
{ "word": "Farfadet", "definition": """Nom masculin.
Mot provençal, forme renforcée de « fadet », de « fado » qui signifie fée.
Esprit follet, lutin doué d’une grâce légère et vive.""" },
{ "word": "Farigoule", "definition": """Nom féminin.
Du latin « fericula » qui signifie thym.
En Provence, le thym.
Se dit aussi d’une eau de toilette parfumée au thym.""" },
{ "word": "Fascine", "definition": """Nom masculin.
De l’ancien français « faissine » issu du latin « fascina » qui signifie
fardeau, fagot.
Fagot serré de branchages, employé dans les travaux de terrassement,
de fortification ou d’hydraulique.
Par exemple:  » Le voisin a installé des fascines le long du mur de son jardin. »""" },
{ "word": "Faseyer", "definition": """Verbe intransitif.
Du néerlandais « faselen » qui signifie agiter.
Terme de marine qui signifie battre au vent, en parlant d’une voile
que le vent n’enfle pas.""" },
{ "word": "Fastidieux", "definition": """Adjectif.
Du latin « fastidiosus » issu de fastidium qui signifie « dégoût ».
Se dit de ce qui rebute en provoquant l’ennui ou la lassitude.""" },
{ "word": "Fastigié", "definition": """Adjectif.
Du latin « fastigatus » qui signifie élevé en pointe, issu de fastigium
qui signifie « faîte ».
En botanique, végétal caractérisé par des ramifications dressées
verticalement formant un angle aigu avec le tronc ou la tige.
Par exemple, on peut dire : »Un cyprès fastigié ».""" },
{ "word": "Félibre", "definition": """Nom masculin.
Mot provençal moderne recueilli par Frédéric Mistral dans une vieille
cantilène. Probablement, issu du latin « fellebris » qui signifie
nourrisson des muses.
Lui-même issu du latin « fellare » qui signifie sucer, têter.
Écrivain ou poète de langue d’oc.
Les sept félibres du félibrige, sont sept écrivains fondateurs en 1854
d’une école littéraire en Provence.""" },
{ "word": "Ferronnière", "definition": """Nom féminin.
Du nom du portrait (peut-être de Léonard de Vinci) dit La Belle
ferronnière. Vient peut-être du mot ferronnier lui-même issu de
« ferron » qui signifie marchand de fer.
Ornement porté sur le front, chaînette ou bandeau garni d’un joyau en
son milieu.""" },
{ "word": "Ferté", "definition": """Nom féminin.
Forme populaire de « fermeté » qui signifie forteresse.
Dans un nom de ville, ce mot signifie forteresse, place forte.
Par exemple: « La Ferté St-Aubin ».""" },
{ "word": "Férule", "definition": """Nom féminin.
Du latin « ferula » issu de deux origines possibles:
a- Du latin « ferio » qui signifie frapper.
b- Du latin « fero » qui signifie porter. Dans l’Antiquité, selon la
légende, Prométhée aurait dérobé le feu sacré en le transportant dans
une tige de férule.
1- En botanique, plante de la famille des apiacées qui pousse surtout
dans les régions méridionales et dont la tige séchée, solide et légère
à la fois, a un diamètre supérieur à 5 cm.
2- Familièrement, palette de bois ou de cuir dont on se servait
autrefois pour punir les écoliers fautifs.
3- Chez les catholiques, bâton pastoral liturgique, marque de la
dignité des évêques, des abbés  et parfois des papes.
« Etre sous la férule de quelqu’un » signifiait d’abord recevoir son enseignement.""" },
{ "word": "Fidejusseur", "definition": """Nom masculin.
Du latin « fidejussor » issu de « fides » qui signifie confiance et
« jubere » qui signifie ordonner.
Terme vieilli de droit. Celui qui se porte garant de la dette d’un autre.
Par exemple: « Le fidejusseur est l’équivalent de celui qui se porte caution. »""" },
{ "word": "Flandrin", "definition": """Nom masculin.
De la Flandre.
Dans le langage familier, homme grand d’allure gauche.
Le synonyme de ce mot est dadais.""" },
{ "word": "Flexitarien", "definition": """Adjectif et nom.
Issu de la contraction de flexible et de végétarien.
Flexible vient de « flexus » qui est le participe passé du verbe
« flexere » qui signifie fléchir.
Végétarien vient de l’anglais « vegetarian » construit sur le mot « vegetable » qui
signifie légume.
Désigne ceux qui ont une alimentation végétarienne – où le lait, les œufs, le
beurre et le miel sont permis – mais qui consomment occasionnellement de la
viande et du poisson.""" },
{ "word": "Formeret", "definition": """Nom masculin.
De « forme » fenêtre d’église en moyen français.
En architecture, se dit de l’arc dans l’axe de la voûte, recevant sa retombée.""" },
{ "word": "Fractal", "definition": """Adjectif et nom féminin.
Du latin « fractus » qui signifie brisé.
1- Un objet fractal est un objet mathématique qui sert à décrire des
objets de la nature dont les formes découpées laissent apparaître à
des échelles d’observation de plus en plus fine des motifs similaires.
Par exemple les éponges, les flocons de neige, les cristaux de glace.
On dit aussi une fractale.
2- Une dimension fractale est un nombre décimal qui traduit
l’occupation d’un objet dans l’espace et ce par opposition aux trois
dimensions traditionnelles de la géométrie euclidienne.""" },
{ "word": "Franc-alleu", "definition": """Nom masculin.
De « franc » qui signifie libre et du franque « al-ôd » qui signifie
totale propriété.
Dans l’histoire de la féodalité, se dit d’une terre de pleine
propriété, affranchie de toute obligation ou redevance, par opposition
à fief.""" },
{ "word": "Freinte", "definition": """Nom féminin.
Du latin frangere, qui a donné l’ancien français « frainte » participe
passé de « fraindre », qui signifie chose brisée, bruit de chose brisée.
Dans le commerce, perte de volume ou de poids subie par certaines
marchandises pendant la fabrication ou le transport.""" },
{ "word": "Fricative", "definition": """Adjectif dans l’expression : « Une consonne fricative »
Ou bien nom féminin.
Du latin fricatum supin de fricare qui signifie frotter.
En phonétique de l’articulation, se dit d’une consonne dont
l’expression comporte une constriction au moment de l’articulation
avec un effet de frottement ou de souffle.
La friction est obtenue par la position anatomique respective que
peuvent prendre les lèvres, la langue, les dents et le voile du palais
au moment de l’articulation.
Par exemple la consonne « F » est une fricative dont le son est obtenu
par un certain rapprochement des dents contre les lèvres. De même pour
le « V ».
Le « F » et le « V » sont des fricatives dento-labiales.""" },
{ "word": "Fuligineux", "definition": """Adjectif.
Du latin « fuliginosus » qui provient de « fuligo » qui signifie suie.
Qui donne de la suie, qui évoque la suie ou qui en a la couleur.
Au sens figuré se dit de ce qui est d’une obscurité épaisse.""" },
{ "word": "Fuligule", "definition": """Nom masculin.
Du latin « fuligo » qui signifie suie, par allusion au plumage terne de ce canard.
Canard plongeur de la famille des anatidés dont le corps est rond et trapu.
Le morillon et la macreuse sont des fuligules.""" },
{ "word": "Fulminer", "definition": """Verbe intransitif ou transitif.
Du latin « fulminare » qui signifie lancer la foudre.
En tant que verbe intransitif.
1- Lancer la foudre.
2- Se laisser aller à une violente explosion de colère. Se répandre en
menaces ou en reproches.
3- En chimie, faire explosion. La nitroglycérine fulmine violemment par le choc.
En tant que verbe transitif.
1- En droit canon, lancer une condamnation dans les formes. Par
exemple, lancer un anathème.
2- Par extension, formuler avec véhémence, des reproches, des imprécations.""" },
{ "word": "Fumeterre", "definition": """Nom féminin.
Du latin « fumus terrae » qui signifie fumée de la terre, parce que
selon Olivier de Serres, son jus fait pleurer les yeux comme la fumée.
Plante de la famille des fumariacées dont les feuilles sont très
découpées et dont les feuilles sont roses.
Une des variétés, la fumeterre officinale est utilisée comme dépuratif.""" },
{ "word": "Fuscine", "definition": """1- Nom féminin.
Du latin « fuscina » qui signifie fourche à trois dents, trident.
Dans l’Antiquité romaine, fourche à trois dents des pêcheurs et
emblème de Neptune, dieu de la mer.
2- Nom féminin.
Du latin « fuscus » qui signifie noir.
En biochimie, pigment noir de la rétine.""" },
{ "word": "Fustiger", "definition": """Verbe transitif.
Du latin « fustigare » issu de « fustis » qui signifie bâton.
-Anciennement, corriger à coups de bâton.
-Dans un sens moderne, blâmer ou stigmatiser.""" },
{ "word": "Gabardine", "definition": """Nom féminin.
De l’ancien français « gaverdine » qui signifie manteau, de l’allemand
« Wallevart » qui signifie pèlerinage.
1- Tissu croisé de laine ou de coton à fines côtes sur l’endroit.
2- Imperméable en gabardine.""" },
{ "word": "Gabbro", "definition": """Nom masculin.
Mot florentin. Peut-être le nom d’un village toscan.
Roche éruptive composée de plagioclase et de pyroxène.""" },
{ "word": "Gabegie", "definition": """Nom féminin.
De l’ancien français « gaber » qui signifie railler de l’ancien
scandinave « gabb » qui signifie raillerie.
Désordre qui résulte d’une organisation défectueuse.""" },
{ "word": "Gabier", "definition": """Nom masculin.
Du moyen français « gabie » qui signifie demi-hune, issu de l’ancien
provençal « gabia » qui signifie cage.
Matelot chargé de l’entretien et de la manœuvre des voiles et du gréement.""" },
{ "word": "Gades", "definition": """Nom masculin pluriel.
Du grec « gados » qui signifie morue.
En zoologie, famille de poissons (on dit aussi gadiformes ou gadidés)
généralement marins. Ils vivent dans des eaux froides ou tempérées et
sont péchés activement.
Les cabillauds ou morues, les églefins, les merlans, les merlus, les
lieus, les tacauds sont des gades.""" },
{ "word": "Galerne", "definition": """Nom féminin.
Mot de l’Ouest probablement gaulois.
Terme de marine. Le vent de galerne ou la galerne est un vent
d’ouest-nord-ouest.""" },
{ "word": "Galgal", "definition": """Nom masculin.
Du redoublement du gaélique « gal » qui signifie caillou.
En archéologie, tumulus celtique renfermant une crypte.
Le galgal date du néolithique. C’est un dolmen recouvert d’un
monticule de pierres.
Au pluriel on écrit des « galgals ».""" },
{ "word": "Galibot", "definition": """Nom masculin.
Mot picard issu de « galibier » qui signifie polisson.
Jeune manœuvre travaillant au  service des voies dans les galeries de mines.
Par exemple: « Les galibots devaient se reposer, car ils ne répondaient
ni l’un ni l’autre. » Germinal Emile Zola""" },
{ "word": "Galipot", "definition": """Nom masculin.
Altération de « garipot » qui signifie pin résineux et dont l’origine
est inconnue.
1- Matière résineuse qui exsude en hiver des incisions des pins et qui
est aussi appelée térébenthine de Bordeaux.
2- Mastic fait de résines et de matières grasses que l’on enduit à
chaud sur les surfaces à protéger de l’eau de mer.""" },
{ "word": "Galluchat", "definition": """Nom masculin.
Cuir de poisson cartilagineux des sélaciens (raie, requin, squale).
Ce mot à pour origine l’artisan Jean-Claude Galluchat, mort en 1774,
qui était un maître gainier de louis XV et de la Marquise de
Pompadour. Il fabriqua ses premiers cuirs de poisson à partir de cuir
de roussette et de cuir de raie.
Les cuirs de poisson étaient utilisés en ébénisterie, en gainerie et
en maroquinerie. On fabriqua des coffres, des malles et des poignées
d’épées.
Ce matériau fut ensuite oublié jusque dans les années 30 puis oublié à
nouveau jusqu’au milieu des années 80.
C’est une matière à la fois animale et minérale qui est difficile à tanner.
Le galuchat est recouvert de perles de silice et présente différents
aspects granuleux, brillant ou poncé.
Lorsqu’il est poncé il est alors lisse et laisse apparaître une
surface cloisonnée de petites cellules comme de petites rangées de
perles scintillantes.
Dès le VIII ème siècle les peaux de poissons étaient utilisées au
Japon. Les poissons étaient péchés en mer Rouge, en mer de Chine et
dans l’Océan Indien.
Il était autrefois appelé « requin de Chine ».
On retrouve une mention ancienne de « chien de mer » concernant des
peaux de poisson travaillées Faubourg St Antoine à Paris.
La chanson d’Aristide Bruant « Nini peau de chien » en est une évocation.
Aujourd’hui le galuchat vient principalement de Thaïlande. Il en
existe deux types : le gros grain et le petit grain.
Le petit grain provient de la roussette ou chien de mer et du requin
du Groenland.
Deux sortes de roussettes, une est aussi appelée « peau de chagrin » car
elle rétrécit beaucoup au séchage.
Le gros grain vient de la raie pastenague à la queue très longue qui
vit dans les mers européennes.""" },
{ "word": "Galvaniser", "definition": """Verbe transitif.
Du nom du savant Luigi Galvani qui montra l’existence d’une
« électricité animale » avec les muscles de la grenouille.
1- Électriser au moyen de la pile galvanique ou pile de Volta.
2- En particulier. Mettre les muscles en mouvement, soit pendant la
vie, soit peu de temps après la mort, au moyen de la pile galvanique.
3- Plonger un métal dans un bain de zinc fondu pour le recouvrir d’une
couche de ce métal et le préserver de l’oxydation. La première
technique, pour « protéger par une couche de zinc » était l’électrolyse.
Par exemple: « Ce toit de tôle a été galvanisé. »
4- Au figuré. Donner un encouragement, une impulsion. Stimuler.
Par exemple: Cette épreuve l’a galvanisé. Il en est sorti plus fort. »""" },
{ "word": "Gambit", "definition": """Nom masculin.
Nom masculin.
De l’italien « gambetto » qui signifie croc en jambe.
Aux échecs, coup qui consiste à sacrifier un pion, une pièce pour
s’assurer un avantage d’attaque ou de position.
On dit : »Jouer gambit ».""" },
{ "word": "Gamelan", "definition": """Nom masculin.
Du javanias « gamel » qui signifie instrument.
Orchestre traditionnel indonésien comprenant des gongs, des xylophones
et des tambours.""" },
{ "word": "Ganoïde", "definition": """Adjectif et nom masculin.
Du grec « ganos » qui signifie éclat.
En zoologie, des écailles ganoïdes sont caractérisées par une couche
épaisse d’émail brillant.
L’esturgeon possède des écailles ganoïdes. On disait qu’il faisait
partie des ganoïdes. Cet emploi du mot est désormais considéré comme
vieilli.""" },
{ "word": "Garum", "definition": """Nom masculin.
Du latin « garum » par le grec ancien « garon » qui signifiait chez les
anciens une sauce de très grand prix faite avec la saumure d’un
poisson que l’on suppose être le maquereau.
Dans l’Antiquité. Le garum était une sauce, principal condiment
utilisé à Rome dès la période étrusque et en Grèce antique (garos). Il
s’agissait de chair ou de viscère de poisson
voire d’huîtres ayant fermenté longtemps dans une forte quantité de
sel, afin d’éviter tout pourrissement. Il entrait dans la préparation
de nombreux plats auxquels il ajoutait un fort goût salé.
Le garum le plus réputé, dit garum des alliés, était à base de thon rouge.
La présence de sel inhibait la décomposition naturelle, la macération
se produisait probablement sous l’action des sucs digestifs du thon.
Il ne s’agissait donc pas d’une putréfaction.
Tous les garums étaient commercialisés dans des amphores de petite
taille en raison du prix du contenu.
Le garum aurait eu des conséquences néfastes sur la santé des
populations qui en consommaient. Il servait peut-être de vecteur aux
œufs du « ténia du poisson » qui est un parasite qui peut affecter les systèmes
nerveux et digestifs de son hôte.
La saveur du garum serait à rapprocher du nuoc-mâm vietnamien et de
celle de l’allec du surströmming suédois.
Le garum est à l’origine du pissalat, élaboré à partir de sardines et
d’anchois, consommé dans la région de Nice.""" },
{ "word": "Gattilier", "definition": """Nom masculin.
De l’espagnol « gatillo » altération de agno croisé avec « gato » qui
signifie chat.
Plante aussi appelée « agnus-castus ». Le mot castus signifie chaste.
Arbrisseau des régions méditerranéennes, de la famille des
verbénacées, qui aurait des vertus calmantes.""" },
{ "word": "Géhenne", "definition": """Nom féminin.
Du latin « gehenna » issu de l’hébreu ge -hinnom » qui signifie la vallée
de Hinnom, lieu situé près de Jérusalem.
1- Dans le Bible, séjour des parias.
2- Torture appliquée aux criminels ou supposés tels.
Souffrance massive, insupportable.""" },
{ "word": "Gémination", "definition": """Nom féminin.
Du latin « geminatio » qui signifie :
-Etat de ce qui est disposé par paire.
-Redoublement d’une syllabe dans la prononciation d’un mot. Par exemple la
fifille pour la fille.
-Pour ce qui concerne les classes dans l’enseignement, la gémination des classes
de garçons et de filles est synonyme de la mixité.
Ce mot a été entendu sur France Culture dans l’émission d’Emmanuel
Laurentin « La Fabrique de l’Histoire » sur la mixité dans l’enseignement le 19
février, dans la phrase suivante: »…la loi contre la gémination des écoles. »""" },
{ "word": "Génépi", "definition": """Nom masculin.
Mot d’origine savoyarde.
Plante sauvage d’altitude qui appartient aux composées.
Le génépi permettait de fabriquer l’absinthe.""" },
{ "word": "Géomancie", "definition": """Nom féminin.
Du latin « geomantia » qui signifie divination de la terre.
Divination à partir de terre, de poussière ou de cailloux.
« Le Vietnam est un pays qui fait attention à la géomancie » citation
extraite de l’émission d’Emmanuel Laurentin « La Fabrique de
L’histoire » sur France-Culture du vendredi 28 février 2014.""" },
{ "word": "Gibbeux", "definition": """Adjectif.
Du latin « gibbosus » issu de « gibbus » qui signifie bosse.
Se dit de ce qui a la forme d’une bosse.
Se dit aussi de ce qui est muni de plusieurs bosses. Par exemple: « Le
dos gibbeux des chameaux du désert. « """ },
{ "word": "Gibelin", "definition": """Adjectif.
De Weibelingen nom d’un empereur d’Allemagne.
Partisan des empereurs d’Allemagne, en Italie. """ },
{ "word": "Girandole", "definition": """Nom féminin.
De l’italien « girandola » diminutif de « giranda » qui signifie gerbe de feu.
Originellement du latin « girare » tourner.
Faisceau de plusieurs jets d’eau.""" },
{ "word": "Giroflée", "definition": """Nom féminin.
De « girofle » parce qu’elle a l’odeur des clous de girofle.
1- Plante herbacée de la famille des crucifères dont les fleurs sont
odorantes et les couleurs variées.
2- Au figuré et de manière familière. La giroflée à cinq feuilles est
une gifle qui laisse la marque des cinq doigts.""" },
{ "word": "Glaçure", "definition": """Nom féminin.
De l’allemand « glassur » qui signifie vernis de la porcelaine.
Préparation qui donne à un objet un aspect vitrifié ou glacé.
Certaines porcelaines chinoises sont recouvertes d’une glaçure.""" },
{ "word": "Glaïeul", "definition": """Nom masculin.
Du latin « gladiolus » diminutif de « gladius » qui signifie glaive.
Plante herbacée, de la famille des iridacées, à feuilles longues et
pointues et à grandes fleurs décoratives disposées en épi le long
d’une tige dressée.""" },
{ "word": "Glairer", "definition": """Verbe transitif.
De « glaire » issu du latin « clarus » qui signifie clair.
En reliure, technique qui consiste à frotter au blanc d’œuf et à
l’alcool (glaire ou glairure) la reliure en cuir d’un livre pour la
faire briller.""" },
{ "word": "Glatir", "definition": """Verbe intransitif.
Du latin « glattire » qui signifie japper.
1- Dans un langage vieilli: Aboyer, pousser des aboiements répétés.
2- Pousser son cri en parlant de l’aigle.""" },
{ "word": "Glose", "definition": """Nom féminin.
Du latin « glosa » qui signifie mot qui a besoin d’être expliqué, issu
du grec « glôssa » qui signifie langue.
1- Annotation entre les lignes ou en marge d’un texte pour expliquer
un mot difficile ou éclaircir un passage obscur.
 Par extension, commentaire, note explicative.
2- Commentaire oiseux ou malveillant.""" },
{ "word": "Glossolalie", "definition": """Nom féminin.
Du grec « glôssa » qui signifie langue et « lalein » qui signifie parler.
En religion, grâce particulière se manifestant par un don surnaturel des langues.
En psychologie, langage de certains malades mentaux, constitué de néologismes organisés
selon une grammaire rudimentaire. """ },
{ "word": "Glyphe", "definition": """Nom masculin.
Du grec « gluphê » qui signifie ciselure.
Trait gravé en creux qui peut être la représentation graphique d’un
signe typographique.
Par exemple: « Un glyphe gravé dans la roche est appelé un pétroglyphe. »""" },
{ "word": "Glyptothéque", "definition": """Nom féminin.
Du grec « gluptos » qui signifie gravé et « thêkê » qui signifie coffre,
lieu de dépôt.
Cabinet de pierres gravées, de camées mais aussi par extension de sculptures.
Par exemple la glyptothéque de Munich.""" },
{ "word": "Gnome", "definition": """Nom masculin.
Du latin « gnomus » qui signifie intelligent.
A l’origine, petit génie, laid et difforme qui, selon le Talmud et les
Kkabbalistes, habite à l’intérieur de la terre dont il garde les
trésors.
Peut se dire aussi d’un homme très petit et contrefait.""" },
{ "word": "Gnomique", "definition": """Adjectif.
Du grec « gnomikos » qui signifie sentencieux.
Se dit de ce qui se présente sous forme de sentences.
La poésie gnomique, est un ensemble de maximes, de préceptes et de
conseils pratiques versifiés.""" },
{ "word": "Gnôthi seauton", "definition": """Nom masculin invariable.
Du grec qui signifie « Connais-toi toi-même ».
Maxime grecque de Socrate.
On dit: « Le gnôthi seauton de Socrate ».""" },
{ "word": "Godiveau", "definition": """Nom masculin.
De « godebillaux » d’un radical « god » qui signifie enflé et « beille » qui
signifie ventre du latin « botulus » qui signifie boyau.
Boulettes de viande hachée de forme oblongue, le plus souvent pochées
à l’eau bouillante salée.""" },
{ "word": "Goétie", "definition": """Nom féminin.
Du grec « goêtela » qui signifie sorcellerie.
Dans l’Antiquité, magie incantatoire par laquelle on invoquait les
génies malfaisants.""" },
{ "word": "Gogo (A)", "definition": """Nom masculin.
De l’ancien français « gogue » qui signifie réjouissance.
Familièrement, signifie abondamment, à discrétion ou à volonté.
Par exemple, servir du whisky à  gogo.""" },
{ "word": "Golem", "definition": """Nom masculin.
D’un mot hébreu, qui signifie, masse informe, embryon.
Dans la tradition juive d’Europe orientale, être artificiel à forme
humaine, à qui l’on donne momentanément la vie, en fixant sur son front
le verset d’un texte biblique.""" },
{ "word": "Gomorrhéen", "definition": """Adjectif.
De la ville de « Gomorrhe ».
En littérature, se dit de ce qui est relatif à la sexualité féminine.""" },
{ "word": "Gon", "definition": """Nom masculin.
Du latin « gônia » qui signifie angle.
En métrologie, unité de mesure d’angle plan.""" },
{ "word": "Gondole", "definition": """Nom féminin.
Du vénitien « gondola » issu du grec byzanthin « kontoura », de
« kontouros » qui signifie à courte queue.
1- Barque vénitienne à un seul aviron, longue et plate, aux extrémités
relevées et recourbées.
2- Meuble servant à présenter la marchandise dans un magasin à libre-service.""" },
{ "word": "Gongorisme", "definition": """Nom masculin.
Du nom du poète espagnol Gongora 1561-1627.
Préciosité, recherche dans le style par abus d’images et des métaphores.""" },
{ "word": "Gonochorisme", "definition": """Nom masculin.
Du grec « gonos » qui signifie génération et « khôrismos » qui signifie séparation.
En biologie, séparation complète des sexes dans des individus distincts.
Le contraire est l’hermaphrodisme.""" },
{ "word": "Gradus", "definition": """Nom masculin.
Abréviation de  » gradus ad parnassum » qui signifie degré vers le parnasse.
Dictionnaire de prosodie, c’est à dire des techniques qui concernent
l’écriture de la poésie, latine.
Par extension c’est un dictionnaire poétique.""" },
{ "word": "Grantha", "definition": """Nom masculin.
Mot d’origine indienne.
Nom d’un caractère d’écriture utilisé en Inde.""" },
{ "word": "Grégeois", "definition": """Adjectif masculin.
De l’ancien français « grégois » qui signifie grec issu du latin « græcus ».
Le « FEU GRÉGEOIS » est une arme incendiaire,plus particulièrement
marine, qui utilisait un mélange de soufre, de poix, de salpêtre
etc…et que les Byzantins utilisaient à la guerre.
La recette a été gardée secrète, à tel point qu’aujourd’hui, elle est
perdue. On peut cependant spéculer sur une partie de ces composantes.
Par exemple: »Le terme de feu grégeois, était utilisé pour toutes les
armes incendiaires, mais ce sont les byzantins qui en détenaient la
paternité. Les autres armes incendiaires des autres peuples
étaient des pâles copies du feu grégeois Byzantin, originel.""" },
{ "word": "Grimaud", "definition": """Nom masculin.
Du franque »grima » qui signifie masque.
1- Dans un sens vieilli, écolier des mauvaises classes, élève ignorant.
2- Homme inculte ou pédant. Mauvais écrivain.
Par exemple: « Les rayons des librairies contiennent aussi des œuvres
de grimaud. »""" },
{ "word": "Grog", "definition": """Nom masculin.
De l’anglais « grog »  qui vient du sobriquet donné à l’amiral Vernon
vers 1776 et qui était « Old Grog » parce qu’il était habillé de
gros-grain (grogram). Il obligeait les marins sous ses ordres,
à étendre d’eau leur ration de rhum.
Boisson faite d’eau chaude sucrée et d’eau-de-vie ou de rhum.""" },
{ "word": "Grume", "definition": """Nom féminin.
Issu du latin « gluma »  qui signifie cosse, écorce.
1- Grain de raisin.
2- Ecorce qui reste sur le bois coupé non équarri. Par exemple on dit
le bois de grume ou en grume pour un bois recouvert de son écorce.
Nom qui est donné à une pièce de bois non équarrie.""" },
{ "word": "Guarani", "definition": """Adjectif et nom.
Mot d’origine espagnole.
1-En tant qu’adjectif. Qui a trait aux indiens Guarani ou à leur culture. .
En tant que nom masculin. Le guarani est la langue des guaranis. C’est
une langue amérindienne agglutinante de la famille tupi-guarani,
parlée au Paraguay, dans le nord de
l’Argentine dans l’est de la Bolivie ainsi que dans le sud et le
nord-est du Brésil. Elle serait parlée par cinq millions de personnes.
2- En tant que nom masculin.
Unité monétaire du Paraguay.""" },
{ "word": "Guelfe", "definition": """Nom masculin.
De Welf, nom d’une famille d’Allemagne qui prit le parti des papes.
Partisan du pape contre l’empereur du Saint Empire romain germanique dans l’Italie médiévale.
Les guelfes étaient les ennemis des gibelins. """ },
{ "word": "Guillaume", "definition": """Nom masculin.
L’origine de ce mot est incertaine, elle provient peut-être du
patronyme d’un utilisateur de l’outil.
Rabot étroit qui permet de pousser des rainures ou des moulures en menuiserie.""" },
{ "word": "Guimpe", "definition": """Nom féminin.
Du franque « wimpil » issu de l’allemand « Wimpel » qui signifie banderole.
1- Morceau de toile qui couvre la tête et encadre le visage des religieuses.
2- Chemisette de femme sans manches, au col montant en tissu léger.
Plastron que l’on porte sur une robe décolletée ou sur une veste de tailleur.""" },
{ "word": "Guivre", "definition": """Nom féminin.
Du latin « vipera » qui signifie vipère avec influence germanique pour
le gu- à rapprocher du mot « vouivre » qui en est une variante.
Animal fantastique ayant un corps de serpent, des ailes de
chauve-souris et des pattes de pourceau.
On trouve cet animal fabuleux dans les contes populaires et sur les blasons.""" },
{ "word": "Guzla", "definition": """Nom féminin.
Mot emprunté au serbo-croate « gusle » de même sens. Ce mot existe dans
toutes les langues slaves peut-être par l’intermédiaire de l’italien
« gusla ».
Instrument de musique des Illyriens, qui habitaient des territoires
qui correspondent à l’ouest de la Croatie, la Slovénie, la
Bosnie-Herzégovine, le Kosovo, le Monténégro et l’Albanie.
C’est un violon à une seule corde en crin qui sert à accompagner les
chants nationaux.
La Guzla est un texte de Prosper Mérimée.""" },
{ "word": "Gymnosophiste", "definition": """Nom masculin.
Du grec « gymno » qui signifie nu et « sophia » qui signifie sagesse.
Philosophe indien qui ne consommait jamais de viande et se consacrait
à la contemplation.""" },
{ "word": "Gypaète", "definition": """Nom masculin.
Du grec »gups » qui signifie vautour et « aetos » qui signifie aigle.
Grand oiseau rapace nocturne de la famille des falconidés ou des
accipitridés. Il est parfois nommé « vautour des agneaux ».
Son bec est long et crochu, sa queue est large et longue et ses ailes
sont vastes.
Il se nourrit d’os, qu’il casse en les lâchant du ciel. Il en mange
ensuite les fragments et la moëlle.
On l’appelle aussi le « casseur d’os ».
Il vit dans toutes les montagnes jusqu’à la mer (Europe, Eurasie, Afrique).
C’est un oiseau protégé dont il existe peu d’exemplaires en France.
Des specimens sont progressivement réintroduits par la Ligue de
Protection des Oiseaux.""" },
{ "word": "Gyrovague", "definition": """Nom masculin.
Du grec « guros » qui signifie cercle et du latin vagus qui signifie errant.
Nom donné dans les premiers temps du monachisme a des moines qui changeaient de
lieu tous les trois ou quatre jours et qui vivaient d’aumônes.""" },
{ "word": "Hadith", "definition": """Nom masculin.
D’un mot arabe qui « signifie conversation, récit ».
Dans la religion musulmane, se dit du recueil des actes et des paroles
du prophète Mahomet.
Par exemple: « Les hadiths complètent le Coran.""" },
{ "word": "Halbi", "definition": """Nom masculin.
Du néerlandais « hââlbier » qui signifie petite bière.
En Normandie, boisson faite de pommes et de poires fermentées.""" },
{ "word": "Haliple", "definition": """Nom masculin.
Du grec « haliplous » qui signifie qui nage en mer.
Insecte aquatique de la famille des coléoptères qui vit dans les eaux
douces et saumâtres.""" },
{ "word": "Halitueux", "definition": """Adjectif.
Du latin « halitus » qui signifie vapeur.
Dans une acception vieillie, une peau halitueuse est une peau chaude
et moite de sueur.""" },
{ "word": "Halloween", "definition": """Nom masculin.
Mot anglais issu de l’expression abrégée: « All Hallow Even » qui
signifie veille de la Toussaint.
Ce terme est un anglicisme. au Canada et aux Etats-Unis, fête annuelle
qui a lieu le 31 octobre, comparable à la mi-carême, à l’occasion de
laquelle les enfants déguisés et masqués viennent présenter des sacs
ou des paniers pour qu’on y dépose des friandises.
Par exemple: « La fête d’Halloween se répand en Europe, alors qu’elle
était plutôt issue d’une tradition nord-américaine. »""" },
{ "word": "Hanap", "definition": """Nom masculin.
Du latin »hanappus » issu du franque « hnapp » par le haut allemand
« hnapf » qui signifie vase.
L’arabe offrirait aussi une possible étymologie par « hanab » qui
signifie coupe mais le mot arabe ne pourrait être venu que par les
croisades, or hanap se rencontre dans les « Gloses de Cassel » qui sont
antérieures aux croisades.
Anciennement, grand vase à boire  en métal, monté sur un pied et muni
d’un couvercle.""" },
{ "word": "Hangeul", "definition": """Nom masculin.
Du coréen « geul » qui signifie langue et « han » qui signifie proverbes.
Ecriture des proverbes.
Alphabet officiel du coréen. C’est un système d’écriture qui est
considéré comme le plus scientifique au monde. Il appartient à la
famille des langues altaïques,- du mont Altaïr- c’est à dire des
langues turques et mongoles.""" },
{ "word": "Haplologie", "definition": """Nom féminin.
Issu du grec « haplo » qui signifie simple et « logos » qui signifie discours.
En linguistique, amuïssement dans un mot d’un ou plusieurs phonèmes
identiques ou apparentés.
Par exemple, l’ancien français contre-rôle a donné contrôle.
Tragico-comique a donné tragi-comique.
Clermont-Ferrand est la forme simplifiée de Clermont-Montferrand.""" },
{ "word": "Harissa", "definition": """Nom masculin ou féminin.
De l’arabe « harisa » issu de harasa » qui signifie piler.
Purée de piments, très relevée, utilisée comme assaisonnement ou comme
condiment dans la cuisine du Maghreb.
Par exemple, on peut accompagner le couscous de harissa.""" },
{ "word": "Harle", "definition": """Nom masculin.
Mot issu d’un dialecte du Nivernais.
Oiseau aquatique de la famille des ansériformes, anatidés, voisin du canard.""" },
{ "word": "Harmattan", "definition": """Nom masculin.
Mot d’une langue africaine.
Vent qui souffle depuis l’est (alizé) sur le Sahara et l’Afrique occidentale.""" },
{ "word": "Hassidisme", "definition": """Nom masculin.
De l’hébreu « hassid » qui signifie pieux.
Au Moyen-âge, courant religieux juif en Allemagne.
A l’époque moderne, courant religieux juif qui commença en Pologne au
XVIIIème siècle et qui s’inspira de la Kabbale.
Les tenants de ce courant sont appelés des hassidim.""" },
{ "word": "Hasté", "definition": """Adjectif.
Du latin « hast » qui qui signifie lance, hampe de lance.
En botanique, se dit d’une feuille ou d’un pétale qui a la forme d’un
fer de lance.""" },
{ "word": "Hâve", "definition": """Adjectif.
Du francique « haswa » qui signifie gris comme le lièvre.
Se dit d’un être au visage ou au corps amaigri par la faim, la
fatigue, la souffrance.
Par exemple: « La captivité lui avait donné un visage hâve, presque
sans expression. »""" },
{ "word": "Haveneau", "definition": """Nom masculin.
De l’ancien scandinave « hafr-net
Vocabulaire de la pêche. Filet utilisé sur les plages sablonneuses
pour la pêche à la crevette et aux poissons plats.
Par exemple: « Ce matin, le pêcheur répare son haveneau qui est déchiré
par endroits. »""" },
{ "word": "Hectique", "definition": """Adjectif.
Du grec « hektikos » qui signifie habituel.
En médecine une fièvre hectique est une fièvre des états septicémiques
graves caractérisées par de grandes oscillations de températures
accompagnées de frissons violents et d’une abondante transpiration.
Cette fièvre peut se produire dans les crises de paludisme.""" },
{ "word": "Heiduque", "definition": """Nom masculin.
Du hongrois « hajduk » qui signifie boyard.
Mot ancien et dont l’usage est vieilli.
1- Fantassin hongrois.
2- Domestique vêtu à la hongroise en Europe.
3- Patriote chrétien des Balkans.
On disait aussi haïdouc ou haïdouk.""" },
{ "word": "Heimatlos", "definition": """Adjectif et nom masculin.
Mot allemand qui signifie apatride.
Mot rare. Se dit d’une personne qui a perdu sa nationalité d’origine
sans en acquérir une nouvelle.""" },
{ "word": "Hélépole", "definition": """Nom féminin.
Du grec « helepolis » issu de « helein » qui signifie prendre et « polis »
qui signifie ville.
Machine de guerre en forme de tour mobile qui était utilisée par les
Anciens pour s’élever à la hauteur des remparts, lors des combats.""" },
{ "word": "Héliotropisme", "definition": """Nom masculin.
Du grec « helios » qui signifie soleil et « tropéin » qui signifie tourner.
Propriété qu’ont certains végétaux ou animaux fixés de se tourner vers
la lumière solaire, c’est l’héliotropisme positif. Ou de s’en
détourner c’est l’héliotropisme négatif.""" },
{ "word": "Hellébore", "definition": """Nom masculin.
Variante du mot: Ellébore.
Du latin « helleborus » issu du grec « helein » qui signifie faire mourir
et « bora » qui signifie nourriture. C’est une plante vénéneuse.
Plante herbacée de la famille des renonculacées vivace dont la racine
a des propriétés vermifuges et purgatives et qui passait autrefois
pour guérir la folie et la mélancolie.
Plusieurs espèces sont remarquables: L’hellébore fétide ou pied de
griffon. L’hellébore noir ou rose de Noël est une espèce ornementale.
L’hellébore blanc appelé aussi vératre.
La locution:  » Avoir besoin de deux ou de six ou de quelques grains
d’hellébore. » signifie être fou.
Chez les anciens grecs, on appelait l’hellébore « anticyricon ». Dans la
Rome antique le proverbe « Mettre le cap sur Anticytre » signifiait
montre des signes de folie.
Anticytre était une ville antique qui était réputée pour produire une
plante médicinale efficace pour guérir la folie.
Dans le calendrier Républicain le 11 ème jour du mois de Pluviôse
était le jour de l’hellébore.
Dans la fable « Le lièvre et la tortue » de Jean de La Fontaine, un vers
mentionne l’ellébore:
« Ma commère il faut vous purger avec quatre grains d’ellébore » [si
vous n’êtes pas sage].
Dans Harry Potter et l’Ordre du Phénix l’ellébore est mentionné.
Dans le légende on croyait que l’ellébore était utilisé par les
sorcières pour convoquer les démons.""" },
{ "word": "Hendiadys", "definition": """Nom masculin.
Du grec « hen dia duoin » qui signifie une chose au moyen de deux mots.
Figure de style qui consiste à dissocier en deux noms coordonnés une
expression unique. Nom et adjectif ou nom et complément.
Par exemple: « J’aime bien cet ami et sa loyauté » [la loyauté de cet ami]""" },
{ "word": "Hère", "definition": """A- Nom masculin.
De l’allemand « Herr » qui signifie seigneur, dans un emploi ironique;
ou bien de « haire » qui signifie misère, par métonymie (la partie
désignant le tout).
Dans un sens vieilli, homme misérable.
L’expression moderne qui emploie ce mot est « pauvre hère ».
B- Nom masculin.
Du néerlandais « hert » qui signifie cerf.
En vènerie, jeune cerf de plus de six mois, qui n’est pas encore daguet.""" },
{ "word": "Herméneutique", "definition": """Nom féminin.
Du grec « hermêneutikos » qui provient de « hermêneuein » qui signifie
interpréter.
Qui concerne l’interprétation de textes, de discours ou de signes.""" },
{ "word": "Hétairie", "definition": """Nom féminin.
Du grec « hetaireiae qui signifie association d’amis.
Dans l’antiquité grecque, association plus ou moins secrète, à
caractère généralement politique.
A l’époque moderne, société politique ou littéraire de la Grèce du
XIXème siècle.""" },
{ "word": "Heuristique", "definition": """Adjectif.
Du grec heristikein qui signifie trouver.
Qui permet la découverte .
C’est aussi une partie de la science qui consiste en la découverte des faits.
Une méthode heuristique permet à l’élève de découvrir ce que l’on
souhaite lui enseigner.""" },
{ "word": "Hiérarchie", "definition": """Nom féminin.
Du grec « hieros » qui signifie sacré et « archos » commencement ou « ce
qui est en premier » ou « arkhé » qui signifie pouvoir, commandement.
1- Ordre et subordination des chœurs des anges. Ordre et subordination
des degrés de l’état ecclésiastique.
2- Organisation sociale dans laquelle chacun se trouve dans une série
ascendante de pouvoirs ou de situation.""" },
{ "word": "Hierodule", "definition": """Nom masculin.
Du grec « hieoro » qui signifie sacré et « doulos » qui signifie esclave.
Dans l’antiquité grecque, esclave employé au service d’un temple.""" },
{ "word": "Hierogrammate", "definition": """Nom masculin.
Du grec « hierogrammateus, issu de « hieros » qui signifie sacré et
« grammateus » qui signifie scribe.
Dans l’Antiquité égyptienne, scribe au service d’un temple. Ou bien
prêtre qui interprétait les textes sacrés.""" },
{ "word": "Hiérologie", "definition": """Nom féminin.
Du grec « hieros » qui signifie sacré et « logos » qui signifie discours.
Etude ou connaissance des différentes religions.
Non donné à la bénédiction du mariage chez les chrétiens grecs et
chez les juifs.""" },
{ "word": "Himation", "definition": """Nom masculin.
Du grec « himatiou » de même sens.
En Grèce antique, manteau sans manche, ample et enveloppant comme un
châle, qui s’enroule sur l’épaule et ne comporte pas d’attache.""" },
{ "word": "Hippiatre", "definition": """Nom masculin.
Du grec « hippos » qui signifie cheval et « iatros » qui signifie médecin.
Dans un sens vieilli, vétérinaire spécialisé des maladies du cheval.""" },
{ "word": "Hippomancie", "definition": """Nom féminin.
Du grec « hippos » qui signifie cheval et « manteia » divination.
Divination à partir du hennissement et du comportement des chevaux
sacrés en usage chez les peuples Celtes.""" },
{ "word": "Hircin", "definition": """Adjectif.
Du latin « hircus » qui signifie bouc.
Qui tient ou vient du bouc.
Par exemple : « une odeur hircine ».""" },
{ "word": "Hirudine", "definition": """Nom féminin.
Du grec « hirudo » qui signifie sangsue. La sangsue a le nom taxinomique
de « Hirudo medicinalis »
En biochimie, c’est une substance sécrétée par les glandes salivaires
de la sangsue et qui possède des propriétés anticoagulantes.
Cette capacité anticoagulante de la sangsue est connue depuis
l’Antiquité. Elle permettait les saignées et évitait la formation de
caillots.
La sangsue fut excessivement utilisée à cette fonction anticoagulante.
Aujourd’hui, elle est une espèce protégée.
Par exemple: »L’hirudine bloque la coagulation en inhibant l’action de
la thrombine, un des facteurs de la coagulation sanguine. Ce blocage
permet à la sangsue de se nourrir. »""" },
{ "word": "Hispide", "definition": """Adjectif au masculin ou au féminin.
Du latin « hispidus » qui signifie hérissé de poils.
1- En botanique s’applique à un organe hérissé de poils rudes et
espacés. Par exemple une tige hispide.
Ce caractère se rencontre souvent chez les boraginacées.On peut citer
Pentaglottis sempervirens ou Anchusa sempervirens qui est la Buglosse
toujours verte.
Cette plante est utilisée en cuisine: on en fait des salades.
2- En littérature et assez rarement. S’applique à un individu portant
une barbe et des cheveux raides d’un apect repoussant.
3- En littérature et très rarement. Se dit d’une persionne à l’humeur
difficile et au caractère revêche.""" },
{ "word": "Hoax", "definition": """Nom masculin.
Ce mot d’origine anglaise est apparu à la fin du XVIIIème siècle. Il
est une contraction du verbe « hocus » qui signifie tricher, imposer à
quelqu’un ou bien embrouiller à l’aide d’une liqueur apte à droguer.
« Hocus » de « hocus pocus ». Cette expression est un raccourci de la phrase
« Hocus pocus, tontus talontus, vade celeriter jubeo. »
Cette phrase est un charabia en latin de cuisine, c’est à dire un
jargon qui imite le latin; elle permettait à un prestidigitateur de
distraire son public pendant un tour de magie.
En français, c’est un canular informatique.
En anglais, c’est un mensonge créé de toute pièce.""" },
{ "word": "Hoir", "definition": """Nom masculin.
Du latin « heres, herem » qui signifie héritier.
Dans un sens vieilli, héritier, légataire.""" },
{ "word": "Holisme", "definition": """Nom masculin.
Du grec « holos » qui signifie totalité, entier.
Ce mot est un néologisme forgé en 1926, par le philosophe sud-africain
Jan Christian Smuts.
Théorie selon laquelle un homme est un tout qui ne peut être expliqué
par ses différentes composantes séparément, qu’elles soient physique,
physiologique ou psychique. 
En d’autres termes, l’homme y est envisagé dans sa globalité.
Système d’explication globale.
La pensée holiste s’oppose à la pensée réductionniste qui tend à
expliquer un phénomène en le divisant en parties.""" },
{ "word": "Hologamie", "definition": """Nom féminin.
Du grec « holos » qui signifie entier et « gamos » qui signifie mariage.
Chez les algues, les protozoaires et les champignons qui sont des
organismes inférieurs. Mode de reproduction sexuée par union de deux
cellules végétatives qui se comportent comme des cellules sexuelles.""" },
{ "word": "Homérique", "definition": """Adjectif.
Du latin « homericus » de l’écrivain grec Homère.
1- Qui a rapport ou qui appartient à Homère. Par exemple: « L’Iliade et
l’Odyssée. »
2- Qui est digne d’Homère et de ses personnages. Par exemple: Une
lutte homérique.
Locution(1836): Un rire homérique est un rire bruyant comme celui
qu’Homére prêtait aux dieux de l’Olympe.""" },
{ "word": "Homilétique", "definition": """Adjectif.
Du latin « homileticus » issu de homélie.
En religion, dans un sens didactique et vieilli, partie de la
rhétorique qui traite de l’éloquence de la chaire.
C’est à dire qui concerne la prédication religieuse.""" },
{ "word": "Homocerque", "definition": """Adjectif.
De « homo » qui signifie le même, semblable, et « kerkos » qui signifie queue.
En zoologie, qui a deux lobes égaux en parlant de la nageoire caudale
des poissons.
Par exemple on dit que les carpes sont homocerques.""" },
{ "word": "Homoscédatiscité", "definition": """Nom féminin.
Du grec « homo » qui signifie semblable, le même et  « skédastikos » qui
signifie dispersé.
Variance statistique, c’est à dire moyenne des carrés des écarts d’une
grandeur par rapport à sa valeur moyenne, présentant une même
dispersion de l’erreur quelle que soit la condition testée.""" },
{ "word": "Hoplite", "definition": """Nom masculin.
Du latin « hoplites » issu du grec « hoplon » qui signifie arme.
Dans l’antiquité grecque, se disait d’un fantassin lourdement armé.""" },
{ "word": "Horion", "definition": """Nom masculin le plus souvent pluriel.
Issu de l’ancien français « oreillon » qui signifie coup sur l’oreille.
Coups violents.""" },
{ "word": "Horst", "definition": """Nom masculin.
Du mot allemand « horst » qui signifie butoir, élévation de terrain, colline.
En géologie, structure tectonique formée de terrains soulevés entre
des failles parallèles entre elles.
Par exemple: »Les monts du Forez sont un horst qui sépare l’Allier de la Loire. »""" },
{ "word": "Hortillonnage", "definition": """Nom masculin.
Mot picard issu de « (h)ortillon » qui signifie jardinier. De
« ortillier » qui signifie cultiver.
En Picardie, ce sont des jardins flottants situés sur d’anciens
marécages et utilisés pour la culture des légumes.
C’est aussi, le mode de culture qui y est pratiqué.
Par exemple: « Les hortillonnages sont entrecoupés de canaux, les rieux. »""" },
{ "word": "Hosanna", "definition": """Nom masculin.
Du latin « hosanna » issu de l’hébreu « hôsanna » de « hosha » qui signifie
sauve accompagné de la déprécation « na » qui signifie s’il te plaît.
Il serait proche de l’expression « hoshya’ na  » qui signifie: de grâce,
secours-nous, sauve[-nous] donc.
1- Acclamation religieuse utilisée dans certaines prières juives.
Hymne catholique qui chante la joie, le jour des Rameaux, au souvenir
de l’entrée de Jésus dans Jérusalem.
2-Chant de joie ou cri de triomphe.""" },
{ "word": "Hospodar", "definition": """Nom masculin.
On dit « hospodar » ou « gospodar ».
Du slave « gospod » qui signifie seigneur et « dar » qui signifie don ou
offrande. Le seigneur qui donne.
Ancien titre donné aux princes vasaux du sultan de Turquie placés à la
tête des provinces roumaines.""" },
{ "word": "Hottentot", "definition": """Adjectif et nom.
Mot hollandais qui signifie « bégayeur ».
Relatif à une population de pasteurs nomades de l’Afrique du Sud-Ouest
(parfois appliqué abusivement aux Bochimans leurs voisins).
Une Vénus hottentote était un type de femme bochiman dont les fesses
étaient énormes.""" },
{ "word": "Houppier", "definition": """Nom masculin.
De « houppe » issu du franque « huppo » qui signifie touffe.
En arboriculture, sommet d’un arbre ébranché.
Par extension, cet arbre.""" },
{ "word": "Huit-reflets", "definition": """Nom masculin.
De huit et reflet.
Chapeau de soie, haut de forme très brillant, sur le fond duquel on
peut distinguer huit reflets.""" },
{ "word": "Humilité", "definition": """Nom féminin.
Du latin « humilitas » issu de « humus » qui signifie terre.
Attitude morale de faiblesse ou d’insuffisance qui pousse une personne
à s’abaisser de manière volontaire en réprimant une attitude
orgueilleuse.""" },
{ "word": "Hyades", "definition": """Nom féminin pluriel.
Du grec « Huades » qui signifie nymphes changées astres, issu de « huein »
qui signifie pleuvoir.
En astronomie, ensemble des sept étoiles qui forment le front de la
constellation du Taureau.""" },
{ "word": "Hydrargyre", "definition": """Nom masculin.
Du grec « hydrarguros » issu de « hudôr » qui signifie eau et « arguros »
qui signifie argent.
En chimie, ancien nom du mercure de symbole Hg.""" },
{ "word": "Hypallage", "definition": """Nom féminin.
Du grec « hupallagê »  qui signifie échange, interversion.
Figure de style qui consiste à attribuer à un mot ce qui convient à un
autre, sans que cela empêche de comprendre le sens.
Dans ce vers de Baudelaire:  » Ses yeux polis sont faits de minéraux
charmants » il y a hypallage d’adjectif, on aurait du avoir:  » Ses yeux
charmants et minéraux polis. »
Autre exemple: dans « Notre-Dame de Le mot « Lorette » transporte le nom
du quartier à la personne.""" },
{ "word": "Hyperonyme", "definition": """Nom masculin.
Du grec « hyper » qui signifie au-dessus et « ônumos », de « onoma » qui
signifie nom.
Terme dont le sens inclut d’autres mots. Par exemple poisson est
l’hyperonyme de daurade.
Le mot hyperonyme est à rapprocher du mot générique.""" },
{ "word": "Hypnagogique", "definition": """Adjectif.
Du grec hypnos sommeil et ago conduire, mener. Qui mène au sommeil.  
Qui cause le sommeil. Exemple: « Votre conversation est hypnagogique! » Synonyme : soporifique.
Qui précède immédiatement le sommeil. Exemple: Des hallucinations hypnagogiques; images qui précèdent 
immédiatement le sommeil et qui peuvent cependant paraître réelles.""" },
{ "word": "Hypocoristique", "definition": """Adjectif et nom masculin.
Du grec « hupokoristekos »  issu de « hupokorizesthai » qui signifie
parler avec des diminutifs.
Qui exprime une intention affectueuse ou caressante.
Par exemple: un diminutif hypocoristique.
En tant que nom: « doudou » est un hypocoristique.""" },
{ "word": "Hypocras", "definition": """Nom masculin.
D’après le nom d’Hippocrate. Du bas latin hippocrasticum vinum : vin
hippocratique.
Vin sucré où l’on a fait infuser du miel, du gingembre, de la cannelle
et des clous de girofle.D’autres épices peuvent être ajoutées.
Ce vin était utilisé en médecine comme digestif.""" },
{ "word": "Hypogé", "definition": """Adjectif.
Du grec « hupo » qui signifie au-dessous et « gê » qui signifie terre.
En botanique ou en zoologie se dit d’un organisme vivant qui se
développe sous la terre.
Le contraire d’hypogé est épigé.""" },
{ "word": "Hypoglosse", "definition": """Adjectif.
Du grec « hypoglôssios » issu de « hypo » qui signifie en-dessous » et
« glôssa » qui signifie langue.
En anatomie « le nerf grand hypoglosse » est un nerf crânien qui se
distribue aux muscles de la langue.
Nom masculin.
On peut nommer ce même nerf « l’hypoglosse ».""" },
{ "word": "Hyponyme", "definition": """Nom masculin.
Du grec « hypo » qui signifie au-dessous et « ônumos » de onoma  qui signifie nom.
Mot qui désigne une sous-classe. Par exemple une daurade est un
hyponyme de poisson.""" },
{ "word": "Hypostase", "definition": """Nom féminin.
Du grec « huphisthanai » qui signifie placer sous.
1- Accumulation de sang dans les parties basses du poumon, par
complication d’une insuffisance cardiaque.
2- Chacune des trois personnes de la Trinité en tant que
substantiellement différente des deux autres.
3- Substitution d’une catégorie grammaticale à une autre.
Par exemple un adjectif employé en fonction de substantif.""" },
{ "word": "Hypotypose", "definition": """Nom féminin.
Du grec « hupotuposis »  de « hupo » qui signifie au-dessous, en deça et
« tupos » qui signifie marque, caractère.
Description vivante et pertinente.""" },
{ "word": "Hypsomètre", "definition": """Nom masculin.
Du grec « hupsos » qui signifie hauteur et « metron » qui signifie mesure.
1- En physique, instrument qui indique l’altitude d’un lieud’après la
température à laquelle l’eau y entre en ébullition.
2- En télécommunication, appareil qui permet de mesurer, en décibels,
les niveaux dans les systèmes de transmission.""" },
{ "word": "Hysope", "definition": """Nom féminin.
Du grec « hussopos » lui même issu de l’hébreu « ezob » qui signifie origan.
C’est un arbrisseau de la famille des lamiacées qui pousse dans les
régions méditerranéennes.
Les fleurs sont en épis et peuvent être bleues, violettes, blanches ou rouges.
C’est une herbe aromatique, on l’appelle aussi marjolaine; c’est aussi
une plante médicinale aux multiples indications thérapeutiques.
L’hysope est très souvent citée dans la Bible. Elle y a souvent une
fonction purificatrice.""" },
{ "word": "Hystérésis", "definition": """Nom féminin.
Du grec « husterein » qui signifie être en retard.
C’est le retard de l’effet sur la cause dans les réactions de certains
corps soumis à une réaction physique.
En d’autres termes le système tend à demeurer dans un certain état
même après que la cause qui a produit le changement d’état a cessé.
On peut observer des hystérésis électriques ou des hystérésis thermiques.""" },
{ "word": "Hystérie", "definition": """Adjectif.
De « hystérique ». Issu du grec « husterikos » par « hustera » qui signifie
utérus. L’attitude des malades était considérée autrefois comme un
accès d’érotisme féminin.
1- Dans un sens vieilli, ensemble des troubles psychiques,
neurologiques et fonctionnels variés attribués à la simulation.
2- Selon Charcot célèbre neurologue. Ensemble de symptômes
principalement neurologiques, qui prennent l’apparence d’affections
organiques, sans lésion organique décelable.
3- En psychiatrie moderne, Névrose caractérisée par une exagération
des modalités d’expression psychique et affective (névrose
d’expression) qui peut se traduire par des symptômes d’apparence organique
(convulsions, paralysies, douleurs, catalepsie) et par des manifestations
psychiques pathologiques (hallucinations, délire, mythomanie, angoisse).
En psychanalyse:
-Hystérie de conversion dans laquelle le conflit psychique se
manifeste par des symptômes corporels ou somatisation.
-Hystérie de défense contre les représentations déplaisantes.
4-Dans le langage courant. Excitation intense.
Par exemple: »C’est une hystérie collective. »""" },
{ "word": "Hystérologie", "definition": """Nom féminin.
Du grec « husterein » qui signifie être en retard et « logos » qui
signifie discours.
Figure de style qui consiste à inverser l’ordre chronologique de deux
propositions de manière à écrire en dernier lieu ce qui vient en
premier lieu dans l’odre des faits énoncés.""" },
{ "word": "Iambe", "definition": """Nom féminin.
Du grec « iambos » qui signifie lancer,frapper. Au sens propre coup, jet, vers satyrique.
En poésie c’est un pied qui a deux syllabes: la première est une brève et
la seconde est une longue.
Au pluriel c’est une pièce de vers satyriques. Par exemple: »Les Iambes » d’André Chénier
Il peut être aussi employé en tant qu’adjectif.
Par exemple: « Les vers iambés expriment la passion. » """ },
{ "word": "Iatralipte", "definition": """Nom masculin.
Du grec « iatros » qui signifie médecin et « aleiphô » qui signifie oindre.
Médecin qui traite ses malades par des onctions et des frictions.""" },
{ "word": "Iatrophobie", "definition": """Nom féminin.
Du grec « iatros » qui signifie médecin et « phobos » qui signifie
crainte, peur, phobie.
Peur d’aller chez le médecin.""" },
{ "word": "Ibéris", "definition": """Nom féminin.
Du grec « ibêris » qui signifie cresson.
Plante de la famille des cruciferracées, souvent appelée « corbeille
d’argent » que l’on cultive pour ses fleurs.""" },
{ "word": "Icarien", "definition": """Adjectif.
De « Icare » nom propre.
1- Relatif à Icare ou à sa légende.
2- De l’Icarie qui est une île de la mer Égée.
Par exemple: »La mer icarienne. »""" },
{ "word": "Ichneumon", "definition": """Nom masculin.
Du grec « ikhneumôn » qui signifie qui suit à la piste.
Insecte hyménoptère térébrant, c’est à dire qu’il perce des trous ou
des galeries.
Il appartient à la famille des ichneumonidés et sa larve est un
parasite des chenilles.""" },
{ "word": "Ichtyol", "definition": """Nom masculin.
Nom déposé en anglais par une firme allemande. Issu du latin « ikhthus »
qui signifie poisson.
Substance obtenue par distillation de certains schistes bitumeux
contenant des poissons fossiles. Peut permettre de fabriquer des
savons.""" },
{ "word": "Iconostase", "definition": """Nom féminin.
Du russe « ikonostas » issu du grec eikonostasion de « eikôn » qui
signifie icône et « stasis » qui signifie action de poser.
Dans les églises orthodoxes, mur décoré d’images ou d’icônes, qui
sépare la nef du sanctuaire dans lequel le prêtre officie.
A Paris on peut voir une très belle iconostase dans l’église orthodoxe
St Julien le Pauvre.""" },
{ "word": "Icosaèdre", "definition": """Nom masculin.
Du latin « ikosaedrum » du grec eikosaedron » issu de « eikosi » qui signifie vingt.
En géométrie, polyèdre limité par vingt faces. Chaque face d’un
icosaèdre régulier est un triangle équilatéral.""" },
{ "word": "Ictus", "definition": """Nom masculin.
Du latin « ictus » qui signifie coup.
1- En versification antique, battement de la mesure dans le vers.
Par extension, temps fort marqué par une syllabe, une note pour
souligner le rythme.
2- En pathologie, manifestation morbide violente et soudaine.
En psychologie, obscurcissement de la conscience sous l’effet d’une
violente émotion.""" },
{ "word": "Idemiste", "definition": """Nom masculin.
Du latin idem : La même chose.
Ceux qui se contentent d’opiner de la tête et de dire idem dans explication.""" },
{ "word": "Idiolecte", "definition": """Nom masculin.
Du grec « idion » qui signifie spécial et « (dia)lecte » forme d’une langue.
En linguistique, ensemble des particularités langagières propres à un
individu donné.
Par exemple: »Son idiolecte, est un mélange permanent de français,
d’allemand et d’alsacien. »""" },
{ "word": "Idiosyncrasie", "definition": """Nom féminin.
Du grec idios: propre, particulier et sugkrasis: mélange.
En médecine, pour un sujet donné, c’est une disposition particulière
qui le conduit à réagir de manière personnelle à un agent physique ou
chimique.
Par exemple une réaction allergique à un aliment peut être qualifiée
d’idiosyncrasie""" },
{ "word": "Idoine", "definition": """Adjectif.
Du latin « idoneus » qui signifie propre à.
1- Dans une langue vieillie ou qui appartient au droit. Ce qui est
propre à quelque chose.
2- Dans un langage moderne ou plaisant. Ce qui convient parfaitement.
Par exemple; « J’ai trouvé le restaurant idoine. »""" },
{ "word": "Ignigène", "definition": """Adjectif.
Du latin « ignigena » qui signifie né dans le feu, épithète du Dieu Bacchus.
Un sel ignigène est un sel obtenu par évaporation, sous l’action de la
chaleur, d’une saumure extraite par pompage. Il est raffiné ensuite
dans des salines spécialisées.
Ce sont des salines ignigènes.
Il existe une importante saline ignigène à Varangeville en Meurthe-et-Moselle.""" },
{ "word": "Ilote", "definition": """Nom féminin.
Du latin « ilota » lui-même issu du grec « heilôtes » nom de la bourgade
d’Helos située au sud de Sparte en Laconie (Grèce).
1- Habitant de Laconie réduit en esclavage par les Spartiates.
2- Au sens figuré et en littérature se dit d’une personne asservie,
réduite à la misère et à l’ignorance.""" },
{ "word": "Immarcescible", "definition": """Adjectif variable.
Du latin immarcescibilis issu de « marcescere » qui signifie se flétrir.
En botanique caractère d’un végétal qui ne peut pas se flétrir.
Au sens figuré, peut s’employer dans les expressions « jeunesse
immarcescible » ou « gloire immarcescible ».""" },
{ "word": "Immoler", "definition": """Verbe transitif.
Du latin « immolare » qui signifie sacrifier.
Ce mot vient de la « mola salsa » ou farine sacrée, que préparaient les
Vestales à Rome. Les Vestales récoltaient à une certaine et courte
période du mois de mai des épis d’amidonnier, une très ancienne céréale,
proche du blé, de la qualité la plus fine.
La farine obtenue était additionnée d’une saumure obtenue à partir de sel et d’eau.
Le mélange obtenu, « mola salsa » ou farine rituelle dont l’invention
était censée remonter à Numa (selon Pline l’Ancien) était répandu sur
la tête des animaux destinés au sacrifice et de manière générale sur
toute offrande faite aux dieux.
Cette pratique à donné le mot immoler, de « in-molare » qui signifie enduire
de mola.
A- Dans la religion. Offrir une personne ou un animal en sacrifice à
la divinité.
Par exemple: « Les anciens Hébreux immolaient des animaux. »
En théologie, au passif ou réfléchi, dans des phrases où le sujet est le Christ.
Par exemple: « J-C s’est offert en sacrifice sur la croix. »
B- Par extension littéraire, sacrifier la vie de quelqu’un.
Par exemple: « La première guerre mondiale a immolé de jeunes hommes. »
C’est aussi immoler quelqu’un pour quelqu’un d’autre ou pour quelque chose.
Par exemple: La pendaison était une immolation voulue par la société
révolutionnaire. »
Dans un emploi pronominal réfléchi:
Par exemple: « Il s’est immolé pour sa patrie. »
C- Au figuré et dans un sens littéraire.
1- Immoler quelqu’un ou quelque chose, dans les sens de détruire ou de
sacrifier.
Par exemple: « Il a immolé ses ambitions sur l’autel du devoir. »
Ou: »Il a immolé tous ceux qui le dérangeaient pour assouvir ses passion. »""" },
{ "word": "Impanation", "definition": """Nom féminin.
Du latin « impanatio » issu de « panis » qui signifie pain.
Dans la doctrine luthérienne coexistence du pain et du corps de
Jésus-Christ dans l’Eucharistie.""" },
{ "word": "Implexe", "definition": """Adjectif.
Du latin « implexus » issu de « implectere qui signifie entremêler.
Dans un sens vieilli, se dit d’une œuvre dont l’intrigue est compliquée.
En philosophie, se dit d’un concept qui ne peut se réduire à un schème.
Nom Masculin.
En généalogie, personnes identiques que l’on retrouve à plusieurs
endroits d’un arbre généalogique.""" },
{ "word": "Imposte", "definition": """nom masculin.
De l’italien « imposta » issu de « imporre » qui signifie placer sur.
1-Moulure saillante surmontant le montant vertical d’une porte ou un
pilier de nef.
2-Partie supérieure d’une baie de porte ou de fenêtre.
Partie vitrée dormante d’une porte pleine ou d’une cloison.""" },
{ "word": "In petto", "definition": """Locution adverbiale.
De l’italien « in petto » qui signifie dans la poitrine.
Dans le secret de son coeur. A part soi.""" },
{ "word": "Inattingible", "definition": """Adjectif.
Construit sur le modèle de « inatteignable ». Du latin « attingere » de
« tangere » qui signifie toucher. 
Le préfixe « in » est privatif et le suffixe « able » vient du latin « abilis »
qui signifie qui peut être.
But ou objectif qui ne peut être atteint.
Par exemple on peut dire: « La paix dans le monde est-elle un objectif
inattingible? »""" },
{ "word": "Inchoatif", "definition": """Adjectif.
De « inchoare » qui signifie commencer.
En linguistique, se dit de ce qui sert à exprimer une action
commençante, un devenir, une progression.
Par exemple: Lorsque l’on écrit la phrase suivante: »L’enfant commença
à manger son repas. » Le verbe commencer est qualifié d’inchoatif. »""" },
{ "word": "Incipit", "definition": """Nom masculin.
Mot latin issu du verbe « incipere » qui signifie commencer et qui est à
la troisième personne du singulier au présent de l’indicatif.
Premiers mots d’un manuscrit ou d’un livre.""" },
{ "word": "Incube", "definition": """Nom masculin.
Du latin « incubus » qui signifie cauchemar.
Démon mâle qui abuse des femmes pendant leur sommeil.""" },
{ "word": "Indécidable", "definition": """Adjectif qui vient de l’anglais undecidable. 
Se dit lorsque l’on est en présence d’un énoncé par exemple mathématique qui ne peut être ni démontré ni réfuté.
En d’autres termes ce qui est indécidable est l’impossibilité absolue et définitivement démontrée de résoudre par un procédé général de calcul un problème donné.  
Ainsi de ce problème de géométrie élémentaire
Soient une liste de formes polygonales; peut-on paver un plan sans recouvrement, ni espace vide avec des exemplaires de chaque forme polygonale?
Résolution: On n’a pas de formule qui permette par un calcul fini et à partir des données(les formes polygonales)d’établir si oui ou non il est possible de paver le plan avec des exemplaires des formes
géométriques considérées. En conséquence le problème est indécidable. 
Source:Calculabilité  et décidabilité J. P. Delahaye Université Sciences et Technologies de Lille.
Laboratoire d’Informatique Fondamentale de Lille.""" },
{ "word": "Indiction", "definition": """Nom féminin.
Du latin « indictio » issu de « indicire » qui signifie publier.
Dans le domaine religieux, fixation d’un jour dit.
Indiction d’un concile ou d’un synode.""" },
{ "word": "Innocuité", "definition": """Nom féminin.
Du latin « innocuus » issu de « in » élément de négation et « nocuus » qui
signifie nuisible.
1- En médecine, caractère de ce qui n’est pas nuisible. Employé dans
le domaine de la santé, à propos de substances qui ne causeraient
aucun dommage organique.
Par exemple: »Certaines personnes doutent de l’innocuité des O.G.M »
Autre exemple: « On peut parler d’une parfaite innocuité de ce vaccin. »
2- Sur le plan littéraire
1- Concernant un fait ou une chose, qualité de quelque chose qui ne
cause aucun dommage moral.
2- Concernant une personne, qualité de quelqu’un qui ne cause aucun
dommage à autrui, qui est innofensif.
Par exemple: « Ne t’inquiète pas, cette femme est d’une innocuité absolue. »
Historiquement les deux « n » étaient prononcés.
L’antonyme (contraire) de ce mot est « nocuité » [caractère de ce qui
est nuisible.]
.""" },
{ "word": "Innominé", "definition": """Adjectif.
De « innominatus » de même signification.
En anatomie et dans un sens vieilli, Se disait des os et des artères
illiaques qui n’avaient pas de dénomination précise.
Par exemple: »Os innominé. Artère innominée. »
Au XXème siècle. La ligne innominée est le relief osseux à la face
interne de l’os illiaque.""" },
{ "word": "Inri", "definition": """Acronyme [abréviation] de l’inscription « Jesus Nazarenus rex
Judagorum » Jesus de Nazareth roi des Juifs que Pilate inscrivit sur la
croix.""" },
{ "word": "Irénisme", "definition": """Mot masculin. Du latin eirênikos qui signifie pacifique.
A l’origine c’était une attitude d’empathie et de charité dans la discussion, entre chrétiens de confessions différentes.
Par extension, toute attitude d’apaisement entre des personnes de sensibilités opposées. """ },
{ "word": "Irréfragable", "definition": """Adjectif.
Du bas latin irrefragabilis de refragari s’opposer, à voter contre.
Propos ou idée que l’on ne peut ni récuser, ni contredire.""" },
{ "word": "Isatis", "definition": """Nom masculin.
Du grec « isatis » qui signifie pastel.
1- Plante de la famille des crucifères dont les feuilles et les tiges
contiennent un colorant bleu. On l’appelle aussi pastel.
2- Renard polaire à la fourrure grise en été et blanche en hiver. Il
est communément appelé le renard bleu.""" },
{ "word": "Isiaque", "definition": """Adjectif.
Du grec « isiakos » de même signification, issu de Isis, déesse
égyptienne, sœur et femme d’Osiris, mère d’Horus. Type d’épouse et de
mère idéale.
Relatif à la déesse Isis et à son culte qui connut un fort engouement
dans le monde gréco-romain.
On disait: »Les mystères isiaques. »""" },
{ "word": "Isocorie", "definition": """Nom féminin.
Du grec « isos » qui signifie égal et « koré » qui signifie jeune fille,
poupée, pupille. Pupille et poupée sont issus du même mot grec parce
que l’on voit par reflet dans l’œil de son interlocuteur, une image
miniature de soi comme celle d’une poupée.
En latin aussi le mot « pupilla qui signifie pupille est issu de « pupa »
qui signifie poupée, petite fille. Ce sens est retrouvé dans le mot pupille
qui désigne un enfant sans parents confié aux soins d’un tuteur.
En anatomie, le fait d’avoir deux pupilles de diamètre identique.""" },
{ "word": "Isoglosse", "definition": """Nom féminin.
Du grec « glôsa » qui signifie langue et « iso » qui signifie même. Langue identique. 
En linguistique, ligne imaginaire séparant deux zones géographiques qui se distinguent
par un trait caractéristique dialectal particulier.
Celui-ci peut être de nature lexicale, sémantique, phonologique, phonétique ou tout autre.
Par exemple la langue bretonne peut subir des prononciations distinctes pour le même mot selon les lieux.
De même pour l’orthographe ou pour la signification.
Chaque espace à l’intérieur de la Bretagne est délimité par une isoglosse qui recouvre les particularités
du breton dans ces lieux-là.
De même pour d’autres patois ou langues comme le français
qui ne se parle pas en Provence autour de Marseille comme en Provence autour d’Avignon.""" },
{ "word": "Istanbul", "definition": """Nom d’une ville de Turquie.
Du grec  » Is tin polin  » qui signifie  » dans la ville  » . A donné la
forme intermédiaire  » Stimboli  » , puis  » Istambul « .
Il y eut des hésitations autour de la graphie du nom. On eut le nom
dérivé  » Islambol  » qui émergea entre les XVIème et XIXème siècle
à partir de la fausse étymologie « Islam bol  » qui signifie ville d’Islam.
Aujourd’hui la ville ancienne à pour nom  » Stamboul » et la grande
agglomération se nomme  » Istanbul « .
Avant  » Istanbul  » trois noms se sont succédés au cours de l’histoire
: Byzance vers 658 avant J-C, La Nouvelle Rome et Constantinople vers
300 avant J-C.
Le nom  » Istanbul  » fut donné à la ville vers 1451 après J-C.""" },
{ "word": "Ithyphallique", "definition": """Adjectif.
Du grec « ithuphallos » qui signifie pénis en érection.
Dans l’antiquité grecque, se dit de ce qui a trait au phallus en érection.
Une statue ithyphallique représente un personnage en état d’érection.""" },
{ "word": "Ixode", "definition": """Nom masculin.
Du latin « ixodus » qui signifie gluant.
En zoologie, tique.""" },
{ "word": "Jachère", "definition": """Nom féminin.
Du latin « gascaria » issu du gallo-romain « ganskaria » par le radical
gaulois « gansko » qui signifie branche charnue.
Etat d’une terre labourable qu’on laisse temporairement reposer en ne
lui faisant pas porter de récolte.
Par exemple : « Une année de jachère après sept années de culture ».""" },
{ "word": "Jaconas", "definition": """Nom masculin.
De la ville de « Jagannath » en Inde où ce tissu était fabriqué.
Anciennement, étoffe de coton fine et légère.
Par exemple: »Elle portait une robe d’été en jaconas jaune paille. »""" },
{ "word": "Jacqueline", "definition": """Nom féminin.
Ustensile attribué à Jacqueline de Bavière.
Cruche de grès à large panse, en usage dans les Flandres.
On dit aussi un « jaquelin ».""" },
{ "word": "Jaculatoire", "definition": """Adjectif.
Du latin « jaculari » qui signifie lancer.
Se dit d’une prière courte et fervente.
Par exemple: « Il fonda tous ses espoirs dans cette oraison jaculatoire. »""" },
{ "word": "Jais", "definition": """Nom masculin.
Du latin d’origine grecque « gagates » qui signifie pierre de Gagas, du
nom d’une ville d’Asie Mineure.
Variété de lignite dure et fibreuse d’un noir luisant, que l’on peut
tailler ou travailler au tour et polir.
Par exemple: « Ce collier de jais est splendide. »
Par comparaison; « Noir » comme du jais. »
De manière elliptique: « Des cheveux de jais. »
On disait aussi « jayet »""" },
{ "word": "Jalap", "definition": """Nom masculin.
De l’espagnol « Xalapa » nom d’une ville du Mexique, près de laquelle
cette plante aurait été découverte.
1- Plante d’Amérique de la famille des convolvulacées, dont la fleur
ressemble au liseron et dont le tubercule renferme une gomme résineuse
utilisée comme purgatif.
C’est le jalap tubéreux, lpomoea purga.
2- Poudre purgative tirée des tubercules.
Par exemple: »Le turbith entre dans la préparation de la teinture de
Jalap composée, appelée aussi « eau-de-vie allemande. »""" },
{ "word": "Jaque", "definition": """Nom masculin.
De « Jacques » sobriquet que portait le paysan en France.
Historiquement, justaucorps à manches que portaient les hommes au Moyen-Âge.
Par exemple: »Il portait un jaque usé et sale. »""" },
{ "word": "Jaseron", "definition": """Nom masculin.
De « Al-Djezaïr » qui est le nom arabe d’Alger.
Anciennement chemise de mailles.
En bijouterie, terme vieilli. C’est une chaîne de cou à mailles très
fines d’or ou d’argent.""" },
{ "word": "Jenny", "definition": """Nom féminin.
De l’anglais correspondant au français « Jeannette » symbolisant la fileuse.
Machine à filer le coton.""" },
{ "word": "Jettatura", "definition": """Nom féminin.
Mot italien de « gettare » (il malaugurio) qui signifie jeter (un mauvais sort).
En Italie du Sud, c’est le mauvais œil envoyé par le jeteur de sort :
le « jettatore ».""" },
{ "word": "Jeûne", "definition": """Nom masculin.
Du latin « jejunare » qui signifie jeûner, faire abstinence.
1- Privation volontaire de toute nourriture.
En particulier, pratique religieuse qui consiste en l’abstention
totale ou partielle de nourriture pendant une durée déterminée.
Par exemple: « On observe le jeûne. »
2- Privation forcée d’aliments.
Au figuré: Toute espèce d’abstention ou de privation.
Par exemple: « Le jeûne des sens.C’est-à-dire la privation de tout ressenti. « """ },
{ "word": "Jocrisse", "definition": """Nom masculin.
Nom d’un personnage de théâtre.
Dans un sens vieilli, benêt qui se laisse mener sans réagir.
Par exemple: « Il joue les jocrisses, cela lui évite de prendre ses
responsabilités. »""" },
{ "word": "Jomon", "definition": """Nom masculin.
Du japonais « jōmon » qui signifie cordé.
Période prénéolithique et néolithique du Japon, qui va de 7000 à 300
avant notre ère et qui est caractérisée par des poteries portant des
marques de corde ou des impressions de coquillages.""" },
{ "word": "Jovial", "definition": """Adjectif.
Du latin « jovialis » issu de Jupiter, le Dieu ou la planète choisi par
les astrologues médiévaux au sens de « né sous le signe de Jupiter »
signe de bonheur et de gaieté.
Se dit d’une personne qui est d’une gaieté franche, simple et communicative.
Par exemple: « C’est un homme de tempérament jovial. »""" },
{ "word": "Joyau", "definition": """Nom masculin.
De « jeu » auquel on a ajouté le suffixe « au ».
1- Objet de matière précieuse, or, argent ou pierreries, de grande
valeur et qui est destiné à orner ou à parer.
Par exemple: « Le bijou qu’elle porte est un véritable joyau. »
2- Au figuré, chose rare et belle, de grande valeur.
Par exemple: « La Joconde est un joyau de la peinture. »""" },
{ "word": "Jubé", "definition": """Nom masculin.
De la prière dite en ce lieu: « Jube, Domine » qui signifie ordonne seigneur.
Tribune transversale en forme de tribune, élevée entre la nef et le
chœur ans certaines églises.""" },
{ "word": "Julep", "definition": """Nom masculin.
De l’espagnol « julepe » issu de l’arabe « djulâb » par le persan « goulab »
qui signifie eau de rose.
Terme de pharmacie, vieilli. Potion à base d’eau et de sucre,
aromatisée à l’aide d’une essence végétale, et servant d’adjuvant à
certains médicaments.""" },
{ "word": "Jungle", "definition": """Nom féminin.
Mot anglais issu de l’hindoustani « jangal » qui signifie steppe.
1- Dans les pays où a lieu la mousson ; forme de savane couverte de
hautes herbes, de broussailles et d’arbres où vivent les grands
fauves.
2- Par analogie, tout endroit, tout lieu humain où règne la loi des
fauves, de la sélection naturelle, les plus forts éliminant les plus
faibles.
En France, « la jungle de Calais » est un lieu où vivent des populations
migrantes.""" },
{ "word": "Jusquiame", "definition": """Nom féminin.
Du grec « huoskuamos » issu de hûs » qui signifie porc et kuamos » qui
signifie fève.
Plante herbacée de la famille des solanacées, aux fleurs jaunes rayées
de pourpre qui possède des propriétés narcotiques et toxiques.
La jusquiame noire est utilisée en médecine pour ses propriétés
calmantes, on l’appelle aussi herbe aux chevaux ou herbee aux poules.""" },
{ "word": "Juxtalinéaire", "definition": """Adjectif.
Du latin « juxta » qui signifie près de et  de « linea » qui signifie ligne.
Se dit d’une traduction dans laquelle le texte traduit fait face,
ligne à ligne, au texte à traduire dans deux colonnes contiguës.
Par exemple, la traduction juxtalinéaire des « Géorgiques » de Virgile,
dans laquelle le texte latin est face au texte français.""" },
{ "word": "Kabbale", "definition": """Nom féminin.
De l’hébreu « qabbalah » qui signifie tradition.
Tradition juive ésotérique qui donne une interprétation mystique et
allégorique de l’Ancien Testament.""" },
{ "word": "Kabig", "definition": """Nom masculin.
Néologisme de Marc Le Berre. Du breton « kab » qui signifie cape auquel
on a ajouté le suffixe « ig ». Veste à capuche créée par les goëmoniers
du Pays Pagani en Finistère Nord. Elle fut ensuite portée par les marins bretons.
Ce vêtement a la particularité d’être en laine tissée
très serrée ce qui le rend imperméable.
Il possède des ailerettes au niveau des épaules qui évitent le ruissellement
de l’eau en cas de pluie et une double poche ventrale dite poche-Napoléon.
Un crantage du tissu en ralentit l’usure.""" },
{ "word": "Kakemphaton", "definition": """Nom masculin.
Du grec « kakemphatos » qui signifie malsonnant.
Rencontre de sons qui provoque un énoncé déplaisant.
Par exemple ce vers de Baudelaire : « Fruits purs de tout outrage ».
On y entend « toutou » ce qui n’est pas très heureux!""" },
{ "word": "Kaki", "definition": """Nom masculin.
Du japonais « kakino » nom du fruit.
Plaqueminier du Japon que l’on cultive dans le Sud de la France.
C’est un arbuste ou arbrisseau qui produit des fruits d’un jaune
orangé de la forme de la tomate.
Par exemple: « Les kakis sont mûrs. »""" },
{ "word": "Kaolin", "definition": """Nom masculin.
Du chinois « kaoling » qui signifie colline élevée, lieu où l’on
extrayait le kaolin.
Silicate d’alumine pur, provenant de l’altération ou kaolinisation des
feldspaths, des granits, de l’argile blanche.
Cette substance est réfractaire et friable et elle entre dans la
composition de la céramique et de la porcelaine.""" },
{ "word": "Kaolin", "definition": """Nom masculin.
Du chinois « kaoling » qui signifie colline élevée, nom du lieu où l’on
extrayait le kaolin.
Silicate d’alumine pur provenant de l’alcalinisation des feldspaths,
des granits.
Argile blanche et friable qui entre dans la composition des pâtes
céramiques ou de la porcelaine.""" },
{ "word": "Karma", "definition": """Nom masculin.
Du sanskrit « karma » qui signifie acte.
Dogme central de la religion hindouiste selon lequel la destinée d’un
être vivant et conscient est déterminée par la totalité de ses actions passées,
de ses vies antérieures.""" },
{ "word": "Karst", "definition": """Nom masculin.
Nom d’une région de Yougoslavie.
1- Ensemble des phénomènes de corrosion qui peuvent affecter le calcaire.
2- Plateau calcaire touché par l’érosion chimique.""" },
{ "word": "Kasha", "definition": """Nom masculin.
Du mot russe « kâsha » qui signifie bouillie de gruau ou d’une autre céréale.
Plat populaire russe à base de bouillie de sarrasin ou d’orge mondé.""" },
{ "word": "Kathakali", "definition": """Nom masculin.
Mot malayalam, de « katha » qui signifie récit  et « kali » qui signifie jeu.
Théâtre dansé sacré de l’Inde, relatant de grandes épopées mythologiques.""" },
{ "word": "Kava", "definition": """Nom masculin.
Mot du sud-ouest polynésien qui signifie eau-de-vie par le portugais « ava ».
Poivrier de nom latin Piper Methysticum qui pousse en Polynésie et
dont la racine est utilisée pour fabriquer une boisson enivrante.
Le nom de cette boisson.
Cette racine a des propriétés anesthésiantes, myorelaxantes,
stimulantes et euphorisantes. Elle est aussi anti-dépresseur et
diurétique.
A forte dose, elle est hypnotique.""" },
{ "word": "Keepsake", "definition": """Nom masculin.
De l’anglais « keep » qui signifie garder et « (for my) sake » qui
signifie pour l’amour de moi.
Terme vieilli; livre-album généralement illustré de fines gravures,
qu’il était à la mode d’offrir en cadeau, comme souvenir, à l’époque
romantique.""" },
{ "word": "Kentia", "definition": """Nom masculin.
De « Kent » nom d’un horticulteur anglais.
Palmier australien, cultivé en Europe comme plante d’appartement.""" },
{ "word": "Kermès", "definition": """Nom masculin.
De l’espagnol « alkermès » lui même issu de l’arabe « al-qirmiz » qui
signifie cochenille.
1-  Insecte hémiptère de la famille des cochenilles qui parasite
certains chênes. A la ponte, la femelle se recouvre pour protéger ses
oeufs d’une pellicule très dure comme une graine appelée graine
d’écarlate. Cette graine est recueillie puis séchée et permet de
fabriquer une teinture rouge carmin.
2-  Chêne, dit « chêne-kermès » chêne arbustif des garrigues de la
méditerrannée dont les feuilles sont semblables à celles du houx et
qui est parasité par une cochenille.
3-  Teinture rouge obtenue à partie de la graine d’écarlate fabriquée
par la femelle kermès.
Cette teinture était appelée le « kermès officinal » et entrait dans la
pharmacopée comme base de certains médicaments qui facilitaient la
digestion et apaisaient les maux d’estomac.
Cette teinture constituait la base et la couleur de la liqueur
« Alkermès » composée aussi de cannelle, de girofle et d’autres
ingrédients. C’était une boisson prisée en Italie au XIX ème siècle.
Aujourd’hui elle est utilisée pour colorer en rose et parfumer
certaines pâtisseries.""" },
{ "word": "Ketmie", "definition": """Nom féminin.
Du latin botanique « ketmia » issu de l’arabe « hatmi » qui signifie guimauve.
Arbre ou arbrisseau de la famille des malvacées, qui pousse dans les
régions chaudes mais dont certaines variétés sont cultivées en France
et dont le fruit est le nafé. Ce dernier entre dans la composition de
certains médicaments.
Cette plante est très proche de l’hibiscus.""" },
{ "word": "Khâgne", "definition": """Nom féminin.
De « cagne » mot régional qui signifie paresse, par ironie.
Dans un langage familier, classe préparatoire à l’Ecole normale supérieure. """ },
{ "word": "Khan", "definition": """Nom masculin.
1- De « kan » mot persan qui signifie gouverneur de province.
Titre que prenaient les souverains mongols comme Gengis Khan et les
chefs tartares, qui se diffusa en Inde et au Moyen-Orient.
2- De l’arabo-persan « han ».
Caravansérail, étape des caravanes au Moyen-Orient.""" },
{ "word": "Kharidjisme", "definition": """Nom masculin.
De l’arabe « kharadja » qui signifie sortir.
Mouvement politique et religieux de l’Islam qui est puritain et fanatique.""" },
{ "word": "Khédive", "definition": """Du turc « khediw » qui signifie roi, souverain.
Titre porté par le vice-roi d’ Égypte entre 1867 et 1914.""" },
{ "word": "Kief", "definition": """Nom masculin.
Mot turc qui vient de l’arabe « kef » qui signifie aise.
Repos total au milieu du jour chez les Turcs. état de béatitude.""" },
{ "word": "Kimberlite", "definition": """Nom féminin.
De « Kimberley » nom d’une ville sud-africaine.
Roche éruptive dans laquelle on trouve le diamant.""" },
{ "word": "Koinè", "definition": """Nom féminin.
Du grec « koinos » qui signifie commun.
Langue commune de la Grèce aux époques hellénistiques et romaines.
Par extension, langue commune vulgaire d’un groupe humain.""" },
{ "word": "Koré", "definition": """Nom féminin.
Du grec « korê » qui signifie jeune fille.
Statue de l’art grec archaïque -de 600 à 500 avant notre ère-
représentant une jeune fille.""" },
{ "word": "Koumis", "definition": """Nom masculin.
Du nom des Coumans nomades d’Asie Centrale. Du tatar ou du russe.
Boisson à base de lait fermenté de jument, originaire d’Asie Centrale.
Elle contient peu d’alcool, présente un aspect mousseux, avec un goût
particulier très fort et fumé.""" },
{ "word": "Kouros", "definition": """Nom masculin.
Du grec « couros » qui signifie jeune garçon.
Statue grecque représentant un jeune homme.""" },
{ "word": "Kraken", "definition": """Nom masculin.
Mot norvégien à l’origine inconnue.
Monstre marin fabuleux des légendes scandinaves médiévales. Il était
de grande taille et possèdait de nombreuses tentacules. Il attaquait
les navires.
On pense que c’est un calmar géant habitant les grandes profondeurs et
observé très rarement.""" },
{ "word": "Kumquat", "definition": """Nom masculin.
Du chinois-cantonais, variation de « kin-kû » qui signifie orange d’or,
probablement par l’anglais.
Fruit d’un citrus appelé « citronnier du Japon »; très petite orange qui
se mange le plus souvent confite ou macérée dans l’alcool.
Arbuste qui produit ce fruit.""" },
{ "word": "Kwas", "definition": """Nom masculin.
Du vieux slave « kwas » qui signifie levain, ferment.
Boisson originaire d’Europe de l’est (Russie, Pologne…) légèrement
alcoolisée, obtenue à partir de la fermentation du seigle ou de l’orge
et auquel on a ajouté des fruits acides ou de la menthe.""" },
{ "word": "Kwashiorkor", "definition": """Nom masculin.
Dans la langue des Ashanti du Ghana, de « kwashi » qui signifie enfant
et « orkor » qui signifie rouge. En référence à la rougeur des enfantrs
qui sont atteints par cette maladie.
Syndrome de dénutrition infantile, dû à une carence protéique et très
courant en Afrique tropicale.
Par exemple: »Le kwashiorkor touche principalement les jeunes enfants
de neuf mois à trois ans, à la naissance d’un second enfant dans leur
famille, brutalement sevrés de lait maternel qui doivent passer à une
alimentation trop pauvre en protéines. »""" },
{ "word": "Kyrielle", "definition": """Nom féminin.
De « keriele » qui signifie litanie; issu de « kyrie eleison » du grec
« Kurie » qui signifie Seigneur et « eleison » qui signifie aie pitié.
1-Longue suite de paroles. Par exemple « Une kyrielle de mots ».
2-Par extension, suite, série interminable. Par exemple « Une kyrielle
de reproches ».
Familièrement, une kyrielle d’enfants signifie une ribambelle d’enfants.""" },
{ "word": "Labarum", "definition": """Nom masculin.
Mot d’origine latine passé directement dans la langue française
mais dont l’origine étymologique est inconnue.
Étendard romain sur lequel, avant la bataille du pont Milvius en
312, l’empereur Constantin 1er fit placer la croix et le
monogramme de Jésus-Christ avec l’inscription latine suivante:
« in hoc signo vinces » dont la traduction est:
« par ce signe tu vaincras ».
Le labarum fut ensuite adopté par tous les empereurs romains
qui succédèrent à Constantin. 
A titre d’exemple, les armes de la ville d’Arles portent le
labarum impérial avec l’inscription « civ.arel »
pour « civitas arelatensis » « citoyen d’Arles ».""" },
{ "word": "Labelle", "definition": """Nom masculin.
Du latin « labellum » qui signifie petite lèvre.
1- En botanique, pétale supérieur de la corolle des orchidées.
2- En zoologie, bord renversé de certains coquillages.""" },
{ "word": "Lactucarium", "definition": """Nom masculin.
Du latin « lactuca » lui-même issu de « lac, lactis » qui signifie le
lait. A cause du suc végétal qui ressemble à du lait et qui provient
de la plante.
Suc de laitue obtenu par incision des feuilles puis par dessiccation
au soleil. Il possède de faibles effets narcotiques et analgésiques
qui lui ont valu le nom d’opium de laitue et le font employer quelques
fois comme calmant.""" },
{ "word": "Ladino", "definition": """Nom masculin.
De l’espagnol « ladino » qui signifie langue parlée par les juifs séfarades.
En linguistique, langue qui mêle l’espagnol, l’hébreu et d’autres mots
turcs, grecs ou bulgares provenant des différents pays d’accueil de la diaspora séfarades.
Par exemple: »Le ladino est considéré par l’Unesco parmi les langues
les plus menacées au monde. »""" },
{ "word": "Ladre", "definition": """Nom masculin.
De l’hébreu « Lazarus » nom du  pauvre couvert d’ulcères, dans la
parabole de St Luc.
1- Nom et adjectif, d’un emploi vieilli qui signifie lépreux.
2- Adjectif. Se dit du porc ou du boeuf atteint de ladrerie (lèpre).
Par exemple: » Une truie ladre ».
3- Nom. Dans un emploi vieilli ou littéraire, se dit d’un avare. Par
exemple: « Vous me refusez cet argent, vous n’êtes qu’un ladre! « """ },
{ "word": "Laïus", "definition": """Nom masculin.
De Laïos: le père d’Œdipe.
Discours long et saturé de mots.""" },
{ "word": "Lamanage", "definition": """Nom masculin.
De l’ancien français « laman » issu du néerlandais « lootsman » qui
signifie pilote.
Terme de marine. Pilotage des navires à l’entrée et à la sortie des
ports, dans les passes et dans les chenaux.
Par exemple: »Le lamanage est pour le capitaine du bateau une manœuvre délicate. »""" },
{ "word": "Lamarckisme", "definition": """Nom masculin.
De « Lamarck » naturaliste français 1744-1829.
Théorie qui explique l’adaptation des êtres vivants à leur milieu et
par l’hérédité des caractères acquis.
Cette idée d’une transformation des espèces en fonction des conditions
extérieures, qui peuvent freiner ou modifier l’expansion vitale,
conduit à qualifier cette théorie de transformiste. 
Lamarck précise que le milieu extérieur peut modifier ou susciter un
besoin durable qui agira sur un organe ou le créera.
Un organe peut disparaître par manque d’usage alors qu’un usage
intensif de celui-ci le développera.
Par exemple la girafe est contrainte sur un sol desséché de brouter
les feuilles des arbres, en conséquence elle déploie des efforts
constants qui se traduiront par un allongement de ses jambes ou de son cou.""" },
{ "word": "Lambdacisme", "definition": """Nom masculin.
Du latin « lambdacismus », issu de « lambda » lettre de l’alphabet grec
correspondant au « l » latin.
Vice de  prononciation qui consiste à bégayer sur la lettre « l », à la
mouiller mal à propos ou à prononcer le « r » comme un « l ».""" },
{ "word": "Lambrequin", "definition": """Nom masculin.
Du néerlandais « lamperkjin » de « lamper » qui signifie voile.
1-Bande d’étoffe festonnée par le bas dont on décore les cantonnières
des baies vitrées et les ciels de lit.
2-Motif décoratif capricieux à symétrie axiale employé en céramique et
en reliure.
3- Dans le vocabulaire des blasons, il est utilisé au
pluriel:lambrequins: longs rubans partant du heaume et entourant
l’écu.""" },
{ "word": "Lanthanides", "definition": """Nom masculin pluriel.
De lanthane issu du grec « lanthaneîn » qui signifie être caché.
En chimie, groupe d’éléments dont le numéro atomique va de 37
(lanthane) à 71 (lutécium) appelés aussi terres rares.
Ce sont des oxydes métalliques à propriétés très voisines et qui
existent en proportions variables dans des minerais disséminés, mais
rarement en quantité suffisante pour être exploitables.""" },
{ "word": "Lapiaz", "definition": """Nom masculin.
Du latin « lapis » qui signifie pierre.
En géologie, rainure superficielle qui peut avoir des formes variées
et qui est creusée par les eaux en terrain calcaire.
Par exemple : « Des champs de lapiaz ».
On peut dire aussi « lapié ». On aura alors par exemple « Des champs de lapiés »""" },
{ "word": "Laps", "definition": """1-Nom masculin.
Du latin « lapsus »qui signifie qui est tombé, participe
passé de « lapso, lapsare » qui signifie chanceler, tomber.
Un laps de temps est un intervalle de temps.
2- Adjectif variable.
Même étymologie. 
Laps au masculin, lapse au féminin.
Vocabulaire vieilli de la religion. La locution « laps et relaps ou
lapse et relapse » se dit d’une personne qui a quitté une première fois
la religion catholique.""" },
{ "word": "Lapsus", "definition": """Nom masculin.
Du latin, l’expression complète est
Soit 1- « Lapsus linguae » qui signifie faux pas de la langue.
Soit 2- « Lapsus calami » qui signifie faux pas de la plume.
Emploi involontaire d’un mot pour un autre, en langage parlé ou écrit.""" },
{ "word": "Laptot", "definition": """Nom masculin.
Origine inconnue.
Au Sénégal ou dans les ports africains, nom donné aux marins qui
pilotent les pirogues, aux matelots et aux débardeurs.""" },
{ "word": "Lare", "definition": """Nom masculin.
Du latin las, laris de même sens.
Chez les Romains, esprit tutélaire chargé de protéger la maison, la
cité, les rues.
Lares domestiques: les âmes des ancêtres devenues protectrices du foyer.
Le culte des lares avait lieu dans un laraire, qui était une niche, un
autel ou une petite chapelle.""" },
{ "word": "Larigot", "definition": """Nom masculin.
L’étymologie de ce mot se confond avec l’histoire de l’expression
« A tire-larigot ».
Le mot et l’expression sont attestés au XV ème siècle.
Le larigot est alors une sorte de flûte ou petit flageolet dont la
forme primitive est arigot ou harigot.
L’arigot devient ensuite larigot par agglutination de l’article.
On ignore l’origine de ce premier sens.
L’arigot était primitivement un chalumeau, c’est à dire un instrument
de musique dont l’origine incertaine serait le latin « aliquot ».
A tire-larigot est une expression populaire imagée qui représente
quelqu’un qui boit sans s’arrêter comme on  joue de la flûte.
On peut noter d’autre part que « flûter » a signifié boire.
Une autre origine possible de cette expression viendrait de l’aligot,
préparation culinaire à base de tomme dont la consistance est élastique
et peut donc s’étirer.
Enfin une troisième origine possible serait Rigault une des cloches de
la cathédrale de Rouen. Elle était très dure à mettre en branle et les
sonneurs buvaient pour se donner de la force.
D’où « boire à tire-la Rigault » dont l’orthographe aurait changé par la suite.
L’expression « boire comme un sonneur » existe elle aussi.
Une variante de l’explication est qu’un prélat aimait beaucoup
entendre cette cloche et payait cher le sonneur qui dépensait cet argent en boisson.
Le dictionnaire Le Quillet évoque une autre explication possible:
Boire à tire larigot comme un artilleur qui tire la Rigaud.
La Rigaud était une pièce d’artillerie.
Le larigot est un jeu d’orgues de la famille des mutations, c’est à
dire que chaque note comporte plusieurs tuyaux de différentes longueurs
qui émettent des harmoniques. Les tuyaux appartiennent à la famille des flûtes.
Ce  jeu d’orgues est un des jeux les plus aigus qui soit. On l’appelle
aussi le petit nasard.""" },
{ "word": "Larme-de-Job", "definition": """Nom féminin.
De larme et de Job, personnage de la Bible. Cette plante doit son nom
à la forme de ses graines qui est semblable aux larmes.
Dans un sens vieilli ou régional, plante herbacée exotique, de la
famille des poacées (graminées) des lieux humides de Birmanie dont la
graine semblable à une perle est utilisée pour la confection de colliers ou de chapelets.
Le nom scientifique de cette plante est Coix lacryma-jobi. Les graines
sont aussi utilisées comme diurétiques.""" },
{ "word": "Latitudinaire", "definition": """Adjectif et nom.
Du latin « latitudo » qui signifie largeur
En littérature, se dit d’une personne qui a une morale très large,
très relâchée.""" },
{ "word": "Latomies", "definition": """Nom féminin pluriel.
Du grec « latomia » issu de « lâs » qui signifie pierre et « temnein » qui
signifie couper.
Dans l’antiquité c’étaient des carrières situées dans la région de
Syracuse en Sicile et au sein desquelles le travail était très dur.
Les parois formaient une véritable
prison naturelle.
Au Vème siècle avant notre ère 7000 athéniens y furent enfermés après
l’échec de l’expédition de Sicile.
Ces carrières restèrent une prison pour l’Empire Romain. Beaucoup de
chrétiens y furent enfermés et y subirent un véritable martyre .
Latomie est synonyme de torture ou de souffrance.""" },
{ "word": "Latrie", "definition": """Nom féminin.
Du grec « latréia » qui signifie adoration.
Dans la religion catholique culte rendu à Dieu seul.""" },
{ "word": "Laudanum", "definition": """Nom masculin.
Du latin « ladanum » qui signifie résine de ciste ».
Teinture alcoolique d’opium, aux propriétés soporifiques et qui fut
largement utilisée avant la mise sur le marché des neuroleptiques par
les laboratoires pharmaceutiques.""" },
{ "word": "Lauze", "definition": """Nom féminin.
De l’ancien provençal « lauza » « lausa » qui signifie dalle, issu du
gaulois « lausa » qui signifie pierre plate.
Pierre plate de schiste ou de calcaire qui est utilisée comme dalle ou
comme tuile.
Les toits de lauze des maisons de l’Aveyron.""" },
{ "word": "Leishmania", "definition": """Nom féminin.
De Leishman, nom d’un bactériologiste anglais. (1910).
En bactériologie, protozoaire flagellé, parasite des cellules
endothéliales, des tissus, des organes et parfois des leucocytes.
Par exemple: La leishmania provoque une maladie qui est nommée la leishmaniose.""" },
{ "word": "Lemme", "definition": """Nom masculin.
Du latin « lemma » qui signifie proposition auxiliaire.
1- En mathématique : résultat intermédiaire qui permet de construire une
démonstration.
2- En philosophie: proposition qui représente une étape d’un raisonnement.
3- Forme normée d’un mot variable. Par exemple l’infinitif pour un verbe ou le
masculin singulier pour un substantif.""" },
{ "word": "Lépisme", "definition": """Nom masculin.
Insecte aptère, de la famille des thysanoures, dont le corps est
effilé et couvert d’écailles argentées. On l’appelle communément le
poisson d’argent.""" },
{ "word": "Lésine", "definition": """Nom féminin.
De l’italien « lesina » qui signifie alène (poinçon éffilé destiné à
percer les cuirs) à propos d’avares qui raccommodaient eux-mêmes leurs
souliers.
Dans un sens vieilli ou littéraire, épargne sordide jusque dans les
plus petites choses.
On peut dire par exemple: « La lésine est une avarice exacerbée ».""" },
{ "word": "Leude", "definition": """Nom masculin.
Du latin « leudes » issu du franque « leudi » qui est le pluriel de gens.
Sur le plan historique, chez les Germains et les Francs, grand vassal
attaché à la personne du chef ou du roi.
Par exemple: « Le roi et ses leudes. »""" },
{ "word": "Léviger", "definition": """Verbe transitif.
Du latin « levigare » issu de « levis » qui signifie lisse, uni.
En chimie, réduire une substance en une poudre très fine, notamment en
la délayant dans un liquide et en laissant précipiter la poudre.""" },
{ "word": "Libration", "definition": """Nom féminin.
Du latin « libratio » qui signifie mouvement régulier, balancement.
En astrophysique, balancement apparent d’un astre et plus
particulièrement de la lune.
La libration de la lune est l’ensemble de ses mouvements.""" },
{ "word": "Lige", "definition": """Adjectif.
Issu peut-être du bas latin liticus, par le radical germanique let-. A
rapprocher du mot allemand « ledig » qui signifie libre.
1- Dans les temps féodaux, un vassal lige, rendait à son seigneur un
hommage qui l’engageait à une fidélité absolue.
Par extension on pouvait dire : »Un hommage lige ».
 2- La locution moderne « homme lige de » une personne ou une
organisation, signifie une personne entièrement dévouée à…
On peut dire: » Les hommes liges d’une organisation mafieuse. »""" },
{ "word": "Limes", "definition": """Nom masculin.
Du latin « limes » qui signifie chemin, frontière.
Historiquement, c’était le système de fortifications établi le long de
certaines frontières de l’empire romain.
Le Mur d’Hadrien situé au nord de l’actuelle Angleterre est un limes.
On écrirait mieux un limès, tel que ce mot doit être prononcé.""" },
{ "word": "Lingam", "definition": """Nom masculin.
Mot sanskrit.
Symbole phallique du dieu Shiva, dont le culte est lié à l’idée de création.
On peut aussi dire linga.""" },
{ "word": "Lingua franca", "definition": """Nom féminin invariable.
Du latin « lingua franca » qui signifie langue franche.
1- Système linguistique réduit en vocabulaire et en règles de
grammaire, au champ lexical restreint à un domaine particulier, dans
les ports de la méditerranée du XIII ème au XIX ème siècle.
2- Langue auxiliaire de relation, premier peuple de Romeation,
utilisée par des groupes de langues maternelles différentes.
Autrement dit, langue commune qui permet des échanges entre
des personnes qui ne parlent pas la même langue.""" },
{ "word": "Lise", "definition": """Nom féminin.
Variation de « glise » ou de « glaise ».
Dans certaines régions, nom donné au sable mouvant en bord de mer.""" },
{ "word": "Liteau", "definition": """Nom masculin.
De l’ancien français « listiel » qui signifie bordure.
1- Baguette de bois fixée à un mur et qui soutient une tablette.
2- Raie de couleur parallèle à chaque lisière de linge uni.
3- Bois débité en tronçons de section carrée ou rectangulaire.
Du mot « lit ».
Lieu où le loup se repose pendant le jour.""" },
{ "word": "Lithodome", "definition": """Nom masculin.
Du grec « lithodomos » qui signifie qui bâtit avec des pierres.
En zoologie, mollusque lamellibranche à coquille cylindrique, qui
creuse les roches pour s’y loger.""" },
{ "word": "Lithophanie", "definition": """Nom féminin.
Du grec « lithos » qui signifie pierre et « phainéin » qui signifie apparaître.
Effet translucide dans la porcelaine et le verre opaque rendu possible
par variation d’épaisseur de la pâte.""" },
{ "word": "Litote", "definition": """Nom féminin.
Du grec « litotês » qui signifie simplicité.
Figure de rhétorique qui consiste à atténuer l’expression de sa pensée
pour faire entendre le plus en disant le moins.
Par exemple, si l’on dit:  » Ce n’est pas très bien » pour « C’est
mauvais ». C’est une litote.""" },
{ "word": "Longanimité", "definition": """Nom féminin.
Du latin longanimitas lui même formé de « longus » qui signifie patient
et de « anima » qui signifie âme.
Patience à supporter des souffrances morales ou à supporter ce que
l’on pourrait réprimer.""" },
{ "word": "Lorette", "definition": """Nom féminin.
De l’église Notre-Dame de Lorette, située dans un quartier où
habitaient beaucoup de femmes de moeurs légères.
Dans un sens vieilli ou historique, jeune femme élégante et facile.""" },
{ "word": "Louise-bonne", "definition": """Nom féminin.
De « Louise » le prénom féminin et « bonne ».
Poire d’automne, fondante et douce.""" },
{ "word": "Loustic", "definition": """Nom masculin.
De l’allemand « lustig » qui signifie gai.  A l’origine, bouffon
rattaché aux régiments suisses.
1- Anciennement, amuseur attitré d’une compagnie.
2- Dans un emploi vieilli, individu plaisantin ou farceur.""" },
{ "word": "Lovelace", "definition": """Nom masculin.
Nom d’un personnage du roman « Clarissa Harlowe » de Richardson écrit en 1749.
De « love » qui signifie amour et « lace » qui signifie filet, piège.
Nom donné à un séducteur, un Don Juan.""" },
{ "word": "Loxodromie", "definition": """Nom féminin.
Du grec « loxos » qui signifie oblique et « dromos » qui signifie course.
Terme maritime. Courbe suivie par un navire lorsqu’il coupe les
méridiens sous un même angle.""" },
{ "word": "Lubie", "definition": """Nom féminin.
Peut-être du latin « lubere » variation de « libere » qui signifie trouver bon.
Idée, envie capricieuse et saugrenue, peu raisonnable.""" },
{ "word": "Lubrique", "definition": """Adjectif.
Du latin « lubricus » qui signifie glissant, incertain, dangereux, hasardeux.
Littéraire ou plaisant. Se dit de celui ou celle qui a ou qui
manifeste un penchant pour la luxure.
En ce qui concerne les choses, se dit de ce qui est empreint de lubricité.
Par exemple: « Des idées lubriques ».""" },
{ "word": "Lucane", "definition": """Nom masculin.
Du latin « lucanus » qui signfie cerf-volant.
Coléoptère de grande taille, à la cuirasse brun-noir, dont le mâle se
distingue par des mandibuules fortes et ramifiées.""" },
{ "word": "Lucernaire", "definition": """Nom masculin.
Du latin «  »lucerna » qui signifie lampe.
1- Dans la liturgie chrétienne, c’est la première partie de la vigile
qui était l’office que les premiers chrétiens célébraient à la lueur
des lampes, dans la nuit du samedi au dimanche.
2- En zoologie, espèce de méduse de la famille des scyphozoaires, qui
se fixe aux algues ou aux rochers par le sommet
de son ombrelle. Elle présente l’aspect d’un entonnoir portant sur son
bord huit tentacules courts terminés en touffe.""" },
{ "word": "Luette", "definition": """Nom féminin.
Du latin « uva » qui signifie grappe de raisin.
Saillie médiane, charnue, allongée, située au bord postérieur du voile
du palais qui contribue à la fermeture nasale du pharynx lors de la déglutition.
Le synonyme de luette est uvule.""" },
{ "word": "Lupercales", "definition": """Nom féminin pluriel.
Du latin « lupercalia ».
Dans l’antiquité, à Rome, fête annuelle en l’honneur de Lupercus: « le
dieu-loup », dieu de la fécondité.""" },
{ "word": "Lustral", "definition": """Adjectif.
Du latin « lustralis » issu de « lustrum » qui signifie expiatoire ou
sacrifice mais aussi relatif à une période de cinq ans, de lustre ou
quinquenale.
1- Sur un plan religieux, se dit de ce qui est expiatoire ou de ce qui
sert à purifier. Par exemple: L’eau lustrale [du baptême].
2- Dans l’Antiquité, se disait d’un  d’un sacrifice expiatoire qui
était fait tous les cinq ans, Par exemple à la clôture du cens pour
purifier le peuple romain.
Mais c’était aussi la période quinquenale ou lustre d’un bail ou d’un
fermage; les censeurs affermant les biens de l’état tous les cinq ans.""" },
{ "word": "Limon", "definition": """A- Nom masculin.
Du latin « limus » qui signifie limon, boue, fange.
1- Terre ou fines particules, entraînées par les eaux et déposées sur
le lit et les rives des cours d’eau.
2- En minéralogie, roche mixte, argilo-siliceuse, contenant du quartz
détritique et qui est formée d’éléments plus gros que ceux qui
constituent la vase.
B- Nom masculin.
Probablement issu du radical gaulois « -lem » qui signifie traverse.
1- Chacune des deux pièces de bois entre lesquelles on attelle un cheval.
2- Noyau d’un escalier, dans lequel sont engagés les abouts des
marches et la balustrade du côté du vide.
C- Nom masculin.
De l’arabo-persan « limùn » qui signifie citron.
Dans un sens vieilli, citron.""" },
{ "word": "Macaronique", "definition": """Adjectif.
Du latin « macaronici » issu de « macaronea » qui signifie poème burlesque.
En littérature, poésie burlesque où l’auteur entremêlait des mots
latins et des mots de sa propre langue affublés de terminaisons
latiines.
Par exemple: « Le latin macaronique est le latin de cuisine. »""" },
{ "word": "Macassar", "definition": """Nom du chef-lieu de l’île des Célèbes.
1. L’huile de Macassar est une huile de coco parfumée à l’ilang-ilang
qui était utilisée comme cosmétique.
2. Ebène brun veiné de noir.""" },
{ "word": "Macédoine", "definition": """Nom féminin.
Au figuré, par comparaison plaisante ave la Macédoine, empire
d’Alexandre, habitée par des peuples d’origine très diverses .
1- Mets composé d’un mélange de légumes ou de fruits coupés en menus morceaux.
2- Familier et vieilli, assemblage, mélange disparate.""" },
{ "word": "Macis", "definition": """Nom masculin.
De macie, mot latin issu de « macir » qui signifie écorce aromatique.
Tégument de la noix muscade utilisé comme épice.""" },
{ "word": "Madapolam", "definition": """Nom masculin.
D’une ville de l’Inde.
Étoffe de coton, calicot fort et lourd.""" },
{ "word": "Madrague", "definition": """Nom féminin.
Du provençal « madraga » issu de l’arabe « mâdraba » qui signifie enceinte.
Mot à usage régional utilisé dans la pêche. Piège fixe composé de
filets qui forment des compartiments; il est disposé au voisinage
des côtes pour capturer les thons.""" },
{ "word": "Mafflu", "definition": """Adjectif.
De même racine que l’ancien verbe « mafler » qui signifie manger
beaucoup. Du néerlandais « maffelen » qui signifie mâchonnner.
Dans un sens vieilli ou littéraire, se dit de quelqu’un qui a de grosses joues.
Par exemple:  » …quelque robuste servante aux joues colorées et
mafflues » Théophile Gautier""" },
{ "word": "Magnanerie", "definition": """Nom féminin.
Du provençal « magnanarié » issu de « magnan » qui signifie ver à soie.
Local où se pratique l’élevage des vers à soie.""" },
{ "word": "Mahatma", "definition": """Nom masculin.
Mot hindi issu du sanskrit qui signifie « qui possède une grande âme ».
Dans l’Inde moderne, nom donné, à des chefs spirituels, ascètes et sages.
Par exemple: « Le mahatma Gandhi ».""" },
{ "word": "Mahdi", "definition": """Nom masculin.
Variante de « mahadi », de l’arabe qui signifie le guide, le dirigé.
1- Dans la religion musulmane, envoyé d’Allah attendu pour compléter
l’œuvre de Mahomet.
2- Par extension, chef de tribus se prétendant mahdi.""" },
{ "word": "Maïa", "definition": """Nom masculin.
Du grec ancien « Maïa » mère de Mercure ou Hermès. Dérivé du grec
« meter » qui signifie mère.
Du latin « maia » dérivé peut-être de « magnus » qui signifie grand et qui
donna « maïa ».
En zoologie
1- Grand crabe, décapode, brachyoure, appartenant à la sous-classe des
malacostracées dont la carapace est couverte de tubercules velus.
Il est aussi appelé, araignée de mer.
2- Oiseau passereau des îles de la Sonde, du genre munie.
En astronomie
Mot féminin.
Etoile géante bleu-blanche de type spectral B située dans l’amas des
Pléiades.
Avec une majuscule
En mythologie
1- Fille aînée d’Atlas et de Pléïoné. Mère de Mercure ou Hermès. Fait
partie des Pléiades.
2- Fille de Faunus, dieu romain de la fécondité, des troupeaux et des
champs, incarnant le printemps et dont la fête se célébrait en mai.
En géographie
Rivière de Sibérie.
Employé comme prénom
Maïa ou Maya a plusieurs étymologies :
– Provient d’un mot hébreu qui signifie aimée.
– Provient du nom latin de la déesse Maïa que l’on fêtait au printemps
et qui nomma le mois de mai.""" },
{ "word": "Maïeutique", "definition": """Nom masculin du grec maïeutikê art de faire accoucher.
Selon Socrate – dont la mère était sage-femme- c’est l’art d’accoucher les esprits, c’est à dire de faire  advenir leurs pensées.""" },
{ "word": "Maïs", "definition": """Nom masculin.
De l’espagnol « maiz » issu du mot « mahis » dans la langue des Tainos de
Haïti qui le cultivaient. Chez les amérindiens le mot « mahiz »
signifiait ce qui nourrit.
On a donné à cette plante d’autres noms tombés en désuétude blé
d’Inde, blé de Turquie ou blé de Barbarie. Tous ces noms sont les
témoins de la confusion qui régnait en Europe autour de cette plante.
Plante herbacée tropicale annuelle de la famille des Poacées ou
graminées cultivée comme plante céréale mais aussi comme plante
fourragère.
Le terme désigne aussi le grain lui-même.
Cette espèce est originaire du Mexique et elle était l’aliment de base
des Amérindiens avant l’arrivée de Christophe Colomb.
Le maïs tel qu’il est aujourd’hui n’existe pas à l’état sauvage, une
théorie affirme que la plante ancêtre du maïs actuel est la téosinte.
A noter que dans le calendrier républicain le Maïs était le nom donné
au 28ème jour du mois de fructidor.""" },
{ "word": "Majolique", "definition": """Nom féminin.
De l’italien « majolica » qui signifie de l’île de Majorque.
Faïence italienne de la Renaissance.""" },
{ "word": "Majordome", "definition": """Nom masculin.
Du latin « major domus » qui signifie chef de la maison.
1- Chef des domestiques, du sevice intérieur de la masion d’un souverain.
par exemple: « Le majordome du roi. »
2- Maître d’hôtel de grande maison.""" },
{ "word": "Malachite", "definition": """Nom féminin.
Mot grec de « molokhê » ou « malakhê » qui signifie mauve.
Carbonate de cuivre naturel, pierre d’un beau vert diapré, utilisée
dans la fabrication d’objets d’art.
Par exemple: »Une statuette chinoise en malachite. »""" },
{ "word": "Maladrerie", "definition": """Nom féminin.
Altération de « maladerie » issu de malade par croisement avec ladre, ladrerie.
Dans un sens vieilli: léproserie, c’est-à-dire établissement où
étaient soignés les lépreux.
Par exemple: « Il n’existe plus de maladrerie en France. »""" },
{ "word": "Malayalam", "definition": """Nom masculin.
De « malayala » mot de cette langue.
Langue dravidienne proche du tamoul, parlée dans le Kerala, en Inde,
par environ trente millions de personnes.""" },
{ "word": "Mamelouk", "definition": """Nom masculin.
De l’arabe d’Égypte, »mamlûk » qui signifie celui qui est possédé, esclave.
Nom que l’on donnait au cavalier des anciennes milices Égyptiennes
mais aussi au garde du corps du Sultan.
Au pluriel, on écrit « mamelouks ».
Soldat d’un escadron de la garde de Napoléon.
En tant qu’adjectif.
La cavalerie mamelouke.""" },
{ "word": "Mana", "definition": """Nom masculin.
D’un mot mélanésien.
En ethnologie, puissance surnaturelle impersonnelle et principe
d’action, dans certaines religions.""" },
{ "word": "Mancenillier", "definition": """Nom masculin.
De l’espagnol « manzinellla » qui signifie petite pomme.
Arbre de la forêt tropicale des Antilles et de l’Amérique équatoriale
dont le fruit appelé mancenille ressemble à une petite pomme.
Le fruit n’est pas comestible: le consommer peut provoquer des
brûlures de la bouche et de la gorge.
L’arbre mesure envoron 25 mètres de hauteur. Il pousse sur littoral
sableux et permet de lutter contre l’érosion marine et éolienne. Il
est utilisé en ébenisterie.
Il est aussi appelé « arbre de poison » ou « arbre de mort » . Son ombre
passait pour être mortelle.
On doit éviter de le toucher: sa sève latex est toxique et provoque
des dermatites sévères de la peau et des muqueuses.
Il fait partie de la famille des euphorbiacées. 
Pour protéger le promeneur du danger le tronc est souvent cerclé de
peinture rouge.""" },
{ "word": "Mandore", "definition": """nom féminin.
De « mandoire » altération du grec « pandoura » nom d’un instrument de
musique, à cordes.
Ancien instrument de musique à cordes pincées, semblable au luth.""" },
{ "word": "Manducation", "definition": """Nom féminin.
Du latin « manducare » qui signifie manger.
Action de manger.
Ensemble de tous les mécanismes qui accompagnent l’action de manger et
qui précèdent la digestion.
Ces mécanismes sont: la préhension, la mastication, l’insalivation et
la déglutition.""" },
{ "word": "Mangrove", "definition": """Nom féminin.
De l’anglais mangrove, issu des langues dravidiennes dont le malayalam
où « mang » est à rattacher à mangue mais où le suffixe est obscur,
peut-être « grove » qui signifie bocage.
Formation végétale caractéristique des littoraux marins tropicaux,
constituée de palétuviers dont les fortes racines sont visibles dans
les eaux où se déposent des limons.
Par exemple: « Il existe des mangroves au sud de la Floride. »""" },
{ "word": "Manichéisme", "definition": """Nom masculin.
De « Mani » fondateur de cette religion.
1- Religion de Mani en Perse au IIIème siècle, pour laquelle le bien
et le mal sont deux principes fondamentaux, égaux et antagonistes.
Elle fut rivale du christianime jusqu’au Moyen-Âge
2- Conception qui divise toute chose en deux parties, sans aucune nuance.
Par exemple: « Il y a nos amis et nos ennemis. » ou « Il y a le blanc et le noir ».
Alors qu’il peut y avoir toutes sortes de rapport à l’autre ainsi que
différentes nuances entre ces deux couleurs.""" },
{ "word": "Mantique", "definition": """Adjectif.
Du grec « mantikê » qui signifie divination.
Se dit de la pratique divinatoire.
Par exemple: « La divination peut-elle s’apprendre dans un livre de mantique ? »""" },
{ "word": "Mantra", "definition": """Nom masculin.
D’un mot sanskrit qui signifie « moyen de pensée ».
Formule sacrée du brahmanisme, émanation du principe divin.""" },
{ "word": "Manubrium", "definition": """Nom masculin.
Du latin « manubrium » qui signifie manche, poignée.
1- En zoologie, tube central portant la bouche, au milieu inférieur de
l’ombrelle d’une méduse.
2- En anatomie humaine, le manubrium sternal est le segment supérieur
du sternum auquel s’articulent les deux clavicules.""" },
{ "word": "Manuélin", "definition": """Adjectif.
Du portugais « Manoel » qui signifie Manuel pour Manuel 1er, roi du Portugal.
Style architectural et décoratif qui se développa au Portugal autour
de 1500. Ce style assez proche du style plateresque espagnol ( de
l’espagnol « plata » qui signifie argent) est caractérisé par des sculptures
ornementales sur des structures gothiques avec des influences mauresques
ou orientales.""" },
{ "word": "Marasme", "definition": """Nom masculin.
Du grec « marasmos » qui signifie dessèchement.
1- Forme aiguë de malnutrition chez l’enfant, principalement par
défaut d’apport calorique. Les symptômes de cette carence nutritive
sont une maigreur extrême, avec une atrophie musculaire et une apathie.
2- Affaiblissement, accablement, apathie profonde.
3- Arrêt d’activité, plus ou moins durable, malaise dans les affaires
politiques ou économiques.
4- Petit champignon à pied coriace appartenant à la famille des
agaricacées et qui se dessèche facilement. On peut citer le mousseron
des près ou marasme des Oréades.
Pour illustrer la définition 3 on peut donner l’exemple suivant:
« La crise économique de 2008 a été un véritable marasme pour le monde. »""" },
{ "word": "Marasque", "definition": """Nom féminin.
De l’italien « (a)marasca » issu de « amaro » qui signifie amer. Cerise marasque.
Variété de cerise acide qui pousse dans les régions méditerranéennes.
Cette cerise permet de parfumer une liqueur: Le marasquin.""" },
{ "word": "Marathe", "definition": """Adjectif et nom.
De « marrates » mot de l’Inde.
En tant qu’adjectif:
Qui a rapport aux Marathes, peuple du Dekkan.
En tant que nom masculin:
Langue indo-européenne de l’Inde, dite indo-aryenne et qui est
rattachée au sanskrit.""" },
{ "word": "Marguillier", "definition": """Nom masculin.
Du latin « matricularius » qui signifie registre.
1- Dans un sens vieilli, chacun des membres composant le bureau de
conseil d’une paroisse.
2- Dans un sens moderne, laïc chargé de l’entretien et de la garde d’une église.""" },
{ "word": "Maringouin", "definition": """Nom masculin.
Du tupi-guarani, langue du Brésil, « mbarigui » qui signifie cousin, moustique.
Nom donné à tous les diptères parasites de l’homme comme le moustique
et le cousin dans les Antilles, les pays tropicaux et au Canada.""" },
{ "word": "Marli", "definition": """Nom masculin.
L’origine de ce mot est incertaine. La première attestation de « marly »
est apparue dans l’inventaire du chevalier d’Effiat. Marly était une localité des Yvelines où Louis XIV avait fait construire un château si somptueux que ce nom
servit à la dénomination de plusieurs objets de luxe.
1- Partie périphérique d’une assiette, constituant une couronne
horizontale ou légèrement inclinée tout autour du bassin central.
Cette  bordure n’est généralement pas destinée à recevoir de la
nourriture elle-même. Exceptionnellement, des sauces ou des accompagnements y sont servis.
Le marli sert à manipuler l’assiette, pleine sans se salir les doigts.
Il a également une fonction décorative, lorsqu’il est orné de motifs
par exemple de frises circulaires.
Le marli est aussi le filet en talus qui borde en dedans la moulure
d’une assiette d’argent.
2- Sorte de gaze utilisée pour faire des ouvrages de mode.
Par exemple: « Un plat au marli noyé d’émail. » Colette""" },
{ "word": "Martingale", "definition": """Nom féminin.
Du provençal « martegalo » issu de Martigues ville des Bouches-du-Rhône.
A- 1- Courroie du harnais du cheval qui relie la sangle (sous le
ventre de l’animal) à la partie de la bride qui passe sous le
chanfrein.
    2- Bande de tissu ou de cuir placée horizontalement sur le dos
d’un vêtement, à hauteur de la taille.
B- Du provençal « jouga [jouer] a la martegalo ».
Manière de jouer consistant à miser le double de la perte du coup précédent.
Par exemple: « Jouer la martingale à la roulette. »
Par extension, combinaison plus ou moins scientifique qui serait
fondée sur le calcul des probabilités et que l’on appliquerait au jeu.
Par exemple: « Appliquer une martingale. »""" },
{ "word": "Maryse", "definition": """Nom féminin.
Antonomase de la marque éponyme Maryse.
En cuisine, ustensile servant à racler le fond des récipients.""" },
{ "word": "Maskinongé", "definition": """Nom masculin.
Mot algonquin qui signifie « brochet difforme ou très gros ».
Au Canada, poisson téléostéen (au squelette complètement ossifié) de
la famille des ésocidés, qui vit en eau douce et qui ressemble à un
brochet géant.""" },
{ "word": "Massepain", "definition": """Nom masculin;
De l’italien « marzapane »qui désignait une mesure de capacité sur la
côte sud de l’Asie Mineure, chez les marchands venant d’Italie, vers
1340.
Par la suite, il se serait appliqué à la petite boîte servant à
emballer la confiserie et par métonymie, à son contenu.
Patisserie composé d’amandes, de sucre et de blanc d’œuf.
Par exemple: »On trouve la première référence concrète au massepain
dans un registre de la ville de Lübeck. »""" },
{ "word": "Mastoc", "definition": """Adjectif.
Peut-être issu de l’allemand « Mastochs » qui signifie boeuf à l’engrais
ou mot rouchi, du radical de « masse » qui signifie massif.
1- Dans un sens vieilli, homme trapu, épais.
2- Dans un sens moderne et péjoratif et en tant qu’adjectif
invariable. Se dit de ce qui a une forme, une silhouette massive.
Par exemple: « Des bijoux mastoc. »""" },
{ "word": "Mastos", "definition": """Nom féminin.
Du grec « mastos » qui signifie sein.
Dans la Grèce Antique, coupe à vin en forme de sein.
On l’appelait aussi une coupe parabolique. Elle était de verre ou d’argent.
Elle était ornée d’un téton à son extrémité et de figures
mythologiques liées à la lactation et à la féminité.
Le plus anciennes de ces coupes datent du Vème siècle avant notre ère.""" },
{ "word": "Matamore", "definition": """Nom masculin.
Nom propre d’un personnage de comédie. De l’espagnol « matamoros » qui
signifie tueur de maures.
Dans un sens vieilli, se dit d’un faux-brave, un vantard, un fanfaron.""" },
{ "word": "Matole", "definition": """Nom féminin.
Étymologie inconnue.
Piège qui permet de capturer vivants de petits oiseaux, comme
l’alouette des champs, le pinson ou l’ortolan.
L’oiseau est attiré par un appelant et va picorer les grains répandus
sous une petite cage « la matole ». S’il déséquilibre la tige de fer qui
retient la cage, il devient prisonnier.
Ce type de chasse est pratiqué dans les Landes, le Lot et Garonne, le
Tarn et Garonne et la Gironde.
Cette technique est interdite pour les ortolans qui sont une espèce
protégée. Elle est autorisée pour l’alouette.""" },
{ "word": "Matorral", "definition": """Nom masculin. Au pluriel matorrals.
De l’espagnol « matorral » de même signification. La racine semble
pré-latine, en effet le sarde « mata » signifie buisson, l’occitan
« mata » signifie touffe d’arbres,
l’hébreu « mattagh » signifie arbuste, le berbère « tha-matta » signifie
buisson, tas d’herbes.
Formation végétale des pays méditerranéens, plus ouverte que le maquis
et constituée de cistes, d’oliviers sauvages, de lentisques,
d’arbousiers et de petits chênes.
Par exemple: « Nous irons nous promener dans le matorral, demain matin. »""" },
{ "word": "Maya", "definition": """Nom féminin.
D’un mot sanskrit qui signifie illusion.
Dans la pensée hindoue, apparence illusoire qui cache la réalité ou
provoque l’ignorance.
Par exemple: « La maya freine notre progrès mental. »""" },
{ "word": "Mazagran", "definition": """Nom masculin.
Du nom d’une ville d’Algérie située près de Mostaganem dans la région d’Oran. .
1- Dans un sens vieilli, café chaud ou froid servi dans un verre.
2- Verre à pied, en porcelaine épaisse, destiné à la consommation de café.""" },
{ "word": "Mécène", "definition": """Nom masculin.
Du latin « Mæcenas » nom d’un ministre de l’Empereur Auguste dans le
monde romain.
Personne fortunée  qui par goût des arts aide les écrivains, les artistes.
Par extension, personne physique ou morale qui apporte un soutien
matériel et sans contrepartie directe à une œuvre, à un ou des
artistes, qui présentent un intérêt dans le domaine de la culture. .""" },
{ "word": "Méconium", "definition": """Nom masculin.
Du grec « mêkônion » qui signifie suc de pavot.
Matière pâteuse et brunâtre qui s’accumule dans l’intestin du fœtus et
qui constitue les premières selles du nouveau-né.""" },
{ "word": "Mégir", "definition": """Verbe transitif.
Se dit du tannage d’une peau ou d’un cuir avec une préparation d’eau,
de cendre et d’alun.
On dit : « Un cuir mégi ».
Le synonyme de mégir est mégisser.  """ },
{ "word": "Mégot", "definition": """Nom masculin.
Peut-être du dialecte « mégauder » qui signifie têter, issu de « mègue »
qui signifie petit lait, du gaulois « mesigu- « .
Familièrement, bout de cigare ou de cigarette que l’on a fini de fumer.""" },
{ "word": "Méhari", "definition": """Nom masculin.
De l’arabe d’Algérie « mehri » qui signifie de la tribu des Mahra.
Dromadaire d’Arabie domestiqué en Afrique du Nord et dressé pour les
courses rapides.""" },
{ "word": "Méjanage", "definition": """Nom masculin.
Du provençal « méjan » qui signifie moyen.
Classement des laines par qualité ou longueur de fibres.""" },
{ "word": "Méléagrine", "definition": """Nom féminin.
Du grec « meleagris » qui signifie pintade.
Nom donné à l’huître perlière. On dit aussi une pentadine.
L’origine de ce nom de mollusque lié à un nom d’oiseau provient de son
anatomie. C’est un mollusque ptériomorphe c’est à dire en forme
d’ailes et par analogie les embranchements de cette classe
prennent des noms d’oiseaux.""" },
{ "word": "Mélisme", "definition": """Nom masculin.
Du grec « melos » qui signifie air de musique.
Technique qui consiste à charger sur de nombreuses notes une seule
syllabe d’un texte chanté à la différence du syllabique qui associe
une note à une syllabe.
On peut trouver des exemples de mélisme dans le chant grégorien, la
liturgie juive, les liturgies de l’islam et de l’hindouisme.""" },
{ "word": "Mélusine", "definition": """Nom féminin.
De la fée Mélusine.
Feutre à poils longs et souples que l’on utilise en chapellerie.""" },
{ "word": "Mème", "definition": """Nom masculin.
De l’anglais « meme ». Ce mot apparut pour la première fois dans le
livre de Richard Dawkins « The Selfish Gene » Le Gène Egoïste en 1976.
Du grec « miméma » qui signifie quelque chose qui est imité. Il a été
choisi pour sa ressemblance à « gène » et au mot français « même » ainsi
que pour sa parenté à l’idée de mémoire.
Le mot « mème » est donc issu d’une fusion sémanrtique autour des
notions d’élément de mémoire imitable, supoort d’évolution.
En anthropologie, le mème est un élément reconnassable relatif à la
culture humaine. Cela peut-être une idée, une forme, une règle de
comportement, un code culturel, un
symbole.
Les mèmes se reproduisent par réplication (transmission écrite, orale
ou gestuelle), peuvent muter et sont en compétition darwinienne dans
la sphère socilae.
Par exemple: »Un mème est un schéma de pensée qui s’exprime et se
duplique au moyen du langage. »Sylvie Denis Paradiqme Party 2000.""" },
{ "word": "Ménade", "definition": """Nom féminin.
Du grec « mainades » issu de « mainomai » qui signifie délirer, être furieux.
Ce mot, souvent au pluriel, appartient à la mythologie grecque; il
équivaut au terme « bacchante » chez les Romains.
Les ménades sont les accompagnatrices de Dyonisos. C’est la tragédie
des « Bacchantes » d’Euripide qui nous a laissé le descriptif des rites
orgiaques des ménades.
Les ménades sont des femmes possédées qui personnifient les esprits
orgiaques de la nature. Elles sont ivres en permanence et ont le
visage tatoué pour pouvoir se dissimuler. 
Elles peuvent devenir folles et alors particulièrement cruelles.
Leur mois de prédilection est le mois d’octobre qui est le mois des vendanges.""" },
{ "word": "Mentisme", "definition": """Nom masculin.
Du latin « mens, mentis » qui signifie esprit.
En psychologie, fuite des idées.""" },
{ "word": "Mentor", "definition": """Nom masculin.
Nom d’un personnage de l’Odyssée d’Homère popularisé par le Télémaque
de Fénelon.
Guide ou conseiller sage et expérimenté.""" },
{ "word": "Mephitique", "definition": """Adjectif.
Du latin « mephitis » vapeur de soufre d’origine volcanique.
Odeur toxique et nauséabonde.""" },
{ "word": "Mercaptan", "definition": """Nom masculin.
Du latin « mercurium captans » qui signifie qui capte le mercure.
En chimie, thioalcool à l’odeur fétide en raison du soufre qui le compose. .
Par exemple: »Le mercaptan est un gaz toxique qui parfume le gaz de ville. »""" },
{ "word": "Méricarpe", "definition": """Nom masculin.
Du grec « meros » qui signifie partie et « karpos » qui signifie fruit.
Dans un fruit tous les éléments qui se dissocient à maturité.""" },
{ "word": "Mérisme", "definition": """Nom masculin.
Du grec « merisma » qui signifie délimitation, dérivé de partie.
Apparenté à « mereo » qui signifie recevoir comme part, mériter.
1- En linguistique, trait distinctif minimal dont la combinatoire
forme des phonèmes.
2- En rhétorique, division d’un sujet, d’un point à traiter en
diverses parties.
Par exemple: Dans la Bible, il existe un cas particulier de mérisme,
qui fait appel à la binarité des membres; comme « Le ciel et la terre »
qui sont les deux termes qui expriment un tout.""" },
{ "word": "Merrain", "definition": """Nom masculin.
Du latin « materiamen » issu de « materia » qui signifie bois de construction.
1- Bois de chêne débité en planches destinées surtout à la fabrication
de tonneaux.
2- En vènerie, tige centrale de la ramure du cerf.""" },
{ "word": "Merzlota", "definition": """Nom féminin.
Mot russe qui signifie terrain congelé.
Couche de sol et de sous-sol qui ne dégèle jamais. Par exemple dans la
toundra.
Le pergélisol et le permafrost sont des synonymes.""" },
{ "word": "Mescaline", "definition": """Nom féminin.
Du mexicain « mexcalli » qui signifie peyotl.
Substance chimique dite alcaloïde, extrait d’une plante de la famille
des cactacées, le peyotl. Ce produit est un puissant hallucinogène.""" },
{ "word": "Métonymie", "definition": """Nom féminin. 
Du grec metônumia : changement de nom.
Procédé d’expression par lequel on exprime un concept par un autre qui lui est lié nécessairement.
Le contenu et le contenant, l’effet et la cause, le tout et la partie.
Exemples : boire un verre, une fine lame (un escrimeur).""" },
{ "word": "Métope", "definition": """Nom féminin.
Du grec »metopê » de « meta » qui signifie entre et « opê » qui signifie ouverture.
En architecture, intervalle séparant deux triglyphes dans une frise
dorique et dans lequel se trouve généralement un panneau sculpté.
Par exemple: les métopes du Parthénon.""" },
{ "word": "Mezzo-Tinto", "definition": """Nom masculin.
Du même mot en italien qui signifie demi-teinte.
Gravure à la « manière noire » exécutée en grattant la planche grenée
pour obtenir à partir d’un noir uniforme, des gris plus ou moins
sombres jusqu’à un blanc pur.""" },
{ "word": "Mimosa", "definition": """Nom masculin. Mais ce mot a été féminin jusqu’au XIX ème siècle.
Du latin « mimus » qui signifie mime par allusion à la contractilité de la plante.
1- Arbre ou arbrisseau de la famille des mimosacées comme l’acacia. Il
est originaire des régions chaudes mais il a été acclimaté dans les
régions tempérées.
Il est cultivé pour ses fleurs jaunes très odorantes en forme de
petites boules duveteuses.
2- Les branches fleuries du mimosa.
3- Œuf mimosa: œuf dur coupé en deux dont le jaune est mélangé avec de
la mayonnaise.""" },
{ "word": "Minaret", "definition": """Nom masculin.
Du turc « minare » issu de l’arabe « manâra » qui signifie phare.
Tour d’une mosquée en haut de laquelle, le muezzin appelle par un
chant, les fidèles à la prière.""" },
{ "word": "Miscellanées", "definition": """Nom féminin pluriel.
Du latin « misecellanea » qui signifie choses mêlées,
adjectif substantivé du verbe « miscere ».
Mélanges d’écrits en rapport avec la science, la littérature ou la culture.""" },
{ "word": "Misogame", "definition": """Nom masculin.
Du grec « misein » qui signifie haïr et « gamos » qui signifie mariage.
Se dit de celui qui hait le mariage.""" },
{ "word": "Mitraille", "definition": """Nom féminin.
De l’ancien français « mitaille » issu de « mit » qui signifie morceau de
cuivre de Flandres, par le moyen néerlandais « mit », d’un radical
« germanique « mit » qui signifie couper en morceaux.
1- Ferraille, puis balles de fonte que l’on utilisait autrefois sur
les canons comme projectiles meurtriers.
Par exemple: »Canons chargés à mitraille. »
Dans une acception moderne et courante: Décharge d’artillerie et plus
spécialement d’obus et de balles.
Par exemple: »Fuir sous la mitraille. »
2- Menue monnaie de métal.
Par exemple: »Avoir les poches pleines de mitraille. »
3- Dans un sens vieilli. Débris de métaux.""" },
{ "word": "Mnème", "definition": """Nom masculin. Selon la plupart des dictionnaires.
Du grec ancien « mnêmê » qui signifie mémoire. Dans la mythologie
grecque, Mnémé était l’une des trois Muses d’origine (béotiennes),
filles de Mnémosyne, même si elles furent plus tard au nombre de neuf.
Elle était la Muse de la mémoire. Ses sœurs étaient Aédé et Mélété.
En philosophie, se dit de la mémoire au sens large comprenant la
mémoire inconsciente et la mémoire organique. Par métonymie, (la
partie représentant le tout)
trace organique qui serait la base matérielle du souvenir.
En psychologie c’est la mémoire d’un événement.
Par exemple: « Le mnème est la trace laissée dans la cellule par les
excitations antérieures. »""" },
{ "word": "Modillon", "definition": """Nom masculin.
De l’italien « modiglione » issu du latin « mutulio », du lain « mutulus »
qui signifie tête de chevron.
En architecture, ornement en forme de console renversée placé sous la
saillie d’une corniche ou face à un mur, pour supporter un vase ou un
buste.""" },
{ "word": "Mogigraphie", "definition": """Nom féminin.
Du grec mogis avec peine et graphein écrire
En médecine c’est la crampe de l’écrivain qui se caractérise par des
troubles des muscles de la main et des doigts qui peuvent empêcher
d’écrire.""" },
{ "word": "Moite", "definition": """Adjectif.
Vient peut-être du latin « mucidus qui signifie moisi  par croisement
avec le latin « musteus » qui signifie juteux et qui vient de « mustus »
qui signifie moût.
Se dit de ce qui est légèrement humide. Par exemple: « Avoir les mains moites ».""" },
{ "word": "Moko", "definition": """Nom masculin.
Origine inconnue.
En argot marin, marin toulonnais.
Par extension, provençal.
« Pépé le Moko » film de Julien Duvivier.""" },
{ "word": "Monade", "definition": """Nom féminin.
Nom féminin.
Du latin « monas, monadis » qui signifie unité.
Chez les Pythagoriciens, unité parfaite qui est le principe des choses
matérielles et spirituelles.
Chez Leibniz, substance simple et indivisible, sans étendue ni figure,
sans début ni fin, non déterminée par des causes extérieures. Du point
de vue intérieur elle est dotée de perception et d’une tendance à accroître
la distinction de ses perceptions.
Trois catégories sont à distinguer:
La monade qui ne possède pas de mémoire; le végétal.
La monade douée de mémoire; l’animal.
La monade douée de raison, de connaissance des vérités éternelles et
de conscience; c’est alors l’esprit propre à l’homme.""" },
{ "word": "Monarque", "definition": """Nom masculin.
Du grec « monarkhês » issu de « monos » qui signifie seul et « arkhein » qui
signifie commander.
1- Chef de l’Etat dans une monarchie.
2- Papillon diurne.""" },
{ "word": "Monère", "definition": """Nom masculin.
Du latin « monêrês » qui signifie simple.
1- En histoire des sciences, mélange de micelles, de bactéries et de
fragments énuclées d’amibes, considéré à la fin du XIX ème siècle
comme un être unicellulaire sans noyau.
2- En biologie, les monères sont un embranchement du règne végétal qui
contient les bactéries et les cyanobactéries. .""" },
{ "word": "Moreau", "definition": """Nom masculin.
Du latin « maurellus » qui signifie brun comme un Maure.
Se dit d’un cheval d’un noir luisant.
Le féminin se dit « morelle ».
Par exemple: « Une jument morelle. »""" },
{ "word": "Morganatique", "definition": """Adjectif.
Du latin « morganaticus » issu du latin « mornanegiba » qui signifie « don
du matin des noces,  du francique « morgan » qui signifie matin et
« geba » qui signifie don.
En droit historique, se dit d’une union contractée entre un roi et une
femme de condition inférieure, et de la femme ainsi épousée qui ne
bénéficie pas de
tous les droits qui seraient accordés à une épouse de sang royal.""" },
{ "word": "Mortadelle", "definition": """Nom féminin.
De l’italien « mortadella » issu du latin « murtatum » qui signifie farce au myrte.
Charcuterie d’origine italienne. Gros saucisson moelleux et de couleur
rosée qui se consomme froid. Il est fabriqué avec du bœuf, du porc et
des morceaux de gras.""" },
{ "word": "Mosan", "definition": """Adjectif.
De « Mosa » qui signifie Meuse.
L’art Mosan est l’art qui s’est développé entre le Rhin et la Meuse du
XIème au XIIIème siècle.""" },
{ "word": "Mosette", "definition": """Nom féminin.
De l’italien « mozetta » altération de « almozetta » qui signifie petite
aumusse. L’aumusse était une petite fourrure que portaient les chanoines sur le
bras en allant à l’office. Cette fourrure était un symbole de canonicat.
La mosette est une courte pèlerine que portent certains dignitaires
ecclésiastiques.""" },
{ "word": "Mot", "definition": """Nom masculin.
Dans le dictionnaire « Le Robert »
Du latin « mutum » issu du verbe « muttire » qui signifie souffler mot,
littéralement dire mu.
Dans le dictionnaire « Larousse »
Du latin « muttum » qui signifie grognement.
Chacun des sons ou groupe de sons qui forment la langue.""" },
{ "word": "Moulin-à-vent", "definition": """Nom masculin invariable.
Nom d’un vignoble.
Vin rouge du Beaujolais, issu du vignoble de ce nom, très apprécié
pour son bouquet.""" },
{ "word": "Mousmé", "definition": """Nom féminin.
Retranscription du mot japonais « musume » prononcé « mousoume » qui
signifie fille au sens de la filiation.
Dans le français du début de siècle, ce mot désignait une fille facile.
Ce terme a été utilisé par Marcel Proust dans « Du côté de Guermantes ».
il y définit le mot mousmé de la façon suivante.
« C’est Loti qui introduisit ce mot en France. C’est un mot qui
signifie très jeune fille ou très jeune femme. C’est un des plus jolis
mots de la langue nippone; il semble qu’il y ait, dans ce mot, de la moue
(de la petite moue gentille et drôle comme elles en font) et de la frimousse
(de la frimousse chiffonnée comme est la leur). Je l’emploierai souvent n’en
connaissant aucun en français qui le vaille. »
Van Gogh a intitulé un tableau en 1888 : « La Mousmé dans le fauteuil ».""" },
{ "word": "Moxa", "definition": """Nom masculin.
Du japonais « mogusa » nom d’une variété d’armoise dont le parenchyme
sert de combustible.
Bâtonnet ou branche d’armoise que l’on utilise en médecine
traditionnelle chinoise, brûlé au contact de la peau dans des régions
précises et dont les effets sont comparables à ceux de l’acupuncture.""" },
{ "word": "Mozarabe", "definition": """Nom et adjectif.
De l’arabe « musta’rib » qui sifgnifie arabisé.
Au temps de l’occupation arabe en Espagne, Espagnol chrétien, qui
devait allégeance à un chef maure mais pouvait en échange pratiquer sa
religion.
En tant qu’adjectif, l’art mozarabe est l’art chrétien d’Espagne,
influencé par l’art musulman, pendant l’occupation arabe.""" },
{ "word": "Muid", "definition": """Nom féminin.
Du latin « modius » qui signifie « mesure(principale) ».
1- Ancienne mesure de capacité pour les liquides, les grains, le vin, le sel.
A Paris cette mesure était de 268 litres pour le vin et de 1872 litres
pour les matières sèches.
2- Récipient en forme de tonneau de la capacité d’un muid.""" },
{ "word": "Murex", "definition": """Nom masculin.
Du latin « murex »  qui désignait le gastéropode appartenant à la
famille des muricidae.
Dans l’Antiquité, on extrayait du murex « La pourpre de Tyr ».
Deux murex étaient utilisés pour l’extraction de la pourpre:
« Bolinus brandaris » qui est le murex droite épine.
« Hexaplex truncules » qui est le rocher fascié.
Ces deux espèces ont été décrites par Linné au XVIIIème siècle au sein
de la famille des Murex mais la classification ayant été remaniée, ces
deux murex appartiennent aujourd’hui à des genres différents.
La pourpre était très difficile à extraire et était destinée aux
vêtements de personnages hauts placés issus de la royauté et du
clergé.
Le murex se raréfiant la fabrication de la pourpre s’obtint grâce à la
cochenille et aux colorants synthétiques.""" },
{ "word": "Murrhin", "definition": """Adjectif.
Du latin « murrhinus » de même signification.
Dans l’Antiquité, les vases murrhins étaient des vases d’une matière
irisée et mal-connue appelée la murrhe, sorte de pierre ayant
l’apparence du verre  et qui était peut-être de la fluorine.
Par analogie, le verre murrhin est un verre constitué par assemblage
dans un moule d’une couche de verre ordinaire sur laquelle on dépose
et soude par réchauffage une couche de verre formée de petits morceaux colorés.
Par exemple: » Je vous donnerai en échange ce vase murrhin [….] dans
mon vestibule. » Alexandre Dumas père « Catilina »""" },
{ "word": "Muscarine", "definition": """Du latin « muscaria amanita » qui signifie amanite tue-mouches d’où est
extrait ce poison. Issu du radical « musca » qui signifie mouche.
Alcaloïde toxique de certains champignons vénéneux qui affecte les
mouvements musculaires volontaires et provoque la mort par asphyxie.
L’atropine est l’antidote de la muscarine.""" },
{ "word": "Mussif", "definition": """Nom masculin.
Du latin « (aurum) musivum » issu de « musivus » qui signifie « de mosaïque ».
L’or mussif est un sulfure d’étain d’une belle couleur jaune doré,
utilisé pour bronzer les statuettes de plâtre.
Par exemple: « Tu as pris cette statuette dorée à l’or mussif pour de l’or ? »""" },
{ "word": "Mustang", "definition": """Nom masculin.
Mot anglas de l’espagnol « mestengo » qui signifie sans maître.
Cheval d’Amérique du Nord vivant à l’état sauvage, capturé pour le rodéo.""" },
{ "word": "Myope", "definition": """Nokm masculin et adjectif.
Du latin « myops » issu du grec « muôps » qui signifie qui cligne des yeux.
En tant que nom.
1- Personne qui a la vue courte, qui ne voit distinctement que les
objets rapprochés.
Par exemple: « Tu crois qu’il t’évite, mais il est a des yeux de myope. »
En tant qu’adjectif.
2- Atteint de myopie.
Par exemple: « Il est myope comme une taupe. »
Au figuré:  Qui manque de perspicacité, de largeur de vue.
« Les politiciens sont peut-être myopes. »""" },
{ "word": "Myrmécophile", "definition": """Nom masculin.
Du grec « murmêx, murmêkos » qui signifie fourmi et « philéin » qui signifie aimer.
Se dit d’un organisme, plante ou insecte (pucerons), qui vit avec les
fourmis ou en association avec elles.""" },
{ "word": "Myrobolan", "definition": """Nom masculin.
Du grec « murobalanos » issu des mots « muron » qui signifie parfum et
« balanos » qui signifie gland et qui a donné aussi le mot mirabelle.
1- Nom donné aux fruits séchés issus de différentes espèces d’arbres
exotiques qui étaient utilisés autrefois comme purgatif et qui sont
employés aujourd’hui comme substance tannante.
2- Le prunier myrobolan ou myrobolan est un prunier sauvage de la
famille des rosacées qui est utilisé comme porte-greffe.""" },
{ "word": "Myroxyle", "definition": """Nom masculin.
Du grec « muron » qui signifie parfum et « xulon » qui signifie bois.
Arbre d’Amérique du Sud qui fait partie de la famille des légumineuses
papilionacées dont le tronc fournit une résine (baume de Tolu, baume
du Pérou).""" },
{ "word": "Mytiliculture", "definition": """Nom féminin.
Du latin « mytilus » qui signifie moule, coquillage et « cultura » qui
signifie culture.
Elevage des moules dans des parcs à moules ou moulières.""" },
{ "word": "Nadir", "definition": """Nom masculin.
De l’arabe « nâdir » qui signifie opposé [au zénith].
En astronomie, point de la sphère céleste diamétralement opposé au
zénith et qui se trouve à la verticale de l’observateur.""" },
{ "word": "Nankin", "definition": """Nom masculin.
De Nankin ville de Chine centrale.
Tissu de coton, jaune chamois qui fut d’abord fabriqué à Nankin.""" },
{ "word": "Napalm", "definition": """Nom masculin.
De l’anglais, issu de « na(phtalenate) » et « palm(itate) ».
Essence solidifiée au moyen de palmitate de sodium ou d’aluminium et
qui servit à fabriquer des bombes incendiaires.
Des bombes au napalm on été utilisées par les américains pendant la
guerre du Vietnam.""" },
{ "word": "Napée", "definition": """Nom féminin.
Du grec « napê » qui signifie bois, vallon.
Dans la mythologie grecque, nymphe des bois et des près.""" },
{ "word": "Nard", "definition": """Nom masculin.
Du latin « nardus » de même signification issu d’un mot d’origine orientale.
1- Nard indien, plante herbacée, exotique de la famille des
valérianacées. Aromate très apprécié des Anciens.
Parfum extrait de cette plante.
2- Nom de diverses valérianacées, Nard celtique, des montagnes.
3- Nard raide; plante herbacées de la famille des graminées, dont les
feuilles sont piquantes et qui est commune dans les près.
4- Synonyme de lavande aspic dont l’huile essentielle soigne les
brûlures légères.""" },
{ "word": "Narthex", "definition": """Nom masculin.
Du grec « narthêx » qui signifie férule, cassette.
En architecture, vestibule de l’église, distinct du porche en ce qu’il
est situé sous la même couverture que la nef et qu’il est souvent
surmonté d’une tribune.""" },
{ "word": "Naucore", "definition": """Nom masculin.
Du grec « naus » qui signifie navire et « koris » qui signifie punaise.
Insecte carnivore des eaux stagnantes souvent appelé « punaise d’eau ».""" },
{ "word": "Naumachie", "definition": """Nom féminin.
Du latin naumachia, issu du grec « naus » qui signifie navire et « makhê »
qui signifie combat.
-Représentation d’un combat naval dans un cirque dans lequel l’arène
était remplacée par un bassin.
-Le bassin où avait lieu le combat naval. .""" },
{ "word": "Naupathie", "definition": """Nom féminin.
Du grec « naus » qui signifie navire et « pathos » qui signifie maladie.
En médecine, nom du mal de mer.""" },
{ "word": "Navarin", "definition": """Nom masculin.
De « navarins » qui signifie navets par déformation. D’après Navarin
ville célèbre pour la bataille qui y eut lieu en 1827.
Viande de mouton ou d’agneau cuisinée en ragoût, accompagnée de petits
oignons, de pommes de terre, de carottes et de navets.""" },
{ "word": "Nebka", "definition": """Nom féminin.
Variation de l’arabe Nebkha.
Amas de sable autour d’un obstacle dans un désert.""" },
{ "word": "Nemrod", "definition": """Nom masculin.
Antonomase de « Nemrod » personnage Biblique du livre de la Genèse,
chasseur devant l’éternel.
Le mot « Nimrod » serait issu du verbe hébreu « mered » qui signifie se
rebeller ou bien serait issu de l’arabe « Nimr » qui signife tigre et
« rawad » qui signifie dompter, par
conséquent il signifierait celui qui a dompté le tigre.
Se dit d’un chasseur passionné qui tue beaucoup de gibier.
Par exemple: »Les nemrods se serrent les coudes. » Phrase tirée d’un
article sur la chasse dans le quotidien Le Monde du 17 novembre 2016.""" },
{ "word": "Néodyme", "definition": """Nom masculin.
De l’allemand « Neodym ».
Élément atomique de symbole Nd, de numéro atomique 60 et de masse
atomique 144,24, qui se présente sous la forme d’un métal blanc et qui
fait partie de la série des lanthanides ou terres rares.""" },
{ "word": "Néoténie", "definition": """Nom féminin.
Du grec « neos » qui signifie jeune et « teînein » qui signifie étendre, prolonger.
En bieologie animale, coexistence, chez l’animal de caractères
larvaires et de l’aptitude à se reproduire.
Par exemple: « L’exemple le plus connu de néoténie est l’axolotl.
Il se reproduit à l’état de larve sans avoir atteint l’âge adulte. »""" },
{ "word": "Néotie", "definition": """Nom féminin.
Du grec « neotteia » qui signifie nid d’oiseau.
En botanique, sorte d’orchidée sans chlorophylle, de la famille des
orchidacées, saprophyte et qui croît dans l’humus des hétraies.""" },
{ "word": "Néphélométrie", "definition": """Nom féminin.
Du grec « nephelos » qui signifie nuage et « métron » qui signifie mesure.
En chimie, mesure de la concentration d’une émulsion d’après sa transparence.""" },
{ "word": "Néréîde", "definition": """Nom féminin.
Du grec « Néréides » pluriel de « Nereis », de « Nérée » père des Néréides,
lié au verbe « néo » qui signifie nager.
1- En mythologie grecque, nymphe de la mer. Elles sont fille du dieu
marin Nérée et de l’océanide Doris. Elles sont au nombre de cinquante.
Elles sont dans le cortège de Poséidon et sont associées à la mer Egée.
Les plus connues sont :
Amphitrite épouse de Poséidon.
Thétis mère d’Achille.
Galatée aimée du cyclope Polyphème.
2- En zoologie, nom d’un ver marin, annélide, fouisseur, de la famille
des polychètes, qui vit sur les fonds vaseux.""" },
{ "word": "Nestorien", "definition": """Nom et adjectif.
De « Nestorius » patriarche de Constantinople au Vème siècle.
Disciple de Nestorius, hérésiarque qui affirmait que les deux natures
du Christ (divine et humaine) possédaient leur individualité propre.
Les nestoriens furent condamnés par le concile d’Éphèse.
En tant qu’adjectif, on peut dire: « L’hérésie nestorienne. »""" },
{ "word": "Neume", "definition": """Nom masculin et féminin.
Du latin médiéval « neuma », altération grecque de « pneuma » qui signifie
souffle, émission de voix.
Nom masculin
En histoire de la musique, signe servant autrefois à la notation du
plain-chant ( notation neumatique ).
Nom féminin.
Groupe de notes émises d’un seul souffle; courte mélodie qui se
vocalise, sans paroles ou sur la dernière syllabe du dernier mot, à la
fin de l’alléluia de certaines antiennes.""" },
{ "word": "Niaouli", "definition": """Nom masculin.
Mot originaire de Nouvelle-Calédonie.
Arbuste exotique de la famille des myrtacées. On extrait de ses
feuilles une huile essentielle appelée essence de Niaouli ou huile
goménolée utilisée comme antibactérienne et décongestionnante.
Son écorce est claire et très épaisse. Elle est molle et s’exfolie
comme du papier. On l’emploie pour envelopper pour la nourriture et
pour tapisser les fours.""" },
{ "word": "Nichet", "definition": """Nom masculin.
Du latin « nidus » qui signifie nid.
Œuf en plâtre, en marbre ou en albâtre que l’on place dans les nids
pour que les poules aillent pondre.""" },
{ "word": "Nicodème", "definition": """Nom masculin.
Nom d’un pharisien qui posa au Christ des questions naïves.
Familier. Se dit d’un niais, d’un nigaud.
Par exemple: »Passé un certain âge, celui qui croit encore au Père
Noël, est un Nicodème. »""" },
{ "word": "Nicol", "definition": """Nom masculin.
De « Nicol » physicien anglais.
Instrument d’optique qui est constitué principalement par un spath
d’Islande et qui est utilisé pour l’étude des phénomènes de
polarisation de la lumière.""" },
{ "word": "Nictation", "definition": """Nom féminin.
Du latin « nictatio » qui signifie clignement d’yeux.
1- Clignement des paupières.
2- Clignements fréquents de durée prolongée dus à la contraction des
muscles orbiculaires des paupières.""" },
{ "word": "Nifé", "definition": """Nom masculin.
De Ni et de Fe qui sont les symboles chimiques du nickel et du fer.
Noyau de la Terre, qui serait constitué de nickel et de fer.""" },
{ "word": "Nille", "definition": """Nom féminin.
Du latin « anaticula » qui signifie petit canard.
Manchon mobile autour du manche d’une manivelle. """ },
{ "word": "Nimbe", "definition": """Nom masculin.
Du latin « nimbus » qui signifie nuage.
1- En archéologie, cercle figuré autour de la tête de certains
empereurs, sur les médailles antiques.
2- Zone lumineuse qui entoure la tête des représentations de Dieu, des
anges ou des saints.
C’est un synonyme d’auréole.
Pour le Christ, on dit : « Nimbe crucifère ».
Le professeur Nimbus est le personnage d’une bande dessinée française,
muette et en quatre images, qui fut créée par André Daix en 1934.
C’est un homme chauve avec un seul cheveu en forme de point
d’interrogation et des lunettes rondes. Ses aventures sont de courtes
« blagues » d’un comique simple.
Aujourd’hui, un « professeur Nimbus » désigne un scientifique farfelu,
distrait ou gaffeur.""" },
{ "word": "Niobium", "definition": """Nom féminin.
De « Niobé » nom propre grec de la fille deTantale.
En chimie, élément de nombre atomique 41. Métal blanc brillant et
rare, toujours associé avec le tantale dans ses minerais, d’où son
nom.""" },
{ "word": "Nirvana", "definition": """Nom masculin.
Mot sanskrit qui signifie extinction du désir.
Dans le bouddhisme, extinction du karma qui entraîne la fin du cycle
des naissances et des morts. C’est un état de sérénité absolue.""" },
{ "word": "Nivôse", "definition": """Nom masculin.
Du latin « nivosus » qui signifie neigeux.
Historiquement, c’était le quatrième mois du calendrier républicain,
créé à la suite de la Révolution Française, vers 1793.
Ce mois s’étendait du 21 ou 22 décembre au 21 ou 22 janvier.""" },
{ "word": "Nixe", "definition": """Nom féminin.
De l’allemand « nixe » qui signifie ondine, issu du verbe « neichen » qui
signifie arroser.
Dans les légendes germaniques, génie ou nymphe des eaux.""" },
{ "word": "Nizeré", "definition": """Nom masculin.
Du persan « nizrin » qui signifie rose musquée.
En parfumerie, essence de rose blanche.""" },
{ "word": "Noctiluque", "definition": """1- Adjectif.
Du latin « noctilucus » qui signifie qui luit pendant la nuit.
En zoologie, se dit d’un être vivant qui a la propriété d’émettre une
lueur dans l’obscurité. Par exemple le lampyre noctiluque qui est le
ver luisant.
2- Nom féminin.
Protozoaire luminescent qui vit dans la mer et se présente sous forme
d’une sphère minuscule et molle.""" },
{ "word": "Nocuité", "definition": """Nom féminin.
Du latin « nocuus » qui signifie nuisible.
Caractère de ce qui est nuisible.""" },
{ "word": "Noétique", "definition": """Adjectif. Du grec noêtikos qui signifie doué d’intelligence. 
En philosophie, c’est la théorie de l’intelligence, de la pensée (la noèse).
La noèse est l’acte même de la pensée selon Husserl au sein de la phénoménologie. C’est le noème l’objet intentionnel de la pensée.""" },
{ "word": "Noli me tangere", "definition": """Nom masculin invariable.
Expression latine qui signifie: »Ne me touche pas. » Extraite de
l’Évangile selon saint Jean.
1- En médecine. Terme vieilli. Ulcère cutané que les divers topiques
(médicaments locaux que l’on applique) ne font qu’irriter.
2- En botanique. Balsamine des bois, voisine de l’impatiens.""" },
{ "word": "Nome", "definition": """Nom masculin.
Ce mot a deux origines étymologiques et deux définitions distinctes.
1- Du grec « nomos » qui signifie portion de territoire, division,
district. mais aussi pâturage qui est une division de la terre en
champs.
Issu de « nemein »qui signifie diviser et par extension, mener paître
les troupeaux, couper, ronger.
a- Historiquement, division adminnistrative de l’Egypte ancienne.
Aujourd’hui, circonscription administrative de la Grèce moderne.
b- En médecine, nom d’un ulcère qui attaque la peau.
2- Du grec « nomos » qui signifie loi.
a- Dans l’Antiquité, sorte de poèmes qui se chantaient en l’honneur d’Apollon.
b- Dans l’Antiquité, chant ou air assujetti à une certaine cadence.""" },
{ "word": "Nominalisme", "definition": """Nom masculin.
Du latin « nomen » qui signifie nom.
1- En philosophie, doctrine selon laquelle les idées ne sont que des
noms, des mots.
Cette doctrine a vu le jour au sein de la scolastique médiévale. Son
fondateur est Roscelin de Compiègne.
Par exemple le mot homme n’existe que dans sa singularité et ne
représente pas l’essence de l’homme en général.
2- Le nominalisme scientifique est une doctrine scientifique qui
substitue l’idée de réussite empirique ou de commodité à celle de
connaissance absolue et de vérité.
3- En droit le nominalisme monétaire, est un principe en vertu duquel
la somme due par un débiteur est celle qui avait été prévue au moment
de la contraction de la dette sans autre considération sur les fluctuations
monétaires.""" },
{ "word": "Nomographe", "definition": """Nom masculin.
Du grec « nomos » qui signifie loi et « graphein » écrire.
Auteur d’un recueil de lois ou d’une étude sur les lois.""" },
{ "word": "Nomologie", "definition": """Nom féminin.
Du latin « nomos » qui signifie loi et « logos » qui signifie discours.
Etude des lois.""" },
{ "word": "Noologie", "definition": """Nom féminin.
Du grec « noos » qui signifie esprit et « logos » qui signifie discours.
En philosophie, se dit de ce qui a pour objet le monde de l’esprit,
par opposition à la cosmologie qui a pour objet l’univers.""" },
{ "word": "Nopal", "definition": """Nom masculin.
Mot espagnol issu de l’aztèque nopalli.
Cactus à rameaux aplatis (raquette) dont les fruits sont comestibles.
Ce sont les figues de Barbarie.""" },
{ "word": "Nostoc", "definition": """Nom masculin.
De « nostoch » au XVIIème siècle. Ce mot d’origine incertaine aurait été
créé par Paracelse.
En botanique, algue bleue microscopique de la famille des
cyanobactéries qui forme des masses gélatineuses dans les sols
humides.""" },
{ "word": "Notonecte", "definition": """Nom masculin ou féminin.
Du grec « notos » qui signifie dos et « nektos » qui signifie nageur.
En zoologie, punaise d’eau, de la famille des hémiptères, qui nage sur le dos.""" },
{ "word": "Noumène", "definition": """Nom masculin.
Mot allemand créé par Kant. Du grec « noumena » qui signifie choses
pensées, lui-même issu de « noein » qui signifie penser.
En philosophie, se dit de l’objet de la raison, de la réalité
intelligible, opposée à « phénomène » qui est la réalité sensible.
C’est aussi une chose en soi.""" },
{ "word": "Nuoc-Mam", "definition": """Nom masculin.
D’un mot vietnamien qui signifie eau de poisson.
Sauce de poisson macéré dans une saumure et qui constitue un
assaisonnement très employé dans la cuisine vietnamienne.
Par exemple: « Peux-tu me passer le nuoc-mam que j’en verse un peu sur mon riz ? »""" },
{ "word": "Nuraghe", "definition": """Nom masculin.
Du sarde « nurage » issu de l’hébreu « nour » qui signifie lumière et
« hag » qui signifie toit.
En archéologie, tour antique en forme de cône tronqué, propre à la
Sardaigne. Au pluriel on dit des « nuraghi ».""" },
{ "word": "Nycthémère", "definition": """Nom masculin.
Du grec « nus, nuktos » qui signifie nuit et « hêmera » qui signifie jour.
Espace de temps d’une durée de vingt quatre heures qui comprend un
jour et une nuit et qui correspond à un cycle biologique.""" },
{ "word": "Oaristys", "definition": """Nom féminin.
Du grec « oaristus » issu de « oar » qui signifie compagne, épouse.
En littérature désigne une idylle ou des ébats amoureux.""" },
{ "word": "Obel", "definition": """Nom masculin.
Du latin « obelus » qui signifie broche.
En paléographie, trait noir en forme de broche qui sert à signaler un
passage interpolé -c’est à dire ajouté à l’original- sur les manuscrits anciens.""" },
{ "word": "Obèle", "definition": """Nom féminin.
Du latin d’origine grecque « obelus » qui signifie broche.
En paléographie, trait noir en forme de broche qui sert à signaler un
passage intercepté sur les manuscrits anciens.
Par exemple: « L’obèle, ce symbole typographique est utilisé pour
signaler une forme attendue mais in-attestée ou une forme incorrecte
dans l’écriture d’un texte. »
L’obèle primitif était un trait horizontal au-dessus et au-dessous
duquel était placé un point. Ce symbole est aujourd’hui le symbole de
la division, en mathématiques. .
L’obèle moderne a la forme d’une dague.""" },
{ "word": "Obi", "definition": """Nom féminin.
Mot japonais.
Ceinture de soie, longue et large, qui s’enroule sur le costume
japonais traditionnel: « le kimono ».""" },
{ "word": "Oblation", "definition": """Nom féminin.
Du latin « oblatio » par « oblativus » qui signifie qui s’offre.
1- Dans un langage littéraire, action d’offrir quelque chose à Dieu.
2- Dans le langage liturgique, acte par lequel le prêtre offre à Dieu
le pain et le vin qu’il doit consacrer.""" },
{ "word": "Obsécration", "definition": """Nom féminin.
Du latin « obsecratio » issu de « obsecrare » composé de « ob » qui signifie
vers, devant et de « sacer » qui signifie sacré.
Prière par laquelle on implore Dieu où on conjure quelqu’un au nom de Dieu.""" },
{ "word": "Obvie", "definition": """Adjectif.
Du latin « obvius » qui signifie littéralement « qui vient au-devant ».
En théologie, le sens obvie est un sens qui vient naturellement à l’esprit.
Par exemple, le texte biblique a un sens au premier degré qui est un sens obvie.""" },
{ "word": "Ochlophobie", "definition": """Nom féminin.
Du grec « ochlos » qui signifie la foule.
Phobie de la foule.""" },
{ "word": "Odalisque", "definition": """Nom féminin.
Du turc « odalik » qui signifie femme de chambre de « oda » qui signifie chambre.
Femme de chambre esclave qui était au service des femmes d’un harem.
« L’Odalisque couchée » est un tableau d’Ingres.""" },
{ "word": "Olécrane", "definition": """Nom masculin.
Du grec « ôlekranon » issu de « ôlenê » qui signifie bras, coude et
« kranion » qui signifie tête.
En anatomie, apophyse du cubitus qui forme la saillie du coude.""" },
{ "word": "Ombudsman", "definition": """Nom masculin.
Du suédois « ombud » qui signifie délégué et « man » qui signifie homme.
Dans les pays scandinaves, personne chargée de défendre les droits des
citoyens face aux pouvoirs publics.
En France cette fonction est assurée par le Médiateur de la République
et au Québec par le protecteur du citoyen.""" },
{ "word": "Omerta", "definition": """Nom féminin.
De l’italien « omerta » forme dialectique de « umiltà » qui signifie humilité.
Loi du silence, dans les milieux proches de la Maffia.""" },
{ "word": "Omophore", "definition": """Nom masculin.
Du grec « omophorion » issu de « ômos » qui signifie épaule et « phérein »
qui signifie porter par « phoros ».
Portée par des dignitaires de l’Eglise, c’est une grande écharpe de
laine ou de soie qui est pliée autour de la tête et retombe devant et
derrière. Elle symbolise la brebis perdue que le Christ porte sur ses
épaules. C’est le symbole même de l’épiscopat. Elle est portée par les
Patriarches et les Métropolites des Eglises orientales. C’est
l’équivalent du « pallium » de l’Eglise latine  qui est porté par le
Pape et par les archevêques métropolitains.
Les évêques des Eglise orientales portent le grand omophore lors des
offices liturgiques excepté pour la liturgie eucharistique où ils
portent le petit omophore. Ce dernier est une petite bande de soie
brodée d’une croix et fermé sur la poitrine par une couture ou par des boutons.""" },
{ "word": "Onagre", "definition": """Nom masculin.
Du grec « onagros » qui signifie âne sauvage.
1- Âne sauvage et de grande taille.
2- En archéologie, par analogie avec la ruade de l’âne: machine de
guerre ou catapulte qui était utilisée au cours des sièges.
3- En botanique, plante cultivée pour ses fleurs et qui est appelée
aussi herbe aux ânes ou œnothère.
Le genre « oenothera » comporte 80 espèces dont aucune n’est toxique. On
pense qu’elle a été introduite accidentellement par des bâteausx en
provenanace d’Amérique du Nord.
Une des principales espèces est « Oenothera biennis » plante bisanuelle
aux fleurs jaunes très lumineuses et parfumées qui s’épanouissent au
coucher du soleil et pour une seule nuit au cours de laquelle elle
fait le régal des papillons de nuit. Elle porte aussi les noms de
« Belle du soir « et de « Primevère de la nuit ».
On extrait des graînes d’onagre une huile riche en oméga 3. Elle est
utilisée comme régulateur hormonal chez la femme et dans les
affections cutanées.
En Angleterre, elle eut son heure de gloire dans la préparation de la
« Panacée du Roi » ou « King’s cure-all ». Infusion de tiges et de
feuilles séchées qui soignait les crises d’asthme et les rhumes.
C’est aussi un « légume ancien » dont on consomme les racines. Au XIX
ème siècle on l’appelait « jambon de St Antoine » ou « jambon du
jardinnier ».""" },
{ "word": "Onc", "definition": """Adverbe.
Du latin « unquam » qui signifie quelques fois.
Mot ancien qui signifie jamais.""" },
{ "word": "Ondine", "definition": """Nom féminin.
Du latin « unda » qui signifie eau courante.
Déesse des eaux dans la mythologie germanique ou alsacienne. C’est une
nymphe, elle ne vit pas dans la mer mais dans les cours d’eau, les
rivières et les fontaines.
Elle n’a pas comme les sirènes de queue de poisson. .
Ce mot existe au masculin « ondin » mais plus rarement.
« Ondine » est aussi une pièce de théâtre de Jean Giraudoux.""" },
{ "word": "Onomasiologie", "definition": """Nom féminin.
Du grec « onomasia » qui signifie désignation issu de « onoma » qui
signifie nom et « logos » dicours, parole.
Étude de la désignation par un mot, c’est-à-dire: on part d’un concept
ou d’une notion et on recherche les noms qui y sont rattachés.""" },
{ "word": "Onyx", "definition": """Nom masculin.
Du grec « onux » qui signifie ongle, cette pierre étant translucide
comme un ongle.
Variété d’agate, qui présente des zones concentriques régulières, de
couleurs variées.
Ce peut être aussi une variété de marbre.""" },
{ "word": "Ophite", "definition": """Nom masculin.
Du grec « ophis » qui signifie serpent. Les rayures de cette pierre
évoquent une peau de serpent.
1- Marbre de couleur sombre, souvent verdâtre et parfois veiné de
cristaux blancs de feldspath.
2- Membre d’une secte gnostique égyptienne, vers le IIème siècle après
Jésus-Christ, vouant un culte au serpent tentateur de la Création et
en faisant un symbole du Messie.""" },
{ "word": "Ophrys", "definition": """Nom féminin.
Du grec « ophrys » qui signifie sourcil.
Orchidée terrestre, vivace dont les fleurs ressemblent à des insectes.
Certaines ressemblent à des mouches, d’autres à des abeilles, d’autres
encore à des araignées.""" },
{ "word": "Opimes", "definition": """Adjectif féminin pluriel.
Du latin « opimus » qui signifie riche.
Dans l’Antiquité, des dépouilles opimes étaient les armes du général
ennemi tué et dépouillé de la propre main du général romain vainqueur.
Elles étaient ensuite consacrées à Jupiter.""" },
{ "word": "Opisthodome", "definition": """Nom masculin.
Du grec « opisthen » qui signifie derrière, en arrière et « domos » qui
signifie maison.
Partie postérieure d’un temple grec. Pièce qui abritait le trésor et à
laquelle seuls les prêtres et les prêtresses avaient accès.""" },
{ "word": "Opisthographe", "definition": """Nom masculin.
Du grec « opisthen » qui signifie derrière, en arrière et « graphéin » qui
signifie écrire.
Manuscrit qui est couvert d’écriture au recto comme au verso.""" },
{ "word": "Opodeldoch", "definition": """Nom masculin.
Peut-être du grec « opos » qui signifie suc.
En pharmacologie, médicament à base de savon et d’ammoniac qui est
utilisé en frictions contre les douleurs.""" },
{ "word": "Oponce", "definition": """Nom féminin.
Du grec « opuntios » issu de « Oponte » ville de Grèce antique.
Plante grasse de la famille des cactées à tiges aplaties en raquettes
portant des tubercules épineux d’où sortent de grandes fleurs.
Le figuier de Barbarie est une oponce.""" },
{ "word": "Opopanax", "definition": """Nom masculin.
Du grec « opos » qui signifie suc et « panax » qui signifie plante médicinale.
Plante vivace qui fait partie de la famille des ombellifères et qui
possède une forte tige et de grandes inflorescences.
Elle pousse dans les rochers et dans les sables des régions méditerranéennes.
Une de ses variétés appelée Commiphora erythraea pousse en Afrique du
Nord et fournit une gomme-résine aromatique utilisée en parfumerie
qui a le même nom que la plante qui la produit : l’opoponax.
Cette gomme-résine est obtenue par exsudation de l’écorce de la tige
et possède un parfum velouté, balsamique, chaud et un peu terreux.
Elle est utilisée en note de fond des parfums de type oriental.""" },
{ "word": "Optatif", "definition": """Adjectif.
Du latin « optativus » issu de « optare » qui signifie souhaiter.
En linguistique se dit de ce qui exprime le souhait.
Le mode optatif et par ellipse l’optatif est un mode de conjugaison
servant à exprimer le souhait. Il existe en grec ancien et en
sanskrit. Ce mode était encore utilisé dans certains livres de grammaire
française à la place de l’impératif, au début du XXème siècle.""" },
{ "word": "Optogénétique", "definition": """Nom féminin.
Du grec « optos » qui signifie visible et « genetikos » qui signifie
propre à la génération.
Mot créé en 2006 qui nomme la faculté d’activer un ou plusieurs
neurones au moyen d’une source lumineuse.
Les travaux sont encore à l’état de recherche et pourraient ouvrir la
voie à la guérison de certaines pathologies cérébrales mais aussi
permettre la manipulation de certaines cellules cérébrales.""" },
{ "word": "Orbitèle", "definition": """Nom féminin.
Du latin « orbis » qui signifie cercle et « tela » qui signifie toile.
En zoologie, araignée qui tisse une toile polygonale à symétrie
centrale, qui forme des cercles concentriques.
Par exemple: « Toutes les araignées ne tissent pas des toiles comme le
font les orbitèles. »""" },
{ "word": "Ordalie", "definition": """Nom féminin.
Du latin « ordalium » qui signifie jugement.
Anciennement, c’était une épreuve de jugement par les éléments
naturels. Ce jugement de Dieu, avait lieu par l’eau ou par le feu.
Par exemple, lors de l’épisode biblique du veau d’or, on fit boire aux
hébreux une boisson composée d’eau et du veau d’or broyé, afin de
juger de leur culpabilité.""" },
{ "word": "Orfraie", "definition": """Nom féminin.
Du latin « ossifraga » qui signifie qui brise les os.
1- Dans un sens vieilli, pygargue c’est à dire grand aigle de mer.
2- Expression « Pousser des cris d’orfraie » . Pousser des cris
épouvantables, très aigus (par confusion avec effraie).""" },
{ "word": "Orfroi", "definition": """Nom masculin.
Du latin « aurum phrygium » qui signifie or phrygien.
Large, bande de soie ou d’une autre matière, richement brodée de fils
d’or ou de fils d’argent, qui orne les vêtements des prêtres.""" },
{ "word": "Organeau", "definition": """Nom masculin.
Du latin « organum » qui signifie instrument.
1-Anneau métallique très épais scellé dans la maçonnerie d’un quai
pour amarrer les bâteaux.
2-Anneau d’une ancre sur laquelle se place la chaîne ou le cable.""" },
{ "word": "Orgeat", "definition": """Nom masculin.
Du provençal « orjat » de « orge ».
Sirop qui était préparé autrefois avec une décoction d’orge.
De nos jours ce sirop est une émulsion d’amandes douces et d’amandes amères.""" },
{ "word": "Orichalque", "definition": """Nom masculin.
Du grec « orelkhalkos » qui signifie cuivre de montagne, de « oros » qui
signifie montagne et « khalkos » qui signifie cuivre.
Dans la Rome antique, se dit d’un métal composé d’un alliage de cuivre
et de zinc ou laiton.
Ce métal était considéré comme fabuleux; il était présent dans de
nombreux textes anciens. Platon l’a décrit comme le métal utilisé par
les Atlantes habitants de l’Atlantide.
L’archal est de même origine étymologique. Le fil d’archal est un fil de laiton.""" },
{ "word": "Oriel", "definition": """Nom masculin.
De l’anglais « oriel window » qui signifie fenêtre sous une galerie, un
auvent. Issu de l’ancien français « oriol » dont l’origine est inconnue
et qui signifie « porche ».
Fenêtre en encorbellement faisant saillie sur une façade de maison.""" },
{ "word": "Orin", "definition": """Nom masculin.
Ce mot vient peut-être du moyen néerlandais « ooring » qui signifie
boucle d’oreille puis anneau d’ancre. Il est attesté seulement à
partir du XIX ème siècle.
Il est à rapprocher du catalan « orri » qui signifie port.
Terme de marine, qui désigne un cordage reliant une ancre à la bouée
qui permet d’en relever l’emplacement.
C’est aussi le câble qui sert à maintenir une mine immergée entre deux eaux.""" },
{ "word": "Ornithorynque", "definition": """Nom masculin.
Du grec « ornithos » qui signifie oiseau et « rhinkos » qui signifie bec.
Mammifère vivipare semi-aquatique de la famille des monotrèmes, à bec
corné, à longue queue plate et aux pattes palmées qui vit en Australie
et en Tasmanie.""" },
{ "word": "Orphéon", "definition": """De « Orphée » personnage mythologique.
1- Dans le langage vieilli sorte d’instrument de musique à cordes et à clavier.
2- Ecole, assemblée d’hommes pratiquant le chant choral.""" },
{ "word": "Orseille", "definition": """Nom féminin.
Du catalan « orxella » par l’arabe « urga » à la définition incertaine.
Lichen des côtes rocheuses de la Méditerranée qui fournit une matière
colorante de couleur pourpre.
Teinture tirée de ce lichen et utilisée comme colorant.""" },
{ "word": "Orthodromie", "definition": """Nom féminin.
Du grec « orthodromein » qui signifie courir en ligne droite.
Route d’un avion ou d’un navire qui suit la voie la plus directe.
Le chemin le plus court entre deux points sur une surface plane ou courbe.""" },
{ "word": "Ortolan", "definition": """Nom masculin.
Du provençal « ortolan » issu du latin « hortulanus « qui signifie jardin.
Petit oiseau à chair très estimée, de la famille des passereaux,
cousin du moineau et migrateur. C’est une variété de bruant à gorge
jaune et ventre orangé, qui vit en Europe méridionale.
La chasse des ortolans est interdite depuis 1979 par une directive
européenne mais reste pratiquée dans le sud-ouest de la France.""" },
{ "word": "Orvet", "definition": """Nom masculin.
De l’ancien français « orb » qui signifie aveugle.
Reptile de la famille des sauriens. proche des lézards, ovovivipare et
dépourvu de membres. Il ressemble à un serpent.""" },
{ "word": "Orviétan", "definition": """Nom masculin.
De l’italien « orvietano » qui signifie d’Orveto, ville d’Italie.
Dans un sens vieilli, drogue inventée par un charlatan d’orvieto et
qui fut très à la mode au XVII ème siècle.
Au sens figuré et littéraire: un marchand ou un vendeur d’orviétan est
un imposteur, un charlatan.""" },
{ "word": "Oryx", "definition": """Nom masculin.
Mot latin, issu du grec « orux » qui signifie gazelle.
Mammifère vivant dans les déserts et appartenant à la famille des
artiodactyles. C’est une sorte de gazelle aux cornes longues et
pointues.Longtemps menacé d’extinction, il ne l’est plus.
Les efforts pour le préserver ont porté leurs fruits.
Par exemple: »L’oryx blanc est issu de la péninsule arabique tandis que
les autres espèces sont issus d’Afrique. »""" },
{ "word": "Ostiak", "definition": """Nom masculin.
De « Ostiackes » nom d’un peuple.
En linguistique, nom d’une langue finno-ougrienne de l’Ob (Sibérie).""" },
{ "word": "Ouaille", "definition": """Nom féminin.
Du latin « ovicula » issu de « ovis » qui signifie brebis.
1- Dans un sens vieilli.
2- D’après la parabole du bon et du mauvais pasteur. Dans un mode
familier et surtout au pluriel.
Les Chrétiens, par rapport à l’un de leurs pasteurs. Synonyme de
fidèles, de paroissiens.""" },
{ "word": "Ouananiche", "definition": """Nom masculin.
De « annanish » mot indien qui signifie petit égaré.
Au Canada, nom donné à un saumon d’eau douce.""" },
{ "word": "Ouaouaron", "definition": """Nom masculin.
D’un mot iroquois, qui signifie grenouille verte.
Au Canada, grenouille géante d’Amérique du Nord  pouvant atteindre
vingt centimètres de long et dont le coassement ressemble à un
meuglement.
On l’appelle aussi grenouille mugissante ou grenouille-taureau.""" },
{ "word": "Ouche", "definition": """Nom féminin.
1- De l’ancien français « osche » qui signifie enclos, terre cultivée.
Terrain clos, cultivé en potager ou planté d’arbres fruitiers.
2- Du préroman « osca » qui signifie entaille.
Entaille sur le canon d’un fusil.""" },
{ "word": "Ouroboros", "definition": """Nom masculin invariable.
Du grec « ouroboros » issu de « oura » qui signifie queue et « boros » qui
signifie vorace, glouton.
1- En héraldique, représentation d’un serpent ou d’un dragon qui se
mord la queue.
2- Se dit de quelque chose qui revient sur lui-même ou dont le
développement amène un retour à la position initiale.""" },
{ "word": "Outarde", "definition": """Nom féminin.
Du latin « austarda » contraction de « avis tarda » qui signifie oiseau lent.
1- Oiseau échassier, au corps massif aux pattes fortes et au long cou.
2- Bernache du Canada.""" },
{ "word": "Oxymore", "definition": """Nom masculin.
Figure de style qui consiste à réunir deux mots de sens contradictoire pour
exprimer plus fortement une idée.
Par exemple : « Une terrible douceur. »""" },
{ "word": "Oxyton", "definition": """Nom masculin.
Du grec « oxutonos » qui signifie ton.
En linguistique, se dit d’un mot qui a l’accent tonique sur sa dernière syllabe.""" },
{ "word": "Œcuménique", "definition": """Adjectif.
Du grec « oikoumenê (gê) » qui signifie terre habitée, univers »
Dans la religion, se dit de ce qui est Universel.
Un concile œcuménique est un concile présidé par le pape ou ses légats
et où sont convoqués tous les évêques catholiques.
Le Patriarche œcuménique est le titre que se donnent les évêques de
Constantinople.
Par analogie, se dit de ce qui rassemble des personnes de religions ou
d’idéologies différentes.""" },
{ "word": "Pachomètre", "definition": """Nom masculin.
Du grec « pakos « qui signifie épaisseur et « metron » qui signifie mesure.
Appareil qui permet de mesurer l’épaisseur de vitres ou de miroir. Il
peut aussi mesurer l’épaisseur du béton.""" },
{ "word": "Pack", "definition": """Nom masculin.
De  l’anglais « pack-ice » qui signifie paquet de glace.
Plaque de glace de mer qui dérive sur l’océan.""" },
{ "word": "Pagaïe", "definition": """Nom féminin.
De « pagaie » (qui vient du malais « pengajoeh ») par allusion aux
mouvements désordonnés que l’on fait avec cette sorte de rame.
1- Grand désordre d’objets.
2- En pagaïe, signifie en grande quantité.
On peut aussi écrire pagaille.""" },
{ "word": "Palafitte", "definition": """Nom masculin.
Du latin « palus » qui signifie pieu et « fingere » qui signifie façonner.
En archéologie, construction lacustre sur pilotis qui date du néolithique.
Par exemple: « Il existe des palafittes sur le Lac du Bourget. »""" },
{ "word": "Palimpseste", "definition": """Nom masculin. Du grec palimpsêstos qui signifie gratté à nouveau
Manuscrit qui a été écrit sur un parchemin et dont on a gratté ou bien lavé la première écriture pour l’utiliser à nouveau et y écrire un autre texte.
Cette technique était utilisée par les copistes,autour du Xème siècle, en raison du prix des parchemins.
Des textes précieux ont ainsi été perdus. De nouvelles techniques scientifiques permettent de dévoiler le premier texte.
On a découvert que le texte de Cicéron De Republica datant du IVème siècle a été recouvert par un texte de Psaumes de St Augustin au VIIème siècle.""" },
{ "word": "Palindrome", "definition": """Nom masculin.
Du grec « palin » qui signifie de nouveau et « dromos » qui signifie course.
Mot ou ensemble de mots formant une phrase qui peuvent être lus de
gauche à droite ou de droite à gauche.""" },
{ "word": "Palinodie", "definition": """Nom féminin.
Du grec « palin » qui signifie de nouveau ou en sens inverse et « ôdé »
qui sgnifie chant.
Poème dans lequel l’auteur rétractait ce qu’il avait dit dans un autre poème.
Plus généralement tout changement d’opinion. 
Par exemple: « Les palinodies d’un homme politique ».""" },
{ "word": "Pallium", "definition": """Nom masculin.
Du latin « pallium » qui signifie manteau.
1- Ornement sacerdotal en laine blanche brodée de croix noires que le
pape, les primats et les archevêques portent autour du cou.
2- Dans l’antiquité romaine, manteau d’origine grecque.
3- Cortex cérébral des animaux supérieurs comme l’homme ou le chimpanzé.
   – Manteau d’un mollusque qui recouvre la masse viscérale et sécrète
la coquille, les plaques ou les tubes.""" },
{ "word": "Palonnier", "definition": """Nom masculin.
De l’ancien français palonnel puis palonneau.
Provient du latin « palus » qui signifie pieu.
Pièce mécanique qui sert à répartir les efforts lors d’une traction.
On la rencontre aussi dans le gouvernail d’un avion.
La barre transversale qui fixe les traits des chevaux est un palonnier.""" },
{ "word": "Palustre", "definition": """Adjectif.
Du latin « paluster » qui signifie marécageux.
Qui se rapporte aux marais.
Par exemple: Des plantes palustres.""" },
{ "word": "Pampero", "definition": """Nom masculin.
De l’espagnol « pampero » issu de « pampa » mot emprunté à une langue
indigène d’Amérique latine.
Vent violent soufflant du sud et de l’ouest et qui amène les pluies
d’hiver en Argentine.""" },
{ "word": "Pampero", "definition": """Nom masculin.
De pampa, mot d’Amérique latine emprunté à un langue indigène.
Vent violent, soufflant du sud et de l’ouest, qui amène les pluies
d’hiver en Argentine.""" },
{ "word": "Pamphlet", "definition": """Nom masculin.
D’un mot anglais altération de « Pamphilet » nom d’une comédie en vers
latin du XIIème siècle.
Court récit satirique qui s’attaque avec violence à la république, aux
institutions, à la religion, à un personnage publique.""" },
{ "word": "Pancalisme", "definition": """Nom masculin.
Du grec « pan, pantos » qui signifie tout et « kalos » qui signifie beau.
Doctrine philosophique qui fait dépendre du beau toutes les autres catégories.""" },
{ "word": "Pancrace", "definition": """Nom masculin.
Du grec « pankration » issu du grec « pan » qui signifie tout et « kratos » qui signifie force.
Dans la Grèce antique, exercice de gymnastique qui combinait la lutte et le pugilat. """ },
{ "word": "Pancréas", "definition": """Nom masculin.
Du latin « pankreas » composé de « pan-« qui signifie tout et « kreas » qui
signifie chair.
Glande annexe du tube digestif, de forme allongée, située derrière
l’estomac, entre la deuxième portion du duodénum et la rate.
La sécrétion externe du pancréas est le suc pancréatique. La sécrétion
interne du pancréas est hormonale, c’est l’insuline et le glucagon.""" },
{ "word": "Pandit", "definition": """Nom masculin.
Du sanskrit « pandita » qui signifie savant.
Titre honorifique donné dans l’Inde, à un fondateur de secte ou à un
sage (brahmane).
Par exemple: « Nehru avait le titre de pandit. »""" },
{ "word": "Panégyrique", "definition": """Nom masculin.
Du grec « panêguris » qui signifie assemblée de tout [le peuple].
1- Discours destiné à la louange d’une personne célèbre, d’une nation
ou d’une ville.
En religion, sermon dont le sujet est l’éloge d’un saint.
2- Parole ou écrit qui fait la louange de quelqu’un.
De manière péjorative, éloge outré ou emphatique.
Employé de manière ironique, discours malveillant ou médisant.""" },
{ "word": "Pangée", "definition": """Nom féminin.
Du grec « pan » qui signifie tout et « gaïa » qui signifie terre.
Littéralement « toutes les terres ».
Super-continent qui rassemblait la quasi totalité des terres émergées.
Il a existé à la fin du carbonifère est au début du jurassique, avant
que ne dérivent les continents.""" },
{ "word": "Panglossisme", "definition": """Nom masculin.
Du héros de Voltaire « Pangloss ».
Création ironique du personnage de Pangloss qui parle toutes les
langues et dont le discours absurde vise la totalité.""" },
{ "word": "Panic", "definition": """Nom masculin.
Du latin « panicum » issu de « panus » qui signifie fil de tisserand.
Plante herbacée de la famille des graminées, annuelle ou vivace,
cultivée comme céréale ou plante fourragère.
Le millet est le synonyme de ce mot.""" },
{ "word": "Panique", "definition": """Nom féminin.
Du latin « panicus » du Dieu Pan qui passait pour troubler et pour
effrayer les esprits.
1- Sentiment de peur qui trouble subitement et violemment.
2- Terreur extrême et souvent collective devant un danger réel ou possible.""" },
{ "word": "Panlogisme", "definition": """Nom masculin.
De l’allemand « Panlogismus », issu du grec pan, pantos qui signifie
« tout et du grec « logia » qui signifie théorie.
En philosophie, doctrine d’après laquelle tout ce qui est réel est intelligible.
S’applique, principalement, à la pensée de Leibniz et de Hegel.""" },
{ "word": "Panne", "definition": """Nom féminin.
Du latin « penna » qui signifie aile, partie latérale.
Bande de nuages près de l’horizon.""" },
{ "word": "Pantière", "definition": """Nom féminin.
Du latin d’origine grecque « panthera » qui signifie large filet.
Filet que les chasseurs tendent verticalement pour prendre les oiseaux
qui volent par bande.""" },
{ "word": "Pantois", "definition": """Adjectif.
De l’ancien français « pantaisier » issu du latin « phantasiare » qui
signifie avoir des visions, par le grec « phantasiein ».
1- Dans un sens vieilli: haletant.
2- Dans un sens moderne: dont le souffle est coupé par l’émotion, la surprise.
Par exemple: « Cette question l’a laissé pantois. »""" },
{ "word": "Parabase", "definition": """Nom féminin.
Du grec « parabasis » action de s’avancer.
Dans une oeuvre littéraire, introduction d’une réflexion de l’auteur
au sein de la narration. Sur le contenu de l’histoire ou les
sentiments du lecteur.""" },
{ "word": "Paraclet", "definition": """Nom masculin.
Du grec « paraklêtos » qui signifie avocat ou intercesseur.
Dans la religion catholique le Paraclet est le Saint-Esprit de la Sainte
Trinité.
-Ce mot a été entendu sur France-Culture dans l’émission d’Emmanuel
Laurentin « La Fabrique de l’Histoire » qui traitait de la mixité dans l’Eglise
le jeudi 20 février 2014.
Il se trouvait dans la phrase suivante:
« …c’est aussi le rêve d’Abélard pour le Paraclet d’Héloïse. »
– « Le Vent Paraclet » de Michel Tournier est son autobiographie.
L’écrivain y mêle des réflexions littéraires et philosophiques qui éclairent
son parcours.""" },
{ "word": "Paradigme", "definition": """Nom masculin.
Du grec « paradeigma » qui signifie exemple.
1-Mot-type qu’on donne comme exemple dans une conjugaison ou dans une
déclinaison.
Par exemple: le verbe « aimer » est le verbe type qui représente le
premier groupe. « Aimer » est le paradigme des verbes du premier groupe.
En latin, le substantif « rosa, rosae » représente la première
déclinaison. « Rosa » est le paradigme de la première déclinaison.
2-Peut signifier aussi un modèle.
Par exemple : « un paradigme de société »""" },
{ "word": "Paramidophénol", "definition": """Nom masculin.
De « para » « amidon » et « phénol ».
Dérivé du phénol employé comme révélateur dans la photographie argentique.""" },
{ "word": "Paramnésie", "definition": """Nom féminin.
Du grec « para » qui signifie à côté et « mnésis » qui signifie mémoire.
Mot qui signifie « déjà vu » et qui a  été créé par Emile Boirac
1851-1917 dans son livre « Avenir des sciences psychiques ».
Sensation d’avoir été témoin ou d’avoir vécu la situation présente et
qui s’accompagne d’une impression d’irréalité et d’étrangeté.""" },
{ "word": "Parangon", "definition": """Nom masculin.
Du grec « parakoné » pierre à aiguiser.
1- Modèle. Par exemple: un parangon de vertu est un modèle de vertu.
2- Perle ou diamant dépourvus de défaut.
3- Marbre noir d’Egypte ou de Grèce. On dit un marbre parangon""" },
{ "word": "Parégorique", "definition": """Adjectif.
Du latin « paregoricus » qui signifie propre à calmer.
En médecine se dit d’un médicament qui calme ou qui adoucit.
Exemple: l’Elixir Parégorique est un ant-diarrhéique à base d’opium.""" },
{ "word": "Parémiographe", "definition": """Nom masculin.
Du grec « parémia » qui signifie proverbe.
Auteur d’un recueil de proverbes.""" },
{ "word": "Parémiologie", "definition": """Nom féminin.
Du grec « paroimia » qui signifie proverbe et « logos » qui signifie discours.
Étude des proverbes.""" },
{ "word": "Parhélie", "definition": """Nom masculin.
Du grec « parêlios » issu de « para » qui signifie à côté de et « hêlios »
qui signifie soleil.
Image du soleil -dite aussi faux-soleil- due au phénomène de
réfraction que produit également le halo.""" },
{ "word": "Parisette", "definition": """Nom féminin.
Diminutif de Paris.
Plante de la famille des liliacées, à baies bleuâtres, commune dans
les bois et les prairies humides. Elle est appelée parfois « raisin de
renard ».""" },
{ "word": "Parmélie", "definition": """Nom féminin.
Du latin « parma » qui signifie petit bouclier rond par analogie de forme.
En botanique, lichen des régions froides.""" },
{ "word": "Paronomase", "definition": """Nom féminin.
Du latin « paronomasia » de même signification, issu du grec
« paronomasia » dérivé de « paronomadzô » qui signifie transformer un mot,
issu de « para » qui signifie à côté de et « onomadzein » qui signifie nommer
par « onoma » qui signifie nom.
Figure de style qui consiste à rapprocher des mots comportant des
sonorités semblables mais qui ont des sens différents. Les paronymes
sont des mots qui se ressemblent par leur son.
Par exemple: » Qui vole un œuf, vole un bœuf. »""" },
{ "word": "Paroxyton", "definition": """Nom masculin.
Du grec « paroxutonos » qui signifie marqué de l’accent aigu sur la
pénultième [ou avant-dernière]. Issu de « oxutonos » qui signifie ton.
En linguistique, se dit d’un mot dont l’accent tonique est situé sur
l’avant-dernière syllabe.
Par exemple: « Tout mot espagnol sans accent aigu et se terminant par
une voyelle, par n ou par s est un paroxyton. »
Comme le mot « bienvenida » qui signifie bienvenue.""" },
{ "word": "Parsec", "definition": """Nom masculin.
De par(allaxe) et seconde.
En métrologie et en astronomie, unité de mesure de longueur de symbole
pc, utilisée en astronomie et qui vaut 3, 26 années-lumière.""" },
{ "word": "Parsi", "definition": """1- Nom masculin et adjectif.
Mot persan de « parashika » qui signifie peuple de Perse.
Personne qui en Inde suit la religion de Zoroastre et descend des
perses zoroastriens chassés de leur pays par les musulmans.
2- Nom masculin.
Langue indo-européenne du groupe iranien, usitée en Perse à l’époque
des derniers rois sassanides et intermédiaire entre le vieux perse et
le persan moderne.""" },
{ "word": "Pasquin", "definition": """Nom masculin.
De l’italien « Pasquino », qui est le nom d’une statue antique sur
laquelle on affichait des écrits satiriques à Rome.
1- Sens vieilli: Ecrit satirique.
2- Sens vieilli. Bouffon, pitre.
De la même famille et dans un sens littéraire et vieilli, une
pasquinade est une raillerie bouffonne.""" },
{ "word": "Passion", "definition": """Nom féminin.
Du latin « passio » qui signifie action de supporter, soufrance,
maladie, perturbation morale. Issu du verbe latin « patior » qui
signifie souffrir, endurer.
Plusieurs sens.
1- Passion avec une majuscule signifie la Passion du Christ, c’est à
dire sa souffrance et son supplice.
2- Passion amoureuse, relation amoureuse exclusive, puissante et obsédante.
3- Vive inclination pour un objet; par exemple passion de la littérature.""" },
{ "word": "Patache", "definition": """Nom masculin.
De l’espagnol  « pataje » qui signifie navire ou bateau de guerre léger,
lui même issu de l’arabe « batâs » qui signifie bateau à deux mâts.
1- Petit navire de surveillance.
2- Diligence inconfortable à prix modique.""" },
{ "word": "Pataquès", "definition": """Nom masculin.
Formation imitative ironique, d’après les phrases « ce n’est
pas-t-à-moi », « je ne sais pas-t-à qui est-ce ».
1- Mauvaise liaison entre deux mots.
On fait un pataquès en substituant par exemple un s à un t final ou un
t à un s final.
Par extension, faute grossière de langage.
2- Situation embrouillée. Gaffe grossière ou impair.""" },
{ "word": "Patène", "definition": """Nom féminin.
Du latin « patene » qui signifie bassin, plat.
Vase ou petite assiette qui sert à l’oblation de l’hostie.
… »le calice et la patène »…Teilhard de Chardin. Extrait d’un texte
lu dans l’émission « Les nouveaux chemins de la philosophie. » sur
France-Culture le 10 janvier 2017.""" },
{ "word": "Paulette", "definition": """Nom féminin.
De « Paulet » nom du premier fermier de cet impôt.
Vers le XVIIème siècle, impôt annuel que devaient payer les titulaires
de charges de judicature pour en devenir propriétaire.""" },
{ "word": "Péan", "definition": """Nom masculin. On écrit aussi paean.
Du grec « poean » qui signifie hymne en l’honneur d’Apollon ou d’un autre dieu.
Emprunté au latin « Paean ». Pean est un des noms d’Apollon. C’est aussi
l’hymne en l’honneur de ce dieu ou d’un autre dieu.
A- Dans l’Antiquité, hymne d’allégresse et de reconnaissance en
l’honneur d’Apollon.
  Par exemple: »Dans le Colisée en liesse, le péan était chanté par
toute la foule réunie. »
  – Par extension, chant collectif entonné pour honorer certaines
divinités ou certains héros.
Par exemple: »L’Epître à François est un des grands paeans de la
Renaissance française. » d’après Valéry Larbaud.
B- Par analogie, hymne de louange, chant d’espoir ou de victoire.
  – Chanter, entonner le péan signifie chanter, crier victoire.
Par exemple: »En cas de victoire, nous entonnerons le péan ».""" },
{ "word": "Pécopteris", "definition": """Nom masculin.
Du grec « pekos » qui signifie toison et « pteris » qui signifie fougère.
En paléontologie, fougère arborescente fossile que l’on rencontre sur
des terrains carbonifères.""" },
{ "word": "Pecorino", "definition": """Nom masculin.
De l’italien.
Fromage italien, voisin du parmesan et qui sert à assaisonner les pâtes.""" },
{ "word": "Pelagos", "definition": """Nom masculin.
Du même mot grec qui signifie haute-mer.
Ensemble des organismes marins vivant en pleine eau loin du fond et
n’en dépendant pas pour leur subsistance.""" },
{ "word": "Péliké", "definition": """Nom féminin.
L’origine de ce mot est incertaine.
Amphore à embouchure étroite et dont la panse est ventrue.""" },
{ "word": "Pélodyte", "definition": """Nom masculin.
Du grec « pelos » qui signifie boue, glaise et « dutes » qui signifie plongeur.
En zoologie, batracien anoure du groupe des crapauds, qui creuse des
galeries dans le sol et qui peut s’enfoncer dans les sols meubles.""" },
{ "word": "Pénates", "definition": """Nom masculin pluriel.
Du latin « penates » issu de « penus » qui signifie « intérieur de la maison ».
1- Dieux domestiques protecteurs de la cité ou du foyer chez les anciens
romains.
2- Les statuettes de ces dieux.
3- Par métaphore le mot pénates se dit de tout ce qui peut se transporter de
la maison dans un autre endroit. Par exemple des livres, des meubles ou
des photos.
4- La maison. Par exemple: » Je reste dans mes pénates » signifie : « Je reste
chez moi »""" },
{ "word": "Pendrillon", "definition": """Nom masculin.
Du latin « pendere » qui signifie pendre, être suspendu.
Au théâtre, rideau de faible largeur et en velours noir qui sert a
cacher les coulisses. 
L’ourlet du bas est lesté et allongé légèrement de manière à
« l’asseoir » ou « le mettre à genoux ».
Ainsi, il empêche la lumière des coulisses de filtrer dans la salle.""" },
{ "word": "Pennon", "definition": """Nom masculin.
Du latin « penna » qui signifie grosse plume.
Drapeau triangulaire à longue pointe que les chevaliers du Moyen-Âge
portaient au bout de leur lance.
Sur un blason, un pennon généalogique est un écu dont les différents
quartiers indiquent les alliances  ou les degrés généalogiques.""" },
{ "word": "Penon", "definition": """Nom masculin.
Du latin « penna » qui signifie grosse plume.
Terme de marine. Petite girouette ou banderole qui indique la direction du vent.""" },
{ "word": "Péplum", "definition": """Nom masculin.
Du grec « peplon » qui signifie tunique.
1- Dans l’Antiquité, vêtement de femme sans manche qui s’agrafait sur
l’épaule.
2- Film à grand spectacle ayant pour sujet un épisode réel ou imaginé
de l’Antiquité.""" },
{ "word": "Perestroïka", "definition": """Nom féminin.
Du russe « perestroïka » qui signifie reconstruction. 1986.
Dans l’histoire de l’union soviétique, réorganisation du système
socioéconomique avec une modification des mentalités et d’une
meilleure circulation de l’information.""" },
{ "word": "Péricope", "definition": """Nom féminin.
Du grec « pericopi » qui signifie découpage.
Dans l’exégèse des textes qui sont sacrés ou qui ne le sont pas;
extrait formant une unité ou une pensée cohérente, qui a un sens même
hors de son contexte.
Concerne la liturgie religieuse et se situe dans le cadre d’une
lecture publique à laquelle on ajoute parfois l’étude et le
commentaire du texte.""" },
{ "word": "Périgueux", "definition": """Nom masculin.
Du nom de la ville de Périgueux, capitale du Périgord, près de
laquelle on trouve cette pierre.
Pierre noire très dure utilisée par les verriers, les potiers et par
les émailleurs pour polir.""" },
{ "word": "Périssodactyles", "definition": """Nom masculin pluriel.
Du grec « perisos » qui signifie impair et « daktulos » qui signifie doigt.
En zoologie, ordre de mammifères placentaires ongulés qui comprend des
animaux reposant sur le sol par un nombre impair de doigts (imparidigités)
dont le médian est le plus développé.
Le rhinocéros et le tapir sont des périssodactyles.""" },
{ "word": "Périssologie", "definition": """Nom féminin.
Du grec « perissologia » issu de « perissos » qui signifie superflu.
En grammaire, répétition dans l’expression des idées ou de la pensée.
C’est un pléonasme qui constitue une faute dans la langue ou c’est un
procédé d’insistance volontaire.""" },
{ "word": "Périthèce", "definition": """Nom masculin.
Du grec « peri » qui signifie autour et « thêkê » qui signifie étui.
Enveloppe de la fructification, de certains champignons ascomycètes.
Elle est en forme de bouteille et renferme les asques.
Les champignons concernés sont par exemple: La truffe et les pézizes.""" },
{ "word": "Pers", "definition": """Adjectif.
Du latin « persus » qui signifie de couleur jacinthe, violet, bleu foncé.
« Persus » est issu de « Persia » La Perse (nom du pays, Iran actuel).
En effet, d’après le témoignage de Pline dans son « Histoire Naturelle »,
on utilisait des cocons (de vers à soie) importés d’Assyrie dans la
fabrication des « bombycinae vestes » ou « vêtements de soie ».
Au lieu de « assyriens » on disait « persans » et il est possible que l’on ait
appelé « persae vestes » « vêtements de Perse » ces vêtements de soie.
Certains d’entre eux étaient peut-être teints en bleu foncé, ainsi
l’adjectif « persus »issu de « persa » par spécialisation d’emploi en
est venu â désigner cette couleur.
Dans un genre littéraire :
1- Désigne une couleur où le bleu domine.
2- D’un bleu qui tire vers une autre couleur : vert ou violet. 
Par exemple:
« Athéna, la déesse aux yeux pers »""" },
{ "word": "Pétase", "definition": """Nom masculin.
Du grec « petasos » issu de pétazo pétannumi j’étends.
Sorte de chapeau à larges bords qu’utilisaient les grecs et les romains.
On représentait Mercure avec le pétase ailé.""" },
{ "word": "Pétrichor", "definition": """Nom masculin (indénombrable).
Du grec « petra » qui signifie pierre et ‘ichor » qui signifie fluide,
sang. Ichor était le sang des dieux dans la mythologie grecque.
Odeur distinctive qui accompagne la chute de pluie sur la terre sèche.
Ce terme a été créé par deux chercheurs dans un article de Nature en 1964.
C’est le liquide huileux sécrété par certaines plantes et absorbé par
les sols et les roches argileux pendant les périodes sèches qui après
la pluie dégage une odeur caractéristique en se combinant à la géosmine.
En 2015, des chercheurs ont constaté que lorsqu’une goutte de pluie
atterrit sur une surface poreuse, l’air des pores forme de petites
bulles qui flottent à la surface et relâche des aérosols qui emportent
les virus et les bactéries (actinobactéries) depuis le sol.
Plus les gouttes tombent lentement plus il y a d’aérosols, ce qui explique
que le pétrichor soit observé dans les pluies légères.    .""" },
{ "word": "Pétulance", "definition": """Nom féminin.
Du latin « petulantia » issu de « petere » qui signifie se jeter sur.
Énergie débridée, brusque et chaotique.""" },
{ "word": "Peulven", "definition": """Nom masculin.
Du breton « peulvan » à la définition incertaine.
Mégalithe dressé.""" },
{ "word": "Phalangine", "definition": """Nom féminin.
Du grec phalagx qui signifie gros bâton.
Sur la main humaine, c’est la deuxième phalange des doigts (sauf le
pouce) lorsqu’ils en comptent trois.""" },
{ "word": "Phébus", "definition": """Nom masculin.
Du grec » phoibos » qui signifie brillant et qui était le surnom d’Apollon.
Dans une langue littéraire et vieillie, manière de présenter de façon
peu intelligible mais brillante des idées relativement simples.
Écriture dans un langage affecté et prétentieux.
On dit : »Faire du phébus »""" },
{ "word": "Phellogène", "definition": """Adjectif.
Du grec « phellos » qui signifie liège et « génos » qui signifie naissance, origine.
Tissu végétal qui produit du liège.
Le chêne-liège est un arbre phellogène.""" },
{ "word": "Phénicoptères", "definition": """Nom masculin pluriel.
Du grec « phoinikopteros », de ‘phoinix » qui signifie pourpre et
« pteron » qui signifie ailes.
Ordre d’échassiers auquel appartient le flamant.""" },
{ "word": "Phénicoptères", "definition": """Nom masculin pluriel.
Du grec « phoinikopteros », issu de « phoinix » qui signifie pourpre et
« pteron » qui signifie aile.
En zoologie c’est un ordre d’échassiers auquel appartient le flamant
rose, dont le nom scientifique est « phœnicopteri formes »""" },
{ "word": "Phénologie", "definition": """Nom féminin.
Du grec ancien « phainen » qui signifie briller et logos qui signifie étude.
Étude des phénomènes périodiques de la vie végétale et animale, en
fonction du climat.""" },
{ "word": "Phénoménologie", "definition": """Nom féminin.
Du grec « phainomena » qui signifie « phénomènes célestes » et « logos » qui
signifie discours.
Qui concerne la description du monde et des choses.""" },
{ "word": "Phéromone", "definition": """Nom féminin.
Issu du grec « pherein » qui signifie porter et « (hor)môn » qui signifie exciter.
En biologie, produit sécrété par un organisme et qui stimule une
réponse physiologique ou comportementale chez un autre individu
appartenant à la même espèce.
Par exemple : « Les phéromones que sécrète l’homme et les phéromones
que sécrète la femme ont une influence sur leurs comportements
amoureux respectifs. »""" },
{ "word": "Philistin", "definition": """Nom masculin.
De l’allemand « philister » qui signifie celui qui n’a pas fréquenté les
universités, dans l’argot des étudiants, du nom du peuple combattu par
Samson dans la Bible.
Personne aux goûts vulgaires, fermée aux arts, aux lettres et aux nouveautés.
On peut dire: « C’est un vrai philistin » ou « il est un peu philistin ».""" },
{ "word": "Philosophale", "definition": """Adjectif.
Formé sur le mot philosophe, du grec « philosophos » ami de la sagesse.
La pierre philosophale était une substance qui fut longtemps
recherchée par les alchimistes. Elle devait posséder des propriétés
merveilleuses, notamment celles de transformer les métaux en or.""" },
{ "word": "Phlox", "definition": """Nom masculin.
Du même mot grec qui signifie flamme.
Plante herbacée de la famille des polémoniacées cultivée pour ses
fleurs de couleurs vives.""" },
{ "word": "Phlyctène", "definition": """Nom féminin.
Du grec « phluktaina » issu de « phluzein » qui signifie couler en abondance.
En dermatologie, bulle se formant à la surface de la peau suite à un
frottement et qui est remplie de sérosité transparente.
Nom savant d’une cloque ou d’une ampoule.""" },
{ "word": "Phoeniciculture", "definition": """Nom féminin.
Du latin « phoenix » qui est le nom de genre du palmier dattier et
« cultura » qui signifie culture.
Nom donné à la culture du palmier dattier dont le nom savant est
Phoenix dactylifera. Le palmier dattier est de la famille des
arécacées: les palmiers.""" },
{ "word": "Phonolithe", "definition": """Nom féminin.
Du grec « phonos » qui signifie son et « lithos  » qui signifie pierre.
Pierre qui résonne.
En minéralogie, trachyte feldspathique qui se présente sous forme de
laves compactes qui sont sonores au choc.""" },
{ "word": "Phormion", "definition": """Nom masculin.
Du latin « phormium » qui signifie natte, par le grec « phormion ».
Plante vivace de la famille des liliacées, à rhizome épais et qui est
aussi appelée chanvre ou lin de Nouvelle-Zélande.
C’est un crin végétal appelé aussi phormium.""" },
{ "word": "Phosphène", "definition": """Nom masculin.
Du grec « phôs » qui signifie lumière et « phaineien » qui signifie apparaître.
Sensation lumineuse qui résulte de l’excitation des récepteurs de la
rétine par un agent autre que la lumière, comme un choc ou une
stimulation électrique.
Les trente six chandelles que voient les héros de bandes dessinées
lorsqu’ils subissent un choc violent sont des phosphènes.""" },
{ "word": "Phréno-glottisme", "definition": """Nom masculin.
Du grec « phrên » qui signifie diaphragme et « glottis » qui signifie
languette par « glotta/ glossa » qui signifie langue.
Spasme de la glotte et du diaphragme, sorte de névrose.""" },
{ "word": "Piaculaire", "definition": """Adjectif masculin ou féminin, selon le substantif qu’il qualifie.
Du latin « piacularis » qui signifie expiation.
Dans un emploi rare, se dit de ce qui a rapport à l’expiation.
Par exemple: » Selon Georges Didi-Huberman, l’expression publique et
collective des larmes peut être considérée comme un rite piaculaire. »
D’après « Peuples en larmes, peuples en armes » Georges Didi-Huberman
Éditions de Minuit (2016)""" },
{ "word": "Pica", "definition": """Nom masculin.
Du latin « pica » qui signifie pie par allusion à la voracité de cet oiseau.
En médecine, goût morbide pour des substances non comestibles voire toxiques.
Par exemple: les enfants qui mangent les écailles de peintures tombées
à terre et contenant du plomb; ce qui entraine chez eux du saturnisme.""" },
{ "word": "Picaresque", "definition": """Adjectif.
De l’espagnol « picaresco » issu de « picaro » qui signifie aventurier.
Type littéraire du XVIème au XVIIIème siècle relatif ou propre aux
picaros, c’est à dire aux aventuriers espagnols.
« Don Quichotte » de Cervantès est un récit picaresque.""" },
{ "word": "Pidgin", "definition": """Nom masculin.
Mot anglais. Altération du mot « business » par les chinois. Une autre
origine a été proposée par certains chercheurs, ce serait une
altération de l’écriture du mot pigeon.
Langue seconde composite née du contact commercial entre l’anglais et
les langues d’Extrême-Orient.
Cette langue ne remplit pas toutes les fonctions d’une langue ordinaire.
Le pidgin-english ou pidgin, est composé d’un vocabulaire anglais et
d’une base grammaticale chinoise.
Le pidgin mélanésien comporte un vocabulaire mixte, à la fois anglais
et malais.
Par exemple: « Il existe d’autres pidgin comme le pidgin de
Papouasie-Nouvelle-Guinée, aussi appelé le « tok pisin ».""" },
{ "word": "Pièze", "definition": """Nom féminin.
Du grec « plessein » qui signifie presser.
En physique, ancienne unité de mesure de pression, d’abréviation « pz »,
et qui valait 1000 pascals.""" },
{ "word": "Pigdgin", "definition": """Nom masculin.
Pidgin english, Mot anglais qui résulte de l’altération du mot
« business » par les chinois.
Langue seconde, composite, née du contact commercial entre l’anglais
et les langues d’Extrême-Orient. elle ne remplit pas toutes les
fonctions d’une langue ordinaire.
Le pidgin-english ou pidgin est composé d’un vocabulaire anglais et
d’une base grammaticale chinoise; il se distingue du pidgin mélanésien
qui comporte un vocabulaire mixte anglais et malais.""" },
{ "word": "Pimprenelle", "definition": """Nom féminin.
Du latin « pipinellea » issu peut-être de « piper » qui signifie poivre.
Plante herbacée de la famille des rosacées, dont les fleurs sont
souvent rouges et dont les feuilles servent à l’assaisonnement des
salades.""" },
{ "word": "Pindarisme", "definition": """Nom masculin.
Du grec « Pindaros » qui signifie Pindare. Pindare était un poète
lyrique grec né en 518 et mort en 438 avant notre ère.
Se dit d’un style poétique dans la manière lyrique de Pindare est qui
est obscur et ampoulé.""" },
{ "word": "Pirole", "definition": """Nom féminin.
Du latin « pirola » issu de « pirus » qui signifie poirier.
Petite plante herbacée de la famille des monotropacées dont les
feuilles vertes ressemblent à celles du poirier et qui pousse dans les
lieux humides.""" },
{ "word": "Pitchpin", "definition": """Nom masculin.
De l’anglais « pitchpine » qui signifie pin à résine.
Bois appartenant à plusieurs espèces de pins d’Amérique du Nord, de
couleur rouge-brun et qui est utilisé en menuiserie.
Par exemple: « Il a fabriqué cette bibliothèque en pitchpin. »""" },
{ "word": "Pithiatique", "definition": """Adjectif.
De ‘peithein » qui signifie persuader et « iatos » qui signifie guérissable.
En psychiatrie, se dit d’un trouble non organique qui peut être guéri
ou reproduit par la suggestion. Les troubles de cet ordre font partie
intégrante de l’hystérie.""" },
{ "word": "Pithiatisme", "definition": """Nom masculin.
Du grec « pith » issu de ‘peithein » qui signifie persuader et « iatos »
qui signifie guérissable.
En psychiatrie, ensemble de troubles à caractère pithiatique
c’est-à-dire qui peuvent être guéris ou reproduits par la suggestion.
Par exemple: « Il serait simple de penser que le pithiatisme
expliquerait ces douleurs. »""" },
{ "word": "Plagioclase", "definition": """Nom masculin.
Du grec « plagios » qui signifie oblique et « clasis » qui signifie cassure.
En minéralogie, feldspath contenant du calcium et du sodium.""" },
{ "word": "Plaqueminier", "definition": """Nom masculin.
De l’algonquin « plakimin » de même signification.
Arbre de la famille des ébénacées, dont le bois est très dur.
Le plaqueminier d’Inde est l’ébénier, il fournit l’ébène.
Le plaqueminier du Japon est cultivé pour son fruit: le kaki.""" },
{ "word": "Plassava", "definition": """Nom  masculin.
Du portugais « plassaba » qui provient d’une langue indienne du Brésil.
Palmier de l’Amérique du Sud dont on extrait une fibre textile.
Par métonymie, (la partie désignant le tout), la fibre issue du palmier.
Par exemple: »Les plassavas sont majestueux. »
Autre exemple: »J’ai acheté un paillasson en plassava. »""" },
{ "word": "Plectre", "definition": """Nom masculin.
Du grec « plektron » issu de la racine « plêssein » qui signifie frapper.
Dans l’Antiquité, petite baguette de bois ou d’ivoire servant à
gratter ou à pincer les cordes de la lyre ou de la cithare.
Dns un emploi moderne. Médiator. Plectre d’une mandoline.""" },
{ "word": "Pléïade", "definition": """Nom féminin.
Du grec « pleias ados » qui signifie constellation de sept étoiles.
La Pléiade ou Le groupe des Pléiades est l’ensemble des sept étoiles
visibles à l’œil nu et qui forment un amas dans la constellation du
taureau.
Les Pléiades sont sept sœurs filles d’Atlas et de Pleioné.
Voici leurs prénoms: Astérope, Mérope, Electre , Maïa, Taygete,
Celaéno et Alajone.
En fait, ce sont les neuf étoiles les plus brillantes-sept soeurs et
leurs parents-. L’amas de ces étoiles est visible dans un ciel clair
d’automne. Les voir, représente un excellent test d’acuité visuelle. 
A l’observation, on aperçoit rapidement cinq étoiles, puis les autres,
peu à peu au gré de l’accommodation.
En histoire littéraire, c’était le nom donné aux sept poètes
d’Alexandrie qui vivaient au IIIème siècle avant notre ère.
C’est aussi le groupe des sept grands poètes français de la
Renaissance, au XVI ème siècle, qui fut d’abord appelé La Brigade et
qui comprenait entre autres Ronsard et Du Bellay.
C’est aussi une célèbre collection d’un grand éditeur français,
reliure en cuir et papier bible, qui comprend la plupart des grands
auteurs français et certains auteurs étrangers.""" },
{ "word": "Pléiotropie", "definition": """Nom féminin.
Du grec « pleiôn » qui signifie plus, nombreux et « tropos » qui signifie
tour, direction.
En biologie, propriété que possède un gène -le gène pléiotrope- d’agir
sur plusieurs caractères.
Par exemple: »Chez le chat siamois, le gène qui est responsable des
dégradés de couleur sur le pelage est aussi responsable du strabisme
convergent. »""" },
{ "word": "Pléonexie", "definition": """Nom féminin.
Du grec pleonexia constitué de « pleos » qui signifie plein et du
radical « nek » qui signifie prendre.
Désir d’avoir plus que les autres en toute chose.""" },
{ "word": "Pleuronecte", "definition": """Nom masculin.
Du grec « pleuron » qui signifie côté et « nektos » qui signifie nageant.
Genre de poissons plats qui nagent sur un côté du corps et ont les
yeux sur le même côté de la tête.
On peut citer en exemple la sole, le turbot ou la limande.""" },
{ "word": "Pleutre", "definition": """Nom masculin et adjectif.
Du flamand « pleute » qui signifie chiffon. Employé au figuré comme injure.
De manière littéraire, homme sans courage
Par exemple: « Un pleutre est le contraire d’un héros. »
En tant qu’adjectif. Par exemple: « Il est pleutre son épouse est pleutre aussi. »""" },
{ "word": "Plombée", "definition": """Nom féminin.
De « plommée » refait sur « plomber » issu de « plomb ».
1-  En archéologie. arme du Moyen-Âge, masse garnie de plomb.
Dard lesté de plomb.
2- Dans le langage de la pêche, ensemble des plombs qui lestent le bas
d’une ligne.""" },
{ "word": "Ploutocrate", "definition": """Nom masculin.
Du grec « ploutos » qui signifie richesse et « kratos » qui signifie
force, puissance.
Personnage très riche qui exerce par son argent une influence politique.""" },
{ "word": "Pogonophores", "definition": """Nom masculin pluriel.
Du grec « pôgôn » qui signifie barbe et « pherein » qui signifie porter.
En zoologie, classe de l’embranchement des annélides, qui comprend de
petits invertébrés marins vermiformes ( en forme de ver), couronnés de
tentacules, qui vivent sur les hauts-fonds et qui dépourvus de tube digestif
absorbent directement leur nourriture par la peau et les tentacules.
Par exemple: »Les pogonophores peuvent vivre jusqu’à 200 000 ans! »""" },
{ "word": "Pogrom", "definition": """Nom masculin.
On peut écrire aussi « pogrome »
Du russe « po » qui signifie entièrement et « gromit » qui signifie détruire.
Agression qui vise l’oppression et le meurtre d’un groupe de
population contre les Juifs d’un ghetto et qui est soutenue par le
pouvoir politique.""" },
{ "word": "Poliste", "definition": """Nom féminin ou masculin.
Du grec « polistês » qui signifie bâtisseur de ville.
En zoologie, guêpe qui vit dans un nid de plein-air formé d’une seule
cellule fixée à une branche ou sous une pierre.""" },
{ "word": "Pomologie", "definition": """Nom féminin.
Du latin « pomum » qui signifie fruit et du grec « logos » qui signifie discours.
Partie de la culture des arbres qui concerne les fruits comestibles.""" },
{ "word": "Pomœrium", "definition": """Nom masculin.
Du latin « post » qui signifie après et « murus » qui signifie mur.
Dans l’antiquité romaine, espace libre réservé au culte et qui était
ménagé autour des villes latines avec l’interdiction d’y bâtir.""" },
{ "word": "Pontuseau", "definition": """Nom masculin.
Probablement altération de « pontereau » qui signifie petit pont.
Tige de  métal traversant les vergeures dans les formes à papier et
laissant une trace sur le papier.
Par extension, cette trace.
Par exemple: »Papier vergé dont on aperçoit les pontuseaux par transparence. »""" },
{ "word": "Porion", "definition": """Nom masculin.
Mot d’origine picarde, issu probablement d’une aphérèse de « caporion »
qui signifiait chef d’escouade en français de belgique.
D’après le flamand « porion » qui signifie poireau.
Agent de maîtrise, contremaître dans les mines de charbon.
Contremaître dans les puits de pétrole. Porion d’huile qui organise le pompage.
Par exemple: « Seule, la lampe à feu du porion, dans la berline voisine
brillait comme un phare. » Germinal Emile Zola""" },
{ "word": "Portulan", "definition": """Nom masculin.
De l’italien « portolano » qui signifie pilote, issu de « porto » qui signifie port.
Anciennement, carte marine des premiers navigateurs, aux environs des
XIIIème jusqu’au XVIème siècle.
Mais aussi, livre contenant la description des ports et des côtes.""" },
{ "word": "Potiron", "definition": """Nom masculin.
Peut-être du syriaque « pâturtâ » qui signifie morille.
Plante au nom de Cucurbita maxima. Elle appartient à la famille des
cucurbitacées et elle est originaire des régions tropicales d’Amérique
du Sud.
Le terme désigne aussi le fruit de cette plante consommé comme légume.
Le potiron est plus ou moins aplati, sa couleur va d’un orange
rougeâtre au vert foncé, son pédoncule est tendre et spongieux,
cylindrique et évasé près du fruit.
C’est l’une des cinq espèces de courges les plus couramment utilisées.""" },
{ "word": "Potlatch", "definition": """Nom masculin.
De l’anglo-américain « potlatch » issu de « pashati » puis « poshati » qui
signifie don, action de faire un don, en chinook, langue des indiens
de l’Ouest de L’Amérique du Nord.
Ensemble de cérémonies marquées par des dons échangés entre des
groupes sociaux distincts et rivaux.
Système d’échanges dans lequel ont lieu ces cérémonies.""" },
{ "word": "Poudingue", "definition": """Nom masculin.
Du francisque issu de l’anglais « pudding-stone » qui signifie pierre-pudding.
En géologie, roche détritique constituée par des cailloux roulés, liés
entre eux par un ciment naturel.""" },
{ "word": "Poudrin", "definition": """Nom masculin.
De « poudre » issu du latin « pulveris » qui signifie poussière.
En langage marin, embruns marins.
A Terre-Neuve, se dit d’une pluie fine et glacée.""" },
{ "word": "Pouième", "definition": """Nom masculin.
Issu de « pou » insecte parasite de l’homme, auquel on a ajouté le
suffixe -ième sur le modèle de centième ou de millième.
1- Quantité infime.
Par exemple: »[Nos candidats] Ils se font des sueurs froides pour des
pouièmes en plus ou en moins » Le Monde 30 janvier 2017 Benoît Hopquin
« Des chiffres et des lettres. »
2- Subdivision approximative d’une unité conventionnelle.
Par exemple: »Un pouième de seconde. »
On peut aussi écrire « pouillème »""" },
{ "word": "Pouillard", "definition": """Nom masculin.
De l’ancien français « pouil » qui signifie coq.
Dans une langue régionale, jeune perdreau ou jeune faisan.""" },
{ "word": "Pouillé", "definition": """Adjectif.
De l’ancien français « pouille », « pueille » qui signifie rente, registre
de compte issu du pluriel du latin « polyptycha » qui signifie
polyptiques, registres, rôles, matricules.
En histoire, sous l’Ancien Régime, registre des biens et des bénéfices
ecclésiastiques dans une région.
Par exemple: « Le pouillé d’un diocèse. »""" },
{ "word": "Poutargue", "definition": """Nom féminin.
Du copte « outarakhon » qui devient en arabe « boutharkha » qui signifie
œufs de poissons salés et séchés. Ce mot est lié à la racine verbale
« baltarikh » qui signifie conserver dans la saumure.
Il donnera « boutargo » en provençal.
Masse d’ œufs de mulet pressés, salé et enrobés de cire.
En France, la poutargue est une spécialité de Martigues""" },
{ "word": "Poutser", "definition": """Verbe transitif.
De l’allemand « putzen » qui signifie nettoyer.
En Suisse dans un langage familier, nettoyer, astiquer.""" },
{ "word": "Pouzzolane", "definition": """Nom féminin.
De l’italien « pozzolana » de Pozzuoli » qui signifie Pouzzoles, nom
d’une ville près de Naples.
En géologie, nom donné à une roche siliceuse d’origine volcanique qui
est formée de scories à l’état meuble et qui mélangée à de la chaux
entre dans la composition de certains ciments.""" },
{ "word": "Praline", "definition": """Nom féminin.
De « du Plessis-Praslin » dont le cuisinier inventa cette confiserie.
1- Amande ou noisette grillée enrobée de sucre cuit et glacé.
2- En Belgique, bonbon au chocolat généralement fourré.""" },
{ "word": "Praséodyme", "definition": """Nom masculin.
De « praesodynium » mot allemand issu du grec « prasinos » qui signifie
d’un vert de poireau.
En chimie, élément du groupe des lanthanides ou terres rares, de
numéro atomique 59 et de masse atomique 140,92.
C’est un métal jaune clair, extrait de la monazite et qui donne des
sels d’un beau vert.""" },
{ "word": "Préadamisme", "definition": """Nom masculin.
Du latin « prae » qui signifie en avant devant, et qui marque
l’antériorité dans le temps et de « Adam » issu de l’hébreu « adama » qui
signifie la terre.
Adam est le premier homme de la Création selon la Bible.
En histoire des religions, doctrine selon laquelle Adam n’aurait pas
été le premier homme de la création; mais seulement l’ancêtre de
peuple juif.
Par exemple: »Le préadamisme est apparu pour la première fois dans un
livre d’Isaac de la Peyrère en 1655. »""" },
{ "word": "Prédicat", "definition": """Nom masculin.
Du latin  « praedicatum » issu de « praedicare » qui signifie prêcher.
1- En linguistique, second terme d’une énonciation où il est possible
de distinguer ce dont on parle ou ce que l’on affirme ou nie; attribut
du sujet.
Par exemple dans l’expression : »Cet enfant est sage. » Le prédicat est
« est sage’.
2- En linguistique, ce qui dans un énoncé est affirmé à propos d’un
autre terme qu’il soit sujet ou thème.
Par exemple: » Dans une phrase, il y a un groupe en fonction sujet et
un groupe en fonction prédicat. Le sujet est ce à propos de quoi on
parle et le prédicat est ce que l’on en a dit. »
Spécialement. Le verbe et l’attribut qui dépendent d’un nom.""" },
{ "word": "Présure", "definition": """Nom féminin.
Du latin « prendere » qui signifie prendre.
Substance extraite de la caillette des jeunes ruminants, qui contient
une enzyme qui permet de faire cailler le lait.""" },
{ "word": "Prétentaine", "definition": """Nom féminin.
Issu peut-être du normand « pertintaille » qui signifie ornement de
robe, suivi du suffixe « taine » que l’on retrouve dans les refrains
des vieilles chansons populaires tontaine, dondaine.
L’expression « courir la prétentaine » signifie faire sans cesse des
escapades mais aussi avoir de nombreuses aventures galantes.""" },
{ "word": "Prétérition", "definition": """Mot féminin. Du latin praeteritum, supin (forme nominale) de praeterire qui signifie omettre. 
Figure littéraire du discours qui consiste à dire une chose tout en assurant que l’on se gardera bien de la dire. 
Par exemple : Je ne vous dirai pas à quel point votre attitude m’a déplu.
La prétérition est aussi appelée prétermission.""" },
{ "word": "Preux", "definition": """Adjectif masculin et nom masculin.
Du latin « prode » issu de prodesse, de prosum qui signifie être utile.
Dans un sens vieilli et appartenant à la langue de la chevalerie.
Brave, vaillant.
Par exemple, preux en tant qu’adjectif: « Roland est preux, Olivier et
sage » d’après La chanson de Roland.
Par exemple, preux en tant que nom: « Charlemagne et ses preux. »""" },
{ "word": "Prévarication", "definition": """Nom féminin.
A l’origine: abandon de la foi divine, du latin « prævaricatio ».
Acte de mauvaise foi dans la gestion d’affaires
Faute grave d’un fonctionnaire commise dans l’exercice de ses fonctions.""" },
{ "word": "Priapée", "definition": """Nom féminin.
Du latin « priapeium (metrum) » issu du grec « piapeion (metrum) » qui est
le vers priapéen. De « Priape » fils de bacchus et de Vénus, né à
Lampsaque, D.ieu des jardins, qui représente
la vigueur génératrice.
1- Dans l’Antiquité, chant ou fête en l’honneur de Priape.
2- En littérature; poème, peinture scène ou spectacle obscène.""" },
{ "word": "Pro domo", "definition": """Locution adverbiale et adjectif invariable.
Mots latins qui signifient « pour (sa) maison ». D’après un discours de Cicéron.
Plaider pro domo. C’est plaider pour sa propre cause.
Un avocat pro domo. C’est celui qui plaide pour sa propre cause.
Un plaidoyer pro domo. C’est un discours dont le contenu plaide la
propre cause de celui qui le tient.""" },
{ "word": "Proboscidiens", "definition": """Nom masculin pluriel.
Du latin « proboscis, proboscidis » qui signifie museau, trompe d’éléphant.
En zoologie, ordre de mammifères ongulés de très grande taille, qui
possèdent une trompe pour la préhension.
Au singulier, le dinothérium est un proboscidien fossile.
Par exemple: »Aujourd’hui, les proboscidiens sont représentés par les éléphants. »""" },
{ "word": "Prodrome", "definition": """Nom masculin.
Du grec « prodromos » qui signifie avant-coureur.
En littérature, se dit de ce qui annonce un évènement.
En médecine, symptôme avant-coureur d’une maladie.""" },
{ "word": "Prolégomènes", "definition": """Nom masculin pluriel.
Du grec prolegomena : choses dites avant.
Préface très longue qui permet la compréhension d’un livre.""" },
{ "word": "Prolepse", "definition": """Nom féminin.
Du grec « prolambanein » qui signifie prendre par avance, présumer, préjuger.
Figure du discours par laquelle on prévient une objection, en la
réfutant d’avance.""" },
{ "word": "Prométhéen", "definition": """Adjectif.
De Prométhée. Dans la mythologie grecque ce personnage était de la
race des Titans. Il initia la première civilisation humaine. Il déroba
le feu du ciel et le transmit aux hommes. Pour le punir, Zeus l’enchaîna sur le
Caucase où un aigle lui rongeait le foie qui repoussait sans cesse.
Héraclès le délivra.
Le mythe de Prométhée inspira de nombreux œuvres littéraires.
Relatif à Prométhée, c’est à dire caractérisé par le goût de l’action
et la foi en l’homme.""" },
{ "word": "Propitiatoire", "definition": """Nom masculin ou féminin.
Adjectif.
Du latin « propriatorius » qui signifie clément, propritiatoire.
-Employé comme nom.
Couvercle d’or massif qui fermait l’Arche d’Alliance.
-Employé comme adjectif.
Qui a la vertu de rendre Dieu propice.
Par exemple peut se dire d’un rite ou d’un sacrifice.""" },
{ "word": "Propolis", "definition": """Nom féminin.
Du grec « propolis » constitué du préfixe « pro » qui signifie en avant et
« polis » qui signifie ville, soit entrée de la ville.
Résine, dont la couleur va du jaune clair à vert brun.Les abeilles la recueillent sur l’écorce de certains conifères et sur les écailles des bourgeons de nombreux arbres. Ce sont par exemple les bouleaux, les pruniers, mais surtout les peupliers. Grâce à la propolis elles colmatent les fentes des ruches et des gâteaux de cire mais aussi aseptisent certains endroits de la ruche et momifient des animaux morts, trop gros pour être évacués (souris par exemple).
Cette substance est principalement utilisée en pharmacie pour la désinfection de
la gorge et la cicatrisation des plaies de la peau.""" },
{ "word": "Prosopagnosie", "definition": """Nom féminin.
Du grec « prosôpon » qui signifie personne et « gnosis » qui signifie connaissance.
En médecine, affection qui consiste en l’impossibilité de reconnaître ses proches.""" },
{ "word": "Prosopométamorphopsie", "definition": """Nom féminin.
Du grec « prosôpon » qui signifie face, « metamorphoô » qui signifie
transformer et « opsis » qui signifie vue.
En neurologie, trouble caractérisé par une déformation de la
perception des visages.""" },
{ "word": "Prosthèse", "definition": """Nom féminin.
Du grec « prosthistenai » qui signifie face, figure ou personnage.
Ajout au début d’un mot, d’une lettre ou d’une syllabe qui n’en
modifie pas le sens.
Par exemple le passage du latin au français du mot scala donne le mot
escalier. Le e est une prosthèse phonétique.
Il y a des prosthèses stylistiques qui permettent un effet comique.""" },
{ "word": "Protase", "definition": """Nom féminin.
Du latin « protasis » issu du grec « prôtos » qui signifie premier.
1- Dans un sens vieilli, partie d’une pièce de théâtre dans laquelle
le sujet est exposé.
2- En grammaire, subordonnée conditionnelle placée avant la principale.""" },
{ "word": "Prote", "definition": """Nom masculin.
Du grec « protos » qui signifie premier.
Dans un sens vieilli, contremaître dans un atelier d’imprimerie au plomb.
Par exemple: « Le prote dirigeait les correcteurs d’épreuve. »
Par exemple: « [La Revue des Deux Mondes] Rapidement dirigée par
François Buloz dès 1831, un ancien prote d’imprimerie… »
« La Revue des Deux Mondes » dans la tourmente – Nicolas Truong – Le Monde 4 février 2017""" },
{ "word": "Protée", "definition": """Nom masculin.
Du latin « Proteus » nom d’une divinité de la mer qui pouvait prendre
des formes variées.
1- D’une manière littéraire, se dit d’une personne qui change sans
cesse d’opinions ou qui joue toutes sortes de personnages.
Par exemple: « Il change souvent d’avis, il pourrait s’appeler Protée!  »
2- En zoologie, amphibien de la famille des urodèles à branchies
persistantes et qui vit dans les eaux souterraines. Ses yeux ont perdu
leur fonction initiale en raison de l’obscurité.
Il est aveugle.
Le Protée anguillard est dit aussi Salamandre blanche ou Salamandre
des grottes. Il est aussi appelé poisson humain à cause de sa peau qui
ressemble à celle de l’homme.
Par exemple: « Le corps du Protée est blanc dans l’obscurité et se
pigmente à la lumière. »""" },
{ "word": "Proxène", "definition": """Nom masculin.
Du grec « proxenos » de « xenos » qui signifie étranger.
Dans l’Antiquité grecque, officier chargé par le peuple d’accueillir
les étrangers ou les hôtes publics et de régler le cas échéant, leurs
différends.""" },
{ "word": "Prytane", "definition": """Nom masculin.
Du latin « prutanis » qui signifie chef, maître.
Dans la Grèce antique, l’un des premiers magistrats de certaines cités
grecques.
A Athènes, l’un des cinquante sénateurs appartenant aux tribus et qui
avaient un droit de préséance au sénat.""" },
{ "word": "Psalette", "definition": """Nom féminin.
Du grec « psallein » qui signifie jouer d’un instrument à cordes.
École de musique faisant partie d’une église et où sont instruits les
enfants de chœur.
Se dit de l’ensemble des chanteurs de cette psallette.""" },
{ "word": "Psalliote", "definition": """Nom féminin.
Du grec « psallis » qui signifie voûte, cintre.
En botanique, champignon basidomycète, à lamelles de la famille des
agaricacées, et qui existe en de nombreuses espèces dont plusieurs
sont comestibles.
Le psaliiote champêtre ou agaric est le champignon de couche, souvent
appelé champignon de Paris.""" },
{ "word": "Pschent", "definition": """Nom masculin.
De l’égyptien démotique « skhent » précédé de l’article p, qui signifie
les deux puissances.
Double couronne des pharaons formée d’une mitre blanche oblongue
symbole de la Haute Egypte associée au dieu Seth, insérée dans une
couronne rouge plate à fond relevé symbole de la Basse Egypte et
associée au dieu Horus.""" },
{ "word": "Psittacisme", "definition": """Nom masculin.
Du grec « psittakos » qui signifie perroquet.
Répétition mécanique (comme le ferait un perroquet) de mots ou de
phrases entendues par le sujet qui ne les comprends pas.
C’est un phénomène normal chez l’enfant.""" },
{ "word": "Psylle", "definition": """Nom masculin. 
Du latin « psylli » issu du grec « psulloi » qui est le nom d’un peuple de Cyrénaïque. 
Charmeur de serpent en Inde ou en Orient.""" },
{ "word": "Pterygote", "definition": """Nom masculin.
Du grec « pterugos » issu de « pteron » qui signifie aile.
En zoologie se dit de tout insecte ailé.""" },
{ "word": "Ptôse", "definition": """Nom féminin.
Du grec « ptôsis » qui signifie chute.
1- En médecine, descente d’un organe par relâchement de ses moyens de soutien.
2- En linguistique, disparition d’un mot dans une langue.""" },
{ "word": "Pudendum", "definition": """Nom masculin.
Mot latin. Au singulier pudendum et au pluriel pudenda. 
Gérondif de « pudere » qui signifie faire honte ou avoir honte. 
Terme vieilli.
Se disait des parties génitales des deux sexes. S’utilisait en médecine ou en littérature.
« Pudendum virile » synonyme de pénis.
« Pudendum muliere » synonyme de cunnus.""" },
{ "word": "Puna", "definition": """Nom féminin.
Mot espagnol emprunté au quechua.
-Troubles physiologiques liés à l’altitude dans les Andes.
-Haut plateau froid au Pérou et en Bolivie.""" },
{ "word": "Punch", "definition": """Nom masculin.
Mot anglais issu de l’hindi « panch » qui signifie cinq à cause des cinq
composants de la boisson.
Boisson alcoolisée à base d’eau-de-vie (généralement du rhum) et
parfumée de citron et d’épices.
Au pluriel on écrit « des punches ».
Par exemple: »Il existe des punches chauds; »""" },
{ "word": "Pusillanime", "definition": """Adjectif et nom.
Du latin « pusillus animus » qui signifie esprit étroit.
Caractère de celui qui manque d’audace ou de courage; qui refuse les
responsabilités.""" },
{ "word": "Pussilanime", "definition": """Adjectif.
Du latin « pussilanimis » issu de l’expression « pussilus animus » qui
signifie esprit mesquin.
D’une manière littéraire, se dit d’une personne qui manque d’audace,
craint le risque ou les reponsabilités.
Par exemple: « Nous ne pouvons pas donner ce poste de dirigeant à ce
cadre pussilanime. »""" },
{ "word": "Pygmée", "definition": """Nom masculin.
Variation des mots « pymeau », « pumain » issus du latin « pygmaeus » par le
grec « pygmaios » qui signifie grand comme le poing qui se dit « pugmê »
en grec.
1- Dans l’Antiquité, individu appartenant à un peuple légendaire de
nains de la région du Nil. Dans la mythologie gréco-latine, on raconte
qu’Hercule lutta contre les Pygmées.
2- A l’époque moderne, individu appartenant à certaines races d’hommes
de très petite taille et qui vivent en Afrique ou dans l’Insulinde.
Adjectif.
Le terme qualifie le peuple Pygmée.
Par exemple:
La langue pygmée.
Ou aussi: Les coutumes pygmées.""" },
{ "word": "Pylore", "definition": """Nom masculin.
Du grec « pulôros » qui signifie portier.
Orifice faisant communiquer l’estomac avec le duodénum.""" },
{ "word": "Pyrrhocoris", "definition": """Nom masculin.
Du grec « purrhos » qui signifie roux et « koris » qui signifie punaise.
Punaise rouge tachetée de noir, qui vit en été au pied des arbres et des murs.
On l’appelle aussi soldat.""" },
{ "word": "Quérulence", "definition": """Adjectif.
Du grec querula: plainte.
En psychiatrie, forme de délire d’un sujet qui cherche querelle en
permanence et de manière disproportionnée quant à la cause. Ainsi
qu’il revendique la réparation d’un préjudice qu’il aurait subi réellement ou pas.""" },
{ "word": "Quipou", "definition": """Nom masculin.
Chez les Incas, qui ignoraient l’écriture, système de faisceau de
cordelettes dont les couleurs, les combinaisons et les nœuds
étaient porteurs d’une signification précise.""" },
{ "word": "Quôc-Ngu", "definition": """Nom masculin.
Du chinois classique « Chu Quôc ngu » qui signifie langue nationale.
1- Langue nationale.
2- Ecriture romanisée du vietnamien, par le biais de l’alphabet latin
augmenté de nombreux diacritiques qui servent à noter la valeur
phonétique des lettres mais aussi les tons de la
langue. Cette écriture a remplacé d’anciennes écritures locales.
C’est en 1527 que des missionnaires portugais commencèrent d’utiliser
le latin pour écrire la langue locale. C’est le jésuite Alexandre de
Rhodes né à Avignon en 1591 et mort en
1660, qui a compilé, amélioré et systématisé les systèmes de
transcription de ses prédécesseurs missionnaires.Son premier ouvrage
est un dictionnaire vietnamien-portugais-latin paru en 1651.
Cette transcription a acquis en 1918 le statut d’orthographe
officielle de la langue dans le système scolaire français. Ce fut un
vecteur d’unification bien accueilli par tous, y compris par les nationalistes.
Ce fut aussi un outil de démocratisation de l’éducation.""" },
{ "word": "Rabiot", "definition": """Nom masculin.
Argot de marin. Probablement du dialecte « rabes » variante de « raves »
qui signifie œufs de poisson, menu fretin, du latin « rapum » qui a
donné « rave » plante potagère cultivée pour ses racines.
1- Dans une langue familière, supplément ou surplus dans une distribution.
Par exemple; »Nos candidats font dans le gagne-petit, le rabiot
honteux. » Le Monde, 30 janvier 2017, Benoît Hopquin, « Des chiffres et
des lettres. »
2- Temps supplémentaire, qu’un soldat doit passer au régiment en cas
de peines disciplinaires.
Temps de travail supplémentaire.
Supplément.
Par exemple: « Un rabiot de sommeil. »""" },
{ "word": "Rafle", "definition": """Nom féminin.
De l’allemand « Raffel » issu de raffen qui signifie emporter vivement.
Au XIII ème siècle « rafe » est un racloir, un instrument pour racler le feu.
En ancien français « la rafle » était un coup de vent qui a donné le mot
rafale. C’était aussi une hotte ou un grand panier.
La rafle était aussi la lèpre. Mais encore le raifort ou une petite rave.
A la fin du XVI ème siècle « le jeu de rafle » était un jeu de dés où
l’on pouvait enlever toute la mise d’un seul coup si les dés
affichaient la même valeur.
Au XX ème siècle, le mot rafle a pris un autre sens: c’était une
arrestation massive de civils réunis ensuite dans un même lieu afin de
les déporter.""" },
{ "word": "Raïa", "definition": """Nom masculin.
Du turc « raïa » qui signifie troupeau.
Sujet non musulman des turcs de l’empire ottoman.""" },
{ "word": "Raifort", "definition": """Nom masculin.
Du moyen français « raiz fors » de « raiz » issu du latin « radix » qui
signifie racine et de fort dont le masculin et le féminin était
identique en ancien français.
Plante herbacée vivace de la famille des Brassicacées, cultivée pour
sa racine qui sert de condiment. Son nom taxonomique est « Armoracia
rusticana »
Le condiment a une saveur est piquante et poivrée, mais l’effet
piquant disparaît entre chaque bouchée.
La racine a des propriétés dépuratives, stimulantes et digestives.
Elle soignait les rhumatismes.
La plante a de très grandes feuilles, jusqu’à 50 cm de long, ses
fleurs sont petites, blanches ou jaunes et regroupées en grappes. Elle
dégage une très forte odeur.
Par exemple: » Le raifort est employé principalement en Alsace et en
Allemagne ainsi que dans de nombreux pays d’Europe centrale, pour
relever les sauces et les viandes. »""" },
{ "word": "Raiponce", "definition": """Nom féminin.
Du latin « raponzo » issu du latin « rapa » qui signifie rave.
1- Plante herbacée et vivace. Ses fleurs lilas sont en clochettes. Ses
feuilles et ses racines se mangent en salade.
Elle appartient au genre Phyteuma, campanulacées et comporte environ
45 espèces.
2- Conte populaire allemand recueilli par les frères Grimm.""" },
{ "word": "Ramequin", "definition": """Nom masculin.
Du néerlandais rammeken diminutif de ram, issu de l’allemand Rahm qui
signifie crème.
1- Petit gâteau au fromage.
2- Petit récipient utilisé pour la cuisson au four ou au bain-marie.""" },
{ "word": "Ramingue", "definition": """Adjectif.
De l’italien « ramingo » issu de « ramo » qui signifie rameau. Ce mot a
d’abord été appliqué au faucon qui vole de branche en branche.
Se dit d’un cheval qui refuse d’avancer lorsqu’on lui fait sentir l’éperon.
On dit « un cheval ramingue ». C’est un cheval rétif.""" },
{ "word": "Rampeau", "definition": """Nom masculin.
Altération probable du français « rappel ».
Dans un sens vieilli
1- Coup supplémentaire que l’on joue à certains jeux, particulièrement
aux dés, lorsque les adversaires ont obtenu le même nombre de points.
On disait « faire rampeau » c’est-à-dire faire le même nombre de points
que l’adversaire, donc coup nul.
2- Second coup dans une partie qui n’en comporte que deux.
3- Coup joué à titre de revanche quand on a perdu le coup précédent.""" },
{ "word": "Rancio", "definition": """Nom masculin.
Du même mot en espagnol qui signifie rance, issu du latin « rancidus »à
cause du vieillissement.
Vin de liqueur qu’on a laissé vieillir et qui est devenu doux et doré.""" },
{ "word": "Raphé", "definition": """Nom masculin.
Du grec « raphé » qui signifie couture.
En anatomie, entrecroisement de fibres musculaires, tendineuses ou
nerveuses provenant d’organes symétriques, au niveau de leur ligne
médiane et qui ressemble à une couture.
Par exemple:
« Le raphé du périnée »
« Le raphé du scrotum »""" },
{ "word": "Ratiocinner", "definition": """Verbe intransitif.
Du grec ratio:calcul, compte.
Se perdre en raisonnements ou en calculs interminables. Synonyme de
l’expression familière « couper les cheveux en quatre. »""" },
{ "word": "Ratte", "definition": """Nom féminin.
De « rate » l’animal, par analogie de forme.
Pomme de terre allongée, à chair jaune, fine et savoureuse, appelée
aussi quenelle de Lyon ou cornichon.
Par exemple: La ratte du Touquet est une pomme de terre à la saveur renommée.""" },
{ "word": "Réalgar", "definition": """Nom masculin.
Altération de l’arabe « rehj-al-ghar » qui signifie poudre de cave ou
« rhag-al-far »qui signifie mort-aux-rats du fait d’une erreur de
lecture. Le réalgar était, en effet, utiisé comme mort-aux-rats.
Sulfure naturel d’arsenic de couleur rouge.""" },
{ "word": "Reblochon", "definition": """Nom masculin.
Du mot savoyard « reblocher » qui signifie traire de nouveau une vache.
De « blocher » « blossi » en dialecte qui signifie pincer.
Fromage à pâte grasse, de saveur douce, fabriqué en Savoie.""" },
{ "word": "Récollet", "definition": """Nom masculin.
Du latin « recollectus » participe passé de recolligere qui signifie recueillir.
Religieux Franciscain réformé. Il a l’esprit de récollection c’est à
dire l’esprit de se recueillir par la méditation et par la prière.""" },
{ "word": "Rection", "definition": """Nom féminin.
Du latin « rectio » qui signifie gérer.
Propriété que possède le verbe d’être accompagné d’un complément
direct ou d’une préposition.""" },
{ "word": "Redoute", "definition": """Nom féminin.
De l’italien « ridotto » qui signifie refuge, abri, issu du latin
« reductus » qui signifie retiré, participe passé de reducere par
croisement avec redouter.
1- Anciennement, ouvrage de fortification détaché.
Par exemple: Les blockhaus ont remplacé les redoutes.
2- Dans un sens vieilli, Lieu où l’on donne des fêtes, des bals. La
fête, le bal.
Par exemple: Ils ont dansé toute la soirée à la redoute.""" },
{ "word": "Régalien", "definition": """Adjectif.
Du latin « regalis » qui signifie royal.
Qui est le fait du roi.
Cette notion peut s’étendre et s’appliquer au chef de l’exécutif.
Par exemple: « Le droit de grâce est un privilège régalien ».
On fait allusion au droit de grâce du Président de la République.""" },
{ "word": "Régate", "definition": """Nom féminin.
Du vénitien « regata » qui signifie défi. Issu de « regatar » qui signifie
rivaliser mais dont l’origine est inconnue.
1- Employé souvent au pluriel. Course de bateaux à la voile ou à l’aviron.
2- Cravate rappelant celle des marins et qui consiste en un nœud d’où
sortent deux pans verticaux et superposés.""" },
{ "word": "Réminiscence", "definition": """Nom féminin.
Du latin « remisci » qui signifie se souvenir.
1- En psychologie, retour à l’esprit d’un souvenir involontaire.
2- En philosophie, on parle de la théorie platonicienne de la
réminiscence selon laquelle toute connaissance est le souvenir
d’un état antérieur où l’âme possédait une vue directe des Idées.
3- Couramment, souvenir vague et imprécis dominé par l’affect.""" },
{ "word": "Remugle", "definition": """Nom masculin.
De l’ancien nordique « mygla » qui signifie moisissure.
Dans un sens vieilli ou littéraire, odeur désagréable de moisi, de renfermé.""" },
{ "word": "Reseda", "definition": """Nom masculin.
Du latin « resedare » qui signifie calmer, en raison des propriétés
médicinales que l’on attribuait à cette plante.
1- Plante à fleurs blanchâtres ou jaunâtres disposées en grappes. Elle
est répandue en Europe et dans les pays du bassin méditerranéen.
2- Couleur d’un vert jaunâtre.""" },
{ "word": "Résingle", "definition": """Nom masculin.
Du latin « cingula » qui signifie sangle.
Outil d’orfèvrerie en forme de levier courbe et arrondi au bout, qui
permet de redresser des objets métalliques bosselés.""" },
{ "word": "Rétiaire", "definition": """Nom masculin.
Du latin « rete, retis » qui signifie rets, filet.
Dans l’Antiquité Romaine, gladiateur armé d’un trident et d’un
poignard mais aussi d’un filet destiné à envelopper l’adversaire, d’où
son nom.""" },
{ "word": "Rhabdomancie", "definition": """Nom féminin.
Du grec « rabdos qui signifie baguette et « manteia » qui signifie divination.
Mode de divination à l’aide de baguettes, art de déceler les sources,
les trésors, les mines.""" },
{ "word": "Rhéotropisme", "definition": """Nom masculin.
Du grec « rheô, rhein » qui signifie couler et « tropos » qui signifie
tour, direction.
En biologie, tendance d’une plante à répondre au stimulus d’un cours
d’eau par un changement dans la direction de sa croissance.""" },
{ "word": "Rhétique", "definition": """Adjectif et nom masculin.
En tant qu’adjectif.
Du latin « Rhaeticus » de « Rhaetia » qui signifie « Rhétie » .
Qui appartient à la région des Alpes située entre Rhin et Danube.
Par exemple, les Alpes rhétiques
En tant que nom masculin.
Langue ancienne du groupe italo-celtique, dite rhéto-roman.""" },
{ "word": "Rhyton", "definition": """Nom masculin.
Du grec « rhuton » qui signifie vase à boire, issu de « rhein » qui signifie couler.
En archéologie, coupe en corne, en terre cuite ou en métal. Elle a la
forme d’une corne et se termine par une tête d’homme ou d’animal. Elle
comporte une ouverture au fond. On y boit en laissant couler le vin vers le bas.
Le rhyton était utilisé lors de cérémonies ou de rituels religieux
comme les libations.
Au III ème siècle avant notre ère, deux auteurs grecs écrivirent dans
« Le traité de l’ivresse »: »Le rhyton ne se donne qu’aux héros. »""" },
{ "word": "Ripple-mark", "definition": """Nom féminin.
De l’anglais « ripple » qui signifie clapotis et « mark » qui signifie marque.
Anglicisme géographique. Petite ride du sable formée par le
clapotement des eaux à la surface des plages.""" },
{ "word": "Risberme", "definition": """Nom masculin.
Du néerlandais « rijsberme » issu de « rijs » qui signifie branchage et
« berme » qui signifie talus.
Terme technique. Talus de protection recouvert de fascines, au pied
d’un ouvrage hydraulique, comme les piles d’un pont, une jetée…""" },
{ "word": "Risorius", "definition": """Nom masculin.
Du latin « risorius » qui signifie riant.
En anatomie, muscle superficiel de la commissure des lèvres
contribuant à l’expression du rire.""" },
{ "word": "Rodomont", "definition": """Nom masculin et adjectif.
De l’italien « Rodomonte » personnage de l’Arioste.
Personnage qui fanfaronne.
De ce mot est issu le mot « rodomontade » qui est un propos de rodomont
ou une fanfaronnade.""" },
{ "word": "Rogaton", "definition": """Nom masculin.
Ce mot vient du latin médiéval Rogatum qui vient de Rogare qui signifie demander.
Familièrement c’est une chose de peu de valeur et que l’on rejette.
Dans un sens plus moderne et employé au pluriel ce sont des morceaux d’aliments ou les restes d’un repas. """ },
{ "word": "Rogue", "definition": """1- Adjectif.
De l’ancien scandinave « hrokr » qui signifie arrogant.
Se dit d’une personne pleine de morgue. A la fois méprisante, froide et rude.
2- Nom féminin.
De l’ancien nordique « hrogn » qui signifie œuf.
Œufs de morue ou de hareng utilisés comme appâts pour la pêche à la sardine.""" },
{ "word": "Rohart", "definition": """Nom masculin.
De « roal » qui signifie morse, de l’ancien nordique « hrosshvalr ».
Ivoire que l’on tire des défenses du morse ou des dents d’hippopotame.
On dit : « un couvert de table à manche de rohart ».""" },
{ "word": "Romarin", "definition": """Nom masculin.
Du latin « rosmarinus » qui signifie littéralement rosée de mer.
Arbuste aromatique des collines du Midi de la famille des labiées, aux
fleurs bleues.""" },
{ "word": "Rondache", "definition": """Nom masculin.
De l’italien ‘ »rondaccio » issu du français « rond »
Grand bouclier circulaire employé au XVIème siècle par les fantassins.""" },
{ "word": "Roquelaure", "definition": """Nom masculin.
Du duc de Roquelaure, en 1752.
Anciennement, c’était un manteau masculin, demi ajusté et descendant
jusqu’au genoux que l’on portait sous Louis XIV.""" },
{ "word": "Rubellite", "definition": """Nom féminin.
Du latin « rubellus » qui signifie rouge.
En minéralogie, variété de tourmaline généralement de couleur rose.
Il en existe aussi des bleues et des vertes.""" },
{ "word": "S’esbigner", "definition": """Verbe pronominal.
De l’italien d’argot, « sbignare » qui signifie s’enfuir de la vigne
vers 1754. Signifiait « voler » vers 1789.
Dans une langue familière et vieillie, signifie se sauver.""" },
{ "word": "Saanen", "definition": """Nom féminin.
De la haute vallée de Sarine en Suisse, (Saane en allemand, commune de
Saanen) dans l’Oberland bernois.
La saanen ou blanche de Gessenay ou chèvre de Gessenay est une race
caprine oroginaire du Sannerland et de l’Obersimmental en Suisse.
Le blanc et le crème sont les deux seules robes acceptées. C’est une
excellente laitière de la race la plus répandue au monde.
Par exemple: »La saanen avec l’alpine et la poitevine fournissent la
plupart des fromages de chèvre français. »""" },
{ "word": "Sabéen", "definition": """A- Nom et adjectif.
De l’araméen « ç’ba » qui signifie baptème, rattaché à l’hébreu « çaba »
qui signifie armée (du ciel).
1- Membre d’une secte judéo-chrétienne mentionnée dans le Coran, qui
se rapporte à des chrétiens adorateurs des astres.
2- Membre d’une secte de gnostiques, dont la religion s’apparentait à
celle des précédents.
B- Adjectif et nom.
De « Saba » nom du peuple d’Arabie qui vivait au Yémen.
Se dit de ce qui est appartient au pays de Saba.
Par exemple: »Des coutumes sabéennes. »
Par exemple: »Les Sabéens, les Sabéennes. »""" },
{ "word": "Sabellianisme", "definition": """Nom masculin.
De Sabellius.
En religion, doctrine de Sabellius, hérésie selon laquelle la Trinité
(Le Père, Le Fils et le Saint-Esprit ) forme une seule et même
personne qui se manifeste sous trois aspects.""" },
{ "word": "Sabine", "definition": """Nom féminin.
Du latin « sabina herba » qui signifie herbe des Sabins, premier peuple de Rome.
En botanique, genévrier d’Europe méridionale, hautement toxique mais
dont les feuilles ont des propriétés médicinales.""" },
{ "word": "Sabra", "definition": """Nom masculin.
De l’arabe « sabr » qui signifie figue de Barbarie.
Citoyen juif d’Israël, natif du pays.""" },
{ "word": "Sadducéen", "definition": """Nom et adjectif.
Origine inconnue. Peut être issu de « Zadok » qui était le nom d’un grand prêtre.
Dans l’Antiquité, membre d’une secte de juifs conservateurs qui s’en
tenaient à la Thora et rejetaient la résurrection, la vie future et la
rétribution.""" },
{ "word": "Sagine", "definition": """Nom féminin.
Du latin « sagina » qui signifie engraissement, la plante étant utilisée
pour engraisser les moutons.
En botanique, petite plante herbacée de la famille des caryophyllacées
formant gazon et dont les fleurs sont blanches.""" },
{ "word": "Sagum", "definition": """Nom masculin.
Du latin d’origine gauloise « sagum » de même sens.
Court manteau de lin que portaient les romains et les gaulois au cours
des guerres.""" },
{ "word": "Saint-Crépin", "definition": """Nom masculin. 
De saint-Crépin patron des cordonniers.
Dans un sens vieilli, ensemble des outils du cordonnier.
Familièrement et toujours dans un sens vieilli, le synonyme est saint-frusquin.""" },
{ "word": "Saint-Pierre", "definition": """Nom masculin.
Poisson Saint-Pierre: ce poisson porte sur chacun de ses côtés une
tâche ronde. Cette tâche, selon la légende, aurait été causée par
l’empreinte qui laissèrent les doigts de Saint-Pierre, quand sur
l’ordre du Christ, il tira de la bouche du poisson le statère de cens,
qui était une monnaie de l’antiquité servant à payer un impôt pour être
électeur ou être éligible.
Poisson de mer dont la chair est très appréciée. Le zée est l’autre
nom de ce poisson.""" },
{ "word": "Sakieh", "definition": """Nom masculin.
De l’arabe « saqiya » issu du radical « saga » qui signifie irriguer.
Noria égyptienne mue par des bœufs qui tournent en manège.""" },
{ "word": "Salse", "definition": """Nom féminin.
Du latin » salsus » qui signifie salé.
En géologie, dégagement d’hydrocarbures gazeux mêlés à de l’eau, à la
surface terrestre. Volcan de boue.""" },
{ "word": "Samit", "definition": """Nom masculin.
Du latin « samitum » issu de « examitum », du grec byzantin « hexamitos »
qui signifie six fils.
En archéologie, étoffe orientale composée de six fils de couleur,
demi-satin composé d’une chaîne de soie et d’une trame de fil.""" },
{ "word": "Sangaris", "definition": """Nom masculin.
Cyanopyge sangaris est un papillon de Colombie de 55mm d’envergure.
Son corps trapu est noir aux reflets gris vert, ses ailes sont gris
vert métallisé aux reflets mordorés, avec une frange grise et sur
les ailes postérieures une tâche orange.
Sangaris est aussi le nom d’une opération militaire de l’armée
française en République Centrafricaine qui a débuté le 5 décembre
2013.""" },
{ "word": "Sansevière", "definition": """Nom féminin.
Du nom du prince de Sansevieria.
Plante de la famille des liliacées qui pousse dans les régions
tropicales et qui fournit une fibre textile très résistante.""" },
{ "word": "Sanskrit", "definition": """Nom masculin et adjectif invariable.
Du sanskrit « samskr(i)ta » qui signifie « parfait » par opposition à
« prâkrit » qui signifie « à l’état naturel ou peu soigné ».
Forme savante, codifiée de l’indo-aryen ancien, dans laquelle sont
écrits les grands textes brahmaniques de l’Inde.""" },
{ "word": "Sanza", "definition": """Nom féminin.
Mot tiré d’une langue africaine.
Instrument de musique africaine, traditionnel, fait de lamelles vibrantes.
Par exemple: Le chanteur s’accompagne à la sanza.""" },
{ "word": "Saperde", "definition": """Nom féminin.
Du latin « saperda » d’origine grecque qui signifie poisson salé.
Insecte longicorne de la famille des coléoptères, qui possède de
larges élytres et dont les larves vivent dans les bois.
La saperde requin est très nuisible aux saules, aux peupliers et aux trembles.""" },
{ "word": "Sapientiaux", "definition": """Adjectif masculin pluriel.
Du latin « sapientia » qui signifie sagesse.
Se dit du groupe de cinq livres bibliques: « Proverbes, Job,
Ecclésiaste, Ecclésiastique et Sagesse. »
On y adjoint parfois Les Psaumes et Le Cantique des Cantiques.""" },
{ "word": "Sapiteur", "definition": """Nom masculin. 
Du provençal « sapitour » issu du latin « sapere » qui signifie savoir.
En droit marchand, expert chargé d’évaluer la valeur des marchandises.""" },
{ "word": "Saponine", "definition": """Nom féminin.
De la saponaire, du latin « sapon » qui signifie savon.
Glucoside extrait de certains végétaux comme la saponaire ou le bois
de Panama et dont la solution aqueuse mousse par simple agitation.""" },
{ "word": "Sapropèle", "definition": """Nom masculin.
Du grec « sapros » qui signifie putride et « pêlos » qui signifie limon.
En géologie, vase organique pauvre en oxygène et riche en oxygène
sulfuré, qui est à l’origine du pétrole""" },
{ "word": "Sardonique", "definition": """Adjectif.
De « ris sardonic ou sardonien » du grec « sardanios ». Origine
incertaine, mais rattaché à « herba sardonia » qui est la renoncule de
Sardaigne dont l’ingestion provoque une intoxication se manifestant
par un rictus.
1- En médecine, un rire sardonique est un rictus convulsif dû à la
contracture spasmodique des muscles de la face.
2- Par influence de sarcastique ou de satanique, Qui exprime une
moquerie amère, froide et méchante.""" },
{ "word": "Saros", "definition": """Nom masculin.
Mot du latin scientifique issu du grec « saros » qui signifie cycle
babylonien 3600 ans, cycle babylonien 222 mois; avec une origine dans
l’akkadien « sâru » qui signifie cercle, chiffre parfait, 360, 3600.
Période de 6585 jours c’est-à-dire 18 ans et 10 ou 11 jours, qui était
déjà connue par  les Chaldéens et qui permettait de prédire le retour
des éclipses.
Pendant un saros on compte en moyenne 71 éclipses (43 de soleil et 26 de lune).""" },
{ "word": "Sarracénie", "definition": """Nom féminin.
De « sarracéna » issu de « Sarrasin » médecin français.
En botanique, plante exotique de la famille des sarracéniacées, qui
pousse sur le littoral atlantique de l’Amérique du Nord et dont les
feuilles ont la particularité de capturer les insectes.""" },
{ "word": "Sarracénique", "definition": """Adjectif.
Du latin « sarracenus » qui signifie sarrasin.
Qui concerne les populations musulmanes d’Orient au Moyen-Age.
Par exemple on dit: « l’art sarracénique ».""" },
{ "word": "Sasser", "definition": """Verbe transitif.
Du mot français « sas » qui signifie petite pièce étanche entre deux
milieux par exemple l’air et l’eau.
Le mot « sas » vient du latin « setacium » qui signifie soie de porc, crin.
Le verbe sasser a plusieurs significations.
1- Passer au sas, tamiser la farine ou le plâtre.
2- Faire passer par le sas d’une écluse
Expression un peu vieillie « sasser et ressasser » discuter à plusieurs
reprises une théorie.
Ressaser s’emploie encore. Il signifie:
1- Revenir sur les choses. Repasser des faits dans son esprit.
2- Répéter de façon lassante.""" },
{ "word": "Saturnien", "definition": """Adjectif.
De la planète « Saturne ».
1- Dans un emploi rare, se dit de ce qui est de Saturne.
2- Dans un sens vieilli ou littéraire, se dit d’un caractère triste ou
mélancolique.
Par exemple: « Les poèmes Saturniens. » de Paul Verlaine.""" },
{ "word": "Satyriasis", "definition": """Nom masculin.
De « satyrus » qui signifie satyre.
Un satyre était une divinité mythologique de la terre. un être à corps
humain, à cornes et pieds de chèvre ou de bouc.
Exagération morbide des désirs sexuels chez l’homme.""" },
{ "word": "Scabieuse", "definition": """Nom féminin.
Du latin « scabiosus » qui signifie galeux. Cette plante passait pour
guérir la gale qui se dit « scabies » en latin.
1- Plante herbacée de la famille des dipsacacées, annuelle ou vivace,
sauvage ou cultivée. Elle fut autrefois employée comme dépuratif.
Adjectif. 
Même origine étymologique que pour le nom. 
2- Relatif à la gale.
Par exemple: une éruption scabieuse.  """ },
{ "word": "Scala-santa", "definition": """Nom féminin.
De l’italien « scala-santa » qui signifie escalier saint.
Escalier du Palais de Ponce-Pilate à Jérusalem, transporté et réédifié
à Rome, que les pèlerins montent à genoux.""" },
{ "word": "Schwa", "definition": """Nom masculin.
De l’hébreu « chav » qui signifie rien, vide.
Voyelle neutre appelée e muet en français.""" },
{ "word": "Scolie", "definition": """Nom féminin et masculin.
Du grec « skholion » issu de « skkolé » qui signifie éole.
1- Nom féminin.
Note philologique, historique due à un commentateur ancien et servant
à l’interprétation d’un texte de l’Antiquité. Ce peut être aussi une
note ritique.
2- Nom masculin.
Remarque à propos d’un théorème ou d’une proposition.""" },
{ "word": "Scolyte", "definition": """Nom masculin.
L’origine de ce mot semble inconnue. On pense peut-être qu’il est issu
de « skolex » qui signifie ver.
En zoologie, insecte coléoptère qui vit sous l’écorce des arbres et y
creuse de très nombreuses galeries.""" },
{ "word": "Scotopie", "definition": """Nom féminin.
Du grec « skotos » qui signifie obscurité et « opos » qui signifie vue.
Se dit de la vision crépusculaire.""" },
{ "word": "Scriban", "definition": """Nom masculin.
Du latin « scribere » qui signifie écrire.
Secrétaire à tiroirs du XVIIème siècle, d’origine flamande, surmonté
d’un corps d’armoire.""" },
{ "word": "Scripturaire", "definition": """Adjectif.
Du latin « scriptura » qui signifie écriture. Au XIXème siècle c’était
un membre d’une secte juive.
1- Ce qui est relatif à l’écriture sainte.
2- Plus rarement, signifie ce qui est relatif à l’écriture, au graphique.""" },
{ "word": "Scrub", "definition": """Nom masculin.
De l’anglais « scrub » qui signifie brousse, broussaille.
En géographie physique, brousse épaisse d’Australie composée de buissons.""" },
{ "word": "Sébile", "definition": """Nom féminin.
Peut-être issu de l’arabe « sabil » qui signifie aumône.
Petite coupe destinée à recevoir de l’argent issu de quêtes destinées
à des mendiants ou des nécessiteux.""" },
{ "word": "Seide", "definition": """Nom masculin.
De l’arabe « Zayd » nom d’un affranchi de Mahomet.
En littérature homme capable d’un dévouement aveugle et fanatique.""" },
{ "word": "Sélénite", "definition": """-Nom masculin
Sel de l’acide sélénieux.
-Nom
Du grec « Selênê » qui signifie Lune.
Habitant imaginaire de la Lune.""" },
{ "word": "Senestrorsum", "definition": """Adjectif invariable et adverbe.
Du latin sinistrorsum qui signifie vers la gauche, à gauche; issu de
sinistra qui signifie main gauche.
Se dit d’un enroulement sénestre, vers la gauche, c’est à dire
contraire au sens des aiguilles d’une montre.""" },
{ "word": "Sépia", "definition": """Nom masculin.
Du latin « sepia » qui signifie seiche.
1- En zoologie, liquide noirâtre sécrété par la seiche.
2- Matière colorante d’un brun très foncé (d’abord extraite du liquide
de la seiche), employée dans les dessins, les lavis.
En apposition, on dit: « De vieilles photos (couleur) sépia. »
Dessin ou lavis exécuté avec cette matière. Des sépias.""" },
{ "word": "Sépiolithe", "definition": """Nom féminin.
Du grec » sêpion » qui signifie os de seiche et « lithos » qui signie pierre.
En minéralogie, silicate hydraté naturel de magnésium.""" },
{ "word": "Séquoia", "definition": """Nom masculin.
Du latin « sequoia » issu du nom d’un célèbre chef indien « See-Quayah ».
Conifère, de la famille des taxodiacées, originaire de Californie,
remarquable par sa longévité et sa hauteur qui peut atteindre 150
mètres.""" },
{ "word": "Sérac", "definition": """Nom masculin.
Du savoyard « serai, serat » qui signifie fromage blanc et compact. Du
latin populaire « seraceum » et du latin classique « serum » qui
signifient petit-lait.
Dans un glacier, se dit d’un bloc de glace qui se forme aux ruptures
de pente, quand se produisent des crevasses transversales élargies par
la fusion.""" },
{ "word": "Serdeau", "definition": """Nom masculin.
Altération de sert d’eau, c’est à dire celui qui sert de l’eau.
Officier de bouche à la table du roi.""" },
{ "word": "Serendipité", "definition": """Nom féminin.
De l’anglais « serendipity » forgé par Horace Walpole à partir du mot
indien « serendip » d’aprés « Les trois contes de Serendip ».
Découverte ou invention faite de façon inattendue et par accident.
Souvent dans le cadre d’une rechjarche sur un autre sujet.
La découverte de L’Amérique par Christophe Collomb ou la découvert de
la pénicilline par Sir Alexander Flemming sont deux exemples de
serendipité.
Su le plan personnelle la sérendipité peut être une rencontre heureuse
permise par une ouverture d’esprit à l’inattendu.""" },
{ "word": "Séricigéne", "definition": """Adjectif.
Du grec ser : Ver à soie de Sêres:Les Sères peuple de l’ouest de la
Chine qui produisait de la soie.
Qui produit de la soie.
Par exemple: « Le bombyx du mûrier produit de la soie. »""" },
{ "word": "Séricine", "definition": """Nom féminin.
Du latin « sericus » issu du grec « serikos » de « sêr » qui signifie ver à
soie, de « Sêres » qui signifie les Sères, peuple de l’ousest de la
Chine qui produisait des vers à soie.
Scléroprotéïne de la soie.
Par exemple: « La séricine est une matière agglutinante qui retient les
filaments de la soie qu’elle colle entre eux.
Elle est détruite par un procédé spécifique nommé le décrusage. »""" },
{ "word": "Seringuero", "definition": """Nom masculin.
Du portugais « seringa » qui est le nom de certains hévéas.
Récolteur de caoutchouc par saignées des hévéas au Brésil.""" },
{ "word": "Shantung", "definition": """Nom masculin.
Du nom d’une province de Chine.
Tissu de soie irrégulier.""" },
{ "word": "Shibboleth", "definition": """Nom masculin.
Ce mot est un mot hébreu qui était employé dans la bible. Il signifie « épi » ou « branche » mais aussi « flot » ou « torrent ».
Un shibboleth est un mot ou un groupe de mots dont l’utilisation ou la prononciation correcte n’est possible que par les éléments d’une communauté ou d’un groupe. Il signe l’appartenance d’un individu à un catégorie quelle qu’elle soit. Il est un signe de reconnaissance verbal. Il peut aussi être un signe de reconnaissance symbolique.
Par exemple dans un article publié dans Le Monde des Dimanche 1er et lundi 2 septembre 2013  Mara Goyet  dans l’article qu’elle signe en page 17 (colonne 4, paragraphe 4) :
 « A Livre Couvert » écrit les phrases suivantes : « Ceux dont le livre ne l’est pas. [couvert]. Un shibboleth l’air de rien.»
Un autre exemple : le terme « Sésame ouvre-toi ! » est un shibboleth.""" },
{ "word": "Sicaire", "definition": """Nom masculin.
Du latin « sicarius » qui provient de « sica » qui signifie poignard.
Tueur à gages.""" },
{ "word": "Siccité", "definition": """Nom féminin.
Du latin « siccus » qui signifie sec.
Qualité de ce qui est sec.
Par exemple: »La siccité de l’air du Sahara. »""" },
{ "word": "Sidérolithique", "definition": """Adjectif.
Du grec « sidero » qui signifie fer et « lithos » qui signifie pierre.
En géologie, se dit de roches qui sont riches en concrétions ferrugineuses.""" },
{ "word": "Sigisbée", "definition": """Nom masculin.
De l’italien « cicisbeo » qui signifie galant.
Homme qui, dans la noblesse de l’Italie du XVIIIème siècle,
accompagnait officiellement et au grand jour une dame mariée avec un
autre homme.
C’était souvent un jeune homme, amant de cœur ou même amant, qui
accompagnait la femme dans des spectacles ou des dîners lorsque son
époux était absent.
La coutume posait un problème de fidélité et de filiation et a
contribué à donner une piètre image de la morale des italiens. Aussi,
dans la première moitié du XIXème siècle,
la pratique déjà en recul grâce aux idées de la Révolution française
fut condamnée et il y fut mis un terme par les patriotes de
Risorgimento.""" },
{ "word": "Sillet", "definition": """Nom masculin.
De l’italien « ciglietto » diminutif de « ciglio », issu du latin « cilium »
qui signifie cils.
En lutherie, petite pièce de bois collée sur le manche de certains
instruments à cordes, pour empêcher que les cordes n’appuient sur la
touche.""" },
{ "word": "Simagrée", "definition": """Nom féminin.
1) Employé de manière familière et au pluriel.
Attitudes, gestes ou paroles affectées qui sont utilisées
pour se donner certaines apparences, pour se faire valoir ou pour tromper.
Par exemple : « Cessez vos simagrées, essayez d’être franc pour une fois ! »
2) Dans un langage soutenu et au singulier.
Manière artificielle ou affectée.
Par exemple : « Cette cérémonie de remise de médaille a été une véritable simagrée. »
3) En particulier, sorte de parodie.
« Les dictateurs nous miment parfois la démocratie : c’est une simagrée. »""" },
{ "word": "Simarre", "definition": """Nom féminin.
De l’italien « zimarra » issu de l’espagnol « zamarra » qui signifie
vêtement de berger. Selon J.B.B de Roquefort ce mot viendrait d’un mot
turc signifiant « peau de martre » car souvent ce vêtement état doublé de fourrure.
1- Longue robe de femme ou d’homme faite d’une riche étoffe.
2- Vêtement de femme long et traînant.
3- Sorte de soutane que certains magistrats ou professeur d’université
portent par dessous leur robe.
4- Soutane d’intérieur.
5- Vêtement d’apparat porté par les sénateurs vénitiens aux XVI et
XVIIème siècle.
6- En poésie, manteau.""" },
{ "word": "Simonie", "definition": """Nom féminin.
Du latin simonia, du nom de Simon le Magicien.
Le nom Simon a deux étymologies:
1-Du grec « simôn » nom dérivé de « simos » qui signifie « qui a le nez camus ».
2-Nom masculin de l’hébreu « shimeone » qui signifie: « Dieu a entendu
ma souffrance ».
Péché dont l’origine vient de Simon le Magicien qui avait voulu
acheter à St Pierre le pouvoir de faire des miracles.
L’apôtre lui avait répondu: « Que ton argent périsse avec
toi, puisque tu as cru que le don de Dieu s’acquérait à prix d’argent. »
Volonté réfléchie d’acheter à un prix temporel une chose spirituelle.
Ce mot a été lu dans Le Monde du 10 septembre 2014, à propos du fait
que le pape nationalise la vente des bénédictions apostoliques jusqu’alors
dévolues à une cinquantaine de commerçants privilégiés du Vatican.
Je cite la phrase:«…il [le pape] évite à l’Eglise l’infâme
accusation de simonie. """ },
{ "word": "Sinople", "definition": """Nom masculin.
Depuis le XIVème siècle, ce mot signifie « vert » par une évolution
obscure puisqu’il est issu au XIIème siècle de « sinopre » qui
signifiait rouge, par le grec « sinôpis » qui signifiait terre rouge
de Sinôpe, port de Paphlagonie dont la terre était de couleur rouge.
On ignore pourquoi ce mot a désigné la couleur rouge avant de désigner
la couleur verte. Le changement brusque de sens pourrait provenir du
fait d’une confusion dans la langue orale avec le mot « vair ».
Couleur héraldique classée dans les émaux. Vert en représentation
polychrome, il est symbolisé par des hachures diagonales de gauche à
droite en représentation monochrome soit en gravure, architecture ou sceaux.
Pour désigner l’émail de couleur rouge on utilise le mot « gueules ».
Sinople est tombé en désuétude. Il existait pourtant un synonyme
ancien du mot vert qui était « prasine ».
Par exemple: « Le sinople est un émail peu employé dans les armoiries
occidentales parce qu’il vient d’Orient. »""" },
{ "word": "Sirocco", "definition": """Nom masculin.
De l’italien « scirocco » issu de l’arabe « sarqi » qui signifie vent
oriental. En marocain, c’est le « chergui ».
Vent de sud-est extrêmement chaud et sec. Il arrive du Sahara et
résulte des dépressions qui se forment sur la méditerranée.
On écrit aussi « scirocco ».
« Le Coup de Sirocco » est un film d’Alexandre Arcady.""" },
{ "word": "Situationnisme", "definition": """Nom masculin.
Du français « situation » issu du latin « situs » de même signification.
Mouvement politique littéraire et artistique, d’avant-garde, héritier
du surréalisme et du lettrisme, qui s’est manifesté
par des positions radicales lors des événements de mai 1968.
Guy Debord est un des fondateurs de ce mouvement.""" },
{ "word": "Smille", "definition": """Nom féminin.
Peut-être du latin « smila » issu du grec « smilé » qui signifie ciseau.
Vocabulaire technique. Marteau à deux pointes avec lequel le carrier
pique les moellons pour en régulariser les faces.""" },
{ "word": "Smorrebrod", "definition": """Nom masculin.
Du danois « smorrebrod » qui signifie littéralement pain beurré.
Chacun des petits canapés composés très diversement et qui peuvent
constituer un repas en Scandinavie.""" },
{ "word": "Sodoku", "definition": """Nom masculin.
Du japonais « so » qui signifie rat et « doku » qui signifie poison.
Maladie infectieuse due à un spirochète transmise par la morsure de
rongeurs notamment du rat.""" },
{ "word": "Solécisme", "definition": """Nom masculin.
Du grec « soloikismos » de Soloi « Soles » nom d’une ville de Cilicie dont les colons athéniens parlaient, dit-on, un grec très incorrect.
Emploi syntaxique fautif, de formes existant par ailleurs dans la langue.
Par exemple: « Je suis été en vacances. »""" },
{ "word": "Solénoïde", "definition": """Nom masculin.
Du grec « solên » qui signifie étui, tuyau et « eidês » de « eidos » qui
signifie aspect. Ce suffixe signifie le plus souvent semblable à.
En électricité, bobine cylindrique de révolution constituée par une ou
plusieurs couches de fil conducteur enroulé et traversé par un courant
qui crée sur son axe un champ magnétique qui lui est proportionnel.""" },
{ "word": "Solifluxion", "definition": """Nom féminin.
Du latin « solum » qui signifie sol et « fluctio » qui signifie écoulement.
En géologie, glissement de terrain qui se traduit par un lent
écoulement de boue.""" },
{ "word": "Solipsisme", "definition": """Nom masculin.
Du latin « solus »qui signifie seul et « ipse » qui signifie soi-même. 
Théorie selon laquelle le sujet, avec ses sentiments et ses
sensations, représente la seule réalité qui existe.""" },
{ "word": "Solmisation", "definition": """Nom féminin.
De solmiser, issu de sol et mi, notes de musique.
En musique ancienne, action de solfier dans le système de l’hexacorde,
avant l’emploi de la gamme actuelle""" },
{ "word": "Solutréeen", "definition": """Adjectif et nom masculin.
De « Solutré » ville de Bourgogne.
Relatif à une période du paléolithique récent et à la culture qui y correspond.
En tant qu’adjectif : « Une feuille de laurier solutréenne. »
En tant que nom masculin : « Le solutréen précède le magdalénien. « """ },
{ "word": "Sorite", "definition": """Nom masculin.
Du latin « sorites » et du grec « sôereitês », issu de « soros » qui signifie tas.
En logique, raisonnement composé d’une série de propositions agencées
de telle sorte que l’attribut de chacun devienne le sujet de la
suivante,
jusqu’à la dernière (conclusion) qui a pour sujet le sujet de la
première proposition , et pour attribut l’attribut de l’avant
dernière.
Par exemple, tout A est B, or tout B est C, or tout C est D, donc tout A est D.
« Le paradoxe de sorite »  est aussi appelé le paradoxe du tas. il
décrit un raisonnement qui conclut l’impossibilité de constituer un
tas, par exemple de sable, en accumulant un
grain après l’autre. Le paradoxe met en jeu un raisonnement par
récurrence tout en exploitant dans les assertions, le flou sémantique
qui entoure les mots du langage courant.""" },
{ "word": "Sosie", "definition": """Nom masculin.
De « Sosie » esclave d’Amphythrion dont Mercure prend l’aspect.
Personne qui a une parfaite ressemblance avec une autre.
Par exemple: Cette femme est le sosie de ta sœur.""" },
{ "word": "Sotch", "definition": """Nom masculin.
Mot régional issu d’un mot prélatin « tsotto » qui signifie trou, creux du sol.
En géologie, dans les Causses, grande dépression fermée.""" },
{ "word": "Sotériologie", "definition": """Nom féminin.
Du grec « sôterion » qui signifie salut issu de « sôter » qui signifie sauveur.
En religion, doctrine qui exprime l’existence d’un salut par un rédempteur.""" },
{ "word": "Souchet", "definition": """Nom masculin.
Du français « souche » à cause des rhizomes de la plante.
Plante herbacée de la famille des cypéracées poussant au bord de
l’eau. Le souchet comestible dit amande de terre permet de fabriquer
une boisson rafraichissante. C’est une spécialité espagnole de la région de Valence, l’horchata de chufa.""" },
{ "word": "Spalax", "definition": """Nom masculin.
Du même mot grec qui signifie taupe.
En zoologie, petit rongeur d’Europe centrale et orientale, sans queue,
à oreilles courtes et fourrure épaisse, appelé aussi rat-taupe.""" },
{ "word": "Spalter", "definition": """Verbe transitif.
De l’allemand « spalten » qui signifie fendre, crevasser.
Brosse de peintre en bâtiment qui est utilisée pour faire les faux bois.""" },
{ "word": "Sparterie", "definition": """Nom féminin.
De « sparte » issu du latin « spartum » qui est le nom d’un genêt d’Espagne.
Fabrication d’objets en fibres végétales, jonc, alfa ou crin, qui sont
vannées ou tissées.
Par exemple: »Des semelles d’espadrilles en sparterie. »""" },
{ "word": "Speakeasy", "definition": """Nom masculin.
Mot anglais de « speak » qui signifie parler et « easy » qui signifie doucement.
Local où l’on servait clandestinement des boissons alcoolisées, aux
Etats-Unis, pendant la prohibition.""" },
{ "word": "Spéléothème", "definition": """Nom masculin.
Du grec »spelaion » qui signifie caverne et « thema » qui signifie dépot.
Se dit de toutes les formations particulières qui peuvent se
développer au sein d’une grotte et qui sont dues à l’écoulement de
l’eau, comme les stalactites ou les stalagmites.""" },
{ "word": "Spéos", "definition": """Nom masculin.
Du grec « spéos » qui signifie caverne.
Temple d’Egypte creusé dans le roc.""" },
{ "word": "Spirochète", "definition": """Nom féminin.
Du grec « sperein » qui signifie spire et « khaitê » qui signifie longs
cheveux, crinière.
Micro-organisme à corps grêle et spiralé, mobile par des mouvements en vrille.""" },
{ "word": "Starets", "definition": """Nom masculin.
De « staretz », « starietz ». Mot russe qui signifie vieillard.
Dans l’ancienne Russie, saint moine, ermite ou pèlerin considéré comme
thaumaturge [qui fait des miracles] ou prophète. Il était souvent
choisi comme maître spirituel.
Par exemple: »Raspoutine était considéré comme un starets. »""" },
{ "word": "Stéatopyge", "definition": """Adjectif.
Du grec « stear, steatos » qui signifie graisse et « pugé » qui signifie fesses.
Se dit d’une personne dont le tissu adipeux est très développé au
niveau des fesses.
La Vénus hottentote est stéatopyge.""" },
{ "word": "Stéganographie", "definition": """Nom féminin.
Du grec « steganos » qui signifie étanche et « graphé » qui signifie écriture.
Art de faire passer inaperçu un message dans un autre message ou de
classer dans des fichiers qui n’ont rien à voir entre eux.
Par exemple, ranger son argent dans une boîte de sucre plutôt que dans
un coffre-fort.""" },
{ "word": "Stégomye", "definition": """Nom féminin.
Du latin « stegomyia » issu du grec « stegos » qui signifie toit et « muia »
qui signifie mouche, à cause de sa forme.
Moustique des régions chaudes qui transmet la fièvre jaune et la filariose.""" },
{ "word": "Stellionat", "definition": """Nom masculin.
Du latin « stellio » qui signifie lézard. Cet animal a été choisi pour
symbole de la fraude.
Action de vendre ou d’hypothéquer un immeuble dont on n’est pas le propriétaire.""" },
{ "word": "Stemmata", "definition": """Nom masculin pluriel.
Du latin « stemma » qui signifie couronne du grec « stephein » qui
signifie encercler.
En paléographie, arbres  généalogiques conservés dans des écrits.""" },
{ "word": "Sténopé", "definition": """Nom masculin.
Du grec « stenos » qui signifie étroit et « ôps » qui signifie œil.
Petit trou faisant office d’objectif photographique.""" },
{ "word": "Stentor", "definition": """Nom masculin.
Du nom d’un héros troyen à la voix puissante.
1- Une voix de stentor est une voix extrêmement  puissante et sonore.
Par exemple: « Il a une voix de stentor qui traverse les murs. »
2- Protozoaire d’eau douce, de l’embranchement des ciliés, en forme de
trompe ou de porte-voix.""" },
{ "word": "Stertoreux", "definition": """Adjectif.
Du latin « stertere » qui signifie ronfler.
En médecine une respiration stertoreuse est une respiration bruyante qui est accompagnée de ronflements.""" },
{ "word": "Sthène", "definition": """Nom masculin.
Du grec « sthenos » qui signifie force.
Ancienne unité du système M.T.S (mètre, tonne, seconde) qui a été
remplacée par le newton.""" },
{ "word": "Stichomythie", "definition": """Nom féminin.
Du grec « stikhos » qui signifie vers et « muthos » qui signifie fable.
Dialogue tragique dans lequel les interlocuteurs se répondent de façon
symétrique.
Par exemple vers pour vers ou quatrain pour quatrain.""" },
{ "word": "Stoïcien", "definition": """Nom masculin.
Du grec « stoikos » issu de « stoa » portique (du Pécile) lieu où enseignait Zénon.
Qui suit la doctrine de Zénon. Cette doctrine enseigne que le bonheur
réside dans la vertu et recommande l’indifférence devant ce qui
affecte la sensibilité.""" },
{ "word": "Stol", "definition": """Nom masculin.
Acronyme anglais de Short Taking-Off and Landing,
Avion susceptible de décoller ou d’atterrir sur une distance très courte.
Selon une recommandation officielle, l’acronyme français est « adac »:
Avion à Décollage et à Atterrissage Court.""" },
{ "word": "Stomoxe", "definition": """Nom masculin.
Du grec « stoma » qui signifie bouche et « oxus » qui signifie aigu.
Mouche piqueuse susceptible de transmettre le bacille du charbon.""" },
{ "word": "Strobile", "definition": """Nom masculin.
Du grec « strobilos » qui signifie toupie.
1- En botanique, c’est une formation compacte en forme d’épi ou de
cône chez les fougères, les conifères, le houblon.
2- En zoologie, ensemble des segments qui forment le corps du ténia.""" },
{ "word": "Stromatolithe", "definition": """Nom masculin.
Du grec « strôma, stromatos » qui signifie couche et « lithos qui signifie pierre.
Structure laminaire souvent calcaire qui se développe en milieu
aquatique peu profond marin ou d’eau douce. Cette roche est construite
par des bactéries. Elle est d’origine biogénique et organique.
Le stromatolithe n’est pas vivant seules les bactéries qui le constituent
le sont. Ils sont constitués par une structure en feuillet, alternant couche de
bactéries et couche sédimentaire.""" },
{ "word": "Stylite", "definition": """Nom masculin.
Du grec « stulitês » qui signifie colonne.
Solitaire qui vivait au sommet d’une colonne ou d’une tour.
Par exemple:  » Ce n’est pas parce que tu habites en haut d’un
gratte-ciel qu’il faut te prendre pour un stylite et rester seul! »""" },
{ "word": "Styrax", "definition": """Nom masculin.
Dans un premier temps c’est « storax »
Du grec « sturax » qui signifie arbre, baume.
1- Nom scientifique de l’aboulifier, arbre de la famille des
styracacées. Certaines espèces fournissent des baumes. On en tire le
benjoin.
2- Baume extrait des arbres du genre liquidambar et styrax.
Les styrènes, matières premières des plastiques, étaient extraits,
autrefois, du styrax.""" },
{ "word": "Stœchiométrie", "definition": """Nom féminin.
Du grec « stockéion » qui signifie éléments et « métros » qui signifie mesure.
Etude des proportions suivant lesquelles les corps chimiques
réagissent entre eux.""" },
{ "word": "Suburbicaire", "definition": """Adjectif.
Du latin « suburbicarius » issu de « Urbs » la Ville (de Rome).
Dans la religion catholique se dit de ce qui appartient aux sept
diocèses qui entourent Rome.
Par exemple: « Des évéques suburbicaires ».""" },
{ "word": "Succube", "definition": """Nom masculin ou féminin.
Du latin « succuba » qui signifie concubin; provient de sub qui signifie
« sous » et cubare qui signifie « coucher ».
Démon femelle qui abuse des hommes pendant leur sommeil.""" },
{ "word": "Succursale", "definition": """Adjectif et nom féminin.
Du latin « succursus » qui signifie secours, issu de « succurere » qui
signifie aider secourir.
1- Dans le domaine religieux, une église succursale est une église qui
supplée à l’insuffisance de l’église paroissiale.
2- Etablissement créé par une société ou une entreprise et qui est
autonome par rapport à cette société ou cette entreprise.""" },
{ "word": "Sybarite", "definition": """Nom et adjectif.
Du latin Subaritês: »Habitant de Sybaris. »vivant dans le luxe et la molesse.
Personne qui vit dans le luxe et la douceur.""" },
{ "word": "Sycophante", "definition": """Nom masculin.
Du grec « sûkon »qui signifie figue et « phainô » qui signifie découvrir.
Littéralement « celui qui dénonce les voleurs de figues ».
Dans la Grèce antique délateur professionnel qui dénonçait un suspect
devant le tribunal pour en tirer l’argent du paiement de l’amende.
L’expression liée aux figues est d’une origine obscure.
Deux explications possibles:
– Celui qui montrait les figues cachées par un voleur dans son vêtement.
– Celui qui dénonçait ceux qui volaient les figues dans les figuiers sacrés.
Aujourd’hui ce mot signifie délateur, puis par extension espion, fourbe.
Mot entendu sur France-Culture,le lundi 10 mars,
sur les Matins de Marc Voinchet dans la chronique de Philippe Meyer
à propos d’un article sur Wagner par Daniel Barenboïm dans Books
du mois de mars.""" },
{ "word": "Syli", "definition": """Nom masculin.
Du guinéen « soussou » qui signifie éléphant. Ce mot était utilisé
pendant la première république en Guinée comme second nom de l’ex-chef
d’état
Ahmed Sékou Toure pour le magnifier.
Devise officielle de la Guinée entre 1972 et 1986.
Par exemple: « Un syli est divisé en cent cauris. »""" },
{ "word": "Syllogomanie", "definition": """Nom féminin.
Du grec « syllogos » qui signifie rassemblement.
Tendance maniaque a accumuler de manière excessive des objets, souvent
sans les utiliser, indépendamment de leur utilité et de leur valeur.
Ce trouble pathologique fait partie des troubles mentaux et est
inscrit dans le manuel diagnostic des troubles mentaux ou DSM 5 de
2013.""" },
{ "word": "Sylphe", "definition": """Nom masculin.
Pour le dictionnaire Le Robert, ce mot est issu du latin des
inscriptions sylphus qui signifie génie mais qui aurait peut-être une
origine gauloise.
Pour le CNTRL, l’étymologie de ce mot est inconnue. Première
occurrence du mot par le latin sylphus chez Paracelse, vers 1529.
Mais l’ouvrage a d’abord été écrit en allemand.
On ne retient pas non plus l’origine allemande pour ce mot qui fut
diffusé par des textes latins au XVIIème siècle.
Pour le Wiktionnaire, sylphe serait issu du latin « silva » qui signifie
forêt. Le mot semblerait être un mot valise de sylva et de nymphe.
Cette dernière étymologie, qui n’est étayée par aucun texte ancien me
paraît être fantaisiste.
Génie de l’air dans les mythologies celtique, gauloise et germanique.
Dans « La Tempête » de Shakespeare, le sylphe se prénomme Ariel.""" },
{ "word": "Symbole", "definition": """Nom masculin.
Du latin « symbolus » signe de reconnaissance.
Dérive du grec « sumbolon » qui vient de « sumbalein » composé des radicaux « syn » qui
signifie avec et « ballein » qui signifie jeter, soit mettre ensemble, joindre.
A l’origine en Grèce ancienne, le sumbolon était un tesson de poterie
coupé en deux qui constituait un signe de reconnaissance lorsque les
porteurs pouvaient le réunir.
Au figuré, le symbole devient l’ensemble qui lie deux représentations
ayant la même signification.""" },
{ "word": "Symploque", "definition": """Nom féminin ou nom masculin.
Du grec « symplokê » qui signifie entrelacement, union.
En tant que nom féminin.
1- En rhétorique. Figure de style dans le langage oral ou écrit, où
les mêmes mots sont répétés en début de phrase et les mêmes autres
mots sont répétés en fin de phrase.
C’est-à-dire, emploi simultané de l’anaphore -mêmes mots répétés en
début de phrase- et de l’épiphore -mêmes mots répétés en fin de
phrase-. On peut schématiser ce processus de la manière suivante: A—–B / A—–B.
Par exemple:
« Bonjour, le ciel est bleu, parce que je t’aime.
 Bonjour, le soleil est brillant, parce que je t’aime.
 Bonjour, le temps est chaud, parce que je t’aime. »
2- En botanique. Algue, de l’ordre des Cyanophycées, forme des
filaments simples isolés ou groupés en faisceaux et recouverts d’une
mince gaine gélatineuse.
En tant que nom masculin.
En botanique, genre de styracées à feuilles alternes, aux fleurs
disposées en petites grappes latérales, et dont le fruit est une
drupe.
C’est une plante qui pousse dans les régions chaudes de l’Asie, de
l’Amérique et de l’Australie.
Par exemple: « Le symploque de Martinique est localement appelé le comat blanc. »""" },
{ "word": "Syncrétisme", "definition": """Nom masculin.
Du grec « sugkrétismos » qui signifie union des Crétois.
1- Combinaison cohérente, mélange de doctrines ou de systèmes.
2- Réunion de deux éléments culturels ou religieux.
3- Approche générale plus ou moins claire d’un tout.""" },
{ "word": "Synecdoque", "definition": """Nom féminin.
Du latin « synecdoche » par le grec « synekdokhé » qui signifie
compréhension simultanée. De « syn » qui signifie avec et « dekhomai » qui
signifie je reçois.
En rhétorique, figure de style par laquelle on fait entendre le plus
en disant le moins, ou le moins en disant le plus. On prend le genre
pour l’espèce ou l’espèce pour le genre.
On prend le tout par la partie ou la partie par le tout. C’est un cas
particulier de métonymie.
Par exemple on dit: « Le menu de ce restaurant est à 100 euros par
tête. » pour: « Le menu de ce restaurant est à 100 euros par personne. »
Il s’agit de prendre une partie du tout (les têtes) pour le tout
lui-même (les personnes).""" },
{ "word": "Syneisaktisme", "definition": """Nom masculin.
Du grec « sunessaktoi » qui signifiait compagne de l’ascète dans sa
pratique; issu d’un verbe grec qui signifie vivre avec quelqu’un.
En latin on disait : subintroductae ou mulierum consortia ou agapetae.
Dans une forme d’ascèse, de discipline spirituelle, cohabitation
chaste entre un homme et une femme. On dort « sous le même manteau » de
manière métaphorique ou littérale.
C’est un élément de mortification qui a pour but de surmonter les
tentations charnelles.
Cette attitude a été décrite chez les Pères du désert et dans le
monachisme celtique.
Robert d’Arbrissel fut la personnalité chrétienne la plus célèbre à
l’avoir pratiqué. Il en fut sévèrement critiqué par l’Eglise.""" },
{ "word": "Syntagme", "definition": """Nom masculin.
Du grec « syntagma » qui signifie régiment.
En grammaire c’est une unité située entre le mot et la phrase.
Ce mot est équivalent du mot groupe.
Par exemple « La fleur » est un syntagme ou groupe nominal.""" },
{ "word": "Syrinx", "definition": """Nom masculin.
Du grec « surigx » qui signifie tuyau.
1- En musique, flûte de pan.
2- En zoologie, larynx inférieur des oiseaux.""" },
{ "word": "Syrte", "definition": """Nom masculin.
Du grec « surtis » qui signifie sables mouvants, issu du verbe grec
surein qui signifie entraîner, balayer.
1- Dans une emploi vieilli et au pluriel, sables mouvants.
2- Région côtière sablonneuse; spécialement Golfe désertique. La
Grande et la Petite Syrte sont les golfes de Libye.
« Le Rivage des Syrtes » est un roman de Julien Gracq.""" },
{ "word": "Syzygie", "definition": """Nom féminin.
Du latin « syzygia » d’origine grecque qui signifie assemblage, réunion.
En astronomie, position de la Lune (ou par extension d’une planète) en
conjonction ou en opposition avec le Soleil. C’est la nouvelle lune ou
la pleine lune.
Une marée de syzygie est une marée qui a lieu pendant la pleine lune
ou la nouvelle lune.""" },
{ "word": "Tabard", "definition": """Nom masculin.
De « tabar » étymologie incertaine.
Au Moyen-Âge, manteau court, amples à manches formant ailerons et à
fentes latérales, qui était porté sur l’armure.""" },
{ "word": "Tabellion", "definition": """Nom masculin.
Du latin « tabellio » qui signifie qui écrit sur des tablettes.
1- Dans un sens vieilli, officier chargé de conserver les actes
rédigés par les notaires et d’en délivrer les grosses c’est à dire les
copies en gros caractères.
2- Dans une œuvre littéraire, en manière de plaisanterie, nom que l’on
donnait au notaire.""" },
{ "word": "Tachyphyllaxie", "definition": """Nom féminin.
Du grec « takhus » qui signifie rapide et « prophulassein » qui signifie
veiller sur.
Immunisation rapide contre une dose mortelle de poison par
administration préalable d’une dose non mortelle d’un même poison.""" },
{ "word": "Tagalog", "definition": """Nom masculin.
De « taga » qui signifie résident et « ilog » qui signifie fleuve. Tagalog
signifie les habitants du fleuve.
Dialecte du rameau des langues philippines de la branche
malayo-polynésienne des langues austronésiennes.
Il est principalement parlé en Asie du sud-est. C’est de facto
(c’est-à-dire de fait) et non de jure ( c’est à dire de droit)
la langue du filipino, langue officielle – avec l’anglais entre
autres- de la République des Philippines,
C’est une des 170 langues des Philippines et la plus parlée outre-mer.
Le tagalog comprend 22 millions de locuteurs comme première langue et
65 millions comme seconde langue.
Elle est classée 40 ème langue la plus parlée au nombre de locuteurs.""" },
{ "word": "Taleb", "definition": """Nom masculin.
De l’arabe « talib » qui signifie étudiant, candidat, demandeur, solliciteur.
Pluriels: Talebs. Taleban. Tolba.
1- Dans la religion musulmane, étudiant dans une université coranique,
souvent dans le but de devenir mollah.
Par exemple: »Sois patient, c’est un taleb. Il lui reste beaucoup à apprendre. »
2- Au Maghreb, nom donné à l’écrivain public.
Par exemple: « Va voir le taleb, il t’écrira ta lettre. »""" },
{ "word": "Taler", "definition": """Verbe transitif du premier groupe c’est à dire qu’il se conjugue comme chanter.
Du germain « talôn » qui signifie arracher. Il est passé en latin
« talare » qui signifie ravir, dérober puis dans les langues romanes
comme l’espagnol avec « talar » qui signifie dévaster ou
l’ancien provençal « talar » qui signifiait dévaster, endommager, détruire.
Taler arrive en français au XV ème siècle plutôt dans un dialecte de
l’est et du sud-est du domaine de la langue d’oïl.
A- Au sens propre, signifie marquer, meurtrir.
Verbe conjugué. Par exemple: « Au temps de l’esclavage, le fouet
tallait la peau des esclaves. »
Participe passé employé comme adjectif: Par exemple: « La peau des
esclaves, talée sur tout le corps.  »
En particulier. Concerne les fruits, et signifie les abîmer en leur
faisant subir des chocs. Par exemple: »Le transport a tallé ces pêches.
Elles seront difficilement mangeables. »
Participe passé employé comme adjectif. Par exemple: « Je ne peux pas
acheter ces abricots tallés. Ils ne sont pas assez présentables pour
mes invités. »
Dans une langue populaire, familière et ancienne, concerne un
châtiment corporel sur le derrière, les fesses. Par exemple: « Taler
les fesses d’un enfant est un châtiment corporel interdit dans de nombreux pays.
Ce mot est peu employé. »
B- Au sens figuré, signifie harceler, importuner.
Par exemple: « Sa conscience, ne le tallait plus. » Marcel Aymé""" },
{ "word": "Tantale", "definition": """Nom masculin.
Au XVIIème siècle, « celui qui a des désirs irréalisables ».
Du grec « tantalos » qui signifie Tantale, criminel, hôte des enfers.
1- En zoologie, oiseau échassier d’Amérique centrale proche de la cigogne.
2- En chimie, du latin « tantalus » par allusion à la difficulté d’en
préparer des composés.
Elément de numéro atomique 73. métal d’aspect analogue à l’argent ou
au platine, mais légèrement bleuté et d’une grande densité. Il est
très réfractaire.
Il accompagne le niobium et le vanadium dans ses minerais. Les
alliages et les aciers au tantale sont utilisés pour la fabrication
d’instruments chirurgicaux.""" },
{ "word": "Taphonomie", "definition": """Nom féminin.
Du grec « taphos » qui signifie enfouissement et « nomos » qui signifie loi.
Discipline de la paléontologie et de l’archéothanatologie qui étudie
la formation des gisements fossiles et tous les processus qui
interviennent depuis la mort jusqu’à la fossilisation d’un organisme.
Par exemple: « la taphonomie s’appuie sur l’écologie, la géochimie et
la sédimentologie. »""" },
{ "word": "Tapinois (en)", "definition": """Locution adverbiale.
Issu de l’ancienne locution « en tapin » qui signifiait en cachette du
verbe « se tapir ».
En se cachant, à la dérobée, avec dissimulation.
Par exemple: »L’enfant se tenait en tapinois derrière le buisson. »""" },
{ "word": "Tapioca", "definition": """Nom masculin.
Du portugais « tapiocha », issu du tupi-guarani « tipioca » qui vient de
« tipi » qui signifie résidu et « ok- » qui signifie presser.
Fécule amylacée extraite de la racine de manioc qui est cuite puis
concassée en flocons et séchée.
Note: Le tupi et le guarani sont deux langues des indiens du Brésil et
du Paraguay qui ont fourni de nombreux termes aux langues romanes que
sont le français, l’espagnol et le portugais.""" },
{ "word": "Tarasque", "definition": """Nom féminin. 
Du provençal « tarasco », nom de la ville de Tarascon.
1- Animal fabuleux, dragon des légendes provençales qui est parfois
promené dans certaines villes du Sud de la France.
Par extension monstre sculpté, sorte de gargouille.
2- Dans un sens figuré et littéraire. Danger fabuleux.""" },
{ "word": "Tarin", "definition": """1- Nom masculin.
L’origine de ce mot, serait peut-être l’onomatopée produite d’après le
chant de l’oiseau.
Petit chardonneret jaune, vert et noir qui vit surtout en Europe septentrionale.
2- Nom masculin.
Origine inconnue ou peut-être issu du sens précédent à cause du bec du chardonneret.
Nom familier donné a nez.""" },
{ "word": "Tarpan", "definition": """Nom masculin.
D’un mot kirghize.
Cheval retourné à l’état sauvage dans les steppes de l’Asie occidentale.""" },
{ "word": "Taurobole", "definition": """Nom masculin.
Du grec « taurobolos » qui signifie où l’on frappe le taureau.
Sacrifice dans les cultes de Cybèle et de Mythra, où le prêtre se
faisait arroser du sang d’un taureau égorgé.""" },
{ "word": "Tautologie", "definition": """Nom féminin.
Du grec « tautologia » issu de « tauto » qui signifie le même et de
« logos » qui signifie discours.
Répétition inutile d’une idée déjà formulée mais sous une forme différente
de la précédente.""" },
{ "word": "Taxinomie", "definition": """Nom féminin.
Du grec « taxis » qui signifie arrangement, ordre et « nemein » qui
signifie distribuer, administrer.
1- Principes d’une classification.
2- Classification d’éléments.""" },
{ "word": "Tchernoziom", "definition": """Nom masculin.
D’un mot russe qui signifie terre noire.
En géographie physique, type de sol que l’on rencontre en Russie et
qui est caractérisé par sa fertilité et par sa couleur noire.""" },
{ "word": "Tchitola", "definition": """Nom masculin.
Mot issu d’une langue africaine.
Bois de la famille des césalpinacées, originaire d’Afrique, résineux,
grossier et de couleur marron-rouge qui est utilisé en menuiserie.""" },
{ "word": "Teddy-Bear", "definition": """Nom masculin.
De l’anglais américain « Teddy » diminutif de Théodore Roosevelt
chasseur d’ours célèbre et « bear » qui signifie ours.
Anglicisme.
1- Dans un sens vieilli, ours en peluche ou en tissu synthétique
imitant la fourrure.
2- Fourrure synthétique imitant la peluche.""" },
{ "word": "Tégénaire", "definition": """Nom féminin.
Du latin teges, tegetis qui signifie couverture.
Araignée des maisons, qui tisse une toile irrégulière dans les angles
des murs et derrière les meubles.""" },
{ "word": "Teille", "definition": """Nom féminin.
Du latin ’tilia » qui signifie écorce de tilleul et pr extension « écorce ».
1- Liber du tilleul, dont on fait des cordes, des nattes.
2- Nom donné à l’écorce de la tige de chanvre.
Par exemple: « Une teille de bonne qualité, solide et souple à la fois. »""" },
{ "word": "Télamon", "definition": """Nom masculin.
Du latin « telamon » issu du grec « talân » qui signifie supporter.
En architecture, statue qui supporte une corniche, un entablement.""" },
{ "word": "Ténement", "definition": """Nom masculin.
Issu de « tenir ».
1- Au temps de la féodalité, se disait de la terre tenue d’un seigneur.
2- Dans une langue plutôt régionale, se dit de la réunion de deux
propriétés contiguës.
Par exemple: »Le mas de la famille X et le mas de la famille Y qui
étaient l’un à côté de l’autre ont été réunis par la famille Y après
rachat. Ces deux mas forment désormais un ténement. »""" },
{ "word": "Tenson", "definition": """Nom féminin.
Au milieu du XV ème siècle ce mot signifiait « querelle ». Du verbe
français « tancer » lui-même issu du latin « tentiare » par « tentus »
participe passé de « tendere » qui signifie tendre, combattre.
Genre poétique dialogué du Moyen-Âge, au sein duquel les protagonistes
s’opposent sur un sujet déterminé à l’avance.""" },
{ "word": "Tenuirostre", "definition": """Adjectif.
Du latin « tenuis » qui signifie fin et « rostrum » qui signifie bec, éperon.
En zoologie, se dit d’un oiseau qui a le bec fin.""" },
{ "word": "Térébenthine", "definition": """Nom féminin.
Du latin « terebinthina » (resina) résine de térébinthe
Huile essentielle résineuse (oléorésine) recueillie par incision ou
perforation de conifères ou de térébinthacées.
La térébenthine a de nombreuses origines.
Térébenthine de Bordeaux appelée aussi galipot ou poix de Bordeaux. On
la nomme aussi térébenthine officinale ou térébenthine du pin. Elle
est tirée du pin maritime.
Térébenthine de Venise ou de Briançon. Elle est tirée d’un mélèze:
larix decidua mais parfois aussi de certains pins.
Térébenthine de Chypre, de Chio ou de Hongrie. Elle est issue de la
sève du pistachier ou térébinthe. C’est un des constituants du
thériaque de la pharmacopée maritime du XVIII ème siècle.
Elle fut ensuite tirée du pin maritime, du pin des marais du pin
d’Alep et du pin ponderosa.
Térébenthine des Vosges ou d’Alsace. elle est tirée de l’épicéa commun.
Térébenthine du Canada ou baume du Canada. elle est tirée de l’abies balsymea.
Après distillation la térébenthine donne deux produits:
1- Un produit solide et inodore : la colophane.
2- Un produit liquide et odorant: l’essence de térébenthine.
La térébenthine est utilisée en pharmacie comme expectorant, baume,
antiseptique urinaire et pulmonaire avec l’eucalyptus et le benjoin
ainsi que révulsif.
Elle a servi aussi de carburant de fusées, lors de l’envoi du lanceur
Diamant Avecteur du premier satellite français Astérix.
.""" },
{ "word": "Térébrant", "definition": """Adjectif.
Du latin « terebrans » issu du verbe « terebrare » qui signifie percer
avec une tarière.
1- En zoologie, qualifie certains insectes ou certains mollusques qui
percent des trous ou forent des galeries.
2- En médecine, se dit de ce qui peut pénétrer profondément dans les
tissus, comme une ulcération.
Peut qualifier une douleur qui fait l’effet de la pénétration d’une
pointe dans la partie qui souffre.
Au sens figuré et littéraire, ce mot est synonyme d’aigu ou de douloureux.
Par exemple : La cupidité de cet individu est térébrante.""" },
{ "word": "Thalamus", "definition": """Nom masculin.
Du latin « thalami nervorum opticorum » qui signifie lits(couches) des
nerfs optiques, issu du grec « thalamos qui signifie lit.
En anatomie humaine, les deux gros noyaux sensitifs de substance grise
situés de part et d’autre du troisième ventricule cérébral, subdivisés
chacun en trois groupes de noyaux par une lame de substance blanche,
et jouant un rôle de relais pour les voies sensitives.""" },
{ "word": "Thalassotoque", "definition": """Adjectif.
Du grec « thalassa » qui signifie mer et « tokos » qui signifie frai.
En zoologie, un poisson thalassotoque, vit en eau douce et se reproduit en mer.
L’anguille est un thalassotoque.""" },
{ "word": "Thalweg", "definition": """Nom masculin.
De l’allemand « Tal » ou « Thal » qui signifie vallée et « weg » qui signifie chemin.
En géographie, ligne de fond d’une vallée.
Dans une vallée drainée, le thalweg est le lit du cours d’eau.
On peut aussi écrire « talweg ».""" },
{ "word": "Thaumaturge", "definition": """Nom masculin.
Du grec « thaumatourgos » qui signifie celui qui fait des tours
d’adresse puis à l’époque chrétienne faiseur de miracles. Issu de
« thauma » qui signifie dieu, prodige et « urgein » qui signifie produire, opérer.
Dans une langue littéraire, se dit de celui qui fait des miracles.
Par exemple: »Les candidats à la présidentielle ne sont pas des thaumaturges. »""" },
{ "word": "Thénar", "definition": """Nom masculin.
Du grec « thenar » qui signifie paume.
En anatomie humaine, le thénar ou l’éminence thénar, est la saillie
formée sur la paume de la main par les muscles courts du pouce.""" },
{ "word": "Théobromine", "definition": """Nom féminin.
De « theobroma cacao » nom scientifique du cacaoyer. Du grec « theos » qui signifie dieu et  « broma » qui signifie nourriture.
En biochimie, nom de l’alcaloïde principal du cacao. On le trouve aussi dans le thé, le café et aussi la noix de cola.
La théobromine est un diurétique, un cardiotonique et un vasodilatateur des coronaires. """ },
{ "word": "Théodolite", "definition": """Nom masculin.
Du latin « theodolitus » issu du grec « thea » qui signifie action de
regarder et « odelos » qui signifie circonférence. Ce mot a d’abord désigné un instrument d’arpentage.
Appareil qui consiste en un instrument de visée munie d’une lunette et
qui sert en géodésie à mesurer les angles horizontaux (ou azimuts), mais aussi les angles verticaux (ou sites) ainsi qu’à lever des plans.""" },
{ "word": "Thériaque", "definition": """Nom féminin.
Du latin « thériaca » qui signifie médicament contre les morsures
venimeuses. Lui même issu du grec « thériaké » qui vient de « thérion »
qui signifie bête sauvage.
Préparation pharmaceutique à consistance caractéristique, composée de
nombreux principes actifs dont l’opium, qui était employée comme
antidote aux morsures de serpents ou comme contre-poison.
Elle a été supprimée du Codex à la fin du XIXème siècle.""" },
{ "word": "Thesmophories", "definition": """Nom féminin.
Du grec « thesmophoros » qui signifie législateur, qui correspondait à
l’appellation de Démeter déesse de la terre et des boissons.
Dans la Grèce antique, fêtes en l’honneur de Démeter, célébrées par les femmes.""" },
{ "word": "Thibaude", "definition": """Nom féminin.
De « Thibaud » nom traditionnel du berger.
Molleton de tissu grossier ou de feutre que l’on met entre le sol et le tapis.""" },
{ "word": "Thixotrope", "definition": """Adjectif.
Du grec « thixis » qui signifie action de toucher et « tropéin » qui
signifie tourner.
En chimie se dit de gels qui se liquéfient par agitation et reprennent
leur état initiual au repos.""" },
{ "word": "Thixotrope", "definition": """Adjectif.
Du grec « thixis » qui signifie action de toucher et « tropos » qui
signifie tour, direction issu de « tropein » qui signifie tourner.
En chimie, se dit de gels qui se liquéfient par agitation et se
régénèrent (en gels) quand ils sont au repos.""" },
{ "word": "Thuriféraire", "definition": """Adjectif.
Du latin « t(h)urifer » littéralement qui porte « ferre », l’encens « tus, turis ».
1- Dans la liturgie, de différents cultes, se dit du porteur d’encensoir.
2- Au figuré et littéraire.
Se dit de celui qui encense, flatte ou loue.""" },
{ "word": "Tigrigna", "definition": """Nom masculin.
Le mot tire son origine de l’état régional du Tigray.
Langue éthiosémitique parlée au Nord-Est de la Corne de l’Afrique.
C’est la langue officielle de l’Érythrée et de l’Éthiopie, issue de
l’état régional du Tigray.
Cette langue compterait quinze millions de locuteurs.
Comme d’autres langues de la Corne de l’Afrique, le tigrigna s’écrit
au moyen de l’alphasyllabaire guèze.""" },
{ "word": "Tombola", "definition": """Nom féminin.
De l’italien « tombola » qui signifie culbute puis loto.
Loterie organisée par une société où chaque gagnant reçoit un lot en nature.""" },
{ "word": "Tombolo", "definition": """Nom masculin.
De l’italien « tombolo » qui signifie tumulus, tertre.
En géographie, cordon littoral constitué par une levée de sable ou de
galets qui relie une île au continent.""" },
{ "word": "Tonétique", "definition": """Nom féminin.
Du grec « tonos » qui signifie ton. Ce mot est calqué sur le mot phonétique.
Partie de la phonétique qui s’occupe de l’étude des tons.""" },
{ "word": "Tophus", "definition": """Nom masculin.
Au pluriel tophi.
Du latin « tophus » qui signifie tuf, c’est-à-dire roche très poreuse et
de faible densité, souvent pulvérulente.
En médecine, concrétion d’urate de sodium ou de calcium qui se forme
sous la peau des individus atteints de goutte, aux articulations
et parfois au pavillon de l’oreille.
Par exemple: « La présence de tophus peut aboutir à une destruction du
cartilage. »""" },
{ "word": "Toscan", "definition": """Adjectif et nom.
Du latin « tuscanus » qui signifie étrusque.
En tant qu’adjectif.
De la Toscane.
En architecture, l’ordre toscan est un des cinq ordres classiques.
C’est une forme simplifiée du dorique grec.
En tant que nom masculin
En linguistique, le toscan est un dialecte parlé à Florence et dans la
région de la Toscane. Ce parler est devenu la base essentielle de
l’italien.""" },
{ "word": "Touranien", "definition": """Adjectif.
Du persan « Turan » (opposé par Firdoussi à Iran). Terme vague désignant
les pays d’Asie centrale.
En linguistique, se disait autrefois, des langues ouralo-altaïques,
considérées comme les rameaux d’une même famille linguistique, mais
cette théorie a été abandonnée.""" },
{ "word": "Tourier", "definition": """Adjectif et nom.
Issu du mot « tour ».
Se dit du religieux ou de la religieuse non cloîtré qui est chargé de
faire passer au tour des choses apportées au couvent.
Par extension, ce dit de celui ou celle qui s’occupe des relations
avec l’extérieur.
Par exemple: »Un frère toutier. Une soeur tourière. »mais aussi « Une tourière. »""" },
{ "word": "Tourmaline", "definition": """Nom féminin.
Du cinghalais « turamalli » qui signifie pierre de couleur mélangée.
Groupe de minéraux de la famille des silicates. Silicate et borate
naturel d’alumine;
Ces pierres ont un éclat vitreux et des couleurs très variées, jaune,
noir, rose.
Par exemple: « La tourmaline est une pierre fine. »""" },
{ "word": "Tragus", "definition": """Nom masculin.
Latinisation du grec « tragos » qui signifie bouc.
En anatomie humaine, saillie aplatie triangulaire de la partie
antérieure de la conque de l’oreille, au-dessous de l’hélix.""" },
{ "word": "Triboulet", "definition": """Nom masculin.
De l’ancien provençal « tribolet » , issu de l’ancien français
« triboler » par le latin « tribulare » qui signifie agiter, secouer.
– En orfèvrerie, outil servant à arrondir.
– Tige graduée servant à mesurer le diamètre intérieur des bagues.""" },
{ "word": "Tricoises", "definition": """Nom féminin pluriel.
Altération de « tenailles turcoises » qui signifient « tenailles
turques ». A l’origine, « tenailles telles qu’en emploient les turcs ».
Dénomination dont la cause est inconnue.
1- Tenailles dont se servent les charpentiers, les menuisiers pour
arracher les clous ou les chevilles.
2- Tenailles de maréchal-ferrant, qui servent à ferrer et déferrer les chevaux.
3- Au singulier: Clé utilisée par les pompiers pour serrer ou
desserrer les raccords des tuyaux ou manœuvrer certains robinets.
4- En chirurgie. La tricoise de Velpeau, est une pince coupante en bout.
5- Dans le langage de la guerre: Machine de guerre utilisée jadis pour
démanteler certaines parties du rempart d’une place assiégée.""" },
{ "word": "Tridacne", "definition": """Nom masculin.
Du grec « tridaknos » qui signifie dont on ne peut pas faire moins de
trois bouchées.
Mollusque bivalve, géant des mers chaudes appelé aussi bénitier.
Par exemple: « Ce mollusque a aussi pour nom bénitier car une de ses
valves pourrait servir de bénitier. »""" },
{ "word": "Trirègne", "definition": """Nom masculin.
De l’italien « triregno » issu de « regno » qui signifie règne.
Tiare du Pape, ou triple couronne symbolisant les trois pouvoirs du
souverain, impérial, royal et sacerdotal.""" },
{ "word": "Triskéle", "definition": """Nom masculin.
Du latin « triscellum » qui signifie figure à trois côtés, triangle »
issu du grec « triskèles » de « tri » qui signifie trois et « skelos » qui
signifie jambe.
En numismatique et en archéologie, motif décoratif représentant trois
jambes repliées ou trois branches incurvées dans le même sens, qui
rayonnent au centre de la figure et qui sont souvent inscrites dans un
triangle équilatéral.""" },
{ "word": "Trochisque", "definition": """Nom masculin.
Du grec « trokhiskos » qui signifie petite roue, pastille.
En pharmacie. Terme vieilli. Médicament composé de substances sèches
pulvérisées et moulées en forme de cônes, destiné aux fumigations par
combustion ou incorporé dans un liquide approprié.
Par exemple; « Il existe plusieurs sortes de trochisques : Des
purgatifs, des fortifiants… »
On peut citer le trochisque alhandal, de l’arabe hadal qui signifie
coloquinte. C’était une des remèdes de la pharmacopée maritime
occidentale au XVIIIème siècle.
Il était préparé avec de la poudre de coloquinte et du mucilage. Il
soignait l’hydropisie, la léthargie…
En peinture dorure. Couleurs broyées puis séchées, qui se présentent
en petites unités de forme conique.""" },
{ "word": "Trope", "definition": """Nom masculin.
Du grec « tropos » qui signifie tour, manière.
Figure de style destinée à embellir un texte ou à le rendre plus
vivant et qui consiste à employer un mot pour une expression dans un
sens détourné de son sens propre.
Par exemple deux sortes de tropes:
1- Dans « Mon amoureux est un ange » il y a trope « in praesantia »; avec
une double indication de sens; l’amoureux et l’ange.
2- Dans « Tu es mon ange » il y a trope in absentia, le terme tropique
est seul à véhiculer l’information pertinente; l’ange.
La métaphore, la métonymie, l’hypallage sont des tropes.""" },
{ "word": "Truisme", "definition": """Nom masculin.
De l’anglais « truism » issu de « true » qui signifie vrai.
Se dit d’une vérité d’évidence et qui est si banale qu’elle ne vaut
même pas d’être prononcée.
Par exemple; »C’est un truisme de dire que Noël tombe le 25 décembre. »""" },
{ "word": "Turcique", "definition": """Adjectif.
Du latin « turcicus » qui signifie turc dans selle turque.
En anatomie humaine, dans la tête, la selle turcique est la face
supérieure du corps de l’os sphénoïde, en forme de selle, où est
située la glande hypophyse.""" },
{ "word": "Turquin", "definition": """Adjectif.
De l’italien « turchino » qui signifie « qui vient de Turquie » puis turquoise.
Couleur d’un bleu foncé.""" },
{ "word": "Tussah", "definition": """Nom masculin.
Mot anglais altération de « tussar » issu de l’hindoustani « tasar ».
Soie sauvage indienne produite par la chenille d’un lépidoptère, le
bombyx de l’ailante.
Le tussah est une soie légère à l’aspect scintillant.""" },
{ "word": "Tussor", "definition": """Nom masculin.
De l’anglais « tussore » issu l’hindoustan « tasar » par le sanskrit
« tasara, trasara » qui signifie navette, probablement à cause de la
forme de navette du ver à soie.
Étoffe légère de soie analogue au foulard.""" },
{ "word": "Tyrosémiophile", "definition": """Nom masculin.
Du grec « turos » qui signifie fromage, « sêmeïon » qui signifie signe et
« philein » qui signifie aimer.
Nom donné à un collectionneur d’étiquettes de fromages.""" },
{ "word": "Uchronie", "definition": """Nom féminin.
Mot formé du préfixe grec « u » qui est privatif et de « chronos » qui
signifie temps. Littéralement temps qui n’existe pas.
Réécriture de l’histoire à partir d’un évènement du passé.""" },
{ "word": "Uhlan", "definition": """Nom masculin.
Mot allemand issu du turc « oglan » par le polonais et qui signifie
jeune homme, garçon, valet.
Dans les anciennes armées allemandes, autrichiennes, polonaises et
russes, se disait du cavalier armé d’une lance ou lancier.
Par exemple: « Les premiers régiments de uhlans ont été créés au XVIIIème siècle.""" },
{ "word": "Unguis", "definition": """Nom masculin.
Du latin « unguis » qui signifie ongle.
En anatomie humaine, mince lamelle osseuse située à la partie
antérieure de la paroi interne de l’orbite (de l’œil).""" },
{ "word": "Urbicide", "definition": """Adjectif.
Du latin « urbs » qui signifie la ville et de « caedere » -qui donne le
suffixe- cide-  et signifie tuer.
Qualifie la destruction de la ville et plus généralement les violences
contre la ville qui peuvent y mener.
Ce terme a été utilisé de manière élargie en 1992 à propos de la
destruction de Mostar et des actes de violence contre les villes de
Bosnie.""" },
{ "word": "Urbicide", "definition": """Nom masculin.
Du latin « urbs » qui signifie ville et « occido » qui signifie tuer .
Désigne les violences qui visent à la destruction d’une ville non pas
en tant qu’objectif stratégique mais en tant qu’objectif identitaire.
Ce mot formé sur le mot génocide, fut « inventé » par Bogdan Bogdanovich
à la suite du siège de Sarajevo en 1994.""" },
{ "word": "Uræus", "definition": """Nom masculin.
Du grec « ouralos » qui signifie de la queue.
En archéologie, représentation du serpent naja dressé et portant sur
la tête un disque solaire qui est l’emblème des pharaons.""" },
{ "word": "Uxorilocal", "definition": """Adjectif.
Provient de l’anglais uxorilocal composé du latin uxor qui signifie
épouse et de l’anglais local.
Une société est dite uxorilocale lorsque le mari habite dans la maison
de son épouse.""" },
{ "word": "Valhalla", "definition": """Nom masculin.
Du vieux norois « valholl » lui-même issu de « valr » qui signifie
guerriers morts sur le champ de bataille et « holl » qui signifie la
halle ou le palais.
Dans la mythologie nordique, c’est le paradis viking au sein du
royaume des dieux. Les braves et valeureux guerriers morts sur les champs
de bataille sont choisis par les valkyries pour y être conduits.""" },
{ "word": "Vandale", "definition": """Nom.
Du latin « vandali » nom d’un peuple germanique.
1- Membre d’un peuple germanique, originaire de la région de l’Oder,
qui au Vème siècle envahit et dévasta la Gaule, l’Espagne du sud et
l’Afrique du nord.
Adjectif.
Un empire vandale.
2- Destructeur brutal, ignorant.""" },
{ "word": "Varech", "definition": """Nom masculin.
De l’ancien scandinave « Vàgrek » qui signifie épave. Au Moyen-Âge, le
varech désignait tout ce que rejetait la mer, poissons, baleines et
épaves de toutes sortes.
Ensemble des algues, de la famille des Phaeophyceae, ou algues brunes
laissées par le retrait des marées ou récoltées à marée basse sur le
rivage.
Le varech comprend les laminaires, les fucus, les ascophyllum.  Le
varech est appelé goémon en Bretagne et en Normandie. Il sert à
amender les terres sablonneuses. Il est utilisé comme litière.
Par combustion, il fournit de l’iode et de la soude.""" },
{ "word": "Vasistas", "definition": """Nom masculin.
De l’allemand « was ist das?  » qui signifie qu’est-ce que c’est?
question posée à travers un guichet.
Petit vantail mobile pouvant s’ouvrir dans une porte ou dans une fenêtre.""" },
{ "word": "Veld", "definition": """Nom masculin.
Du néerlandais « veldt » qui signifie champ, campagne.
En géographie, nom donné à la steppe de l’Afrique du Sud.
On écrit aussi « veldt ».""" },
{ "word": "Vènerie", "definition": """Nom féminin.
De « vener » qui signifie chasse à courre issu du latin « venor » qui
signifie chasser.
1- Art de la chasse à courre.
2- Administration des officiers de chasse.""" },
{ "word": "Ventis", "definition": """Nom masculin pluriel.
Vient du mot vent.
Arbres abbatus par le vent lors d’une tempête.""" },
{ "word": "Vénusté", "definition": """Nom féminin.
Du latin « venustas » issu de Vénus déesse de la beauté et de l’amour.
Dans une langue littéraire, grâce, beauté ou charme digne de Vénus.""" },
{ "word": "Vergeoise", "definition": """Nom féminin.
Vient du mot « verge » à cause des cerceaux de coudrier qui formaient le
moule dans lequel on coulait le sucre.
-Dans un sens vieilli: moule pour pain de sucre.
-Dans le sens moderne: sucre coloré à partir de betteraves.
La vergeoise blonde est un sirop cuit une fois.
La vergeoise brune est un sirop cuit deux fois.""" },
{ "word": "Vermouth", "definition": """Nom masculin.
De l’allemand « Wermut » qui signifie absinthe.
Apéritif à base de vin aromatisé de plantes amères et toniques
(absinthe, gentiane, écorces d’orange, quinquina et genièvre).""" },
{ "word": "Vernaculaire", "definition": """Adjectif.
Du latin « vernaculus » qui signifie indigène, domestique; issu du latin « verna »
qui signifie esclave né dans la maison.
Qui est propre au pays. Par exemple langue vernaculaire par opposition
à véhiculaire. Langue parlée au sein d’un groupe communautaire.
En sciences botanique ou zoologique, le nom vernaculaire est le nom
dans la langue courante. Par opposition au nom scientifique donné en
latin.
Ce mot a été entendu sur France Culture dans l’émission « Cultures d’Islam »
d’Abdelwahab Meddeb qui traitait du fonds photographique de « l’Ecole Biblique De
Jérusalem » le vendredi 21 février 2014.
Il se trouvait dans la phrase suivante:
« …petit sanctuaire d’architecture vernaculaire. »""" },
{ "word": "Vertex", "definition": """Nom masculin.
Du même mot en latin qui signifie sommet de la tête.
En anatomie, point le plus élevé sur la ligne médiane de la voûte du crâne.""" },
{ "word": "Vibice", "definition": """Nom féminin.
Du latin « vibices » pluriel de « vibex, vibecis » qui signifie meurtrissures.
En médecine.
1- Vergeture (rare au singulier).
2- Hémorragie cutanée formant des stries sur la peau.""" },
{ "word": "Vicariant", "definition": """Adjectif.
Du latin « vicarius » qui signifie suppléant.
Se dit de quelque chose qui remplace ou qui se substitue à autre chose.
En biologie, un hôte vicariant est l’hôte occasionnel d’un parasite
qui remplace l’hôte habituel.
En médecine, l’utilisation de ce terme est vieilli mais on parlait du
rôle vicariant d’un organe; celui-ci était capable de suppléer à un
autre organe devenu défaillant.
Par exemple un rein.""" },
{ "word": "Vicésimal", "definition": """Adjectif
Du latin « vicesimus » qui signifie vingtième.
En mathématique, système qui a pour base le nombre vingt.
Le nombre quatre-vingts est une trace de la numération vicésimale dans
notre numération décimale, c’est à dire en base dix.""" },
{ "word": "Virescence", "definition": """Nom féminin.
Du latin « virescere » qui signifie devenir vert.
En botanique, se dit d’un organe végétal qui verdit après avoir été
d’une autre couleur. Ce phénomène se produit après que la plante soit
infestée par un parasite qui provoque une présence anormale de chlorophylle.
Par exemple:  » La virescence des pétales de rose ».""" },
{ "word": "Voeu", "definition": """Nom masculin.
Du latin « votum » qui signifie vote.
Souhaits adressés à quelqu’un.""" },
{ "word": "Vogoul", "definition": """Nom masculin.
Nom donné par les russes au kanti, nom autochtone de cette langue.
Langue ougrienne parlée dans l’Oural.""" },
{ "word": "Voisement", "definition": """Nom masculin.
De « voisé » issu de voix par le latin « vox, vocis » de même signification.
En phonétique, résonance produite par la vibration des cordes vocales,
lors de l’articulation.
Par exemple: « Le voisement permet de distinguer les sons [b] et [p]. »""" },
{ "word": "Volapük", "definition": """Nom masculin.
De « vola » génitif de vol issu de l’anglais « world » qui signifie monde
et « pük » issu de l’anglais speak qui signifie parler.
Langue construite qui a été inventée par le prêtre catholique allemand
Johann martin Schleyer (1831-1879).
C’est une langue internationale comme l’espéranto.
Dans un sens péjoratif, c’est un mélange de langues.""" },
{ "word": "Volition", "definition": """Nom féminin.
Du radical du latin « voluntas » qui signifie volonté.
1- En psychologie se dit d’un acte de volonté. La volonté est
envisagée en tant que faculté.
2- En parapsychologie, exercice de la volonté dans une expérience paranormale.""" },
{ "word": "Volute", "definition": """Nom féminin.
Du latin « volutus » participe passé de « volvere » qui signifie rouler.
1- Ornement d’architecture, enroulement sculpté en spirale.
 – Partie ronde du bas d’un limon d’escalier sur laquelle repose le
pilastre de la rampe.
2- Forme enroulée en spirale ou en hélice.
Par exemple: »Les volutes bleues de la fumée d’une cigarette. »
3- En zoologie, mollusque gastéropode, de la famille des
prosobranches, à coquille ovoïde largement ouverte et terminée en
hélice qui vit dans les mers tropicales.""" },
{ "word": "Volvoce", "definition": """Nom masculin.
Du latin « volvox » qui signifie chenille.
En botanique, algue verte des eaux douces, qui vit en colonies.
On peut dire aussi « volvox ».""" },
{ "word": "Vulpin", "definition": """Adjectif.
Du latin « vulpinus » issu de « vulpes » qui signifie renard.
1- Qui vient du renard. Par exemple la rage vulpine.
2- En botanique, plante herbacée de la famille des graminées, à
panicules en forme de queue de renard, qui est cultivée comme
fourrage.""" },
{ "word": "Vultueux", "definition": """Adjectif.
Du latin « vultus » qui signifie mine, visage.
Se dit du visage lorsqu’il est congestionné, gonflé.""" },
{ "word": "Walé", "definition": """Nom masculin.
Mot issu d’une langue africaine.
Jeu africain qui consiste à faire passer des pions ( graines, cauris)
d’un trou à l’autre, selon des règles précises dans une table évidée
de douze trous.
La table de ce jeu.""" },
{ "word": "Walkyrie", "definition": """Nom féminin.
De l’ancien nordique « valkyrja », en allemand « walküre » de « wal » qui
signifie champ de bataille et « kirja » qui signifie celle qui choisit.
Dans la mythologie scandinave, c’est une des trois déesses guerrières
qui décident du sort des combats et de ceux qui doivent mourir.
La Walkyrie est un opéra de Richard Wagner.
En manière de plaisanterie, une walkyrie est une femme plantureuse et solide.""" },
{ "word": "Wanderer", "definition": """Mot anglais qui s’emploie en français au masculin ou au féminin.
De l’anglais « to wander » qui signifie errer, flâner,
lui-même issu de « wand » dont l’étymologie est obscure et qui a signifié d’abord muraille d’osier, puis tissu, puis toile.
Vagabond. Flâneur.
Wanderer s’emploie quelquefois en français. Par exemple, cette phrase lue dans
« Le Monde » du 8 Août 2014, dans la notice nécrologique de Jacques Merlet,
producteur de radio à France Culture et à France Musique disparu le 2 août 2014 :
« …avec le concours de ses réalisateurs qui suivaient à grands pas
cet infatigable et imprévisible wanderer sur les routes de France et de Navarre. »
Wanderer est un poème anglo-saxon du Xème siècle. 
Der Wanderer est le Lied (chant) opus 4 numéro 1 D493 de Franz Schubert. 
De nos jours, le Trio Wanderer est une formation de musique de chambre. """ },
{ "word": "Wassingue", "definition": """Nom féminin.
Mot flamand d’origine germanique. De l’allemand « waschen » qui signifie « laver ».
Dans le nord de la France, terme qui désigne une toile à laver, une serpillière.""" },
{ "word": "Wombat", "definition": """Nom masculin.
Mot anglais emprunté à une langue australienne.
Marsupial d’Australie qui vit dans les forêts montagneuses où il
creuse de vastes terriers. Il ressemble à un gros ourson et appartient
à la famille des vombatidés.
Il est également appelé « phascolome ».
Par exemple: »Le wombat est un herbivore qui creuse des terriers comme
le blaireau. » Jules  Verne""" },
{ "word": "Xélénasie", "definition": """Nom féminin.
Du grec « xelênasia » issu de « xenos » qui signifie étranger et
« elaunein » qui soignifie chasser.
Droit pour un état belligérant d’expulser les membres du peuple ennemi.""" },
{ "word": "Xylostomiase", "definition": """Nom féminin.
Du grec « xulo » , de « zulon » qui signifie bois et du grec « stoma » qui
signifie bouche.
Nom savant de la « gueule de bois ». Ce terme est plutôt employé au Québec ou
en Belgique.""" },
{ "word": "Yet", "definition": """Nom masculin.
Du wolof. l’étymologie est manquante.
Mollusque gastéropode marin africain du genre « Cymbium ». Spécialement
« Cymbium sengalensis »
Il est collectionné mais aussi apprécié dans la cuisine sénégalaise.
Par exemple: « Le yet vit dans les zones aquatiques riches en racines
de mangrove. »""" },
{ "word": "Yeuse", "definition": """Nom féminin.
De l’occitan « euse » issu du latin « quercus ilex » qui signifie chêne vert.
Chêne vert.
Par exemple: »La colline était recouverte de grandes yeuses crêpues.  »
Jean Giono""" },
{ "word": "Ysopet", "definition": """Nom masculin.
Du nom de Esope fabuliste grec VII-VI ème siècle avant J.-C.
Nom donné au Moyen-Âge à un recueil de fables.""" },
{ "word": "Zénana", "definition": """Nom masculin.
De l’hindi « zânane » issu du persan « zanân » qui signifie femmes.
1- Nom donné à l’appartement des femmes chez les musulmans de l’Inde.
Correspond au mot « harem » utilisé dans d’autres pays.
2- Etoffe cloquée employée pour les vêtements d’intérieur; a été
nommée ainsi en référence à l’intimité du harem.""" },
{ "word": "Zététique", "definition": """Adjectif.
Du grec « zêtêticos » de « zêtein » qui signifie chercher.
En philosophie, comme le scepticisme de l’Ecole de Pyrrhon, au IIIème
siècle avant notre ère, c’est le refus de toute affirmation
dogmatique. Mais c’est aussi le doute et la recherche d’une explication
rationnelle à des phénomènes inexpliqués.
Plus largement c’est le doute cartésien en sciences et en philosophie.""" },
{ "word": "Zeugma", "definition": """Nom masculin.
On peut dire aussi zeugme
Du grec « zeugma » qui signifie lien.
C’est une construction qui consiste à ne pas répéter un ou plusieurs
mots déjà présents dans une phrase voisine quand l’esprit peut les
rétablir sans difficulté.
Par exemple: « Louis a fait son problème de maths et Jean sa dictée. »""" },
{ "word": "Zinzinuler", "definition": """Verbe intransitif.
Se dit de la mésange, de la fauvette qui pousse son cri.
Par exemple: »Cette mésange zinzinule en haut du figuier depuis l’aube. »""" },
{ "word": "Zinzolin", "definition": """Nom masculin.
De l’italien « zuzulino », provenant de l’arabe d’Espagne « djoudjolân » qui
signifie semence de sésame.
Couleur d’un violet rougeâtre que l’on obtient du sésame.""" },
{ "word": "Zizanie", "definition": """Nom féminin.
Du latin « zizania » qui signifie ivraie. Issu du sumérien » zizan » qui
signifie blé.
1- Dans un sens vieilli. Nom donné à l’ivraie enivrante « Iolium
temlentum » et nom donné à la mauvaise graine qui pousse parmi le bon
grain.
2- Au figuré. Désunion, discorde.
Par exemple. »A force de vous disputer, vous semez la zizanie. »
3- Plante herbacée de la famille des poacées (graminées), très proche du riz.""" },
{ "word": "Zoé", "definition": """Nom féminin.
Du grec « zôé » qui signifie vie.
Forme larvaire des crustacées décapodes qui succède au stade nauplius.""" },
{ "word": "Zooglée", "definition": """Nom féminin.
Du latin « zooglea » issu de « zôon » qui signifie être vivant, animal et
« glotos » qui signifie glu.
En sciences naturelles. masse mucilagineuse en forme de voile,
constituée de bactéries agglutinées.
Aujourd’hui, on utilise plutôt le mot « biofilm ».
Par exemple: « On rencontre des zooglées ou des biofilms sur la paroi
interne des canalisations d’eau. »""" },
]

class RandomWordFr(object):
	"""
	{'word': str, 'definition': str}
	"""

	def __init__(self):
		self.data = data

	def __str__(self):
		w = self.__get_word()
		return "# %s\n%s" % (w['word'], w['definition'])

	def __get_word(self):
		return self.data[randint(0, len(self.data) - 1)]

	def get(self):
		return self.__get_word()
