import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)

messages = ["Avanza", "Retrocede", "Gira derecha", "Gira izquierda"]

print("Hola")
while True:
    print("Elige un mensaje:")
    for i, message in enumerate(messages, start=1):
        print(f"{i}. {message}")

    try:
        choice = int(input("Número del mensaje: "))
        if 1 <= choice <= len(messages):
            selected_message = messages[choice - 1]
            client.publish("topic/spider-move", selected_message)
            print(f"Enviado: {selected_message}")
        else:
            print("Opción no válida. Introduce un número válido.")
    except ValueError:
        print("Por favor, introduce un número válido.")

client.disconnect()
