from tkinter import *
import json



def main():
    def load_json(Yandex, Discord):
        file = "config.json"
        with open(file) as file:
            f = json.load(file)
            w = json.dump(file)
            if (f['y_music_api_key'] != None) and (f['presence_client_id'] != None):
                print(f['y_music_api_key'], )
            else:
                with open(file) as file:
                    json.dump(data, file)
                    f['y_music_api_key'] = Yandex
                    f['presence_client_id'] = int(Discord)

    def click_button():
        ApiKeyYandex, DiscordPresence = ApiKeyYandexKey.get(), DiscordPresenceKey.get()
        print(ApiKeyYandex, DiscordPresence)
        load_json(ApiKeyYandex, DiscordPresence)
        win.destroy()

    win = Tk()
    opts = { 'ipadx': 10, 'ipady': 10, 'fill': BOTH }

    ApiKeyYandexKey, DiscordPresenceKey = StringVar(), StringVar()

    Label(win, text="Api Key for YandexMusic").pack(side=TOP, **opts)
    Entry(textvariable=ApiKeyYandexKey).pack(side=TOP, **opts)

    Label(win, text="Discord Presence ClientId").pack(side=TOP, **opts)
    Entry(textvariable=DiscordPresenceKey).pack(side=TOP, **opts)




    Button(win, text="Submit", activebackground="red", activeforeground="blue", command=click_button).pack(side=TOP, **opts)



    win.mainloop()

if __name__ == '__main__':
    main()