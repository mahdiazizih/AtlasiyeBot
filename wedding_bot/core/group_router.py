# wedding_bot/core/group_router.py

import logging
import importlib
from wedding_bot.core.config.groups_config import GROUP_CONFIG

def setup_group_routers(dp):
    for group_id, config in GROUP_CONFIG.items():
        module_name = config["router_module"]
        try:
            module_path = f"wedding_bot.groups.{module_name}"
            module = importlib.import_module(module_path)
            dp.include_router(module.router)
        except Exception as e:
            logging.error(f"[ERROR] Cannot load router for group {group_id} ({config['name']}): {e}")
