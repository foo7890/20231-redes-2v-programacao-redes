from scapy.all import *

#Dicionarios para manter o contador de pacotes por ip de origem, ip de destino e tipo de protocolo
packet_count_src_ip = {}
packet_count_dst_ip = {}
packet_count_protocol = {}

#Função para processar os pacotes capturados
def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

    #incrementa o contador de pacotes por IP de origem
    if src_ip in packet_count_src_ip:
        packet_count_src_ip[src_ip] += 1
    else:
        packet_count_src_ip[src_ip] = 1

    #incrementa o contador de pacotes por IP de destino
    if dst_ip in packet_count_dst_ip:
        packet_count_dst_ip[dst_ip] += 1
    else:
        packet_count_dst_ip[dst_ip] = 1

    #incrementa o contador de pacotes por tipo de  protocolo
    if src_ip in packet_count_protocol:
        packet_count_protocol[protocol] += 1
    else:
        packet_count_protocol[protocol] = 1

    #exibe o conteúdo do pacote
    print(packet.summary())

#Captura de pacotes em tempo real
sniff(prn=process_packet, store=0)
