def define_env(env):
    """
    Define variables y macros para MkDocs Macros Plugin.
    """

    # Variable base_url para producción y local
    # Cambia '' a '/logos/' cuando hagas deploy en GitHub Pages
    # Puedes automatizarlo con una variable de entorno si quieres
    # env.variables['base_url'] = ''

    # Ejemplo para producción (descomenta cuando hagas deploy)
    # OJO NO MOVER DE ACA PORQUE ASI FUNCIONA BIEN EN DEPLOY Y EN PRODUCCION
    env.variables['base_url'] = '/logos/'

    # También puedes definir macros o funciones Python aquí si quieres
