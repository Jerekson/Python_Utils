from scapy.all import *
import socket

def trames():
    # Créer uniquement quelques trames du paquet. 
    p = IP()
    p.show() # permettra d'afficher les valeurs par défaut suivant 
    """
    ###[ IP ]### 
        version   = 4
        ihl       = None
        tos       = 0x0
        len       = None
        id        = 1
        flags     = 
        frag      = 0
        ttl       = 64
        proto     = hopopt
        chksum    = None
        src       = 127.0.0.1
        dst       = 127.0.0.1
        \options   \
    """
    # Chacun de ces attributs peuvent être modifié en pointant dessus
    p.ttl = 22
    p.show()

    ethernet = Ether()
    ethernet.dst = "00:19:4b:10:38:79"
    ethernet.show()

    ping = ICMP()
    ping.show()

    frame = ethernet / p / ping
    frame.show()

    # envoie des paquets
    sendp(ethernet)
    # En l'état, rien n'est vraiment envoyé 
 
def encapsulation():
    # En recréant une frame en précisant simplement l'adresse IP du 
    # destinataire, Scapy a compris tout seul qu'il devait modifier 
    # les attributs dst, src et type de Ether() ainsi que l'adresse 
    # IP de l'émetteur (src dans IP()) ! C'est très pratique, 
    # mais évidemment nous aurions pu forcer Scapy à mettre 
    # les valeurs que l'on voulait.

    frame = Ether() / IP(dst="192.168.1.254") / ICMP() 
    # ping vers le routeur

    frame.show()

def encapsulation_2():
    # Comme la fonction "encapsulation" pour vérifier que tout s'adapte
    e = Ether()
    e.show()

    p = IP()
    p.dst="192.168.1.254"

    d = ICMP()

    f = e / p / d
    f.show()
    # De cette façon là, les éléments Ether peuvent aussi s'adapter
    # en fonction de l'ip de destination
    sendp(f)

def send_frame(ip):
    # envoie complet du paquet

    # creation d'un paquet ping vers mon routeur
    ping = Ether() / IP(dst="192.168.1.254") / ICMP()

    # Envoie du paquuet (simple)
    sendp(ping)

    #### SRP()
    print("\n\nSRP test")
    # srp() renvoie deux objets : le premier contient les paquets 
    # émis et leurs réponses associées, l'autre contient les 
    # paquets sans réponse.
    rep, non_rep = srp(ping)
    print("\nrep & non_rep printed : \n", 
          rep, "\n", non_rep)

    print("\necho request response :")
    rep.show()
    # Bien recu un paquet ICMP echo reply

    print("\nAfficher les différents tuples", rep[0])

    print("\nPour afficher le paquet envoyé :")
    rep[0][0].show()

    print("\nPour afficher le paquet de réponse :")
    rep[0][1].show()

    #### SRP1()
    print("\n\nSRP1 test")
    # Pour simplifier tout cela, peut préférer la fonction 
    # srp1(). 
    # Cette fonction renvoie renvoie un seul objet : 
    # la première réponse
    rep = srp1(ping)
    rep.show()

    #### hote inexistant
    # On peut ajouter un petit timeout pour que la requête s'arrête 
    # plus vite lors d'un hote inexistant
    print("\n\n")
    ping2 = Ether() / IP(dst="192.168.1.134") / ICMP()
    rep = sr1(ping2, timeout=0.5)


def scan_plage_ip_sr():
    base_ip = "192.168.1."
    start = 90
    count = 10
    ip_list = [f"{base_ip}{i}" for i in range(start, start + count)]
    print(f"scan adresses between {base_ip}{start} and {base_ip}{(start + count - 1)}")
    # Ici, l'utilisation de sr (sans le p) pour ne pas avoir
    # à renseigner l'Ether()
    rep, non_rep = sr(IP(dst=ip_list) / ICMP(), timeout=2, verbose=0, retry=2) 
    # Pas d'Ether() sur un page d'adresse
    # scapy va gérer la couche 2 dynamiquement
    
    print(rep)
    print(non_rep)
    for send_packet, received_packet in rep:
        print(received_packet[IP].src)
    for sent_packet in non_rep:
        print(sent_packet[IP].dst)

def scan_plage_ip_sr1():
    #TODO faire en sorte que la la requete se fasse sur sr1
    # qui est plus fiable. 
    # La boucle serait faite manuellement. 
    # S'agissant de sr1, on peut maintenant ajouter la couche 2 Ether()
    # TODO : tenter aussi le multithreading pour accélerer un peu la requête.
    # -> from concurrent.futures import ThreadPoolExecutor
    pass

def simple_ping(ip):
    rep, non_rep = srp(Ether() / IP(dst=ip) / ICMP(), timeout=2)
    for send_packet, received_packet in rep:
        print(received_packet[IP].src)
        print(received_packet[Ether].src)
        print(socket.gethostbyaddr(ip)[0])


def scan_port():
    # si dport=[82, 85] alors 2 paquets envoyé, 1 pour chaque port
    # si dport=(82, 85) alors 3 paquets envoyé, 1 pour chaque port entre ceux deux entrées
    frame = IP(dst="192.168.1.254") / TCP(sport=12345, dport=[80, 443, 283], flags="S")
    rep, non_rep = sr(frame)
    rep.show()

def traceroute():
    rep, non_rep = sr( IP(dst="209.85.143.100", ttl=(1,25)) / TCP(), timeout=1)
    for sent_packet, received_packet in rep:
        print(sent_packet.ttl, received_packet.src)

def sniff_function():
    """
        sniff(filter="", count=0, prn=None, lfilter=None, timeout=None, iface=All)
    Elle renvoie une liste de paquets (en comparaison, sr() renvoie deux listes de paquets).
    Ses paramètres sont :
     -count : nombre de paquets à capturer. 0 : pas de limite.
     -timeout : stoppe le sniff après un temps donné.
     -iface : désigne l'interface sur laquelle sniffer. La liste de vos interfaces est donnée par la commande ifconfig.
     -filter : filtre les paquets à garder d'après une chaîne de caractère.
        Exemple : filter="port 80" filtre les paquets ayant un lien avec le port 80.
     -lfilter : même chose, mais utilise une fonction plutôt qu'une chaîne.
        Exemple : lfilter=lambda x: x[1].src=='192.168.1.14' filtre les paquets émis par 192.168.1.14.
     -prn :fonction à appliquer à chaque paquet. Si la fonction retourne quelque chose, cela s'affiche.
        Exemple : prn = lambda x: x.show() va afficher le détail de chaque paquet.
    """
    rep = sniff(filter="host 192.168.1.254") # Mettre la cible
    rep.show()
    # stoper le script pour voir la show ou 
    # A réaliser directement dans un scapy via le terminal, suivre la dernière source pour plus d'infos

# trames()
# encapsulation()
# encapsulation_2()
# send_frame()
# scan_plage_ip_sr()
# simple_ping("192.168.1.96")
# scan_port()
# traceroute()
sniff_function()

"""
Sources:
- https://lipn.univ-paris13.fr/~evangelista/cours/SAE24/tp.pdf
- http://sdz.tdct.org/sdz/manipulez-les-paquets-reseau-avec-scapy.html
"""