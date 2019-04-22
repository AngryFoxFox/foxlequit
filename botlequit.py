import vk_api
import time
import random
 
token = "твой токен"
 
vk = vk_api.VkApi(token="0c9fb4a1d62e25bc3c56dde20ea81b7fc3760f0fb21c2fda6f07e50bb8d792fa10c818fce7c8d08bb17b3")
 
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "я не подписан на канал it things":
                vk.method("messages.send", {"peer_id": id, "message": "Казнить грешника!", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
