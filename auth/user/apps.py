from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    def ready(self):


        from user import grpc_server
        import threading
        def start_grpc_server():
            grpc_server.serve()

        threading.Thread(target=start_grpc_server, daemon=True).start()
