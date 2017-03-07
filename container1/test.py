import redis
import random
import time

conn = redis.StrictRedis(
        host='redis',
        port=6379)

p = conn.pubsub()
p.subscribe('channelred')

time.sleep(0.005)  # b

for x in range(0, 100):
    print('red' + str(x))
    conn.publish('channelred','red' + str(x))

time.sleep(1)  # b
