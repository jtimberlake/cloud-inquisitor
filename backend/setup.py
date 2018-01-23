import setuptools

setuptools.setup(
    name='cloud_inquisitor',
    use_scm_version={
        'root': '..'
    },

    entry_points={
        'console_scripts': [
            'cloud-inquisitor = cloud_inquisitor.cli:cli'
        ],
        'cloud_inquisitor.plugins.commands': [
            'add_account = cloud_inquisitor.plugins.commands.accounts:AddAccount',
            'delete_account = cloud_inquisitor.plugins.commands.accounts:DeleteAccount',
            'api_server = cloud_inquisitor.plugins.commands.apiserver:APIServer',
            'list_plugins = cloud_inquisitor.plugins.commands.plugins:ListPlugins',
            'scheduler = cloud_inquisitor.plugins.commands.scheduler:Scheduler',
            'import-saml = cloud_inquisitor.plugins.commands.saml:ImportSAML',
            'worker = cloud_inquisitor.plugins.commands.scheduler:Worker',
            'userdata = cloud_inquisitor.plugins.commands.userdata:UserData',
            'setup = cloud_inquisitor.plugins.commands.setup:Setup',
            'auth = cloud_inquisitor.plugins.commands.auth:Auth',
        ],

        'cloud_inquisitor.plugins.notifiers': [
            'email_notify = cloud_inquisitor.plugins.notifiers.email:EmailNotifier',
            'slack_notify = cloud_inquisitor.plugins.notifiers.slack:SlackNotifier',
        ],

        'cloud_inquisitor.plugins.types': [
            'ec2instance_type = cloud_inquisitor.plugins.types.resources:EC2Instance',
            'beanstalk_type = cloud_inquisitor.plugins.types.resources:BeanStalk',
            'cloudfrontdist_type = cloud_inquisitor.plugins.types.resources:CloudFrontDist',
            's3bucket_type = cloud_inquisitor.plugins.types.resources:S3Bucket',
            'ebssnapshot_type = cloud_inquisitor.plugins.types.resources:EBSSnapshot',
            'ebsvolume_type = cloud_inquisitor.plugins.types.resources:EBSVolume',
            'ami_type = cloud_inquisitor.plugins.types.resources:AMI',
            'dnszone_type = cloud_inquisitor.plugins.types.resources:DNSZone',
            'dnsrecord_type = cloud_inquisitor.plugins.types.resources:DNSRecord',
        ],

        'cloud_inquisitor.plugins.schedulers': [],

        'cloud_inquisitor.plugins.views': [
            'account_list = cloud_inquisitor.plugins.views.accounts:AccountList',
            'account_details = cloud_inquisitor.plugins.views.accounts:AccountDetail',
            'search = cloud_inquisitor.plugins.views.search:Search',
            'stats = cloud_inquisitor.plugins.views.stats:StatsGet',
            'log = cloud_inquisitor.plugins.views.logs:Logs',
            'log_details = cloud_inquisitor.plugins.views.logs:LogDetails',
            'metadata = cloud_inquisitor.plugins.views.metadata:MetaData',
            'email_list = cloud_inquisitor.plugins.views.emails:EmailList',
            'email = cloud_inquisitor.plugins.views.emails:EmailGet',
            'config_list = cloud_inquisitor.plugins.views.config:ConfigList',
            'config = cloud_inquisitor.plugins.views.config:ConfigGet',
            'config_namespace_list = cloud_inquisitor.plugins.views.config:Namespaces',
            'config_namespace_get = cloud_inquisitor.plugins.views.config:NamespaceGet',
            'user_list = cloud_inquisitor.plugins.views.users:UserList',
            'user_details = cloud_inquisitor.plugins.views.users:UserDetails',
            'password_reset = cloud_inquisitor.plugins.views.users:PasswordReset',
            'role_list = cloud_inquisitor.plugins.views.roles:RoleList',
            'role_get = cloud_inquisitor.plugins.views.roles:RoleGet',
            'auditlog_list = cloud_inquisitor.plugins.views.auditlog:AuditLogList',
            'auditlog_get = cloud_inquisitor.plugins.views.auditlog:AuditLogGet',
        ]
    },

    packages=setuptools.find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests"
        ]
    ),
    include_package_data=True,
    zip_safe=False,

    # Requirements for setup and installation
    setup_requires=['setuptools_scm'],
    install_requires=[
        'APScheduler~=3.3',
        'Babel~=2.4',
        'Flask-Compress~=1.4',
        'Flask-Migrate~=2.1',
        'Flask-RESTful~=0.3',
        'Flask-SQLAlchemy~=2.2',
        'Flask-Script~=2.0',
        'Flask~=0.12',
        'Jinja2~=2.9',
        'Mako~=1.0',
        'MarkupSafe~=1.0',
        'PyJWT~=1.5',
        'Pygments~=2.2',
        'SQLAlchemy~=1.1',
        'Sphinx~=1.6',
        'Werkzeug~=0.12',
        'alabaster~=0.7',
        'alembic~=0.9',
        'aniso8601~=1.2',
        'appdirs~=1.4',
        'appnope~=0.1',
        'argon2-cffi~=16.3',
        'boto3~=1.4',
        'botocore~=1.5',
        'certifi~=2017.4',
        'cffi~=1.10',
        'cinq-auditor-cloudtrail~=1.0.0',
        'cinq-auditor-domain-hijacking~=1.0.0',
        'cinq-auditor-ebs~=1.0.0',
        'cinq-auditor-iam~=1.0.0',
        'cinq-auditor-required-tags~=1.0.0',
        'cinq-auditor-vpc-flowlogs~=1.0.0',
        'cinq-collector-aws~=1.0.0',
        'cinq-collector-dns~=1.0.0',
        'cinq-scheduler-sqs~=1.0.1',
        'cinq-scheduler-standalone~=1.0.0',
        'cinq-auth-local~=1.0.0',
        'cinq-auth-onelogin-saml~=1.0.0',
        'click~=6.7',
        'colorama~=0.3',
        'coverage~=4.4',
        'decorator~=4.0',
        'docutils~=0.13',
        'enum34~=1.1',
        'et-xmlfile~=1.0',
        'flake8-comprehensions~=1.4',
        'flake8-deprecated~=1.2',
        'flake8-pep3101~=1.1',
        'flake8-quotes~=0.9',
        'flake8~=3.3',
        'gevent~=1.2',
        'greenlet~=0.4',
        'gunicorn~=19.7',
        'imagesize~=0.7',
        'ipython-genutils~=0.2',
        'ipython~=6.0',
        'isodate~=0.5',
        'itsdangerous~=0.24',
        'jdcal~=1.3',
        'jedi~=0.10',
        'jmespath~=0.9',
        'logutils~=0.3',
        'lxml~=3.8',
        'mccabe~=0.6',
        'munch~=2.1',
        'mysqlclient~=1.3',
        'openpyxl~=2.4',
        'packaging~=16.8',
        'pexpect~=4.2',
        'pickleshare~=0.7',
        'pkgconfig~=1.2',
        'prompt-toolkit~=1.0',
        'ptyprocess~=0.5',
        'pycodestyle~=2.3',
        'pycparser~=2.17',
        'pyexcel-io==0.3.4.1',
        'pyexcel-xlsx==0.3.0',
        'pyexcel==0.4.5',
        'pyflakes~=1.5',
        'pyparsing~=2.2',
        'pytest-cov~=2.5',
        'pytest~=3.0',
        'python-dateutil~=2.6',
        'python-editor~=1.0',
        'pytz~=2017.2',
        'py~=1.4',
        'rainbow-logging-handler~=2.2',
        'requests~=2.14',
        's3transfer~=0.1',
        'simplegeneric~=0.8',
        'six~=1.10',
        'slackclient~=1.0',
        'smmap2~=2.0',
        'snowballstemmer~=1.2',
        'sphinx-autodoc-typehints~=1.2',
        'sphinx-rtd-theme~=0.2',
        'sphinxcontrib-websupport~=1.0',
        'texttable~=0.9',
        'traitlets~=4.3',
        'typing~=3.6',
        'tzlocal~=1.4',
        'wcwidth~=0.1',
        'websocket-client~=0.40',
        'xmlsec~=1.0',
    ],

    # Metadata
    description='Tool to enforce ownership and data security within cloud environments',
    long_description='Please see https://github.com/RiotGames/cloud-inquisitor for more information',
    author='Riot Games Security',
    author_email='security@riotgames.com',
    url='https://github.com/RiotGames/cloud-inquisitor',
    license='Apache 2.0',
    classifiers=[
        # Current project status
        'Development Status :: 4 - Beta',

        # Audience
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        # License information
        'License :: OSI Approved :: Apache Software License',

        # Supported python versions
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        # Frameworks used
        'Framework :: Flask',
        'Framework :: Sphinx',

        # Supported OS's
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',

        # Extra metadata
        'Environment :: Console',
        'Natural Language :: English',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    keywords='cloud security',
)
