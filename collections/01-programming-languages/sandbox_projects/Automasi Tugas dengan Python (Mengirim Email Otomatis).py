import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Konfigurasi email
    sender_email = "emailkamu@gmail.com"
    receiver_email = "emailpenerima@gmail.com"
    password = "passwordkamu"

    # Membuat objek email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Subjek Email Otomatis'

    # Isi email
    body = "Ini adalah email otomatis yang dikirim menggunakan Python."
    msg.attach(MIMEText(body, 'plain'))

    # Menyambung ke server email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Mengirim email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    print("Email berhasil dikirim!")

# Memanggil fungsi untuk mengirim email
send_email()
