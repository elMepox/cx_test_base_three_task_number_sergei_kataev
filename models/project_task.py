from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = "project.task"

    task_number = fields.Char(string="Task Number", required=True, readonly=True, default='New', edit=False)

    @api.model
    def create(self, vals):
        if vals.get('task_number', 'New') == 'New':
            vals['task_number'] = self.env['ir.sequence'].next_by_code('project.task') or 'New'
        return super(ProjectTask, self).create(vals)

    def name_get(self):
        return [(task.id, "[{0}] {1} - {2}".format(task.task_number, task.name, task.project_id.name)) for task in self]

    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = list(args or [])
        domain = ['|', ('name', 'ilike', name), ('task_number', 'ilike', name)]
        return super(ProjectTask, self).search(args + domain, limit=limit).get_name()

    @api.model
    def init_hook(self):
        task_number = 1
        for rec in self.search([], order='id asc'):
            rec.task_number = task_number
            task_number += 1
        self.env["ir.sequence"].search([('code', '=', 'project.task')]).write({'number_next': task_number})
