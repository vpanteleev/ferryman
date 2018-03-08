def interpreter(connection):
    greetings = '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\r\n220-You are user number 1 of 5 allowed.\r\n220-Local time is now 17:01. Server port: 1060.\r\n220-This is a private system - No anonymous login\r\n220 You will be disconnected after 15 minutes of inactivity.\r\n'
    connection.send(greetings)

    while True:
        message = connection.read()
        formats = '211-Extensions supported:\r\n EPRT\r\n IDLE\r\n MDTM\r\n SIZE\r\n MFMT\r\n REST STREAM\r\n MLST type*;size*;sizd*;modify*;UNIX.mode*;UNIX.uid*;UNIX.gid*;unique*;\r\n MLSD\r\n AUTH TLS\r\n PBSZ\r\n PROT\r\n UTF8\r\n TVFS\r\n ESTA\r\n PASV\r\n EPSV\r\n SPSV\r\r\n211 End.\r\n'
        connection.send(formats)