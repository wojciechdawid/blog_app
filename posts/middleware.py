from time import time


class PrintProcessTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time()
        print("przed response")
        response = self.get_response(request)
        print("po response")
        duration = round(time() - start_time, 2)
        print(f"Zadanie wykonane w {duration} sec.")

        return response



class WebProcessTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time()
        response = self.get_response(request)
        duration = time() - start_time

        if request.path == "/posts/":
            response["X-Processed-Time"] = duration

        return response
