from utils.reset_cache import invalidate_template_cache

def delete_latest_users_videos_cache(sender, **kwargs):
    invalidate_template_cache('latest_users_videos_sidebar')