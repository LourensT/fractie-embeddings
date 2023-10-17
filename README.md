# Moties

Moties en stemgedrag van fracties van Tweede Kamer. Data via `tkapi`, de python interface van de [Tweede Kamer API](https://www.tweedekamer.nl/kamerstukken/open_data).



### installation (linux, python 3.8)

create a virtual environment and install the requirements

    virtualenv -p python3 env
    
    source env/bin/activate

    pip install -r requirements.txt

## Politiek Kompas
Politiek kompas op basis van 1316 moties van januari 2022 tm oktober 2023 (Rutte IV). De x-as is het eerste PCA component, de y-as het tweede. PCA is een statistieke methode om de dimensies van een dataset te reduceren. In dit geval was de dimensie eerst 1316 (voor elke motie heeft een fractie een stem uitgebracht), na PCA is de dimensie 2. Er zit dus **geen** waardeoordeel in de x en y as, het is een statistische representatie van de data.
![Politiek compass](./plots/compass.png)**Observaties**
* De ratio van verklaarde spreiding is voor PCA1 en PCA2 respectievelijk 0.33 en 0.19. 
* Dat PCA1 (de x-as, die de meeste spreiding in data verklaart) overeenkomt met de algemene opvatting van links en rechts, geeft dus een bevestiging dat dit een zinnige opdeling is.
* De y-as lijkt coalitie/oppositie te volgen. Hoe lager op de y-as, hoe meer een fractie tegen de coalitie in stemt.
* GroenLinks en PvdA liggen praktisch op elkaar. Niet gek, aangezien de partijen vrijwel altijd samen stemmen. Die zouden eens moeten fuseren. 

**Valkuilen**
* Bij een dimensie-reductie van 1316 -> 2 gaat er veel nuance verloren. Specifieke onderwerpen die niet vaak aan bod komen hebben weinig invloed op de positie van een fractie in dit kompas. 
* Ik heb eerlijk gezegd geen idee of ik alle moties heb, of dat ik juist stemmingen heb meegenomen die geen moties zijn.
* Niet alle fracties bestaan evenlang. Bijv. ephraim 