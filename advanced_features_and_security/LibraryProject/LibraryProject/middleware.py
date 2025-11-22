

class ContentSecurityPolicyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # Example policy:
        # - default-src 'self' (everything must come from same origin)
        # - script-src 'self' (no external scripts)
        # - style-src 'self' 'unsafe-inline' (allow inline styles only if needed)
        # - img-src 'self' data:
        # Modify as needed for your app (fonts, cdn, analytics)
        self.csp_policy = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self' data:; "
            "connect-src 'self'; "
            "object-src 'none'; "
            "base-uri 'self';"
        )

    def __call__(self, request):
        response = self.get_response(request)
        # Only set on HTML responses
        if hasattr(response, "get(") or "text/html" in response.get("Content-Type", ""):
            response.setdefault("Content-Security-Policy", self.csp_policy)
        else:
            response.setdefault("Content-Security-Policy", self.csp_policy)
        return response
