from itsdangerous import URLSafeTimedSerializer as Serializer

s = Serializer('secret')
token = s.dumps({'user_id':1})

try:
    data = s.loads(token,max_age=30)
    print(data)
except Exception:
    data = None
