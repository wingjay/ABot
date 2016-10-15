# fetch blog by author_name & time_range
from crawler import wingjay_blog


def process(author_name='wingjay', time_range='recently', number=5):
    if author_name is None:
        return "input author's name plz"
    return


def _get_wingjay_blogs(time_range='recently'):
    return wingjay_blog.get_all_blogs()