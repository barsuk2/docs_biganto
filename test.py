def get_path_qr(tour_id):
    path = ''
    k = 10 ** 6
    while 1:
        a, b = divmod(tour_id, k)
        if a != 0:
            path += '/' + str(a)
            tour_id = b
            k = k / 1000
            if k == 0.001:
                break
        else:
            tour_id = b
            k = k / 1000
            path += '/' + '0'
    return path


def get_path_qr_text(tour_id):
    qr_path = '{:,}'.format(tour_id).replace(',', '/')
    if len(qr_path) <= 3:
        return '/0/0/' + qr_path
    elif len(qr_path) <= 6 and len(qr_path) >=4 :
        return '/0/' + qr_path
    else:
        return '/' + qr_path


print(get_path_qr_text(10234))
