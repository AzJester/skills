"""Generic 24x24 icon glyphs drawn as SVG fragments.

Each function returns markup positioned inside a 24x24 box at the origin;
render.py wraps it in a <g transform="translate(x,y) scale(s)">.
Stroke colour is passed in; fills stay open so the glyph reads on any bg.
"""


def _s(c, w=1.8):
    return 'fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" ' \
           'stroke-linecap="round"' % (c, w)


def server(c):
    return ('<rect x="3" y="3" width="18" height="6" rx="1" %s/>'
            '<rect x="3" y="11" width="18" height="6" rx="1" %s/>'
            '<circle cx="7" cy="6" r="1" fill="%s"/><circle cx="7" cy="14" r="1" fill="%s"/>'
            % (_s(c), _s(c), c, c))


def database(c):
    return ('<ellipse cx="12" cy="5.5" rx="8" ry="3" %s/>'
            '<path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13" %s/>'
            '<path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3" %s/>' % (_s(c), _s(c), _s(c)))


def cache(c):
    return ('<rect x="4" y="5" width="16" height="14" rx="2" %s/>'
            '<path d="M8 9h8M8 12h8M8 15h5" %s/>' % (_s(c), _s(c, 1.4)))


def queue(c):
    return ('<rect x="2" y="8" width="5" height="8" rx="1" %s/>'
            '<rect x="9.5" y="8" width="5" height="8" rx="1" %s/>'
            '<rect x="17" y="8" width="5" height="8" rx="1" %s/>' % (_s(c), _s(c), _s(c)))


def storage(c):
    return ('<path d="M3 7l3-4h12l3 4v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" %s/>'
            '<path d="M3 7h18M9 12h6" %s/>' % (_s(c), _s(c, 1.4)))


def cdn(c):
    return ('<circle cx="12" cy="12" r="9" %s/>'
            '<path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" %s/>'
            % (_s(c), _s(c, 1.3)))


def lb(c):
    return ('<circle cx="12" cy="4.5" r="2.5" %s/><circle cx="4.5" cy="19" r="2.5" %s/>'
            '<circle cx="19.5" cy="19" r="2.5" %s/>'
            '<path d="M12 7v4M12 11H5v5M12 11h7v5" %s/>'
            % (_s(c), _s(c), _s(c), _s(c, 1.4)))


def api(c):
    return ('<path d="M9 6L4 12l5 6M15 6l5 6-5 6" %s/><path d="M13 4l-2 16" %s/>'
            % (_s(c), _s(c, 1.4)))


def function(c):
    return ('<path d="M13 2L5 13h6l-2 9 10-12h-6z" %s/>' % _s(c))


def container(c):
    return ('<rect x="3" y="9" width="6" height="6" %s/><rect x="10" y="9" width="6" '
            'height="6" %s/><rect x="6.5" y="3" width="6" height="5" %s/>'
            '<path d="M17 12h4" %s/>' % (_s(c, 1.5), _s(c, 1.5), _s(c, 1.5), _s(c, 1.5)))


def user(c):
    return ('<circle cx="12" cy="8" r="4" %s/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7" %s/>'
            % (_s(c), _s(c)))


def browser(c):
    return ('<rect x="2.5" y="4" width="19" height="16" rx="2" %s/>'
            '<path d="M2.5 9h19" %s/><circle cx="6" cy="6.5" r="0.9" fill="%s"/>'
            % (_s(c), _s(c, 1.4), c))


def mobile(c):
    return ('<rect x="7" y="2.5" width="10" height="19" rx="2" %s/>'
            '<path d="M10.5 18.5h3" %s/>' % (_s(c), _s(c, 1.4)))


def firewall(c):
    return ('<path d="M12 2l8 3v6c0 5-3.4 9.3-8 11-4.6-1.7-8-6-8-11V5z" %s/>'
            '<path d="M9 12l2 2 4-4" %s/>' % (_s(c), _s(c, 1.6)))


def monitor(c):
    return ('<path d="M3 12h4l2.5-6 3.5 12 2.5-6H21" %s/>' % _s(c))


def network(c):
    return ('<circle cx="12" cy="12" r="3" %s/><circle cx="4" cy="5" r="2" %s/>'
            '<circle cx="20" cy="5" r="2" %s/><circle cx="12" cy="21" r="2" %s/>'
            '<path d="M6 6.5l4 3.5M18 6.5l-4 3.5M12 15v4" %s/>'
            % (_s(c), _s(c), _s(c), _s(c), _s(c, 1.3)))


def ml(c):
    return ('<circle cx="6" cy="7" r="2" %s/><circle cx="6" cy="17" r="2" %s/>'
            '<circle cx="14" cy="12" r="2" %s/><circle cx="20" cy="12" r="1.6" %s/>'
            '<path d="M8 8l4 3M8 16l4-3M16 12h2.4" %s/>'
            % (_s(c), _s(c), _s(c), _s(c), _s(c, 1.3)))


def search(c):
    return ('<circle cx="10.5" cy="10.5" r="6.5" %s/><path d="M15.5 15.5L21 21" %s/>'
            % (_s(c), _s(c)))


def secret(c):
    return ('<rect x="4" y="10" width="16" height="11" rx="2" %s/>'
            '<path d="M8 10V7a4 4 0 0 1 8 0v3" %s/><circle cx="12" cy="15.5" r="1.4" fill="%s"/>'
            % (_s(c), _s(c), c))


def gateway(c):
    return ('<path d="M4 20V9l8-5 8 5v11" %s/><path d="M9.5 20v-6h5v6" %s/>'
            % (_s(c), _s(c, 1.4)))


def generic(c):
    return ('<rect x="4" y="4" width="16" height="16" rx="2" %s/>'
            '<path d="M8 12h8" %s/>' % (_s(c), _s(c, 1.4)))


GLYPHS = {
    "server": server, "compute": server, "vm": server, "ec2": server,
    "database": database, "db": database, "rds": database, "sql": database,
    "cache": cache, "redis": cache, "memory": cache,
    "queue": queue, "sqs": queue, "kafka": queue, "topic": queue, "sns": queue,
    "storage": storage, "s3": storage, "bucket": storage, "blob": storage,
    "cdn": cdn, "cloudfront": cdn, "dns": cdn, "route53": cdn, "internet": cdn,
    "lb": lb, "loadbalancer": lb, "alb": lb, "elb": lb,
    "api": api, "apigateway": api, "rest": api,
    "function": function, "lambda": function, "serverless": function,
    "container": container, "ecs": container, "eks": container, "kubernetes": container,
    "docker": container, "pod": container,
    "user": user, "client": user, "actor": user, "users": user,
    "browser": browser, "web": browser, "ui": browser, "frontend": browser,
    "mobile": mobile, "app": mobile,
    "firewall": firewall, "waf": firewall, "security": firewall, "iam": firewall,
    "monitor": monitor, "metrics": monitor, "logging": monitor, "cloudwatch": monitor,
    "network": network, "vpc": network, "mesh": network, "router": network,
    "ml": ml, "ai": ml, "model": ml, "sagemaker": ml,
    "search": search, "elasticsearch": search, "opensearch": search,
    "secret": secret, "vault": secret, "kms": secret, "auth": secret,
    "gateway": gateway, "onprem": gateway, "datacenter": gateway,
    "generic": generic,
}


def get(name):
    if not name:
        return None
    key = str(name).split(":")[-1].strip().lower().replace("-", "").replace("_", "")
    return GLYPHS.get(key)
