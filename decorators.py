# decorators.py

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {str(e)}"
    return wrapper
