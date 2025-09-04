from fastapi import FastAPI
from .users.controller import router as users_router
from .auth.controller import router as auth_router
from config.settings import INSTALLED_APPS, MODEL_FILE_NAME
import importlib

for app in INSTALLED_APPS:
  try:
    importlib.import_module(f'{app}.{MODEL_FILE_NAME[:-3]}')
  except ModuleNotFoundError as e:
    print(e)
    continue

def include_router(app: FastAPI):
  """
    Includes all routers from apps
  """
  app.include_router(users_router)
  app.include_router(auth_router)