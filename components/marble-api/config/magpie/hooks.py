from magpie.api import exception as ax
from magpie.api import schemas as s
from pyramid.httpexceptions import HTTPUnauthorized


def check_user_access(request):
    """
    Deny users whose name does not match the {user_name} in /v1/users/{user_name}/ paths.

    For example a user with user name "fred" would not be allowed to access /v1/users/geoff/
    but would be allowed to access /v1/users/fred/ (assuming that other resource permissions allow
    fred access already). 
    """
    user_path_part, user_name, *_ = request.path.strip("/").split("/")[4:] # skips /ows/proxy/v1/
    # this should always be true since this hook only triggers when the path matches /v1/users/[^\]+/.*
    # but we check anyway just in case:

    if user_path_part == "users":
        if request.user.user_name != user_name:
            ax.raise_http(http_error=HTTPUnauthorized, detail=s.HTTPForbiddenResponseSchema.description)
    return request
