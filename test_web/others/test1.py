
class LevelSetting(object):
    def __init__(self, user_id, model_id, index_id):
        # self.cache = LevelCache
        self.user_id = user_id
        self.model_id = model_id
        self.index_id = index_id
        self.value = None

    @property
    def set_up(self):
        """
        获取映射表
        """
        # self.value = self.cache(user_id=self.user_id, model_id=self.model_id, index_id=self.index_id).my_cache
        self.value = '20'

        return self.value


class LevelCache(object):

    def __init__(self, user_id, model_id, index_id):
        self.value = None
        self.key = 'userid%d:pjstdscore:modelid%d:indexid%d' % (int(user_id), int(model_id), int(index_id))

    @property
    def my_cache(self):
        # self.value = redis_client.json().get(self.key)
        return self.value

    @my_cache.setter
    def my_cache(self, value):
        # redis_client.json().set(name=self.key, path=Path.root_path(), obj=value)
        self.value = value

    @my_cache.deleter
    def my_cache(self):
        # redis_client.json().delete(key=self.key)
        del self.value
