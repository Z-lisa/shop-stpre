import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '../stores/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/category',
    name: 'Category',
    component: () => import('../views/Category.vue')
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('../views/Cart.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue')
  },
  {
    path: '/book/:id',
    name: 'BookDetail',
    component: () => import('../views/BookDetail.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: () => import('../views/Checkout.vue')
  },
  {
    path: '/order-success',
    name: 'OrderSuccess',
    component: () => import('../views/OrderSuccess.vue')
  },
  {
    path: '/address',
    name: 'AddressManage',
    component: () => import('../views/AddressManage.vue')
  },
  {
    path: '/customer-service',
    name: 'CustomerService',
    component: () => import('../views/CustomerService.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/coupons',
    name: 'Coupons',
    component: () => import('../views/Coupons.vue')
  },
  {
    path: '/order/:id',
    name: 'OrderDetail',
    component: () => import('../views/OrderDetail.vue')
  },
  {
    path: '/select-address',
    name: 'SelectAddress',
    component: () => import('../views/SelectAddress.vue')
  },
  {
    path: '/add-address',
    name: 'AddAddress',
    component: () => import('../views/AddAddress.vue')
  },
  {
    path: '/select-coupon',
    name: 'SelectCoupon',
    component: () => import('../views/SelectCoupon.vue')
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: () => import('../views/AboutUs.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫 - 检查登录状态
router.beforeEach((to, from, next) => {
  // 直接从 localStorage 读取 token，避免 store 未初始化问题
  const token = localStorage.getItem('token')
  const isLoggedIn = !!token
  
  // 如果未登录且访问需要登录的页面，跳转到登录页
  const publicPages = ['/', '/category', '/search', '/book/:id', '/login', '/customer-service', '/coupons']
  const isPublicPage = publicPages.some(page => {
    if (page.includes(':')) {
      const regex = new RegExp('^' + page.replace(':id', '\\d+') + '$')
      return regex.test(to.path)
    }
    return page === to.path
  })
  
  if (!isLoggedIn && !isPublicPage) {
    next({ path: '/login', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})

export default router
