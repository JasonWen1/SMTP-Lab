from socket import *
import ssl
import base64

# Set up email and password
originEmail = '2714039600@qq.com'
originPassword = 'makxdtvpbtlidcdd'
email = base64.b64encode(originEmail.encode()).decode() + '\r\n'
password = base64.b64encode(originPassword.encode()).decode() + '\r\n'
receiveEmail = '<wenziqi1999@gmail.com>'


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.qq.com'
port = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send STARTTLS command and print server response.
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
tlsRecv = clientSocket.recv(1024).decode()
print(tlsRecv)
if tlsRecv[:3] != '220':
    print('220 reply not received from server.')

# Encrypt the socket
clientSocket = ssl.SSLContext().wrap_socket(clientSocket)

# Send HELO command again for the encrypted socket and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
clientSocket.write(authCommand.encode())
authRecv = clientSocket.recv(1024).decode()
print(authRecv)

if authRecv[:3] != '334':
    print('334 reply not received from server.')


# Send the Base64 encoded email and print server response.
clientSocket.send(email.encode())
emailRecv = clientSocket.recv(1024).decode()
print(emailRecv)

if emailRecv[:3] != '334':
    print('334 reply not received from server.')

# Send the Base64 encoded password and print server response.
clientSocket.send(password.encode())
passwordRecv = clientSocket.recv(1024).decode()
print(passwordRecv)

if passwordRecv[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <' + originEmail + '>\r\n'
clientSocket.send(mailFromCommand.encode())
mailFromRecv = clientSocket.recv(1024).decode()
print(mailFromRecv)

if mailFromRecv[:3] != '250':
    print('MAIL FROM command failed.')
else:
    print('MAIL FROM command successful.')

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: ' +  receiveEmail + '\r\n'
clientSocket.send(rcptToCommand.encode())
rcptToRecv = clientSocket.recv(1024).decode()
print(rcptToRecv)

if rcptToRecv[:3] != '250':
    print('RCPT TO command failed.')
else:
    print('RCPT TO command successful.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
dataRecv = clientSocket.recv(1024).decode()
print(dataRecv)

if dataRecv[:3] != '354':
    print('DATA command failed.')
else:
    print('DATA command successful.')

# Send message data.
message = 'from: <' + originEmail + '>\r\n'
message += 'to: '+ receiveEmail +'\r\n'
message += 'subject: Computer Networking!\r\n'
message += msg
clientSocket.send(message.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
endMsgRecv = clientSocket.recv(1024).decode()
print(endMsgRecv)

if endMsgRecv[:3] != '250':
    print('End message command failed.')
else:
    print('End message command successful.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
quitRecv = clientSocket.recv(1024).decode()
print(quitRecv)

if quitRecv[:3] != '221':
    print('QUIT command failed.')
else:
    print('QUIT command successful.')

# Close the client socket.
clientSocket.close()
