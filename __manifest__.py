{
    "name": "Sales Order Lines Numeration",
    "summary": "Sales Order Lines Numeration",
    "version": "11.0.1.0.0",
    "category": "Sale",
    "author": "Sergei Kataev, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
         "project",
    ],
    "data": [
        'data/project_task.xml',
        'views/project_task.xml',
        'views/project_task_search_with_number.xml',
        'views/project_task_kanban.xml',
    ],
    'post_init_hook': 'my_post_init_hook',
}