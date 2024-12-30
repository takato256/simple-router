import socket
import time
client1_ip = "92.10.10.25"
client1_mac = "AF:04:67:EF:19:DA"

router = ("localhost", 8200)

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

time.sleep(1)
client1.connect(router)

while True:
    receive_message = client1.recv(1024)
    receive_message = receive_message.decode("utf-8")

    source_mac = receive_message[0:17]
    destination_mac = receive_message[17:34]

    source_ip = receive_message[34:45]
    destination_ip = receive_message[45:56]

    message = receive_message[56:]

    print("\nPacket integrity:\ndestination MAC address matches client 1 MAC address: {mac}".format(mac=(client1_mac == destination_mac)))
    print("\ndestination IP address matches client 1 IP address: {mac}".format(mac=(client1_ip == destination_ip)))
    print("\nThe packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
 
    print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
 
    print("\nMessage: " + message)