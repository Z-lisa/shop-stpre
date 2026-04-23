export const categories = [
  { id: 1, name: '上衣', icon: '👕' },
  { id: 2, name: '裤子', icon: '👖' },
  { id: 3, name: '裙子', icon: '👗' },
  { id: 4, name: '鞋子', icon: '👟' },
  { id: 5, name: '首饰', icon: '💍' },
  { id: 6, name: '包包', icon: '👜' },
  { id: 7, name: '配饰', icon: '🧣' },
  { id: 8, name: '运动', icon: '🏃' }
]

export const banners = [
  { id: 1, image: 'https://images.unsplash.com/photo-1445205170230-053b83016050?w=750&h=300&fit=crop', link: '/category/1' },
  { id: 2, image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=750&h=300&fit=crop', link: '/category/4' },
  { id: 3, image: 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=750&h=300&fit=crop', link: '/category/5' }
]

export const products = [
  {
    id: 1,
    name: '纯棉简约T恤',
    author: '时尚优选',
    publisher: '优衣库代工厂',
    price: 79.0,
    originalPrice: 129.0,
    cover: 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=200&h=280&fit=crop',
    categoryId: 1,
    rating: 4.8,
    stock: 500,
    sales: 2560,
    isbn: '',
    pages: 0,
    publishDate: '2024-03-15',
    binding: '件',
    description: '精选优质纯棉面料，柔软舒适透气，简约百搭款式，是衣橱必备的基础单品。不起球、不变形，经久耐穿。多种颜色可选，适合各种搭配风格。',
    authorIntro: '时尚优选是一个专注于基础款服饰的品牌，致力于为消费者提供高品质、高性价比的日常服装。',
    catalog: ['颜色：白色/黑色/灰色/藏青', '尺码：S/M/L/XL/XXL', '面料：100%纯棉'],
    tags: ['纯棉', '简约', '百搭', '限时优惠'],
    reviews: [
      { user: '时尚达人', rating: 5, content: '面料很舒服，穿起来很透气，颜色也很正！', date: '2024-05-20', likes: 25 },
      { user: '购物小能手', rating: 5, content: '性价比超高的一家店铺，已回购三件！', date: '2024-05-18', likes: 18 },
      { user: '搭配爱好者', rating: 4, content: '版型很好，搭配什么裤子都好看。', date: '2024-05-15', likes: 12 }
    ]
  },
  {
    id: 2,
    name: '宽松休闲牛仔裤',
    author: '牛仔世家',
    publisher: '牛仔裤工厂',
    price: 159.0,
    originalPrice: 259.0,
    cover: 'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=200&h=280&fit=crop',
    categoryId: 2,
    rating: 4.7,
    stock: 300,
    description: '经典宽松版型，舒适不紧绷，修饰腿型效果佳。优质牛仔面料，经过水洗工艺处理，柔软亲肤。'
  },
  {
    id: 3,
    name: '雪纺碎花连衣裙',
    author: '花语绽放',
    publisher: '服装设计工作室',
    price: 199.0,
    originalPrice: 329.0,
    cover: 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=200&h=280&fit=crop',
    categoryId: 3,
    rating: 4.9,
    stock: 180,
    description: '轻盈雪纺面料，仙气十足，碎花设计浪漫甜美。春夏秋三季可穿，适用多种场合。'
  },
  {
    id: 4,
    name: '经典小白鞋',
    author: '步履轻盈',
    publisher: '运动鞋制造厂',
    price: 229.0,
    originalPrice: 369.0,
    cover: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=200&h=280&fit=crop',
    categoryId: 4,
    rating: 4.8,
    stock: 420,
    description: '百搭经典小白鞋，柔软舒适，透气不闷脚。无论是休闲装还是正装都能轻松搭配。'
  },
  {
    id: 5,
    name: '运动休闲跑鞋',
    author: '飞跃运动',
    publisher: '体育用品公司',
    price: 299.0,
    originalPrice: 459.0,
    cover: 'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=200&h=280&fit=crop',
    categoryId: 4,
    rating: 4.7,
    stock: 350,
    description: '专业运动跑鞋，缓震舒适，透气网面设计。适合日常运动和跑步锻炼。'
  },
  {
    id: 6,
    name: '黄金项链吊坠',
    author: '金艺轩',
    publisher: '珠宝首饰厂',
    price: 899.0,
    originalPrice: 1299.0,
    cover: 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=200&h=280&fit=crop',
    categoryId: 5,
    rating: 4.9,
    stock: 80,
    description: '999足金项链，精致吊坠设计，时尚大方。精工打造，佩戴舒适，不易褪色。'
  },
  {
    id: 7,
    name: '银手镯手链',
    author: '银尚优品',
    publisher: '银饰加工厂',
    price: 159.0,
    originalPrice: 259.0,
    cover: 'https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=200&h=280&fit=crop',
    categoryId: 5,
    rating: 4.6,
    stock: 200,
    description: '时尚银手镯，简约大方，精致做工。适合日常佩戴，送礼自用皆宜。'
  },
  {
    id: 8,
    name: '真皮单肩包',
    author: '包罗万象',
    publisher: '皮具制品厂',
    price: 369.0,
    originalPrice: 569.0,
    cover: 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=200&h=280&fit=crop',
    categoryId: 6,
    rating: 4.8,
    stock: 150,
    description: '优质真皮材质，质感出众。大容量设计，满足日常出行需求。多个颜色可选，经典百搭。'
  },
  {
    id: 9,
    name: '休闲双肩包',
    author: '途游',
    publisher: '箱包制造厂',
    price: 129.0,
    originalPrice: 199.0,
    cover: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=200&h=280&fit=crop',
    categoryId: 6,
    rating: 4.5,
    stock: 280,
    description: '轻便双肩包，适合上学上班旅行。分层设计，实用性强。多色可选，青春活力。'
  },
  {
    id: 10,
    name: '羊绒围巾',
    author: '温暖如春',
    publisher: '羊绒制品厂',
    price: 199.0,
    originalPrice: 329.0,
    cover: 'https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?w=200&h=280&fit=crop',
    categoryId: 7,
    rating: 4.9,
    stock: 120,
    description: '100%纯羊绒围巾，柔软保暖，奢华舒适。多种颜色可选，是秋冬必备保暖单品。'
  },
  {
    id: 11,
    name: '休闲西装外套',
    author: '商务风情',
    publisher: '西装定制厂',
    price: 399.0,
    originalPrice: 599.0,
    cover: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=200&h=280&fit=crop',
    categoryId: 1,
    rating: 4.7,
    stock: 200,
    description: '经典休闲西装，版型挺括，面料舒适。适合商务场合和日常穿搭，彰显品位。'
  },
  {
    id: 12,
    name: '高腰阔腿裤',
    author: '潮女坊',
    publisher: '服装设计工作室',
    price: 179.0,
    originalPrice: 279.0,
    cover: 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=200&h=280&fit=crop',
    categoryId: 2,
    rating: 4.6,
    stock: 250,
    description: '高腰阔腿裤，修饰腿型，拉长比例。垂感面料，飘逸显瘦。时尚百搭必备款。'
  },
  {
    id: 13,
    name: '蕾丝半身裙',
    author: '优雅伊人',
    publisher: '蕾丝服装厂',
    price: 189.0,
    originalPrice: 299.0,
    cover: 'https://images.unsplash.com/photo-1583496661160-fb5886a0uj9c?w=200&h=280&fit=crop',
    categoryId: 3,
    rating: 4.8,
    stock: 160,
    description: '精美蕾丝面料，浪漫优雅。轻盈飘逸，适合约会、聚会等场合穿着。'
  },
  {
    id: 14,
    name: '英伦马丁靴',
    author: '铁靴传奇',
    publisher: '靴子制造厂',
    price: 349.0,
    originalPrice: 499.0,
    cover: 'https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=200&h=280&fit=crop',
    categoryId: 4,
    rating: 4.7,
    stock: 180,
    description: '经典马丁靴款式，时尚酷帅。真皮材质，舒适耐穿。是秋冬必备的时尚单品。'
  },
  {
    id: 15,
    name: '水晶耳钉耳环',
    author: '晶彩世界',
    publisher: '饰品加工厂',
    price: 59.0,
    originalPrice: 99.0,
    cover: 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=200&h=280&fit=crop',
    categoryId: 5,
    rating: 4.5,
    stock: 500,
    description: '闪亮水晶耳钉，精致时尚。佩戴舒适，不过敏。低调奢华，彰显气质。'
  },
  {
    id: 16,
    name: '运动健身服套装',
    author: '动能先锋',
    publisher: '运动服饰厂',
    price: 169.0,
    originalPrice: 269.0,
    cover: 'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=200&h=280&fit=crop',
    categoryId: 8,
    rating: 4.8,
    stock: 320,
    description: '专业运动套装，吸湿排汗，弹性舒适。适合健身、瑜伽、跑步等多种运动。'
  },
  {
    id: 17,
    name: '连帽卫衣',
    author: '青春地带',
    publisher: '休闲服饰厂',
    price: 129.0,
    originalPrice: 199.0,
    cover: 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=200&h=280&fit=crop',
    categoryId: 1,
    rating: 4.7,
    stock: 380,
    description: '潮牌连帽卫衣，宽松舒适，时尚百搭。优质面料，不起球不变形。'
  },
  {
    id: 18,
    name: '半身牛仔裙',
    author: '牛仔风情',
    publisher: '牛仔服装厂',
    price: 149.0,
    originalPrice: 229.0,
    cover: 'https://images.unsplash.com/photo-1582418702059-97ebafb35d09?w=200&h=280&fit=crop',
    categoryId: 3,
    rating: 4.6,
    stock: 210,
    description: '时尚牛仔裙，A字版型显瘦。百搭款式，可搭配各种上衣，春秋必备。'
  },
  {
    id: 19,
    name: '平底豆豆鞋',
    author: '舒步天下',
    publisher: '皮鞋制造厂',
    price: 189.0,
    originalPrice: 299.0,
    cover: 'https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=200&h=280&fit=crop',
    categoryId: 4,
    rating: 4.5,
    stock: 260,
    description: '柔软豆豆鞋，舒适轻便。经典款式，适合日常通勤和休闲出行。'
  },
  {
    id: 20,
    name: '手提斜挎包',
    author: '都市丽人',
    publisher: '皮具设计公司',
    price: 259.0,
    originalPrice: 399.0,
    cover: 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=200&h=280&fit=crop',
    categoryId: 6,
    rating: 4.7,
    stock: 180,
    description: '多功能手提斜挎包，实用能装。简约设计，优雅大方，适合职场女性。'
  },
  {
    id: 21,
    name: '棒球帽',
    author: '潮流先锋',
    publisher: '帽饰制品厂',
    price: 49.0,
    originalPrice: 79.0,
    cover: 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=200&h=280&fit=crop',
    categoryId: 7,
    rating: 4.4,
    stock: 450,
    description: '时尚棒球帽，遮阳防晒，潮流百搭。精细做工，佩戴舒适，多色可选。'
  },
  {
    id: 22,
    name: '羽绒服',
    author: '暖冬之选',
    publisher: '羽绒制品厂',
    price: 499.0,
    originalPrice: 799.0,
    cover: 'https://images.unsplash.com/photo-1544923246-77307dd628b1?w=200&h=280&fit=crop',
    categoryId: 1,
    rating: 4.9,
    stock: 150,
    description: '高品质羽绒服，保暖性能极佳。轻薄不臃肿，时尚保暖两不误。冬季必备。'
  },
  {
    id: 23,
    name: '修身小黑裙',
    author: '黑天鹅',
    publisher: '礼服设计工作室',
    price: 289.0,
    originalPrice: 459.0,
    cover: 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=200&h=280&fit=crop',
    categoryId: 3,
    rating: 4.8,
    stock: 140,
    description: '经典小黑裙，修身显瘦。优雅大气，适合各种正式场合，是每个女人衣橱必备。'
  },
  {
    id: 24,
    name: '帆布鞋',
    author: '青春记忆',
    publisher: '帆布鞋厂',
    price: 89.0,
    originalPrice: 149.0,
    cover: 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=200&h=280&fit=crop',
    categoryId: 4,
    rating: 4.6,
    stock: 500,
    description: '经典帆布鞋，舒适透气。青春百搭，承载着满满的青春回忆。'
  },
  {
    id: 25,
    name: '珍珠项链',
    author: '珠光宝气',
    publisher: '珍珠养殖场',
    price: 599.0,
    originalPrice: 899.0,
    cover: 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=200&h=280&fit=crop',
    categoryId: 5,
    rating: 4.9,
    stock: 90,
    description: '天然淡水珍珠项链，圆润光泽。佩戴大方优雅，是送妈妈、送女友的绝佳礼物。'
  },
  {
    id: 26,
    name: '商务公文包',
    author: '绅士品格',
    publisher: '皮具制造厂',
    price: 329.0,
    originalPrice: 499.0,
    cover: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=200&h=280&fit=crop',
    categoryId: 6,
    rating: 4.7,
    stock: 160,
    description: '高端商务公文包，真皮材质，品味之选。分层设计，文件笔记本电脑都能装。'
  },
  {
    id: 27,
    name: '防晒衣',
    author: '阳光守护',
    publisher: '防晒服饰厂',
    price: 129.0,
    originalPrice: 199.0,
    cover: 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=200&h=280&fit=crop',
    categoryId: 1,
    rating: 4.5,
    stock: 400,
    description: '轻薄防晒衣，UPF50+防晒指数。冰凉面料，夏季出行必备，防晒又时尚。'
  },
  {
    id: 28,
    name: '瑜伽服',
    author: '静心瑜伽',
    publisher: '运动服饰公司',
    price: 139.0,
    originalPrice: 219.0,
    cover: 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=200&h=280&fit=crop',
    categoryId: 8,
    rating: 4.6,
    stock: 300,
    description: '专业瑜伽服，弹性面料，透气吸汗。修身设计，练习瑜伽更加舒适自在。'
  },
  {
    id: 29,
    name: '绅士领带',
    author: '领秀风情',
    publisher: '领带制造厂',
    price: 99.0,
    originalPrice: 169.0,
    cover: 'https://images.unsplash.com/photo-1598522325074-042db73aa4e6?w=200&h=280&fit=crop',
    categoryId: 7,
    rating: 4.5,
    stock: 250,
    description: '商务领带，质感丝绸，精致工艺。多种花色可选，是成功人士的必备配饰。'
  },
  {
    id: 30,
    name: '拖鞋凉鞋',
    author: '夏日清风',
    publisher: '凉鞋制造厂',
    price: 69.0,
    originalPrice: 119.0,
    cover: 'https://images.unsplash.com/photo-1603487742131-4160ec999306?w=200&h=280&fit=crop',
    categoryId: 4,
    rating: 4.4,
    stock: 600,
    description: '舒适拖鞋凉鞋，凉爽透气。居家外出皆可穿，轻便实惠，夏日必备。'
  }
]

export const getProductById = (id) => {
  return products.find(p => p.id === id)
}

export const getProductsByCategory = (categoryId) => {
  return products.filter(p => p.categoryId === categoryId)
}

export const getProductsByKeyword = (keyword) => {
  const lowerKeyword = keyword.toLowerCase()
  return products.filter(p => 
    p.name.toLowerCase().includes(lowerKeyword) || 
    p.author.toLowerCase().includes(lowerKeyword)
  )
}

export const getHotProducts = (limit = 10) => {
  return [...products].sort((a, b) => b.sales - a.sales).slice(0, limit)
}

export const getNewProducts = (limit = 10) => {
  return [...products].sort((a, b) => new Date(b.publishDate) - new Date(a.publishDate)).slice(0, limit)
}

export const getRecommendProducts = (productId, limit = 6) => {
  const product = getProductById(productId)
  if (!product) return []
  
  return products
    .filter(p => p.id !== productId && p.categoryId === product.categoryId)
    .slice(0, limit)
}
