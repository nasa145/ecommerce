
import redis
from django.conf import settings
from .models import Product

#connect to redis
r = redis.Redis(host=settings.REDIS_LOCALHOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

class Recommender(object):
    def get_product_key(self, id):
        return f"product:{id}:purchased_with"

    def products_bought(self, products):
        product_ids = [product.id for product in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # Get the pther products bought with each other product
                if product_id != with_id:
                    r.zincrby(self.get_product_key(product_id), 1, with_id)

    
    def suggest_products_for(self, products, max_results=6):
        product_ids = [product.id for product in products]
        if len(products) == 1:
            suggestions = r.zrevrange(self.get_product_key(product_ids[0]), 0, -1)[:max_results]
        else:
            flat_ids = "".join([str(id) for id in product_ids])
            temporary_key = f"temp_{flat_ids}"
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(temporary_key, keys)
            r.zrem(temporary_key, *product_ids)
            suggestions = r.zrevrange(temporary_key, 0, -1)[:max_results]
            r.delete(temporary_key)
        suggested_product_ids = [int(id) for id in suggestions]
        sugggested_products = list(Product.objects.filter(id__in=suggested_product_ids))
        return sugggested_products


    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))