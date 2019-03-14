from rest_framework.routers import DynamicRoute



class TemiiRouter(DynamicRoute):

    def get_urls(self):
        return super().get_urls()