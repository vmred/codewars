# https://www.codewars.com/kata/57f21fcd69e09cb0d2000088/train/python


def order_by_domain(addresses):
    def weights(url):
        domain = url.split('.')[-1]
        return {'com': 0, 'gov': 1, 'org': 2}.get(domain[:3], 3), domain

    return sorted(addresses, key=weights)
