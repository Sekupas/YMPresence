import time
import traceback

from pypresence import Presence
from yandex_music import Client

from load_config import Y_MUSIC_KEY, CLIENT_ID


def main():
    client = Client(Y_MUSIC_KEY).init()

    RPC = Presence(CLIENT_ID)
    RPC.connect()

    cur_track_id = 0
    started = time.time()
    artists = "None"
    title = "None"
    img_uri = "https://yastatic.net/s3/doc-binary/freeze/r-kLVqy2op9wYtE_g9RaJ8lzNtY.png"
    buttons = None

    while True:
        try:
            queues = client.queues_list()
            last_queue = client.queue(queues[0].id)
            last_track_id = last_queue.get_current_track()
            if last_track_id != cur_track_id:
                cur_track_id = last_track_id
                last_track = last_track_id.fetch_track()
                started = time.time()
                artists = ', '.join(last_track.artists_name())
                title = last_track.title
                img_uri = f"https://{last_track.cover_uri[:-2]}400x400"
                buttons = [{"label": "Слушать", "url": f"https://music.yandex.ru/track/{last_track.id}"}]
                print(f"{artists} - {title}")
            RPC.update(
                state=f"{artists} - {title}",
                large_image=img_uri,
                start=int(started),
                buttons=buttons
            )
        except TypeError:
            print(traceback.format_exc())
        except Exception as ex:
            RPC.update(
                state=f"Listening radio",
                large_image=img_uri,
                start=int(started),
                buttons=buttons
            )
        finally:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
