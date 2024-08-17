from ninja import NinjaAPI
from apps.menu.api import router as menu_router
from apps.store.api import router as store_router

api = NinjaAPI()

api.add_router('menu/', menu_router)
api.add_router('store/', store_router)
