# fetch blog by author_name & time_range
from crawler import wingjay_blog, drakeet_blog, pinterest_blog, liwei_blog, wangyin_blog


def process(author_name='wingjay', time_range='recently', number=5):
    print 'fetch blog for: %s' % author_name
    if author_name is None:
        return "input author's name plz"
    if author_name is 'wingjay':
        return _get_wingjay_blogs()
    elif author_name is 'drakeet':
        return _get_drakeet_blogs()
    elif author_name is 'pinterest':
        return _get_pinterest_blogs()
    elif author_name is 'wangyin':
        return _get_wangyin_blogs()
    elif author_name is 'liwei':
        return _get_liwei_blogs()
    else:
        return _get_wingjay_blogs()


def _get_wingjay_blogs():
    print 'fetch wingjay blogs'
    return wingjay_blog.get_all_blogs()


def _get_drakeet_blogs():
    return drakeet_blog.get_all_blogs()


def _get_pinterest_blogs():
    return pinterest_blog.get_all_blogs()


def _get_liwei_blogs():
    return liwei_blog.get_all_blogs()


def _get_wangyin_blogs():
    return wangyin_blog.get_all_blogs()