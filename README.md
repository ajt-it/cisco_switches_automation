# cisco_switches_automation
Ce script sert assister l'administrateur réseau dans l'automatisation de certaines tâches répétitives de configuration des switches Cisco.

Représentation ifrastructure :

![vb](https://user-images.githubusercontent.com/46109209/119550405-ea0eb880-bd87-11eb-9734-9a9c8991fcd5.png)


## Pré-requis
Vous aurez besoin d'un accès Telnet sur les cibles, ainsi que d'un même "Username" sur chacun d'entre eux.

## Installation
apt install python
chmod +xpython-p6aic-switch.py

## Configuration
Vous devez renseigner l'username dans la variable "Username" du fichier python-p6aic-switch.py :

Durant son exécution, le script fera appel au données des fichiers :

switches_list
vlans_allowed_trunk
vlans_interfaces
vlans_number
vlans_trunk_interfaces

Exemple de contenu du fichier : 'switches_list' : (il s'agit des adresses IP des équipements à configurer)

192.168.122.61
192.168.122.62
192.168.122.63

Le script demandera que vous renseigniez le nom (description) de vos vlans.
Il s'agit de renseigner ces éléments en cohérence avec vos desoins.

## Quelques exemples:

Réalisations de l'exécution des commandes du script :

![2](https://user-images.githubusercontent.com/46109209/119551874-a157ff00-bd89-11eb-90da-7efa22b93975.png)

Activités sur le switch:

![5](https://user-images.githubusercontent.com/46109209/119552283-0c093a80-bd8a-11eb-8395-dc9463e83520.png)

Vérification de creation des vlans:

![7](https://user-images.githubusercontent.com/46109209/119553256-ff391680-bd8a-11eb-8536-954878c73eb3.png)

## Licence
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
