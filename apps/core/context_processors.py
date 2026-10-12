from .portfolio_data import PROFILE
def site_profile(request): return {"profile": PROFILE, "site_profile": PROFILE}
