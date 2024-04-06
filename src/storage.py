import pickledb


def get_db():
    return pickledb.load("storage.db", False)


def save_correlation(key, value):
    db = get_db()
    if db.get(key):
        return False
    db.set(key, value)
    db.dump()
    return True


def get_correlation(key):
    db = get_db()
    return db.get(key)


def get_all_correlations():
    db = get_db()
    return db.getall()
