import redis
import random
import time

conn = redis.StrictRedis(
        host='redis',
        port=6379)

p = conn.pubsub()
p.subscribe('channelblue')

time.sleep(0.005)  # b

for x in range(0, 100):
    print('blue' + str(x))
    conn.publish('channelblue','blue' + str(x))

time.sleep(1)  # b
