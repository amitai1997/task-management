from flask import jsonify
from flask import jsonify, request
from sqlalchemy.orm import class_mapper
from datetime import datetime, timedelta


def serialize_model(model):
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def rate_limit_decorator(rate_limit, rate_limit_period):
    def decorator(func):
        def wrapper(*args, **kwargs):
            from app import r
            client_ip = request.remote_addr
            rate_limit_key = f"rate_limit:{client_ip}"

            if r.exists(rate_limit_key):
                request_count, first_request_time = r.hmget(rate_limit_key, 'count', 'timestamp')
                request_count = int(request_count)
                elapsed_time = datetime.now() - datetime.strptime(first_request_time, '%Y-%m-%d %H:%M:%S.%f')

                if elapsed_time > timedelta(seconds=rate_limit_period):
                    first_request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    request_count = 0
                    r.hmset(rate_limit_key, {'count': request_count, 'timestamp': first_request_time})
                else:
                    if request_count >= rate_limit:
                        return jsonify({'error': 'Rate limit exceeded'})

            else:
                request_count = 0
                first_request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                r.hmset(rate_limit_key, {'count': request_count, 'timestamp': first_request_time})

            r.hincrby(rate_limit_key, 'count', 1)

            return func(*args, **kwargs)

        return wrapper

    return decorator
