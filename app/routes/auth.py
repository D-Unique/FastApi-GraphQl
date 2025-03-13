from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException

load_dotenv()

auth_router = APIRouter(prefix="/auth", tags=["Auths"])

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params={"scope": "openid email profile"},
    access_token_url="https://oauth2.googleapis.com/token",
    access_token_params=None,
    client_kwargs={"scope": "openid email profile"},

)

@auth_router.get("/google")
async def login_with_google(request: Request):
    """
    Redirects user to Google's OAuth2 login page.
    """

    return await oauth.google.authorize_redirect(request, os.getenv("GOOGLE_REDIRECT_URI"))

@auth_router.get("/google/callback")
async def google_auth_callback(request: Request):
    """
    Handles the callback from Google and retrieves user info.
    """

    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)
    if not user_info:
        raise HTTPException(status_code=400, detail="Failed to retrieve user info")

    return {"message": "Login successful", "user": user_info}
