{
    'name': 'Gestión de Cursos',
    'version': '1.0',
    'summary': 'Módulo de ejemplo para gestionar cursos',
    'description': """
    Este módulo permite administrar cursos básicos:
    - Crear cursos con nombre, descripción y fecha.
    - Verlos en lista y formulario.
    """,
    'author': 'Alumno Odoo',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/curso_views.xml',
    ],
    'installable': True,
    'application': True,
}
