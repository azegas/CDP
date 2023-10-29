LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format':
            '%(asctime)s %(levelname)s %(module)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
            'filters': [],
        },
    },
    'loggers': {
        logger_name: {
            'level': 'INFO',
            'propagate': True,
        }
        for logger_name in ('django', 'django.request', 'django.db.backends',
                            'django.template', 'core')
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    }
}
