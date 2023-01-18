from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from api.validate_data import MenuValidator, SubmenuValidator, DishValidator
from api.db import MenuModel, SubmenuModel, DishModel, connect_to_db


router = APIRouter(prefix='/api/v1')


@router.get('/menus')
def receive_menu(db: Session = Depends(connect_to_db)):
    menu = db.query(MenuModel).all()
    return menu


@router.get('/menus/{menu_id}')
def receive_current_menu(menu_id: str, db: Session = Depends(connect_to_db)):
    current_menu = db.query(MenuModel).filter(MenuModel.id == menu_id).first()
    if current_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return current_menu


@router.post('/menus', status_code=status.HTTP_201_CREATED)
def create_menu(menu: MenuValidator, db: Session = Depends(connect_to_db)):
    created_menu = MenuModel(id=uuid4(), title=menu.title, description=menu.description)
    db.add(created_menu)
    db.commit()
    db.refresh(created_menu)
    return created_menu


@router.patch('/menus/{menu_id}')
def update_current_menu(menu_id: str, menu: MenuValidator, db: Session = Depends(connect_to_db)):
    menu_to_update = db.query(MenuModel).filter(MenuModel.id == menu_id).first()
    if menu_to_update is None:
        raise HTTPException(status_code=404, detail="menu not found")
    menu_to_update.title = menu.title
    menu_to_update.description = menu.description
    db.add(menu_to_update)
    db.commit()
    db.refresh(menu_to_update)
    return menu_to_update


@router.delete('/menus/{menu_id}')
def delete_current_menu(menu_id: str, db: Session = Depends(connect_to_db)):
    menu_to_delete = db.query(MenuModel).filter(MenuModel.id == menu_id).first()
    db.delete(menu_to_delete)
    db.commit()


@router.get('/menus/{menu_id}/submenus')
def receive_submenus(db: Session = Depends(connect_to_db)):
    submenu = db.query(SubmenuModel).all()
    return submenu


@router.get('/menus/{menu_id}/submenus/{submenu_id}')
def receive_current_submenus(submenu_id: str, db: Session = Depends(connect_to_db)):
    current_submenu = db.query(SubmenuModel).filter(
        SubmenuModel.id == submenu_id).first()
    if current_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return current_submenu


@router.post('/menus/{menu_id}/submenus', status_code=status.HTTP_201_CREATED)
def create_submenu(menu_id: str, submenu: SubmenuValidator,
                   db: Session = Depends(connect_to_db)):
    menu = db.query(MenuModel).filter(MenuModel.id == menu_id).first()
    created_submenu = SubmenuModel(id=uuid4(), title=submenu.title,
                                   description=submenu.description,
                                   menu_id=menu_id)
    menu.add_submenu_count(1)
    db.add(created_submenu)
    db.commit()
    db.refresh(created_submenu)
    return created_submenu


@router.patch('/menus/{menu_id}/submenus/{submenu_id}')
def update_current_submenu(submenu_id: str, submenu: SubmenuValidator,
                           db: Session = Depends(connect_to_db)):
    submenu_to_update = db.query(SubmenuModel).filter(
        SubmenuModel.id == submenu_id).first()
    if submenu_to_update is None:
        raise HTTPException(status_code=404, detail="menu not found")
    submenu_to_update.title = submenu.title
    submenu_to_update.description = submenu.description
    db.add(submenu_to_update)
    db.commit()
    db.refresh(submenu_to_update)
    return submenu_to_update


@router.delete('/menus/{menu_id}/submenus/{submenu_id}')
def delete_current_submenu(menu_id: str, submenu_id: str,
                           db: Session = Depends(connect_to_db)):
    menu = db.query(MenuModel).filter(
           MenuModel.id == menu_id).first()
    submenu_to_delete = db.query(SubmenuModel).filter(
        SubmenuModel.id == submenu_id).first()
    dish_count = submenu_to_delete.dishes_count
    menu.delete_submenu_count(1)
    menu.delete_dishes_count(dish_count)
    db.delete(submenu_to_delete)
    db.commit()


@router.get('/menus/{menu_id}/submenus/{submenu_id}/dishes')
def receive_dish(db: Session = Depends(connect_to_db)):
    dishes = db.query(DishModel).all()
    return dishes


@router.get('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def receive_current_dish(dish_id: str, db: Session = Depends(connect_to_db)):
    current_dish = db.query(DishModel).filter(DishModel.id == dish_id).first()
    if current_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return current_dish


@router.post('/menus/{menu_id}/submenus/{submenu_id}/dishes',
             status_code=status.HTTP_201_CREATED)
def create_dish(menu_id: str, submenu_id: str, dish: DishValidator,
                db: Session = Depends(connect_to_db)):
    menu = db.query(MenuModel).filter(MenuModel.id == menu_id).first()
    submenu = db.query(SubmenuModel).filter(SubmenuModel.id == submenu_id).first()
    menu.add_dishes_count(1)
    submenu.update_dishes_count(1)
    created_dish = DishModel(id=uuid4(), title=dish.title,
                             description=dish.description,
                             price=dish.price,
                             submenu_id=submenu_id)
    db.add(created_dish)
    db.commit()
    db.refresh(created_dish)
    return created_dish


@router.patch('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def update_current_dish(dish_id: str, dish: DishValidator,
                        db: Session = Depends(connect_to_db)):
    dish_to_update = db.query(DishModel).filter(DishModel.id == dish_id).first()
    dish_to_update.title = dish.title
    dish_to_update.description = dish.description
    dish_to_update.price = dish.price
    db.add(dish_to_update)
    db.commit()
    db.refresh(dish_to_update)
    return dish_to_update


@router.delete('/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def delete_current_dish(menu_id: str, submenu_id: str, dish_id: str,
                        db: Session = Depends(connect_to_db)):
    menu = db.query(MenuModel).filter(MenuModel.id == menu_id).first()
    submenu = db.query(SubmenuModel).filter(SubmenuModel.id == submenu_id).first()
    submenu.delete_dishes_count(1)
    menu.delete_dishes_count(1)
    dish_to_delete = db.query(DishModel).filter(DishModel.id == dish_id).first()
    db.delete(dish_to_delete)
    db.commit()
