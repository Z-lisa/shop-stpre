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
            Category(id=1, name='女装', parent_id=None, sort_order=1, is_active=True),
            Category(id=2, name='男装', parent_id=None, sort_order=2, is_active=True),
            Category(id=3, name='配饰首饰', parent_id=None, sort_order=3, is_active=True),
            Category(id=4, name='箱包', parent_id=None, sort_order=4, is_active=True),
            Category(id=5, name='运动户外', parent_id=None, sort_order=5, is_active=True),
            Category(id=6, name='鞋靴', parent_id=None, sort_order=6, is_active=True),
        ]
        db.add_all(categories)
        db.commit()
        print("[OK] 分类数据插入成功")
        
        # 插入商品数据
        products = [
            # 女装
            Product(id=1, name='法式碎花连衣裙', author='ZARA', publisher='ZARA',
                   price=Decimal('299.00'), original_price=Decimal('399.00'), stock=100, category_id=1,
                   description='浪漫法式碎花连衣裙，优雅显瘦，适合春夏穿着',
                   cover_image='https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["S","M","L","XL"],
                   rating=4.5, review_count=10, sales_count=50),
            
            Product(id=2, name='针织开衫外套', author='优衣库', publisher='优衣库',
                   price=Decimal('199.00'), original_price=Decimal('249.00'), stock=80, category_id=1,
                   description='柔软舒适针织开衫，百搭基础款，多色可选',
                   cover_image='https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["S","M","L","XL"],
                   rating=4.8, review_count=15, sales_count=80),
            
            Product(id=3, name='高腰阔腿裤', author='韩都衣舍', publisher='韩都衣舍',
                   price=Decimal('159.00'), original_price=Decimal('229.00'), stock=120, category_id=1,
                   description='高腰设计拉长腿部比例，宽松版型舒适显瘦',
                   cover_image='https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["S","M","L","XL","XXL"],
                   rating=4.6, review_count=20, sales_count=60),
            
            # 男装
            Product(id=4, name='商务休闲衬衫', author='海澜之家', publisher='海澜之家',
                   price=Decimal('179.00'), original_price=Decimal('249.00'), stock=90, category_id=2,
                   description='免烫商务衬衫，简约大气，适合职场穿着',
                   cover_image='https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["M","L","XL","XXL","XXXL"],
                   rating=4.7, review_count=12, sales_count=70),
            
            Product(id=5, name='工装夹克外套', author='太平鸟', publisher='太平鸟',
                   price=Decimal('399.00'), original_price=Decimal('599.00'), stock=60, category_id=2,
                   description='潮流工装风夹克，挺括有型，帅气百搭',
                   cover_image='https://images.unsplash.com/photo-1551028919-ac76c9028d1e?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["M","L","XL","XXL"],
                   rating=4.9, review_count=8, sales_count=40),
            
            # 配饰首饰
            Product(id=6, name='925银项链', author='潘多拉', publisher='潘多拉',
                   price=Decimal('399.00'), original_price=Decimal('599.00'), stock=150, category_id=3,
                   description='精致925银项链，简约优雅，送礼自用皆宜',
                   cover_image='https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=200&h=280&fit=crop', size_type='none',
                   rating=4.8, review_count=25, sales_count=100),
            
            Product(id=7, name='时尚耳环套装', author='周大福', publisher='周大福',
                   price=Decimal('199.00'), original_price=Decimal('299.00'), stock=50, category_id=3,
                   description='多款式耳环组合，日常百搭，闪耀动人',
                   cover_image='https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=200&h=280&fit=crop', size_type='none',
                   rating=4.9, review_count=5, sales_count=30),
            
            # 箱包
            Product(id=8, name='简约单肩包', author='小CK', publisher='小CK',
                   price=Decimal('269.00'), original_price=Decimal('399.00'), stock=200, category_id=4,
                   description='时尚简约单肩包，容量大，通勤必备',
                   cover_image='https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=200&h=280&fit=crop', size_type='none',
                   rating=4.3, review_count=18, sales_count=90),
            
            # 运动户外
            Product(id=9, name='速干运动T恤', author='迪卡侬', publisher='迪卡侬',
                   price=Decimal('99.00'), original_price=Decimal('149.00'), stock=500, category_id=5,
                   description='专业速干面料，透气排汗，运动首选',
                   cover_image='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["S","M","L","XL","XXL"],
                   rating=4.5, review_count=30, sales_count=200),
            
            Product(id=10, name='运动瑜伽裤', author='Lululemon', publisher='Lululemon',
                   price=Decimal('299.00'), original_price=Decimal('450.00'), stock=500, category_id=5,
                   description='高弹亲肤瑜伽裤，修身塑形，运动舒适',
                   cover_image='https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["S","M","L","XL"],
                   rating=4.5, review_count=25, sales_count=180),
            
            Product(id=11, name='户外防晒衣', author='北面', publisher='北面',
                   price=Decimal('399.00'), original_price=Decimal('599.00'), stock=300, category_id=5,
                   description='轻薄防晒皮肤衣，UPF50+，户外活动必备',
                   cover_image='https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=200&h=280&fit=crop', size_type='clothing',
                   sizes=["M","L","XL","XXL"],
                   rating=4.4, review_count=20, sales_count=120),
            
            # 鞋靴
            Product(id=12, name='经典小白鞋', author='耐克', publisher='耐克',
                   price=Decimal('599.00'), original_price=Decimal('799.00'), stock=200, category_id=6,
                   description='百搭经典小白鞋，舒适透气，日常必备',
                   cover_image='https://images.unsplash.com/photo-1549298916-b41d501d3772?w=200&h=280&fit=crop', size_type='shoes',
                   sizes=["36","37","38","39","40","41","42","43","44"],
                   rating=4.7, review_count=40, sales_count=150),
            
            Product(id=13, name='复古帆布鞋', author='匡威', publisher='匡威',
                   price=Decimal('399.00'), original_price=Decimal('499.00'), stock=200, category_id=6,
                   description='经典复古帆布鞋，潮流百搭，年轻首选',
                   cover_image='https://images.unsplash.com/photo-1607522370275-f14206abe5d3?w=200&h=280&fit=crop', size_type='shoes',
                   sizes=["35","36","37","38","39","40","41","42","43"],
                   rating=4.7, review_count=35, sales_count=140),
            
            Product(id=14, name='马丁靴', author='Dr.Martens', publisher='Dr.Martens',
                   price=Decimal('899.00'), original_price=Decimal('1299.00'), stock=150, category_id=6,
                   description='经典英伦马丁靴，硬朗有型，耐穿百搭',
                   cover_image='https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=200&h=280&fit=crop', size_type='shoes',
                   sizes=["36","37","38","39","40","41","42","43"],
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
