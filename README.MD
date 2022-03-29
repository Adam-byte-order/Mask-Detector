------------------------------------------------VC2020-2021---------------------------------------------

# Mask Detector and UnMask
* Adam Lemkhanter Boubri
* Gerard Martínez Espelleta

Avui en dia la situació sanitària actual, recomana i en alguns països obliga a portar una mascareta, per així evitar els contagis per la COVID-19. 
Tenint en compte això, i els avenços que s'han produït en els darrers anys dins l'àmbit de la intel·ligència artificial, hem volgut crear un detector de mascaretes mitjançant una xarxa neuronal convolucional amb la qual hem obtingut uns resultats bastant sorprenents. 
Seguidament hem decidir implementar que a la vegada que es detectés si una persona porta mascareta o no, en cas portar-la, fer una reconstrucció facial de com es veuria aquesta persona sense la mascareta. Aquesta segona fase del projecte s'ha portat a terme utilitzant una xarxa neuronal U-net.

## Organització
De la mateixa manera que el projecte, el nostre repositori està dividit en tres apartats:

1. [Creació de dataset](https://github.com/gerard08/ProjecteVC/tree/master/creaBBDD)
2. [Detecció de mascaretes](https://github.com/gerard08/ProjecteVC/blob/master/CNNMaskDetector.ipynb)
3. [Intents d'eliminació de mascareta](https://github.com/gerard08/ProjecteVC/tree/master/intentsRetiraMascareta)


## Base de Dades
La base de dades utilitzada és la de [Human Faces](https://www.kaggle.com/ashwingupta3012/human-faces), però es pot trobar ja amb les imatges classificades i amb mascaretes afegides a [Google Drive](https://drive.google.com/file/d/1t1eK2lUK97uGiZUHOwGtylMSetWuaR9c/view?usp=sharing). 
Aquesta inclou dues carpetes, una on hi trobarem les imatges amb mascareta i una altra on hi trobarem les que no en tenen. De la mateixa manera dins de cada una d'aquestes carpetes hi trobarem tres carpetes, que ens facilitaràn la divisió train, test i validation.


