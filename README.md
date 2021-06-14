![Python 2.7](https://img.shields.io/badge/python-2.7%2B-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# cisco_switches_automation
Ce script assiste l'administrateur réseau dans l'automatisation de la configuration des commutateurs (switchs) Cisco.

Représentation de l'infrastructure :

![p6 aic](https://user-images.githubusercontent.com/46109209/121824670-6b79ac80-cc9d-11eb-8a6d-826758fb2fbf.png)


## Compatibilité
 - :white_check_mark:CISCO IOS vL2 15.2


## Pré-requis
Vous aurez besoin d'un accès Telnet sur les cibles, ainsi que d'un même "Username" sur chacun d'entre eux.

## Installation

apt install python

Rendre le script exécutable avec la commande : " sudo chmod +x ./python-p6aic-switch_v5.py "

La commande suivante, lancez le script : " sudo ./python-p6aic-switch_v5.py "

## Configuration
Vous devez renseigner l'username dans la variable "Username" du fichier python-p6aic-switch_v5.py :

Durant son exécution, le script fera appel au données des fichiers :

dns_server
domain_name
switches_list
vlans_allowed_trunk
vlans_dhcp_excluded_addr
vlans_dhcp_pool_network
vlans_interfaces
vlans_ip_addr
vlans_name
vlans_number
vlans_trunk_interfaces

Exemple de contenu du fichier : 'switches_list' : (il s'agit des adresses IP des équipements à configurer)

192.168.122.61

192.168.122.62

192.168.122.63

Renseignez également les différents fichiers d'inputs en cohérence avec vos besoins et votre organisation.

## Quelques exemples:

Réalisations de l'exécution des commandes du script :

![1](https://user-images.githubusercontent.com/46109209/121824257-5ea78980-cc9a-11eb-9328-0e8ba02b506b.png)

![2](https://user-images.githubusercontent.com/46109209/121824258-60714d00-cc9a-11eb-9171-a8dfeee2f143.png)

![3](https://user-images.githubusercontent.com/46109209/121824262-65ce9780-cc9a-11eb-9f7a-69bd6821c04c.png)

![4](https://user-images.githubusercontent.com/46109209/121824264-69621e80-cc9a-11eb-8200-03c176a453a9.png)

![5](https://user-images.githubusercontent.com/46109209/121824265-6c5d0f00-cc9a-11eb-931a-eced5a922a14.png)

![6](https://user-images.githubusercontent.com/46109209/121824266-6f57ff80-cc9a-11eb-9017-893222389c5d.png)

![7](https://user-images.githubusercontent.com/46109209/121824269-741cb380-cc9a-11eb-94b8-b8a8ea216874.png)


Activités sur le switch:

![a](https://user-images.githubusercontent.com/46109209/121824446-c90cf980-cc9b-11eb-8bfa-50b8ad4081cf.png)

![b](https://user-images.githubusercontent.com/46109209/121824452-cf9b7100-cc9b-11eb-90d0-1fc2d397f42d.png)

![c](https://user-images.githubusercontent.com/46109209/121824456-d32ef800-cc9b-11eb-97af-05fbabbab5ef.png)

![d](https://user-images.githubusercontent.com/46109209/121824459-d629e880-cc9b-11eb-919e-e9679b0b1af9.png)

![e](https://user-images.githubusercontent.com/46109209/121824464-d9bd6f80-cc9b-11eb-8238-2be5fb0d64d9.png)

Acquisition de l'adressage IP par DHCP des ordinateurs connectés aux interfaces des vlans: 

![f](https://user-images.githubusercontent.com/46109209/121824467-dcb86000-cc9b-11eb-8900-ad153580656b.png)

![g](https://user-images.githubusercontent.com/46109209/121824470-dfb35080-cc9b-11eb-847a-c171425353fa.png)

