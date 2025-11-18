import secrets, jwt
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from jwcrypto import jwk

from tool.models import ToolConfig   # <-- NEW


def build_deep_link_jwt(return_url, title, launch_url, description="", custom_params=None):
    now = datetime.utcnow()

    # Load private/public key
    private_key = open("lti_keys/private.pem", "rb").read()
    pub = jwk.JWK.from_pem(open("lti_keys/public.pem", "rb").read())
    kid = pub.export_public(as_dict=True)["kid"]

    # Deep linking content item
    content_item = {
        "type": "ltiResourceLink",
        "title": title,
        "url": launch_url,
        "text": description,
        "description": description,
    }

    if custom_params:
        content_item["custom"] = custom_params

    # Platform config
    platform = ToolConfig.objects.first()

    payload = {
        "iss": platform.client_id,
        "aud": platform.issuer,
        "iat": now,
        "exp": now + timedelta(minutes=5),
        "nonce": secrets.token_urlsafe(12),

        "https://purl.imsglobal.org/spec/lti/claim/message_type": "LtiDeepLinkingResponse",
        "https://purl.imsglobal.org/spec/lti/claim/version": "1.3.0",

        # Deep link return URL
        "https://purl.imsglobal.org/spec/lti/claim/target_link_uri": return_url,

        # Content items
        "https://purl.imsglobal.org/spec/lti-dl/claim/content_items": [content_item],
    }

    headers = {"alg": "RS256", "kid": kid, "typ": "JWT"}

    return jwt.encode(payload, private_key, algorithm="RS256", headers=headers)


def deeplink(request):
    claims = request.session.get("lti_claims")
    if not claims:
        return HttpResponse("Missing LTI claims", status=400)

    deep_link = claims.get("https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings")
    if not deep_link:
        return HttpResponse("Not a deep linking launch", status=400)

    return render(request, "tool/deeplink.html", {
        "deep_link_return": deep_link["deep_link_return_url"],
    })


@csrf_exempt
def deeplink_submit(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")

    return_url = request.POST.get("return_url")
    title = request.POST.get("title", "Viva Assignment")
    description = request.POST.get("description", "")
    allow_multiple = (request.POST.get("allow_multiple") == "true")

    custom_params = {
        "allow_multiple_submissions": "true" if allow_multiple else "false"
    }

    # Load from ToolConfig instead of settings
    platform = ToolConfig.objects.first()

    jwt_token = build_deep_link_jwt(
        return_url=return_url,
        title=title,
        launch_url=platform.redirect_uri,   # <-- FIXED
        description=description,
        custom_params=custom_params,
    )

    return render(request, "tool/deeplink_return.html", {
        "return_url": return_url,
        "jwt": jwt_token,
    })
