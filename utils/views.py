import random, os, urllib.parse

from django.http import HttpResponseRedirect

from django.conf import settings


def randbg(request):
    full_dir = os.path.join(settings.STATIC_ROOT, settings.BGIMG_STATIC_PATH)
    if os.path.isdir(full_dir) is False:
        raise IOError(f'no such dir: {full_dir}')
    imgs = os.listdir(full_dir)
    if not imgs:
        raise ValueError(f'no files in {full_dir}')
    i = random.choice(imgs)
    s = settings.STATIC_URL
    s = s if s.endswith('/') else f'{s}/'
    u = urllib.parse.urljoin(s, settings.BGIMG_STATIC_PATH)
    if u.endswith('/') is False:
        u = f'{u}/'
    redir = urllib.parse.urljoin(u, i)
    resp = HttpResponseRedirect(redir)
    resp['cache-control'] = 'no-cache, no-store, must-revalidate'
    resp['pragma'] = 'no-cache'
    resp['expires'] = '0'
    return resp

