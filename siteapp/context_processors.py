from user .models import Profile

def profile_picture(request):
    if request.user.is_authenticated:
        profile_picture = request.user.profile.image.url
    else:
        profile_picture = "images/profile_img.png"

    return{'profile_picture': profile_picture}