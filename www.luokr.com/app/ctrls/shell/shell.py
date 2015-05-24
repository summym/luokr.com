#coding=utf-8

import functools

from app.ctrls.basic import alive, BasicCtrl

class ShellCtrl(BasicCtrl):
    pass

def shell(method):
    @alive
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.model('admin').chk_user_is_live(self.current_user):
            return method(self, *args, **kwargs)
        else:
            self.flash(0, {'sta': 403, 'url': self.get_login_url()})
            return
    return wrapper
