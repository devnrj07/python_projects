import redis 
r = redis.Redis()
r.mset({"Master":"Slave", "Key":"Value"})
r.get("Key")
