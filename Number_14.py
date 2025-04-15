class MailServer:
    def __init__(self, name):
        self.name = name
        self.mailbox = {}

    def store_mail(self, user, message):
        if user not in self.mailbox:
            self.mailbox[user] = []
        self.mailbox[user].append(message)

    def retrieve_mail(self, user):
        return self.mailbox.pop(user, [])


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        messages = self.server.retrieve_mail(self.user)
        return messages

    def send_mail(self, server_name, user1, message):
        if server_name not in available_servers:
            print(f"Ошибка: сервер {server_name} недоступен.")
            return
        target_server = servers[server_name]
        target_server.store_mail(user1, message)
        print(f"Письмо отправлено на {server_name} пользователю {user1}.")


# Определяем серверы и доступные сервера
servers = {
    'mailserver1': MailServer('mailserver1'),
    'mailserver2': MailServer('mailserver2'),
}

available_servers = servers.keys()

# Пример использования
client = MailClient(servers['mailserver1'], 'user1')
client.send_mail('mailserver2', 'user2', 'Привет!')
print(client.receive_mail())  # Получение почты, если есть
