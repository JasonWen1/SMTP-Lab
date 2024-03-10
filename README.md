# SMTP-Lab
A client of SMTP

Overview:
This client program first we choose the sender email and password and receiver email.
Then we choose the mail server of sender email with its port, which is the smtp server can perform the send task.
In the main part, the program first create a TCP socket and then connect to the SMTP server
with the socket. Then we try to receive the response message from server.
In the next few lines, we send HELO command to the server and recieve the responsecode, if the
response code is 250, it shows that the command is succuess.
Then we send STARTTLS command and then encrypt the socket (the Optional task1) with ssl.
Then we send HELO again to ensure this function is ok after we encrypt the socket.
Then we send AUTH LOGIN command to ask the server try to login to the email later.
Then we send email account and password Base64 encoded. After that, we send MAIL FROM command to setup the sender
email, and we send RCPT TO command to set up the receiver information. Next, we send DATA command to switch to the 
message send part.  Next we use socket to send the message text. Then we send end message via socket. Last, we
send QUIT command and close the socket to end this connection.


How to setup this program:
set the sender email address and password, and also set receiver's email address.
Notice that in the qq mail. For safety, we can only apply for a application password
instead of using raw password.


How to run this program:
just run with "python3 ./SMTPClient.py"

expected input (No input)
expected output: each response message of each step. Can see in the screenshot of the report.

