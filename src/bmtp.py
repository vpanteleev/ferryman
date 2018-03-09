def interpreter(connection):
    greetings = '220---------- Welcome to Ferryman-BMTP [privsep] [TLS] ---------- \r\n'\
                '220 You will be disconnected after 15 minutes of inactivity.\r\n'
    connection.send(greetings)

    user = {
        "name": "",
        "isAuthorized": False,
        "permissions": [],
        "isSessionActive": True,
    }
    while user['isSessionActive']:
        message = connection.read()
        command, args = parse_message(message)
        response = handlers[command](args, user)
        connection.send(response)


def parse_message(message):
    command, *args = message.split()
    return command, args


def features_list(args, user):
    features = '211-Extensions supported:\r\n EPRT\r\n IDLE\r\n MDTM\r\n SIZE\r\n MFMT\r\n REST STREAM\r\n MLST type*;size*;sizd*;modify*;UNIX.mode*;UNIX.uid*;UNIX.gid*;unique*;\r\n MLSD\r\n AUTH TLS\r\n PBSZ\r\n PROT\r\n UTF8\r\n TVFS\r\n ESTA\r\n PASV\r\n EPSV\r\n SPSV\r\r\n211 End.\r\n'
    return features


def identify_user(args, user):
    response = ""
    if args[0] == 'admin':
        user["name"] = args[0]
        response = "331 User {} OK. Password required\r\n".format(user["name"])
    else:
        response = "ERROR"

    return response


def authenticate_user(args, user):
    response = ""
    if args[0] == 'admin':
        user["isAuthorized"] = True
        response = "230 OK.Current directory is / \r\n"
    else:
        response = "ERROR"

    return response


def close_session(args, user):
    user['isSessionActive'] = False;
    return "Bye Bye"


handlers = {
    "FEAT": features_list,
    "USER": identify_user,
    "PASS": authenticate_user,
    "EXIT": close_session,
}