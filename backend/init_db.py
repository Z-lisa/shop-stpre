"""
数据库初始化脚本
创建数据库并插入初始数据
"""
from app.database import engine, Base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from decimal import Decimal
from app.models import Category, Product, Coupon, User, Address
from app.security import get_password_hash

def init_database():
    """初始化数据库"""
    print("开始初始化数据库...")
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    print("[OK] 数据库表创建成功")
    
    # 创建会话
    db = Session(bind=engine)
    
    try:
        if db.query(Category).first():
            print("[OK] 数据已存在，跳过初始化")
            return
        
        test_user = db.query(User).filter(User.username == 'user').first()
        if not test_user:
            test_user = User(
                username='user',
                nickname='测试用户',
                password_hash=get_password_hash('123456'),
                gender='other'
            )
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print("[OK] 测试用户创建成功 (用户名: user, 密码: 123456)")
            
            # 为测试用户创建默认地址
            default_address = Address(
                user_id=test_user.id,
                name='测试用户',
                phone='13800138000',
                province='北京市',
                city='北京市',
                district='朝阳区',
                detail='建国路88号SOHO现代城1号楼1001室',
                is_default=True
            )
            db.add(default_address)
            db.commit()
            print("[OK] 默认地址创建成功")
        
        categories = [
            Category(id=1, name='文学小说', parent_id=None, sort_order=1, is_active=True),
            Category(id=2, name='历史传记', parent_id=None, sort_order=2, is_active=True),
            Category(id=3, name='科技图书', parent_id=None, sort_order=3, is_active=True),
            Category(id=4, name='生活休闲', parent_id=None, sort_order=4, is_active=True),
            Category(id=5, name='服装', parent_id=None, sort_order=5, is_active=True),
            Category(id=6, name='鞋子', parent_id=None, sort_order=6, is_active=True),
        ]
        db.add_all(categories)
        db.commit()
        print("[OK] 分类数据插入成功")
        
        # 插入商品数据
        products = [
            # 文学小说
            Product(id=1, name='活着', author='余华', publisher='作家出版社', 
                   price=Decimal('29.80'), original_price=Decimal('35.00'), stock=100, category_id=1,
                   description='活着是中国当代作家余华创作的长篇虚构类小说，首次发表于《收获》1992 年第 6 期。',
                   cover_image='book_1.jpg', size_type='none', rating=4.5, review_count=10, sales_count=50),
            
            Product(id=2, name='百年孤独', author='加西亚·马尔克斯', publisher='南海出版公司',
                   price=Decimal('59.00'), original_price=Decimal('69.00'), stock=80, category_id=1,
                   description='《百年孤独》是哥伦比亚作家加西亚·马尔克斯的代表作，也是拉丁美洲魔幻现实主义文学的代表作。',
                   cover_image='book_2.jpg', size_type='none', rating=4.8, review_count=15, sales_count=80),
            
            Product(id=3, name='追风筝的人', author='卡勒德·胡赛尼', publisher='上海人民出版社',
                   price=Decimal('45.00'), original_price=Decimal('52.00'), stock=120, category_id=1,
                   description='《追风筝的人》是美籍阿富汗裔作家卡勒德·胡赛尼的第一部小说。',
                   cover_image='book_3.jpg', size_type='none', rating=4.6, review_count=20, sales_count=60),
            
            # 历史传记
            Product(id=4, name='明朝那些事儿', author='当年明月', publisher='浙江人民出版社',
                   price=Decimal('39.80'), original_price=Decimal('45.00'), stock=90, category_id=2,
                   description='《明朝那些事儿》主要讲述的是从 1344 年到 1644 年这三百年间关于明朝的一些故事。',
                   cover_image='book_4.jpg', size_type='none', rating=4.7, review_count=12, sales_count=70),
            
            Product(id=5, name='史记', author='司马迁', publisher='中华书局',
                   price=Decimal('68.00'), original_price=Decimal('78.00'), stock=60, category_id=2,
                   description='《史记》是西汉史学家司马迁撰写的纪传体史书，是中国历史上第一部纪传体通史。',
                   cover_image='book_5.jpg', size_type='none', rating=4.9, review_count=8, sales_count=40),
            
            # 科技图书
            Product(id=6, name='Python 编程：从入门到实践', author='Eric Matthes', publisher='人民邮电出版社',
                   price=Decimal('79.00'), original_price=Decimal('89.00'), stock=150, category_id=3,
                   description='本书是一本针对所有层次的 Python 读者写的教程式书籍。',
                   cover_image='book_6.jpg', size_type='none', rating=4.8, review_count=25, sales_count=100),
            
            Product(id=7, name='深入理解计算机系统', author='Randal E.Bryant', publisher='机械工业出版社',
                   price=Decimal('139.00'), original_price=Decimal('159.00'), stock=50, category_id=3,
                   description='本书从程序员的视角详细阐述计算机系统的本质概念。',
                   cover_image='book_7.jpg', size_type='none', rating=4.9, review_count=5, sales_count=30),
            
            # 生活休闲
            Product(id=8, name='断舍离', author='山下英子', publisher='广西科学技术出版社',
                   price=Decimal('32.00'), original_price=Decimal('38.00'), stock=200, category_id=4,
                   description='断舍离是日本作家山下英子创作的家庭生活类著作。',
                   cover_image='book_8.jpg', size_type='none', rating=4.3, review_count=18, sales_count=90),
            
            # 服装
            Product(id=9, name='春季新款 T 恤 白色', author='优衣库', publisher='优衣库',
                   price=Decimal('99.00'), original_price=Decimal('149.00'), stock=500, category_id=5,
                   description='春季新款纯棉 T 恤，舒适透气',
                   cover_image='shirt_white.jpg', size_type='clothing',
                   sizes=["S","M","L","XL","XXL"],
                   rating=4.5, review_count=30, sales_count=200),
            
            Product(id=10, name='春季新款 T 恤 黑色', author='优衣库', publisher='优衣库',
                   price=Decimal('99.00'), original_price=Decimal('149.00'), stock=500, category_id=5,
                   description='春季新款纯棉 T 恤，舒适透气',
                   cover_image='shirt_black.jpg', size_type='clothing',
                   sizes=["S","M","L","XL","XXL"],
                   rating=4.5, review_count=25, sales_count=180),
            
            Product(id=11, name='休闲牛仔裤 蓝色', author='优衣库', publisher='优衣库',
                   price=Decimal('299.00'), original_price=Decimal('399.00'), stock=300, category_id=5,
                   description='经典休闲牛仔裤，修身版型',
                   cover_image='jeans_blue.jpg', size_type='clothing',
                   sizes=["28","29","30","31","32","33","34"],
                   rating=4.4, review_count=20, sales_count=120),
            
            # 鞋子
            Product(id=12, name='运动鞋 白色', author='耐克', publisher='耐克',
                   price=Decimal('599.00'), original_price=Decimal('799.00'), stock=200, category_id=6,
                   description='经典款运动鞋，舒适耐穿',
                   cover_image='shoes_white.jpg', size_type='shoes',
                   sizes=["38","39","40","41","42","43","44"],
                   rating=4.7, review_count=40, sales_count=150),
            
            Product(id=13, name='运动鞋 黑色', author='耐克', publisher='耐克',
                   price=Decimal('599.00'), original_price=Decimal('799.00'), stock=200, category_id=6,
                   description='经典款运动鞋，舒适耐穿',
                   cover_image='shoes_black.jpg', size_type='shoes',
                   sizes=["38","39","40","41","42","43","44"],
                   rating=4.7, review_count=35, sales_count=140),
            
            Product(id=14, name='休闲板鞋', author='阿迪达斯', publisher='阿迪达斯',
                   price=Decimal('499.00'), original_price=Decimal('699.00'), stock=150, category_id=6,
                   description='时尚休闲板鞋，百搭款式',
                   cover_image='shoes_casual.jpg', size_type='shoes',
                   sizes=["38","39","40","41","42","43"],
                   rating=4.6, review_count=28, sales_count=110),
        ]
        db.add_all(products)
        db.commit()
        print("[OK] 商品数据插入成功")
        
        # 插入优惠券数据
        now = datetime.now()
        coupons = [
            Coupon(id=1, name='新人优惠券', type='fixed', discount_value=Decimal('20.00'),
                  min_amount=Decimal('100.00'), max_discount=None,
                  description='新用户专享优惠券', total_count=1000, issued_count=0, per_user_limit=1,
                  valid_from=now, valid_to=now + timedelta(days=30), status='active'),
            
            Coupon(id=2, name='满减券', type='fixed', discount_value=Decimal('50.00'),
                  min_amount=Decimal('300.00'), max_discount=None,
                  description='满 300 减 50', total_count=500, issued_count=0, per_user_limit=1,
                  valid_from=now, valid_to=now + timedelta(days=15), status='active'),
            
            Coupon(id=3, name='折扣券', type='percentage', discount_value=Decimal('9.00'),
                  min_amount=Decimal('200.00'), max_discount=Decimal('100.00'),
                  description='9 折优惠，最高减 100 元', total_count=300, issued_count=0, per_user_limit=1,
                  valid_from=now, valid_to=now + timedelta(days=20), status='active'),
        ]
        db.add_all(coupons)
        db.commit()
        print("[OK] 优惠券数据插入成功")
        
        print("\n[SUCCESS] 数据初始化完成！")
        print(f"   - {len(categories)} 个分类")
        print(f"   - {len(products)} 个商品")
        print(f"   - {len(coupons)} 个优惠券")
        
    except Exception as e:
        db.rollback()
        print(f"[ERROR] 数据初始化失败：{e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
