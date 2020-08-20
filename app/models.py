from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin
from app import db, admin


# class User(db.Model, UserMixin):
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     __tablename__ = Column(String(50), nullable=False)
#     active = Column(Boolean, default=True)
#     username = Column(String(50), nullable=False)
#     password = Column(String(50), nullable=False)
#
#     def __str__(self):
#         return self.name

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class ProductView(ModelView):
    can_export = True


class CategoryModelView(ModelView):
    column_display_pk = False
    can_create = False
    can_edit = True
    can_export = True
    can_delete = False
    can_export = True
    form_columns = ('name', )

class AboutUsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/about-us.html")

admin.add_view(CategoryModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(AboutUsView(name="About Us"))

if __name__ == "__main__":
    db.create_all()
