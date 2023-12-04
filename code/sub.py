import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado: " + str(rc))
    client.subscribe("topic/spider-moves")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Mensaje recibido en el tema {msg.topic}: {message}")

    # Realizar acciones según el contenido del mensaje
    if message == "Avanza":
        print("Realizar acción: Avanzar")
        # Agregar código para avanzar aquí
    elif message == "Retrocede":
        print("Realizar acción: Retroceder")
        # Agregar código para retroceder aquí
    elif message == "Gira derecha":
        print("Realizar acción: Girar a la derecha")
        # Agregar código para girar a la derecha aquí
    elif message == "Gira izquierda":
        print("Realizar acción: Girar a la izquierda")
        # Agregar código para girar a la izquierda aquí
    else:
        print("Mensaje no reconocido. No se realizará ninguna acción.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
