import pywhatkit
import datetime

def send_whatsapp_message(number, message, hour, minute):
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    pywhatkit.sendwhatmsg(number, message, current_hour, current_minute + 1)

# Kullanımı:
send_whatsapp_message("+9000000000", "Merhaba, bu bir otomatik mesajdır.", 9, 30)
import pywhatkit

def send_whatsapp_message(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute)

# Kullanımı:
send_whatsapp_message("+900000000", "Merhaba, bu bir otomatik mesajdır.", 9, 30)
