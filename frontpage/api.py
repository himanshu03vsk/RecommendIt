from models import Submit

def params_to_send():
    """This Function will send the fields required for
    recommendation"""
    ins = Submit.objects.all()[-1]
    genres = ins.genre
    rating = ins.rating
    release_year = ins.Release_year
    actors = ins.cast

def api_recieve():
    """
    This function will recieve the movies from movie api
    """
    pass

