import redis
import time

conn = redis.StrictRedis(
        host='redis',
        port=6379)
p = conn.pubsub()
p.subscribe('channelred')

while True:
    for message in p.listen():
        print("container3 messsage",message)
        time.sleep(0.001)  # be nice to the system :)
