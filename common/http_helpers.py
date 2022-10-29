
def is_hx_request(request):
    return request.headers.get("Hx-Request")=='true'
