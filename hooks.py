from odoo import api, SUPERUSER_ID


def my_post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['project.task'].init_hook()
