# API for restaurant wrote on FastAPI.
## Before starting, create and fill .env file in according to .env.example file.
### For start install dependencies
- `pip install -r requirements.txt`
- make migrations `alembic upgrade d279cf5b36d0`
- start main.app

### Technologies:
[![My Skills](https://skillicons.dev/icons?i=py,fastapi,postgres,github)](https://skillicons.dev)

### Requests:
| Description           | Method                                            | Request                                                                |
|-----------------------|---------------------------------------------------|------------------------------------------------------------------------|
| Get menu list         |![GET](https://img.shields.io/badge/-GET-blue)     | `/api/v1/menus/`                                                       |
| Create a menu         |![POST](https://img.shields.io/badge/-POST-success)| `/api/v1/menus/`                                                       |
| Get a specific menu   |![GET](https://img.shields.io/badge/-GET-blue)     | `/api/v1/menus/{menu_id}`                                              |
| Delete a menu         |![DELETE](https://img.shields.io/badge/-DELETE-red)| `/api/v1/menus/{menu_id}`                                              |
| Update a menu         |![PATCH](https://img.shields.io/badge/-PATCH-9cf)  | `/api/v1/menus/{menu_id}`                                              |
| Get submenu list      |![GET](https://img.shields.io/badge/-GET-blue)     | `/api/v1/menus/{menu_id}/submenus`                                     |
| Create a submenu      |![POST](https://img.shields.io/badge/-POST-success)| `/api/v1/menus/{menu_id}/submenus`                                     |
| Get a specific submenu|![GET](https://img.shields.io/badge/-GET-blue)     | `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                        |
| Delete a submenu      |![DELETE](https://img.shields.io/badge/-DELETE-red)| `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                        |
| Update a submenu      |![PATCH](https://img.shields.io/badge/-PATCH-9cf)  | `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                        |
| Get dishes list       |![GET](https://img.shields.io/badge/-GET-blue)     | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes`                 |
| Create a dish         |![POST](https://img.shields.io/badge/-POST-success)| `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes`                 |
| Get a specific dish   |![GET](https://img.shields.io/badge/-GET-blue)     | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}`       |
| Delete a dish         |![DELETE](https://img.shields.io/badge/-DELETE-red)| `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}`       |
| Update a dish         |![PATCH](https://img.shields.io/badge/-PATCH-9cf)  | `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}`       |
    